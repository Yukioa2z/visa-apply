#!/usr/bin/env python3
"""Create a local visa application dossier from the bundled HTML template."""

from __future__ import annotations

import argparse
from datetime import datetime
from html import escape
from pathlib import Path
from urllib.parse import urlparse

from source_registry import find_jurisdiction, load_registry


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "assets" / "visa-dossier-template.html"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", help="Output HTML path to create")
    parser.add_argument("--title")
    parser.add_argument("--country", help="Registry id, country name, or alias")
    parser.add_argument("--destination")
    parser.add_argument("--visa-type", default="Pending")
    parser.add_argument("--form-name", default="Pending")
    parser.add_argument(
        "--application-location",
        "--location",
        dest="application_location",
        default="Pending",
    )
    parser.add_argument("--applicant-label", default="Applicant")
    parser.add_argument("--privacy-mode", default="Pending")
    parser.add_argument("--nationality", "--nationalities", default="Pending")
    parser.add_argument("--passport-type", default="Pending")
    parser.add_argument("--travel-document-issuer", default="Pending")
    parser.add_argument("--legal-residence", default="Pending")
    parser.add_argument("--residence-status", default="Pending")
    parser.add_argument("--purpose", default="Pending")
    parser.add_argument("--official-source-url")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not TEMPLATE.exists():
        raise SystemExit(f"Template not found: {TEMPLATE}")

    output = Path(args.output).expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)

    jurisdiction = None
    registry = None
    if args.country:
        registry = load_registry()
        jurisdiction = find_jurisdiction(registry, args.country)
        if not jurisdiction:
            raise SystemExit(
                f"Unknown registry country: {args.country}. "
                "Use source_registry.py list or pass --destination and --official-source-url."
            )

    destination = args.destination or (
        jurisdiction["name"] if jurisdiction else "Pending"
    )
    official_source_url = args.official_source_url
    if official_source_url:
        parsed_source = urlparse(official_source_url)
        if parsed_source.scheme != "https" or not parsed_source.netloc:
            raise SystemExit("--official-source-url must be an https URL")
    if not official_source_url and jurisdiction:
        official_source_url = next(
            source["url"]
            for source in jurisdiction["sources"]
            if "authoritative_rules" in source["roles"]
        )
    official_source_url = official_source_url or "Pending official verification"
    official_source_href = (
        official_source_url if official_source_url.startswith("https://") else "#"
    )
    source_status = (
        f"Registry seeded {registry['last_verified']}; recheck before filing"
        if registry
        else "Pending official verification"
    )

    title = args.title or f"{destination} Visa Application Dossier"
    replacements = {
        "{{TITLE}}": title,
        "{{DESTINATION}}": destination,
        "{{VISA_TYPE}}": args.visa_type,
        "{{FORM_NAME}}": args.form_name,
        "{{APPLICATION_LOCATION}}": args.application_location,
        "{{APPLICANT_LABEL}}": args.applicant_label,
        "{{PRIVACY_MODE}}": args.privacy_mode,
        "{{NATIONALITY}}": args.nationality,
        "{{PASSPORT_TYPE}}": args.passport_type,
        "{{TRAVEL_DOCUMENT_ISSUER}}": args.travel_document_issuer,
        "{{LEGAL_RESIDENCE}}": args.legal_residence,
        "{{RESIDENCE_STATUS}}": args.residence_status,
        "{{TRAVEL_PURPOSE}}": args.purpose,
        "{{OFFICIAL_SOURCE_URL}}": official_source_url,
        "{{OFFICIAL_SOURCE_HREF}}": official_source_href,
        "{{SOURCE_VERIFICATION_STATUS}}": source_status,
        "{{GENERATED_AT}}": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }

    html = TEMPLATE.read_text(encoding="utf-8")
    for key, value in replacements.items():
        html = html.replace(key, escape(value, quote=True))

    output.write_text(html, encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
