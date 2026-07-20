#!/usr/bin/env python3
"""Monitor registered official visa sources for review-worthy content changes.

This script deliberately detects source-page changes, not legal conclusions. A
changed fingerprint means that a human should review the official page before
updating any visa rule or applicant guidance.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import threading
import urllib.error
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Callable
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = ROOT.parent
REGISTRY_PATH = ROOT / "references" / "official-sources.json"
DIRECTORY_PATH = ROOT / "references" / "jurisdictions.json"
DEFAULT_OUTPUT_PATH = REPOSITORY_ROOT / ".maintenance" / "policy-monitor.json"
MAX_RESPONSE_BYTES = 5 * 1024 * 1024
MIN_NORMALIZED_CHARACTERS = 80
MAX_CONNECTIONS_PER_HOST = 2
GUARDED_STATUSES = {401, 403, 405, 406, 429, 503}
BROWSER_USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36"
)


class VisibleTextParser(HTMLParser):
    """Extract stable visible text while ignoring executable/decorative markup."""

    IGNORED_TAGS = {"script", "style", "noscript", "svg", "template"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._ignored_depth = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        del attrs
        if tag.casefold() in self.IGNORED_TAGS:
            self._ignored_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag.casefold() in self.IGNORED_TAGS and self._ignored_depth:
            self._ignored_depth -= 1

    def handle_data(self, data: str) -> None:
        if not self._ignored_depth:
            self.parts.append(data)


def utc_timestamp() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def normalize_content(payload: bytes, content_type: str = "") -> str:
    """Return whitespace-normalized text suitable for a content fingerprint."""

    text = payload.decode("utf-8", errors="replace")
    if "html" in content_type.casefold() or "<html" in text[:1000].casefold():
        parser = VisibleTextParser()
        parser.feed(text)
        parser.close()
        text = " ".join(parser.parts)
    return re.sub(r"\s+", " ", text).strip()


def fingerprint_content(payload: bytes, content_type: str = "") -> tuple[str, int]:
    normalized = normalize_content(payload, content_type)
    if len(normalized) < MIN_NORMALIZED_CHARACTERS:
        raise ValueError(
            f"normalized response is too short ({len(normalized)} characters)"
        )
    digest = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
    return digest, len(normalized)


def fetch_source(url: str, timeout: float) -> dict:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "text/html,application/xhtml+xml,text/plain;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.8",
            "User-Agent": BROWSER_USER_AGENT,
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            status = response.status
            content_type = response.headers.get("Content-Type", "")
            payload = response.read(MAX_RESPONSE_BYTES + 1)
    except urllib.error.HTTPError as error:
        status_kind = "guarded" if error.code in GUARDED_STATUSES else "error"
        return {
            "status": status_kind,
            "http_status": error.code,
            "error": f"HTTP {error.code}",
        }
    except urllib.error.URLError as error:
        return {"status": "error", "error": str(error.reason)}
    except Exception as error:  # noqa: BLE001
        return {"status": "error", "error": str(error)}

    if len(payload) > MAX_RESPONSE_BYTES:
        return {
            "status": "error",
            "http_status": status,
            "error": f"response exceeds {MAX_RESPONSE_BYTES} bytes",
        }

    try:
        fingerprint, normalized_characters = fingerprint_content(payload, content_type)
    except ValueError as error:
        return {
            "status": "error",
            "http_status": status,
            "error": str(error),
        }
    return {
        "status": "success",
        "http_status": status,
        "fingerprint": fingerprint,
        "normalized_characters": normalized_characters,
    }


def previous_sources_by_url(previous: dict) -> dict[str, dict]:
    sources: dict[str, dict] = {}
    for collection in ("jurisdictions", "route_areas"):
        for destination in previous.get(collection, []):
            for source in destination.get("sources", []):
                if source.get("url"):
                    sources[source["url"]] = source
    return sources


def merge_source_result(
    source: dict,
    fetched: dict,
    previous: dict | None,
    checked_at: str,
) -> dict:
    result = {
        "label": source["label"],
        "url": source["url"],
        "authority": source["authority"],
        "roles": source["roles"],
    }
    previous = previous or {}
    previous_fingerprint = previous.get("fingerprint")

    if fetched["status"] == "success":
        fingerprint = fetched["fingerprint"]
        if not previous_fingerprint:
            status = "baseline"
        elif previous_fingerprint == fingerprint:
            status = "unchanged"
        elif previous.get("candidate_fingerprint") == fingerprint:
            status = "changed"
        else:
            status = "change_candidate"

        result.update(
            {
                "status": status,
                "http_status": fetched["http_status"],
                "last_success_at": checked_at,
            }
        )
        if status == "change_candidate":
            result.update(
                {
                    "fingerprint": previous_fingerprint,
                    "normalized_characters": previous.get("normalized_characters"),
                    "candidate_fingerprint": fingerprint,
                    "candidate_normalized_characters": fetched[
                        "normalized_characters"
                    ],
                    "candidate_seen_at": checked_at,
                }
            )
        else:
            result.update(
                {
                    "fingerprint": fingerprint,
                    "normalized_characters": fetched["normalized_characters"],
                }
            )
        if status == "baseline":
            result["baseline_at"] = checked_at
        elif previous.get("baseline_at"):
            result["baseline_at"] = previous["baseline_at"]
        if status == "changed":
            result["changed_from"] = previous_fingerprint
            result["last_changed_at"] = checked_at
        elif previous.get("last_changed_at"):
            result["last_changed_at"] = previous["last_changed_at"]
        return result

    result["status"] = fetched["status"]
    if fetched.get("http_status"):
        result["http_status"] = fetched["http_status"]
    result["error"] = fetched["error"]
    for key in (
        "fingerprint",
        "normalized_characters",
        "baseline_at",
        "last_success_at",
        "last_changed_at",
        "candidate_fingerprint",
        "candidate_normalized_characters",
        "candidate_seen_at",
    ):
        if key in previous:
            result[key] = previous[key]
    return result


def aggregate_status(sources: list[dict]) -> str:
    statuses = {source["status"] for source in sources}
    if "changed" in statuses:
        return "change_confirmed"
    if "change_candidate" in statuses:
        return "review_required"
    if "baseline" in statuses:
        return "baseline_created"
    if statuses == {"unchanged"}:
        return "unchanged"
    if statuses & {"unchanged"} and statuses & {"guarded", "error"}:
        return "partially_verified"
    return "unverified"


def build_seeded_destination(seed: dict, source_results: dict[str, dict]) -> dict:
    sources = [source_results[source["url"]] for source in seed["sources"]]
    result = {
        "id": seed["id"],
        "name": seed["name"],
        "coverage": "official_source_seeded",
        "monitor_status": aggregate_status(sources),
        "sources": sources,
    }
    if seed.get("iso2"):
        result["iso2"] = seed["iso2"]
    return result


def build_summary(
    destinations: list[dict], route_areas: list[dict], all_sources: list[dict]
) -> dict:
    statuses = [source["status"] for source in all_sources]
    return {
        "destinations_total": len(destinations),
        "destinations_seeded": sum(
            item["coverage"] == "official_source_seeded" for item in destinations
        ),
        "destinations_requiring_live_discovery": sum(
            item["coverage"] == "live_discovery_required" for item in destinations
        ),
        "route_areas_seeded": len(route_areas),
        "sources_total": len(all_sources),
        "sources_checked": sum(
            status in {"baseline", "unchanged", "changed"} for status in statuses
        ),
        "sources_changed": statuses.count("changed"),
        "sources_change_candidates": statuses.count("change_candidate"),
        "sources_baselined": statuses.count("baseline"),
        "sources_guarded": statuses.count("guarded"),
        "sources_failed": statuses.count("error"),
        "destinations_with_changes": sum(
            item["monitor_status"] == "change_confirmed" for item in destinations
        ),
        "destinations_requiring_review": sum(
            item["monitor_status"] == "review_required" for item in destinations
        ),
        "route_areas_with_changes": sum(
            item["monitor_status"] == "change_confirmed" for item in route_areas
        ),
        "route_areas_requiring_review": sum(
            item["monitor_status"] == "review_required" for item in route_areas
        ),
    }


def build_monitor(
    directory: dict,
    registry: dict,
    previous: dict,
    timeout: float,
    workers: int,
    fetcher: Callable[[str, float], dict] = fetch_source,
    checked_at: str | None = None,
) -> dict:
    checked_at = checked_at or utc_timestamp()
    previous_by_url = previous_sources_by_url(previous)
    sources_by_url = {
        source["url"]: source
        for seed in registry["jurisdictions"]
        for source in seed["sources"]
    }
    fetched_by_url: dict[str, dict] = {}
    host_semaphores: defaultdict[str, threading.Semaphore] = defaultdict(
        lambda: threading.Semaphore(MAX_CONNECTIONS_PER_HOST)
    )

    def throttled_fetch(url: str) -> dict:
        hostname = urlparse(url).hostname or url
        with host_semaphores[hostname]:
            return fetcher(url, timeout)

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(throttled_fetch, url): url for url in sources_by_url
        }
        for future in as_completed(futures):
            url = futures[future]
            try:
                fetched_by_url[url] = future.result()
            except Exception as error:  # noqa: BLE001
                fetched_by_url[url] = {"status": "error", "error": str(error)}

    source_results = {
        url: merge_source_result(
            source,
            fetched_by_url[url],
            previous_by_url.get(url),
            checked_at,
        )
        for url, source in sources_by_url.items()
    }
    seeds_by_iso2 = {
        seed["iso2"]: seed
        for seed in registry["jurisdictions"]
        if seed.get("iso2")
    }
    destinations: list[dict] = []
    for destination in directory["jurisdictions"]:
        seed = seeds_by_iso2.get(destination["iso2"])
        if seed:
            destinations.append(build_seeded_destination(seed, source_results))
        else:
            destinations.append(
                {
                    "id": destination["id"],
                    "iso2": destination["iso2"],
                    "name": destination["name"],
                    "coverage": "live_discovery_required",
                    "monitor_status": "not_monitored",
                    "sources": [],
                }
            )

    route_areas = [
        build_seeded_destination(seed, source_results)
        for seed in registry["jurisdictions"]
        if not seed.get("iso2")
    ]
    all_sources = list(source_results.values())
    return {
        "schema_version": 1,
        "generated_at": checked_at,
        "meaning": (
            "A changed source fingerprint requires human review; it is not a visa "
            "policy verdict. Unseeded destinations still require live official-source "
            "discovery for each traveler and itinerary."
        ),
        "summary": build_summary(destinations, route_areas, all_sources),
        "jurisdictions": destinations,
        "route_areas": route_areas,
    }


def markdown_summary(monitor: dict) -> str:
    summary = monitor["summary"]
    lines = [
        "## Weekly visa policy source monitor",
        "",
        f"Checked at: `{monitor['generated_at']}`",
        "",
        "| Result | Count |",
        "| --- | ---: |",
        f"| Destinations in directory | {summary['destinations_total']} |",
        f"| Destinations with registered official sources | {summary['destinations_seeded']} |",
        "| Destinations requiring live source discovery | "
        f"{summary['destinations_requiring_live_discovery']} |",
        f"| Official pages checked | {summary['sources_checked']} / {summary['sources_total']} |",
        f"| Changed page fingerprints | {summary['sources_changed']} |",
        f"| New change candidates | {summary['sources_change_candidates']} |",
        f"| Guarded pages | {summary['sources_guarded']} |",
        f"| Failed pages | {summary['sources_failed']} |",
        "",
        "> A changed fingerprint is a review signal, not a legal or visa-policy conclusion.",
    ]
    changed = [
        item
        for item in (*monitor["jurisdictions"], *monitor["route_areas"])
        if item["monitor_status"] in {"change_confirmed", "review_required"}
    ]
    if changed:
        lines.extend(["", "### Sources requiring review", ""])
        for item in changed:
            changed_sources = [
                source
                for source in item["sources"]
                if source["status"] in {"changed", "change_candidate"}
            ]
            lines.append(f"- **{item['name']}**")
            lines.extend(
                f"  - [{source['status']}] {source['label']}: {source['url']}"
                for source in changed_sources
            )
    return "\n".join(lines) + "\n"


def load_json(path: Path, default: dict) -> dict:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT_PATH)
    parser.add_argument("--summary", type=Path)
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Ignore an existing monitor and create a fresh baseline",
    )
    args = parser.parse_args()
    if args.workers < 1:
        parser.error("--workers must be at least 1")

    directory = load_json(DIRECTORY_PATH, {})
    registry = load_json(REGISTRY_PATH, {})
    previous = {} if args.reset else load_json(args.output, {})
    monitor = build_monitor(
        directory,
        registry,
        previous,
        timeout=args.timeout,
        workers=args.workers,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(monitor, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    summary = markdown_summary(monitor)
    if args.summary:
        args.summary.parent.mkdir(parents=True, exist_ok=True)
        with args.summary.open("a", encoding="utf-8") as summary_file:
            summary_file.write(summary)
    print(summary, end="")


if __name__ == "__main__":
    main()
