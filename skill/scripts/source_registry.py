#!/usr/bin/env python3
"""Validate and query the visa destination and official-source registries."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "references" / "official-sources.json"
DIRECTORY_PATH = ROOT / "references" / "jurisdictions.json"
IATA_TRAVEL_CENTRE = (
    "https://www.iata.org/en/services/compliance/timatic/travel-documentation/"
)
ALLOWED_LEVELS = {"full_adapter", "source_seeded", "discovered"}
ALLOWED_ROLES = {
    "authoritative_rules",
    "official_application",
    "delegated_application",
    "official_status",
}


def load_registry() -> dict:
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def load_directory() -> dict:
    return json.loads(DIRECTORY_PATH.read_text(encoding="utf-8"))


def _candidates(jurisdiction: dict) -> set[str]:
    values = {
        jurisdiction.get("id", ""),
        jurisdiction.get("iso2", ""),
        jurisdiction.get("name", ""),
        *jurisdiction.get("aliases", []),
    }
    return {value.casefold() for value in values if value}


def find_jurisdiction(registry: dict, query: str) -> dict | None:
    normalized = query.casefold()
    return next(
        (
            jurisdiction
            for jurisdiction in registry["jurisdictions"]
            if normalized in _candidates(jurisdiction)
        ),
        None,
    )


def find_directory_jurisdiction(directory: dict, query: str) -> dict | None:
    normalized = query.casefold()
    return next(
        (
            jurisdiction
            for jurisdiction in directory["jurisdictions"]
            if normalized in _candidates(jurisdiction)
        ),
        None,
    )


def find_destination(registry: dict, directory: dict, query: str) -> tuple[dict, dict | None] | None:
    seed = find_jurisdiction(registry, query)
    if seed:
        directory_match = (
            find_directory_jurisdiction(directory, seed["iso2"])
            if seed.get("iso2")
            else None
        )
        return directory_match or seed, seed

    directory_match = find_directory_jurisdiction(directory, query)
    if directory_match:
        seed = find_jurisdiction(registry, directory_match["iso2"])
        return directory_match, seed
    return None


def _valid_https_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def validate(registry: dict, directory: dict | None = None) -> list[str]:
    errors: list[str] = []
    if registry.get("schema_version") != 1:
        errors.append("official source schema_version must be 1")

    jurisdictions = registry.get("jurisdictions")
    if not isinstance(jurisdictions, list) or not jurisdictions:
        return errors + ["official source jurisdictions must be a non-empty list"]

    seen_ids: set[str] = set()
    for index, jurisdiction in enumerate(jurisdictions):
        prefix = f"official_sources.jurisdictions[{index}]"
        jurisdiction_id = jurisdiction.get("id")
        if not jurisdiction_id:
            errors.append(f"{prefix}.id is required")
        elif jurisdiction_id in seen_ids:
            errors.append(f"duplicate official source jurisdiction id: {jurisdiction_id}")
        else:
            seen_ids.add(jurisdiction_id)

        if jurisdiction.get("support_level") not in ALLOWED_LEVELS:
            errors.append(f"{prefix}.support_level is invalid")

        sources = jurisdiction.get("sources")
        if not isinstance(sources, list) or not sources:
            errors.append(f"{prefix}.sources must be a non-empty list")
            continue

        has_rule_authority = False
        for source_index, source in enumerate(sources):
            source_prefix = f"{prefix}.sources[{source_index}]"
            roles = set(source.get("roles", []))
            unknown_roles = roles - ALLOWED_ROLES
            if unknown_roles:
                errors.append(f"{source_prefix}.roles contains {sorted(unknown_roles)}")
            if "authoritative_rules" in roles:
                has_rule_authority = True
            if not _valid_https_url(source.get("url", "")):
                errors.append(f"{source_prefix}.url must be an https URL")
            for key in ("label", "authority", "covers"):
                if not source.get(key):
                    errors.append(f"{source_prefix}.{key} is required")

        if not has_rule_authority:
            errors.append(f"{prefix} needs an authoritative_rules source")

    if directory is None:
        return errors
    if directory.get("schema_version") != 1:
        errors.append("jurisdiction directory schema_version must be 1")

    directory_jurisdictions = directory.get("jurisdictions")
    if not isinstance(directory_jurisdictions, list) or not directory_jurisdictions:
        return errors + ["directory jurisdictions must be a non-empty list"]

    directory_ids: set[str] = set()
    directory_iso2: set[str] = set()
    for index, jurisdiction in enumerate(directory_jurisdictions):
        prefix = f"directory.jurisdictions[{index}]"
        jurisdiction_id = jurisdiction.get("id")
        iso2 = jurisdiction.get("iso2")
        if not jurisdiction_id or not iso2 or not jurisdiction.get("name"):
            errors.append(f"{prefix} requires id, iso2, and name")
            continue
        if jurisdiction_id in directory_ids:
            errors.append(f"duplicate directory jurisdiction id: {jurisdiction_id}")
        if iso2 in directory_iso2:
            errors.append(f"duplicate directory ISO2: {iso2}")
        directory_ids.add(jurisdiction_id)
        directory_iso2.add(iso2)

    for source_index, source in enumerate(directory.get("directory_sources", [])):
        if not source.get("label") or not _valid_https_url(source.get("url", "")):
            errors.append(f"directory.directory_sources[{source_index}] is invalid")

    for jurisdiction in jurisdictions:
        iso2 = jurisdiction.get("iso2")
        if iso2 and iso2 not in directory_iso2:
            errors.append(f"official source ISO2 not in directory: {iso2}")

    return errors


def print_jurisdiction(destination: dict, seed: dict | None) -> None:
    support_level = seed["support_level"] if seed else "live_discovery"
    print(f"{destination['name']} [{destination['id']}] - {support_level}")
    if not seed:
        print("No cached official source seed. Live official-source discovery is required.")
        return
    if seed.get("notes"):
        print(f"Note: {seed['notes']}")
    for source in seed["sources"]:
        roles = ", ".join(source["roles"])
        print(f"- {source['label']} ({roles})")
        print(f"  {source['url']}")


def add_route_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("jurisdiction")
    parser.add_argument("--nationality", default="Pending")
    parser.add_argument("--passport-type", default="Ordinary passport")
    parser.add_argument("--travel-document-issuer", default="Pending")
    parser.add_argument("--residence", default="Pending")
    parser.add_argument("--residence-status", default="Pending")
    parser.add_argument("--application-location", default="Pending")
    parser.add_argument("--purpose", default="Pending")
    parser.add_argument("--arrival-date", default="Pending")
    parser.add_argument("--duration", default="Pending")
    parser.add_argument("--entries", default="Pending")
    parser.add_argument("--arrival-mode", default="Pending")
    parser.add_argument("--transit", default="None declared")
    parser.add_argument("--existing-entry-rights", default="None declared")


def print_live_check_plan(destination: dict, seed: dict | None, args: argparse.Namespace) -> None:
    print(f"Live visa-need check: {destination['name']}")
    print(f"Nationality/status: {args.nationality}")
    print(f"Travel document: {args.passport_type}; issuer: {args.travel_document_issuer}")
    print(f"Legal residence/status: {args.residence}; {args.residence_status}")
    print(f"Application location: {args.application_location}")
    print(f"Purpose: {args.purpose}")
    print(f"Arrival/duration/entries: {args.arrival_date}; {args.duration}; {args.entries}")
    print(f"Arrival mode: {args.arrival_mode}")
    print(f"Transit/self-transfer: {args.transit}")
    print(f"Existing visas/residence permits: {args.existing_entry_rights}")
    print("\nMandatory live research order:")
    print("1. Open the destination immigration authority or foreign ministry.")
    print("2. Find the current visa-exemption, ETA, eVisa, visa-on-arrival, and transit rules for this exact travel document.")
    print("3. Check whether residence permits or third-country visas change eligibility.")
    print("4. Resolve the responsible embassy/consulate and location-specific filing rules.")
    print("5. Check Timatic/IATA for carrier boarding requirements; treat it as an operational cross-check, not legal authority.")
    print("6. Record checked time, effective dates, conditions, conflicts, and a refresh deadline in the HTML.")
    print("\nRequired result fields:")
    print("- verdict: visa_free | eta | evisa | visa_on_arrival | consular_visa | transit_authorization | residence_route | mixed | unresolved")
    print("- allowed purpose, maximum stay, entries, validity window, and extension rules")
    print("- passport validity/blank pages, arrival ports/modes, onward travel, funds, insurance, accommodation, and registration conditions")
    print("- transit and self-transfer result for every intermediate country")
    print("- government source URLs, page dates/effective dates, checked timestamp, and conflict notes")
    print("- Timatic/IATA or carrier cross-check result and checked timestamp")
    print("\nOfficial starting sources:")
    if seed:
        for source in seed["sources"]:
            print(f"- {source['label']}: {source['url']}")
    else:
        print(f"- Search for the official immigration authority or foreign ministry of {destination['name']}.")
        print(f"- Search query: {destination['name']} official visa requirements {args.nationality} passport")
        print(f"- Search query: {destination['name']} immigration eVisa ETA visa on arrival official")
        print(f"- Search query: {destination['name']} embassy {args.application_location} visa official")
    print(f"- IATA Travel Centre: {IATA_TRAVEL_CENTRE}")
    print("\nGate: do not collect the full application form until the verdict is resolved or explicitly marked unresolved for applicant review.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("validate")
    subparsers.add_parser("coverage")
    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("--seeded-only", action="store_true")
    show_parser = subparsers.add_parser("show")
    show_parser.add_argument("jurisdiction")
    add_route_arguments(subparsers.add_parser("live-check-plan"))
    add_route_arguments(subparsers.add_parser("research-plan"))
    args = parser.parse_args()

    registry = load_registry()
    directory = load_directory()
    errors = validate(registry, directory)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)

    seeded_iso2 = {
        jurisdiction["iso2"]
        for jurisdiction in registry["jurisdictions"]
        if jurisdiction.get("iso2")
    }
    if args.command == "validate":
        print(
            f"Valid registries: {len(directory['jurisdictions'])} destinations; "
            f"{len(registry['jurisdictions'])} official source seeds"
        )
    elif args.command == "coverage":
        print(f"Searchable destinations: {len(directory['jurisdictions'])}")
        print(f"Destinations with cached official seeds: {len(seeded_iso2)}")
        print(f"Destinations requiring live source discovery: {len(directory['jurisdictions']) - len(seeded_iso2)}")
        print(f"Additional route areas with seeds: {len(registry['jurisdictions']) - len(seeded_iso2)}")
    elif args.command == "list":
        for destination in directory["jurisdictions"]:
            seed = find_jurisdiction(registry, destination["iso2"])
            if args.seeded_only and not seed:
                continue
            support_level = seed["support_level"] if seed else "live_discovery"
            print(f"{destination['id']}\t{destination['name']}\t{support_level}")
    elif args.command == "show":
        result = find_destination(registry, directory, args.jurisdiction)
        if not result:
            raise SystemExit(f"Unknown destination: {args.jurisdiction}")
        print_jurisdiction(*result)
    elif args.command in {"live-check-plan", "research-plan"}:
        result = find_destination(registry, directory, args.jurisdiction)
        if not result:
            raise SystemExit(f"Unknown destination: {args.jurisdiction}")
        print_live_check_plan(*result, args)


if __name__ == "__main__":
    main()
