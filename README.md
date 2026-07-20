# Visa Apply Skill

Research, prepare, review, and track visa applications with current official sources and a local HTML dossier as the single source of truth.

[Website](https://yukioa2z.github.io/visa-apply/) · [Source](https://github.com/Yukioa2z/visa-apply)

```sh
npx @yukioa2z/visa-apply
```

Run in a terminal and pick your agent when prompted. To skip the prompt, pass your agent's skills directory:

```sh
npx @yukioa2z/visa-apply -- --dest ~/.claude/skills   # Claude Code
npx @yukioa2z/visa-apply -- --dest ~/.codex/skills    # Codex
```

Then invoke. To just check whether you need a visa:

```text
Use $visa-apply: I hold an X passport, live in Y, and want to visit Z for two weeks — do I need a visa?
```

Many trips end there with a visa-free or ETA answer. To prepare a full application:

```text
Use $visa-apply to help me prepare a visa application for my destination and visa type.
```

`--dest` is your agent's skills root; the installer copies the skill into `<dest>/visa-apply`. Point it at whatever directory your agent scans — Claude Code, Codex, Hermes, OpenClaw, or another agent. Run with `--help` to see the target paths.

## Pipeline

1. Resolve destination, passport/status, residence, application location, purpose, dates, arrival mode, and every transit.
2. Perform a fresh official-source check for visa-free, ETA, eVisa, visa on arrival, consular visa, transit authorization, or residence route.
3. Build a country and visa-type question path.
4. Collect raw answers and normalized final values into the HTML dossier.
5. Build and review the document checklist.
6. Assist with portal entry after applicant review.
7. Backfill application IDs, fees, appointments/biometrics, decision, and passport return status.

## Coverage

The searchable directory contains 250 ISO countries/areas, including the commonly used XK code for Kosovo. Cached official starting sources cover 40 destinations plus the Schengen route area; every other destination triggers live official-source discovery. Full country adapters (rules and document checklist verified against official sources) exist for the United States (DS-160), Schengen (Type C), Canada (IRCC), the United Kingdom, Australia, and Japan; every other destination uses a source-seeded or live-discovered adapter.

No cached source stores a visa-free or visa-required answer. Every case must be checked against current destination-government rules for the exact travel document, residence, purpose, date, duration, arrival mode, and transit itinerary. IATA Travel Centre/Timatic or the operating carrier is used as a boarding-document cross-check, not as legal authority.

Government immigration, foreign-ministry, and embassy pages are the rule authority. Delegated visa application centres are used only for appointment and submission logistics.

## Weekly source monitoring

Every Monday at 00:00 Asia/Shanghai, GitHub Actions compares normalized content fingerprints for every registered official visa source. All 250 destinations appear in the generated monitor: destinations with registered sources receive a change status, while destinations without a source seed are explicitly marked as requiring live official-source discovery.

A new fingerprint is first recorded as a review candidate and is only confirmed as changed when the same fingerprint appears in the next run. Either state is a review signal, not a visa-policy verdict. The workflow records the result in `skill/references/policy-monitor.json`, increments the package patch version, commits the report, and dispatches the npm trusted-publishing workflow. This keeps the installable skill current without turning an arbitrary webpage edit into legal guidance.

The applicant model is global. It keeps citizenship, travel-document issuer, legal residence, current location, consular application location, and transit route separate, including dual nationals, third-country applicants, minors, and holders of refugee or other non-passport travel documents.

This skill is not legal advice. The applicant must review all information and handle applicant-only declarations, signatures, certifications, CAPTCHA, and submission.
