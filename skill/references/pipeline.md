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

Do not start a detailed questionnaire until the live route check identifies visa-free, ETA, eVisa, visa on arrival, consular visa, transit authorization, residence route, mixed, or unresolved.

Never use interface language, IP location, time zone, or the user's current city as a proxy for citizenship or residence. Citizenship, document issuer, legal residence, physical location, and consular jurisdiction can all differ.

## 2. Run The Live Visa-Need Check

Resolve the destination through `jurisdictions.json`. Use `official-sources.json` only as a set of cached starting URLs, never as a current visa-policy answer. Browse on every new application and follow this authority order:

1. National immigration authority, foreign ministry, or supranational authority such as the European Commission.
2. Embassy or consulate responsible for the applicant's legal residence.
3. Official government application portal.
4. Delegated visa application centre for logistics only.

A delegated centre can establish appointment, submission, and service-fee logistics. It cannot override government eligibility or document rules. Never treat travel blogs, agencies, forums, search snippets, or AI summaries as application authority.

Check visa exemption, ETA, eVisa, visa on arrival, consular visa, transit, and residence-permit substitution for the exact route key. Check every transit and self-transfer separately. Cross-check IATA Travel Centre/Timatic or the operating carrier for boarding requirements and label that result operational, not legal.

Apply the freshness and conflict rules in `live-route-check.md`. Do not continue to detailed intake until the verdict and its evidence are written to the HTML.

## 3. Create A Source Snapshot

Before asking detailed questions, record in the HTML:

- exact official URLs
- authority name
- page purpose
- date checked
- applicant nationality and residence used for the lookup
- travel-document issuer, residence status, and application location used for the lookup
- unresolved conflicts or location-specific requirements

Recheck immediately before filing or payment, whenever the itinerary changes, and whenever the live route check is more than 7 days old. Recheck entry and carrier requirements within 72 hours before departure.

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

## 6. Quality And Review Gates

Run `quality-gates.md`. Before browser entry, verify:

- the correct visa route and responsible post
- source snapshot is current
- every required field has a final value or explicit unresolved status
- documents support the stated purpose, funding, accommodation, and ties
- dates and identity fields are consistent across documents
- the applicant reviewed all sensitive, security, immigration-history, and declaration answers
- transit, document-format, translation/legalization, deadline/time-zone, fee/refund, evidence-expiry, and post-arrival branches are resolved

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

Progress checkpoints are: live visa-need check, intake, documents, application, fee, appointment/biometrics, decision, and passport/visa received.
