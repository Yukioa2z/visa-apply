#!/usr/bin/env python3
"""Validate and query the official visa source registry."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "references" / "official-sources.json"
ALLOWED_LEVELS = {"full_adapter", "source_seeded", "discovered"}
ALLOWED_ROLES = {
    "authoritative_rules",
    "official_application",
    "delegated_application",
    "official_status",
}


def load_registry() -> dict:
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def validate(registry: dict) -> list[str]:
    errors: list[str] = []
    if registry.get("schema_version") != 1:
        errors.append("schema_version must be 1")

    jurisdictions = registry.get("jurisdictions")
    if not isinstance(jurisdictions, list) or not jurisdictions:
        return errors + ["jurisdictions must be a non-empty list"]

    seen_ids: set[str] = set()
    for index, jurisdiction in enumerate(jurisdictions):
        prefix = f"jurisdictions[{index}]"
        jurisdiction_id = jurisdiction.get("id")
        if not jurisdiction_id:
            errors.append(f"{prefix}.id is required")
        elif jurisdiction_id in seen_ids:
            errors.append(f"duplicate jurisdiction id: {jurisdiction_id}")
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

            parsed = urlparse(source.get("url", ""))
            if parsed.scheme != "https" or not parsed.netloc:
                errors.append(f"{source_prefix}.url must be an https URL")
            for key in ("label", "authority", "covers"):
                if not source.get(key):
                    errors.append(f"{source_prefix}.{key} is required")

        if not has_rule_authority:
            errors.append(f"{prefix} needs an authoritative_rules source")

    return errors


def find_jurisdiction(registry: dict, query: str) -> dict | None:
    normalized = query.casefold()
    for jurisdiction in registry["jurisdictions"]:
        candidates = {
            jurisdiction["id"].casefold(),
            jurisdiction["name"].casefold(),
            *[alias.casefold() for alias in jurisdiction.get("aliases", [])],
        }
        if normalized in candidates:
            return jurisdiction
    return None


def print_jurisdiction(jurisdiction: dict) -> None:
    print(f"{jurisdiction['name']} [{jurisdiction['id']}] - {jurisdiction['support_level']}")
    if jurisdiction.get("notes"):
        print(f"Note: {jurisdiction['notes']}")
    for source in jurisdiction["sources"]:
        roles = ", ".join(source["roles"])
        print(f"- {source['label']} ({roles})")
        print(f"  {source['url']}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("validate")
    subparsers.add_parser("list")
    show_parser = subparsers.add_parser("show")
    show_parser.add_argument("jurisdiction")
    research_parser = subparsers.add_parser("research-plan")
    research_parser.add_argument("jurisdiction")
    research_parser.add_argument("--nationality", default="Pending")
    research_parser.add_argument("--travel-document-issuer", default="Pending")
    research_parser.add_argument("--residence", default="Pending")
    research_parser.add_argument("--residence-status", default="Pending")
    research_parser.add_argument("--application-location", default="Pending")
    research_parser.add_argument("--purpose", default="Pending")
    args = parser.parse_args()

    registry = load_registry()
    errors = validate(registry)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)

    if args.command == "validate":
        print(f"Valid registry: {len(registry['jurisdictions'])} jurisdictions")
    elif args.command == "list":
        for jurisdiction in registry["jurisdictions"]:
            print(f"{jurisdiction['id']}\t{jurisdiction['name']}\t{jurisdiction['support_level']}")
    elif args.command == "show":
        jurisdiction = find_jurisdiction(registry, args.jurisdiction)
        if not jurisdiction:
            raise SystemExit(f"Unknown jurisdiction: {args.jurisdiction}")
        print_jurisdiction(jurisdiction)
    elif args.command == "research-plan":
        jurisdiction = find_jurisdiction(registry, args.jurisdiction)
        if not jurisdiction:
            raise SystemExit(f"Unknown jurisdiction: {args.jurisdiction}")
        print(f"Research plan: {jurisdiction['name']}")
        print(f"Nationality: {args.nationality}")
        print(f"Travel document issuer: {args.travel_document_issuer}")
        print(f"Legal residence: {args.residence}")
        print(f"Residence status: {args.residence_status}")
        print(f"Application location: {args.application_location}")
        print(f"Purpose: {args.purpose}")
        print("1. Determine visa-free, authorization, eVisa, consular, or residence route.")
        print("2. Resolve the embassy/consulate responsible for the legal residence.")
        print("3. Verify route-specific requirements, fees, form, and processing channel.")
        print("4. Record URLs and checked date in the HTML source snapshot.")
        print("5. Build the country and visa-type question overlay before intake.")
        print("Official starting sources:")
        for source in jurisdiction["sources"]:
            print(f"- {source['label']}: {source['url']}")


if __name__ == "__main__":
    main()
