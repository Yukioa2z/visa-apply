# Visa Application Pipeline

## 1. Intake Routing

Collect only the routing facts first:

- destination country or area
- all nationalities, or stateless/refugee status
- travel-document type and issuing country
- country of legal residence and residence status
- current physical location and intended application location
- travel purpose
- intended arrival, duration, and number of entries
- whether the applicant already holds relevant visas or residence permits

Do not start a detailed questionnaire until the route is identified as visa-free, travel authorization, eVisa, consular visa, residence route, or still unresolved.

Never use interface language, IP location, time zone, or the user's current city as a proxy for citizenship or residence. Citizenship, document issuer, legal residence, physical location, and consular jurisdiction can all differ.

## 2. Resolve Official Sources

Use `official-sources.json` and follow this authority order:

1. National immigration authority, foreign ministry, or supranational authority such as the European Commission.
2. Embassy or consulate responsible for the applicant's legal residence.
3. Official government application portal.
4. Delegated visa application centre for logistics only.

A delegated centre can establish appointment, submission, and service-fee logistics. It cannot override government eligibility or document rules. Never treat travel blogs, agencies, forums, search snippets, or AI summaries as application authority.

## 3. Create A Source Snapshot

Before asking detailed questions, record in the HTML:

- exact official URLs
- authority name
- page purpose
- date checked
- applicant nationality and residence used for the lookup
- travel-document issuer, residence status, and application location used for the lookup
- unresolved conflicts or location-specific requirements

Recheck fees, application portals, appointment routes, and time-sensitive entry rules immediately before filing. Recheck all other requirements when the snapshot is older than 90 days.

## 4. Build The Country And Visa-Type Adapter

Load an existing adapter from `references/countries/` when available. Otherwise use `adapter-schema.md` to create a temporary adapter in the dossier from the official sources.

Compose the question set from:

- `core-intake.md`
- destination-country requirements
- visa-type requirements
- applicant-specific branches such as minors, sponsors, prior refusals, dependants, work, study, medical travel, or family relationship

Mark unsupported or uncertain branches as `Pending official verification`.

## 5. Grill And Collect

Use the `grill-me` pattern. Ask one question at a time by default and provide the recommended answer format. If the user asks for batches, group a compact set by form page or evidence category.

Write every answer to the HTML immediately:

- raw wording and provenance under `Source: Collected Answers`
- normalized value under `Final Visa Application Preview`
- required evidence under `Document Checklist`
- missing or inferred values under `Open Issues`

The HTML remains the only source of truth.

## 6. Review Gate

Before browser entry, verify:

- the correct visa route and responsible post
- source snapshot is current
- every required field has a final value or explicit unresolved status
- documents support the stated purpose, funding, accommodation, and ties
- dates and identity fields are consistent across documents
- the applicant reviewed all sensitive, security, immigration-history, and declaration answers

## 7. Assisted Form Entry

Use the available Browser or Computer Use capability. In non-Codex environments, use an equivalent browser/computer skill such as Peekaboo or the runtime's supported automation package.

Do not bypass CAPTCHA or anti-automation controls. Do not invent data. The applicant handles passwords, CAPTCHA, final declaration, signature, certification, and submission unless the official process explicitly permits an authorized representative and the user has established that authority.

## 8. Backfill And Track

After each portal milestone, update the HTML with:

- application or case number
- submission date
- fee and receipt number
- biometrics or appointment date and location
- document-request deadlines
- decision/status and passport-return details

Progress checkpoints are: research, intake, documents, application, fee, appointment/biometrics, decision, and passport/visa received.
