# Visa Apply Skill

Research, prepare, review, and track visa applications with current official sources and a local HTML dossier as the single source of truth.

[Website](https://yukioa2z.github.io/visa-apply/) · [Source](https://github.com/Yukioa2z/visa-apply)

```sh
npx --yes github:Yukioa2z/visa-apply
```

Then invoke. To just check whether you need a visa:

```text
Use $visa-apply: I hold an X passport, live in Y, and want to visit Z for two weeks — do I need a visa?
```

Many trips end there with a visa-free or ETA answer. To prepare a full application:

```text
Use $visa-apply to help me prepare a visa application for my destination and visa type.
```

The installer copies the skill to `~/.codex/skills/visa-apply`. For Claude Code, Hermes, OpenClaw, or another agent with a different skill directory:

```sh
npx --yes github:Yukioa2z/visa-apply -- --dest ~/.claude/skills
```

## Pipeline

1. Resolve destination, passport/status, residence, application location, purpose, dates, arrival mode, and every transit.
2. Perform a fresh official-source check for visa-free, ETA, eVisa, visa on arrival, consular visa, transit authorization, or residence route.
3. Build a country and visa-type question path.
4. Collect raw answers and normalized final values into the HTML dossier.
5. Build and review the document checklist.
6. Assist with portal entry after applicant review.
7. Backfill application IDs, fees, appointments/biometrics, decision, and passport return status.

## Coverage

The searchable directory contains 250 ISO countries/areas, including the commonly used XK code for Kosovo. Cached official starting sources cover 40 destinations plus the Schengen route area; every other destination triggers live official-source discovery. The United States DS-160 workflow remains the first full country adapter.

No cached source stores a visa-free or visa-required answer. Every case must be checked against current destination-government rules for the exact travel document, residence, purpose, date, duration, arrival mode, and transit itinerary. IATA Travel Centre/Timatic or the operating carrier is used as a boarding-document cross-check, not as legal authority.

Government immigration, foreign-ministry, and embassy pages are the rule authority. Delegated visa application centres are used only for appointment and submission logistics.

The applicant model is global. It keeps citizenship, travel-document issuer, legal residence, current location, consular application location, and transit route separate, including dual nationals, third-country applicants, minors, and holders of refugee or other non-passport travel documents.

This skill is not legal advice. The applicant must review all information and handle applicant-only declarations, signatures, certifications, CAPTCHA, and submission.
