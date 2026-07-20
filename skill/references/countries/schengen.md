# Schengen Short-Stay (Type C) Visa — Country Adapter

> Depth: rules + document-checklist. This adapter does NOT script per-field form entry: the actual
> application portals (France-Visas, VIDEX, etc.) are login-walled and not publicly scrapable.
> All rules below trace to official EU Commission sources opened live on 2026-07-20. Two figures
> from the Visa Code (Regulation 810/2009) — the €30,000 insurance minimum and the 59-month
> fingerprint-reuse window — could not be re-verified live (EUR-Lex was unreachable, HTTP 202
> bot-challenge) and are marked **Pending official verification**.

## Metadata

- **Country/area:** Schengen Area. 30 countries listed as accepting Schengen visa applications on the
  EU Commission "Applying for a Schengen visa" page (verified 2026-07-20):
  Austria, Belgium, Bulgaria, Croatia, Czechia, Denmark, Estonia, Finland, France, Germany, Greece,
  Hungary, Iceland, Italy, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Netherlands, Norway,
  Poland, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden, Switzerland — plus the applicant
  applies via the responsible member-state consulate. (Iceland, Liechtenstein, Norway, Switzerland
  are Schengen-associated non-EU states; Bulgaria, Croatia, Romania are EU states in Schengen.)
- **Supported visa routes:**
  - **Uniform short-stay visa (Type C)** — stays of up to **90 days in any 180-day period** across
    the whole Schengen area. Issued single-entry, multiple-entry, or as an **airport transit visa
    (Type A)** (transit through the international zone only — does not permit entry).
  - **ETIAS (not a visa — separate track for visa-EXEMPT travellers):** ETIAS is a travel
    *authorisation*, not a visa. Nationals who are already visa-exempt for short stays do **not**
    apply for a Type C visa; once ETIAS is operational they instead obtain an online ETIAS
    authorisation. Visa-*required* nationals still need a Type C visa and are out of ETIAS scope.
    ETIAS collects no biometrics, needs no consulate visit, and (per the ETIAS Regulation) is valid
    3 years or until passport expiry, whichever is first. **Status on 2026-07-20: ETIAS is NOT in
    operation and no applications are being collected** (per the Commission ETIAS page dated
    2025-10-06). See Route Map note and Review Risks.
- **Applicant assumptions:** Nationality- and residence-agnostic. This adapter applies to any non-EU
  national who is **visa-required** for the Schengen area. Responsible consulate = the consulate of
  the **main destination** (longest stay); if stays are of equal length across countries, the
  consulate of the **country of first entry**; as a general rule the applicant applies at the
  consulate with territorial responsibility for their country of legal residence.
- **Last verified date:** 2026-07-20
- **Official source IDs/URLs:** see `official-sources.json` block at end.
- **Support level:** `full_adapter`

## Route Map (Type C — Uniform Short-Stay Visa)

