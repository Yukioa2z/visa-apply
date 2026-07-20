---
name: visa-apply
description: Use when checking whether a traveler needs a visa, ETA, eVisa, visa on arrival, or transit authorization, or when researching, preparing, reviewing, tracking, or filling an entry application for any destination. Supports a 250-destination directory, mandatory current official-source verification for the exact passport/residence/itinerary, country and visa-type branching, a local HTML dossier as the single source of truth, and assisted browser/computer form entry after applicant review.
---

# Visa Apply

## Purpose

Create and maintain a local HTML dossier as the single source of truth for a visa application. Resolve the correct country and visa route from current official sources, collect applicant facts with a country/visa-specific question path, prepare a final form preview and document checklist, then assist with portal entry after applicant review.

The most common entry point is a lightweight question — "I hold an X passport, live in Y, want to visit Z for two weeks: do I need a visa?" Answer that first by running the live route check (step 3). Many trips end there with a visa-free or ETA verdict and never need a full application; only continue to detailed intake when a visa is actually required.

This skill is not legal advice. The applicant must review every answer and handle any applicant-only declaration, signature, certification, CAPTCHA, and submission.

## Required Workflow

1. Keep all applicant data local. Personal data collected for the application lives only in the local HTML dossier on the user's machine. Never transmit it to any external service, log it outside the dossier, or use it for any purpose other than this application. This is a hard constraint, not a user setting.
2. Collect routing facts only: destination, all nationalities or stateless/refugee status, travel-document type and issuing country, legal residence and residence status, actual application location, purpose, dates/duration, and relevant existing visas or residence permits.
   - First, ask whether the trip is a single destination or involves multiple countries or transit. Most applicants are single-destination; assume that unless the user says otherwise. If multiple countries or transit are involved, treat each leg as its own route and run the live check (step 3) separately per leg; a `mixed` verdict means the legs resolve to different routes.
   - Never infer nationality, residence, consular jurisdiction, or form language from the user's location or preferred language.
   - Treat citizenship, legal residence, current physical location, and application location as separate facts.
3. Run the mandatory live visa-need check before detailed intake.
   - Read `references/live-route-check.md`.
   - Resolve the destination in `references/jurisdictions.json`; cached starting sources are in `references/official-sources.json`.
   - Run `python3 scripts/source_registry.py live-check-plan <country> ...` when useful.
   - Browse current destination-government and responsible-mission sources for the exact passport, residence, purpose, dates, duration, entries, arrival mode, and transit itinerary.
   - Cross-check IATA Travel Centre/Timatic or the operating carrier for boarding requirements. Treat it as operational evidence, not legal authority.
   - Never reuse a static visa-free, ETA, eVisa, visa-on-arrival, or visa-required verdict.
   - If live browsing is unavailable, leave the verdict unresolved and stop; do not substitute model memory.
4. Stop at the route gate. Record the verdict, conditions, effective dates, transit result, sources, checked timestamp, conflicts, and recheck deadline in the HTML. If unresolved, keep it unresolved and name the next verification action.
5. Build the question path.
   - Load `references/core-intake.md`.
   - Load the matching full adapter from `references/countries/` when available.
   - For a source-seeded or unsupported destination, use `references/adapter-schema.md` to create a temporary adapter from official sources before detailed intake.
6. Use the `grill-me` interview pattern. If available, read `/Users/yuuue/.agents/skills/grill-me/SKILL.md`. Ask one question at a time by default and provide a recommended answer format. Use compact, numbered batches only when the user asks for fewer turns.
7. Update the HTML after every answer batch and milestone.
   - Raw answers and provenance go under `Source: Collected Answers`.
   - Normalized final values go under `Final Visa Application Preview`.
   - Required evidence goes under `Document Checklist`.
   - Uncertainty stays visible under `Open Issues`.
   - No chat note or scratch file may become more authoritative than the HTML.
8. Run `references/quality-gates.md`, then stop at the applicant review gate before portal entry. Call out inferred values, stale sources, missing documents, expiring evidence, and unresolved conflicts.
9. Assist with form entry using Browser or Computer Use after review.
   - Before filling anything, make sure the dossier HTML is open in the user's default viewer (open it if it is not) so they can follow progress while you enter the form. Keep updating that file as each field is filled; the user refreshes to see the latest.
   - In non-Codex environments, use the equivalent browser/computer capability, such as Peekaboo or the runtime's supported automation skill.
   - Never bypass CAPTCHA or security controls, invent data, or perform an applicant-only signature/certification.
10. Backfill application IDs, receipts, appointments/biometrics, document requests, decision status, and passport/visa return details into the HTML.

## Dossier Creation

Create a dossier from `assets/visa-dossier-template.html` with:

```sh
python3 scripts/create_dossier.py /path/to/visa-dossier.html \
  --country ca \
  --visa-type "Visitor visa" \
  --form-name "IRCC Portal application" \
  --application-location "Japan, Tokyo" \
  --nationality "Brazil" \
  --travel-document-issuer "Brazil" \
  --legal-residence "Japan" \
  --residence-status "Work permit holder" \
  --purpose "Tourism" \
  --arrival-date "2026-10-01" \
  --duration "14 days" \
  --entries "Single" \
  --arrival-mode "Air" \
  --transit "Singapore, airside"
```

Immediately open the dossier in the user's default viewer so they can watch it fill in as the interview proceeds. Use the platform opener: `open <path>` on macOS, `xdg-open <path>` on Linux, `start "" <path>` on Windows. Open it once; each later HTML update lands in the same file, so the user just refreshes the tab. If no opener is available (headless/remote), tell the user the local path to open manually.

## References

- Full pipeline and source freshness rules: `references/pipeline.md`
- Universal intake sections: `references/core-intake.md`
- Country adapter format: `references/adapter-schema.md`
- Mandatory live visa-need check: `references/live-route-check.md`
- Submission, document, timing, and privacy gates: `references/quality-gates.md`
- Searchable destination directory: `references/jurisdictions.json`
- Official source registry: `references/official-sources.json`
- Full country adapters: `references/countries/` — United States DS-160 (`us.md`), Schengen Type C (`schengen.md`), Canada IRCC (`ca.md`), United Kingdom (`uk.md`), Australia (`au.md`), Japan (`jp.md`). Every other destination uses a source-seeded or live-discovered adapter.
