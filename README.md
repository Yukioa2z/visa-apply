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

The searchable directory covers 250 ISO countries/areas. Any of them can be researched live; six have full adapters with rules and document checklists verified against official sources:

| Destination | Visa routes covered | Depth |
| --- | --- | --- |
| United States | B-1/B-2, F/M, J, H/L/O/P and other DS-160 nonimmigrant classes | Field-level (DS-160) |
| Schengen Area | Type C short-stay (all ~29 member states) | Rules + checklist |
| Canada | Visitor visa (TRV), eTA, Super Visa | Rules + checklist |
| United Kingdom | Standard Visitor visa, ETA | Rules + checklist |
| Australia | ETA (601), eVisitor (651), Visitor visa (600) | Rules + checklist |
| Japan | Short-stay (visa exemption, eVISA, consular) | Rules + checklist |

Every other destination uses a source-seeded start (about 40 more) or live official-source discovery. No cached source stores a visa-free or visa-required answer — every case is checked against current destination-government rules for the exact travel document, residence, purpose, dates, duration, arrival mode, and transit. IATA Travel Centre/Timatic or the operating carrier is a boarding-document cross-check, not legal authority.

Government immigration, foreign-ministry, and embassy pages are the rule authority. Delegated visa application centres are used only for appointment and submission logistics.

The applicant model is global. It keeps citizenship, travel-document issuer, legal residence, current location, consular application location, and transit route separate, including dual nationals, third-country applicants, minors, and holders of refugee or other non-passport travel documents.

## Staying current

An automated Codex maintenance task reviews registered official sources every week, investigates detected changes, updates the public reference files, and publishes a fresh package after validation. It also works through destinations that still need an official source seed. See the public [policy update log](POLICY_UPDATE_LOG.md) for dated, concise maintenance notes; applicant data and detailed local monitor state are never committed.

Automated research can miss, lag behind, or misinterpret a rule change. Visa Apply does not guarantee legal accuracy and is not legal advice. Always confirm the current rule with the destination government, responsible embassy or consulate, and operating carrier before filing or travel. The applicant must review all information and handle applicant-only declarations, signatures, certifications, CAPTCHA, and submission.
