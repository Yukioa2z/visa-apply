---
name: visa-apply
description: Use when helping a user research, prepare, review, track, or fill a visa, travel authorization, eVisa, study permit, work permit, or related entry application for any destination country. Uses current official sources, country and visa-type question branching, a local HTML dossier as the single source of truth, document and progress tracking, and assisted browser/computer form entry after applicant review.
---

# Visa Apply

## Purpose

Create and maintain a local HTML dossier as the single source of truth for a visa application. Resolve the correct country and visa route from current official sources, collect applicant facts with a country/visa-specific question path, prepare a final form preview and document checklist, then assist with portal entry after applicant review.

This skill is not legal advice. The applicant must review every answer and handle any applicant-only declaration, signature, certification, CAPTCHA, and submission.

## Required Workflow

1. Confirm privacy mode before storing personal data. A complete local copy requires explicit consent.
2. Collect routing facts only: destination, all nationalities or stateless/refugee status, travel-document type and issuing country, legal residence and residence status, actual application location, purpose, dates/duration, and relevant existing visas or residence permits.
   - Never infer nationality, residence, consular jurisdiction, or form language from the user's location or preferred language.
   - Treat citizenship, legal residence, current physical location, and application location as separate facts.
3. Resolve the official source set.
   - Read `references/official-sources.json`.
   - Run `python3 scripts/source_registry.py show <country>` when useful.
   - Government immigration/foreign-ministry sources control requirements. Delegated visa centres control logistics only.
   - Recheck current sources before relying on stored knowledge.
4. Identify the route: visa-free, travel authorization, eVisa, consular visa, residence route, or unresolved.
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
8. Stop at the applicant review gate before portal entry. Call out inferred values, stale sources, missing documents, and unresolved conflicts.
9. Assist with form entry using Browser or Computer Use after review.
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
  --application-location "China, Shanghai" \
  --nationality "China" \
  --travel-document-issuer "China" \
  --legal-residence "China" \
  --residence-status "Citizen" \
  --purpose "Tourism"
```

## References

- Full pipeline and source freshness rules: `references/pipeline.md`
- Universal intake sections: `references/core-intake.md`
- Country adapter format: `references/adapter-schema.md`
- Official source registry: `references/official-sources.json`
- United States DS-160 adapter: `references/countries/us.md`
