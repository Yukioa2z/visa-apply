#!/usr/bin/env python3
"""Create a local DS-160 dossier HTML file from the bundled template."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "assets" / "ds160-dossier-template.html"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", help="Output HTML path to create")
    parser.add_argument("--title", default="DS-160 Visa Filing Dossier")
    parser.add_argument("--visa-type", default="Pending")
    parser.add_argument("--location", default="Pending")
    parser.add_argument("--applicant-label", default="Applicant")
    parser.add_argument("--privacy-mode", default="Pending")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not TEMPLATE.exists():
        raise SystemExit(f"Template not found: {TEMPLATE}")

    output = Path(args.output).expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)

    replacements = {
        "{{TITLE}}": args.title,
        "{{VISA_TYPE}}": args.visa_type,
        "{{APPLICATION_LOCATION}}": args.location,
        "{{APPLICANT_LABEL}}": args.applicant_label,
        "{{PRIVACY_MODE}}": args.privacy_mode,
        "{{GENERATED_AT}}": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }

    html = TEMPLATE.read_text(encoding="utf-8")
    for key, value in replacements.items():
        html = html.replace(key, value)

    output.write_text(html, encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