| Attribute | Value (source) |
|---|---|
| **Official name** | Schengen visa (uniform short-stay visa, Type C). Sub-forms: single-entry, multiple-entry, airport transit visa (Type A). [EU: Applying for a Schengen visa] |
| **Purpose / duration boundary** | Short, temporary visit of **up to 90 days in any 180-day period** anywhere in the Schengen area. Use the EU short-stay calculator to compute remaining allowance. [EU: Applying for a Schengen visa] |
| **Eligibility inputs** | Applicant is a national of a country whose citizens are required to hold a visa to cross the Schengen external border (check the EU visa-requirement list); purpose fits short stay (tourism, business, family/friends visit, etc.); intends to leave before 90/180 exhausted. [EU: Applying for a Schengen visa] |
| **Application authority & responsible post rule** | Lodge at the **consulate of the country you intend to visit**. Multiple countries → consulate of the country of **longest stay**. Equal-length stays → consulate of **first country of entry**. General rule: consulate with territorial responsibility for country of legal residence. [EU: Applying for a Schengen visa] |
| **Process** | Hybrid. Application is lodged at a consulate or an authorised visa service centre (which collects on behalf of consulates). May require a prior appointment. Fingerprints collected in person at submission. Some member states use an online form/portal for pre-fill, but the lodging step is in-person/consular. [EU: Applying for a Schengen visa] |
| **Form / portal** | Harmonised Schengen application form (Visa Code Annex I). Per-country online front-ends differ (e.g. France-Visas, Germany VIDEX). See Portal Workflow. |
| **Fee** | **€90 adults; €45 children aged 6–12; €35 for applicants from Armenia, Azerbaijan, and Belarus; €67.50 for applicants from Cabo Verde.** An additional service fee may apply at visa service centres. The visa fee **can be waived for specific categories of applicants**. Under the Free Movement Directive, family members of EU/EEA citizens get a **free and accelerated** procedure. [EU: Applying for a Schengen visa] |
| **Biometrics** | Fingerprints are collected in person when the application is submitted (exemptions exist for specific categories — e.g. children below the Visa Code age threshold, certain officials). Data is stored in the **Visa Information System (VIS)**; VIS performs biometric matching, primarily fingerprints. VIS retention is **5 years**. Fingerprint **59-month reuse window** (previously enrolled prints may be copied from an earlier application): **Pending official verification** (Visa Code Art. 13; EUR-Lex unreachable on 2026-07-20). [EU: Applying for a Schengen visa; EU: VIS] |
| **Appointment / interview** | An appointment may be required before lodging. Submit **at least 15 days before** the intended journey and **no earlier than 6 months** beforehand. [EU: Applying for a Schengen visa] |
| **Travel medical insurance minimum** | Medical insurance covering **emergency medical care, hospitalisation, and repatriation (including in the event of death)** is required. Minimum coverage amount of **€30,000**: **Pending official verification** (Visa Code Art. 15; EUR-Lex unreachable on 2026-07-20 — the EU applying page states the coverage scope but not the euro figure). [EU: Applying for a Schengen visa] |
| **Processing time** | Normal **15 days**; may be extended to **up to 45 days** where a more detailed examination or additional documents are needed. [EU: Applying for a Schengen visa] |
| **Policy freshness trigger** | Re-verify when: (a) the "Applying for a Schengen visa" page "last updated" date changes (was 2025-12-02); (b) ETIAS goes operational (changes the whole visa-exempt track); (c) the Entry/Exit System (EES) rollout alters biometric steps; (d) the €90 base fee is revised (Visa Code fee reviews occur periodically). |
| **Timatic / carrier cross-check note** | A valid Type C visa is necessary but not sufficient for boarding: airlines check document validity against Timatic/IATA rules (passport validity, onward/return, insurance for some carriers). The visa does not guarantee entry — border guards make the final admission decision. Cross-check passport 3-months-beyond rule against carrier boarding rules before travel. |

## Question Overlay

Questions **beyond** a universal core intake (name, DOB, passport number, contact). These map to
non-obvious fields of the harmonised Schengen application form (Visa Code Annex I) and the
responsible-post logic. Field order approximates the harmonised form where known.

