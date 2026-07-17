# Visa Apply Skill

Research, prepare, review, and track visa applications with current official sources and a local HTML dossier as the single source of truth.

```sh
npx --yes github:Yukioa2z/visa-apply
```

Then invoke:

```text
Use $visa-apply to help me prepare a visa application for my destination and visa type.
```

The installer copies the skill to `~/.codex/skills/visa-apply`. For Claude Code, Hermes, OpenClaw, or another agent with a different skill directory:

```sh
npx --yes github:Yukioa2z/visa-apply -- --dest ~/.claude/skills
```

## Pipeline

1. Resolve destination, all nationalities or stateless/refugee status, travel-document issuer, legal residence/status, application location, purpose, and intended stay.
2. Identify visa-free, travel authorization, eVisa, consular visa, or residence route from official sources.
3. Build a country and visa-type question path.
4. Collect raw answers and normalized final values into the HTML dossier.
5. Build and review the document checklist.
6. Assist with portal entry after applicant review.
7. Backfill application IDs, fees, appointments/biometrics, decision, and passport return status.

## First-Round Coverage

The official-source registry currently covers 28 destinations or areas across North America, Europe, Oceania, Asia, the Middle East, Africa, and South America. The United States DS-160 workflow is the first full country adapter. Other destinations are source-seeded: the skill verifies the current official pages and creates the visa-type adapter before collecting detailed answers.

Government immigration, foreign-ministry, and embassy pages are the rule authority. Delegated visa application centres are used only for appointment and submission logistics.

The applicant model is global. It keeps citizenship, travel-document issuer, legal residence, current location, and consular application location separate, including dual nationals, third-country applicants, and holders of refugee or other non-passport travel documents.

This skill is not legal advice. The applicant must review all information and handle applicant-only declarations, signatures, certifications, CAPTCHA, and submission.