| # | Field label | Expected format | Conditional trigger | Evidence source |
|---|---|---|---|---|
| 1 | Main destination member state | Country pick-list | Always. Drives which consulate is responsible. | Applicant's itinerary; longest-stay rule [EU] |
| 2 | Member state of first entry | Country pick-list | Only when stays are of equal length across countries (tie-break for responsible post). | Itinerary [EU] |
| 3 | Country of legal residence + residence-permit details | Country + permit no./validity | If applying outside country of nationality. Determines territorial competence. | Residence permit [EU] |
| 4 | Purpose sub-type of journey | Enum (tourism / business / visiting family or friends / cultural / sports / official / medical / study / transit / other) | Always. Drives the supporting-document set. | Harmonised form field 21 |
| 5 | Number of entries requested | single / two / multiple | Always. Multiple-entry needs stronger justification + longer passport-validity margin. | Harmonised form field 24 |
| 6 | Intended dates of arrival/departure + duration | Dates + day count | Always. Checked against the 90/180 allowance. | Itinerary; short-stay calculator [EU] |
| 7 | Sponsor / inviting person or company | Name, address, relationship; for company: reg. details | If purpose is family/friends visit or business, or if a host covers costs. | Invitation letter / employer letter |
| 8 | Means of support (who pays) | Enum: self / sponsor + cover type (cash, traveller's cheques, credit card, prepaid accommodation/transport, other) | Always. Feeds proof-of-funds evidence. | Harmonised form field 33; bank statements |
| 9 | Previous Schengen visas held | Yes/No + dates of last visa | Always. Multiple-entry / trusted-traveller assessment. | Prior passport/visa stickers |
| 10 | Fingerprints previously collected | Yes/No + date (if within reuse window) | Always. Determines whether biometrics must be re-enrolled. | VIS record / prior application [reuse window Pending verification] |
| 11 | Prior fingerprinting for a Schengen visa — sticker no. of prior visa | Visa sticker number | If prints previously given. | Prior visa sticker |
| 12 | Family member of an EU/EEA/CH citizen | Yes/No + relationship + citizen's details | If applicable → free & accelerated Free-Movement-Directive procedure. | Marriage/birth cert; citizen's ID [EU] |
| 13 | Minor applicant — parental authority / guardian | Guardian name, address, nationality | If applicant is a minor. | Birth certificate; consent (see Documents) |

## Documents

Nothing below is labelled mandatory unless an official EU source states it. The Commission's
"Applying for a Schengen visa" page (verified 2026-07-20) lists the required set; euro-denominated
insurance minimum is flagged Pending verification.

### Always required (per EU "Applying for a Schengen visa")
- **Valid passport.** Expiry date **at least 3 months after** the date of departure from the Schengen
  area (for multiple-entry visas, at least 3 months after departure from the last country visited).
  [EU]
  - *Issued-within-last-10-years* and *at least 2 blank pages*: **Pending official verification** — these
    are standard entry-condition rules (Schengen Borders Code) but were not stated on the EU applying
    page and EUR-Lex was unreachable on 2026-07-20. Treat as strongly expected but verify per consulate.
- **Completed visa application form** (harmonised Schengen form). [EU]
- **Photo compliant with ICAO standards.** [EU]
- **Travel medical insurance** covering emergency medical care, hospitalisation, and repatriation
  (including in the event of death). Minimum **€30,000** coverage: **Pending official verification**
  (scope confirmed by EU; euro figure from Visa Code Art. 15, EUR-Lex unreachable). [EU]
- **Supporting documents on purpose of stay.** [EU]
- **Evidence of financial means (proof of funds).** [EU]
- **Evidence of accommodation during the stay.** [EU]
- **Evidence of intention to return to the home country after the stay.** [EU]
- **Fingerprints (biometrics)** collected at submission unless exempt. [EU]

### Conditional (triggered by purpose / applicant profile)
- **Tourism:** itinerary, hotel/host reservations, round-trip transport reservation. [purpose-of-stay evidence, EU]
- **Business:** employer letter, invitation from Schengen company, event/trade-fair registration. [EU]
- **Family/friends visit:** formal invitation / proof-of-sponsorship from the host (member-state-specific form in many countries). [EU]
- **Minors:** birth certificate; **consent from parents/guardians** (and, when travelling without a
  parent, notarised consent) — form varies by consulate. [minors handling, EU form field for guardian]
- **Family member of an EU/EEA/CH national:** proof of the family relationship + the citizen's status
  → free & accelerated procedure, reduced documentary burden. [EU]
- **Fee-reduced/exempt categories:** documentation supporting reduced (€45 child 6–12; €35 AM/AZ/BY;
  €67.50 CV) or waived fee. [EU]

### Location-specific (per responsible member state / consulate)
- **Additional documents may be requested by the consulates** — the EU explicitly notes consulates may
  ask for more than the common core. [EU]
- Member-state-specific invitation/obligation forms (e.g. formal sponsorship declarations), local
  proof-of-funds thresholds, and local insurance-provider acceptance rules. Determined by the
  responsible post — see Portal Workflow. (Consulate/VFS logistics; not rule authority.)

### Generated after submission
- Application receipt / reference number (from consulate or visa service centre).
- Appointment confirmation (if biometrics/lodging appointment booked).
- Payment receipt for the visa fee (+ service-centre fee if applicable).
- Tracking reference (where a visa service centre handles logistics).
- Decision: visa sticker (single/multiple-entry, with validity + allowed days) or a refusal notice
  stating the reason and how to appeal. [EU: refusal always states reason + appeal route]

## Portal Workflow

Per-country portals differ and most require login. What is publicly knowable (page order) vs.
login-walled is marked.

**Publicly knowable, common flow:**
1. Determine responsible member state (main destination / first entry / residence) — publicly
   documented logic. [EU]
2. Reach the responsible member state's official visa front-end (examples, not exhaustive):
   France → **France-Visas**; Germany → **VIDEX** online form + consular/service-centre appointment
   booking; Italy, Spain, Netherlands, etc. → their own consular systems. (URLs vary; some are
   bot-protected — treat as logistics, not rule authority.)
3. Complete the harmonised application form (online pre-fill or paper). — *Some portals login-walled.*
4. Book an appointment (consulate or authorised visa service centre) where required. — *Booking
   systems typically login-walled.*
5. **VIS biometrics step:** attend in person; fingerprints + photo captured at lodging (unless a valid
   prior enrolment can be reused — reuse window Pending verification). [EU: VIS]
6. Upload / submit supporting documents (portal upload or in-person handover). — *Uploads
   login-walled.*
7. Pay the visa fee (+ any service-centre fee). — *Payment login-walled.*
8. Receive receipt/tracking; await decision (15 days normal, up to 45). [EU]
9. Collect passport with visa sticker or refusal notice. [EU]

**Login-walled / not publicly scrapable:** account creation, per-field form submission, appointment
calendars, document upload endpoints, payment. This adapter deliberately stops at rules +
document-checklist depth for these.

## Review Risks

- **Source conflicts (ETIAS fee):** the current Commission ETIAS page (2025-10-06) states the fee is
  **€20** (raised from the €7 in the 2018 ETIAS Regulation / 2018 Q&A memo). The €20 figure is
  current but "enters into effect as soon as ETIAS is operational" and was still in a Council/Parliament
  review window. Do not present €7 as current.
- **Insurance / coverage edge cases:** the **€30,000 minimum is Pending official verification** here —
  confirm against Visa Code Art. 15 or the responsible consulate before asserting the number. Coverage
  must be valid across all Schengen states and for the full stay; single-country-only or
  under-threshold policies are a common refusal cause. Multiple-entry applicants need policy validity
  matching each trip.
- **"Which consulate is responsible" disputes:** longest-stay vs. first-entry vs. legal-residence can
  conflict for multi-country or equal-length itineraries; the wrong post will reject as not competent.
  Resolve by the documented hierarchy: main destination (longest stay) → first entry (ties) → legal
  residence.
- **ETIAS-vs-visa confusion:** ETIAS is **not** a visa and applies only to visa-*exempt* nationals; a
  visa-required applicant cannot substitute ETIAS. As of 2026-07-20 ETIAS is **not operational**, so
  visa-exempt travellers currently need neither — but this will change on launch. Do not tell a
  visa-required applicant to "just get ETIAS."
- **Passport validity rule:** the 3-months-beyond-departure rule IS confirmed by the EU. The
  issued-within-10-years and 2-blank-pages rules are **Pending verification** here (standard Schengen
  Borders Code entry conditions, but not stated on the applying page and EUR-Lex was unreachable) —
  verify before treating as hard requirements.
- **Minors:** parental/guardian consent requirements and forms vary by consulate; missing notarised
  consent for a child travelling without a parent is a frequent rejection. Birth certificate expected.
- **Free Movement Directive path:** family members of EU/EEA/CH citizens are entitled to a free,
  accelerated procedure — misclassifying them into the standard paid track is a rights/process error.
