# Japan Adapter: Short-Term Stay (Temporary Visitor) visa

Support level: `full_adapter` (rules + document-checklist depth). Covers tourism, visiting relatives/friends, and short-term business (no remunerated activity). Rules verified live against mofa.go.jp on 2026-07-20.

## Metadata

- **Country/area:** Japan
- **Visa class covered:** Short-Term Stay (Temporary Visitor / 短期滞在).
- **Supported visa routes:**
  1. **Visa exemption (visa-free short-term stay)** — Japan has reciprocal visa-exemption arrangements with 74 countries/regions (MOFA, dated Sept 1, 2025). Exempt travellers need NO visa for short-term stay. **Must be checked per nationality against the official MOFA exemption page** — the list changes and carries per-country notes (e.g., Indonesia requires prior "Visa Waiver Registration"; Thailand/Indonesia 15-day stay; Brunei/Qatar 30-day; others up to 90 days). Do NOT hard-code a stale list.
  2. **JAPAN eVISA (electronic visa)** — online single-entry short-term-stay visa, **tourism purpose only**, up to 90 days, for ordinary-passport holders who are NOT visa-exempt and reside in eligible countries/regions. Issued electronically (no sticker); displayed as a "Visa Issuance Notice" at boarding.
  3. **Consular short-term-stay visa** — the standard route via the Japanese Embassy/Consulate-General/Consular Office (or, in some jurisdictions, only via an accredited travel agency / Japan Visa Application Centre). Covers all short-term purposes and single- or multiple-entry.
- **Purpose-driven document differences:** Tourism, visiting relatives/friends, and short-term business each require a distinct evidence set (see Documents). Tourism is lightest; visiting relatives/friends and business add inviter/guarantor documents.
- **Applicant assumptions:** Nationality- and residence-agnostic. Applicable route is a function of (nationality × country of residence). **In some jurisdictions applications cannot be lodged directly at the mission and MUST go through an accredited/approved travel agency** — most notably China (all short-term-stay purposes route through an approved Chinese travel agency), and packaged-tour routing for the Philippines and Viet Nam.
- **Last verified date:** 2026-07-20
- **Official source IDs/URLs:** see `official-sources.json`.
- **Support level:** `full_adapter`

## Route Map

### Route 0 — Visa exemption (pre-route gate, not an application)
- **Official name:** Exemption of Visa (Short-Term Stay).
- **Purpose/duration:** Short-term stay; stay period granted at landing is 90 days for most, 30 days (Brunei, Qatar), or 15 days (Indonesia, Thailand). Not extendable as a rule; no remunerated activity.
- **Eligibility:** Nationals of the 74 exemption countries/regions on the MOFA novisa page, subject to per-country notes. **Determination is per nationality — always resolve live.**
- **Authority:** MOFA (rules); landing permission granted by Immigration at port of entry (not a guarantee of entry).
- **Process:** No visa application. Traveller boards and seeks landing permission on arrival.
- **Freshness trigger:** MOFA novisa page "last updated" date changes; any note about a suspended/added country.
- **Timatic/carrier note:** Carriers check visa/exemption status at check-in. If exempt, no visa; if not exempt, proceed to eVISA or consular route below.

### Route 1 — JAPAN eVISA (single-entry short-term, tourism only)
- **Official name:** JAPAN eVISA system (electronic visa).
- **Purpose/duration:** Single-entry short-term stay for **tourism**, up to 90 days. (Special stay lengths: China residents 15/30 days; Viet Nam and Philippines residents 15 days.)
- **Eligibility (per MOFA eVISA info, dated May 15, 2026):** Ordinary-passport holder; NOT a national of a visa-exemption country; travelling by international flight or scheduled passenger ferry; single-entry, tourism, <90 days. Direct online application for residents of: Australia, Brazil, Cambodia, Canada, Saudi Arabia, South Africa, Taiwan, United Kingdom, U.S.A. Additional residence groups apply **through an accredited agency**: China, Philippines and Viet Nam (packaged tour), and Hong Kong, India, Indonesia, Macau, Mongolia, Republic of Korea (except Jeju consulate jurisdiction), Singapore, UAE. Not available if: dual Japanese national; multiple-entry sought; purpose other than tourism; prior conviction/deportation.
- **Application authority & mission:** MOFA operates the portal; the responsible overseas establishment examines and may summon for interview.
- **Process (portal):** (1) verify visa need & documents, (2) enter application information, (3) receive examination result by email, (4) pay fee online by credit card (only online payment; no cash), (5) eVISA issued.
- **Form/portal:** eVISA portal (https://www.evisa.mofa.go.jp/index). Required documents vary by residence/nationality and surface inside the portal (login-walled).
- **Fee:** Set per reciprocity/nationality; paid online by card. Some nationalities fee-exempt by bilateral agreement (portal auto-issues). Exact figure confirmed inside portal / by responsible mission — treat numeric fee as **verify per mission**.
- **Biometrics note:** No routine biometric capture for eVISA; in-person interview may be requested.
- **Freshness trigger:** MOFA eVISA "As of <date>" changes; portal eligibility list changes.
- **Timatic/carrier note:** No sticker. Traveller must display the "Visa Issuance Notice" (with QR) **live on a device** at check-in — PDF, screenshot, or printout are NOT accepted (proxy applicants excepted). Carrier verifies at boarding.

### Route 2 — Consular short-term-stay visa (standard)
- **Official name:** Short-Term Stay visa (Temporary Visitor).
- **Purpose/duration:** Tourism, visiting relatives/friends, or short-term business affairs; typically up to 90 days per stay; single- or multiple-entry (multiple-entry has additional criteria/forms). No remunerated activity.
- **Eligibility:** Non-exempt travellers, or those needing a purpose the eVISA does not cover (visiting relatives/friends, business, multiple-entry).
- **Application authority & responsible mission:** Japanese Embassy / Consulate-General / Consular Office with jurisdiction over the applicant's place of residence (Taiwan: Taipei/Kaohsiung offices of the Japan-Taiwan Exchange Association). MOFA sets rules.
- **Process:** Prepare documents → submit at the consular section of the responsible mission, **or at an accredited agency / Japan Visa Application Centre, or online, by the method the responsible mission specifies**. Applications cannot be made inside Japan. Inviter/guarantor sends their documents to the applicant.
- **Accredited-agency-only jurisdictions:** China — all short-term-stay purposes must be lodged **through an approved Chinese travel agency**; the applicant cannot apply directly. Philippines/Viet Nam packaged-tour tourism similarly route through designated agencies.
- **Form/portal:** MOFA "Visa application form (English)" PDF. Supporting form templates (letter of guarantee, invitation letters single/multiple, list of applicants, company overview, travel itinerary) linked from the MOFA short-term-stay page.
- **Fee:** Reciprocity-based and **set per mission**, paid at the mission/agency. MOFA does not publish a single universal figure; missions commonly state roughly 3,000 yen (single-entry), 6,000 yen (multiple-entry), 700 yen (transit) or local-currency equivalents — but this **varies by nationality/reciprocal agreement and some categories are waived**. Marked: numeric fee = **verify per responsible mission.**
- **Biometrics note:** No routine consular biometric enrolment for short-term stay in general; some missions/agencies may require in-person submission or interview.
- **Freshness trigger:** MOFA short-term-stay / responsible mission page date changes; checklist PDF revision date; change to accredited-agency list.
- **Timatic/carrier note:** Visa sticker affixed in passport; carrier verifies at check-in. Processing time is at least 5 working days from the day after receipt; additional documents may be requested case-by-case.

## Question Overlay

Beyond core intake (identity, passport, travel dates), Japan's short-term form/checklist order where publicly known (source: MOFA application form, single-entry checklist PDF):

| Field label | Format | Conditional trigger | Evidence source |
|---|---|---|---|
| Purpose of visit (Tourism / Visiting relatives/friends / Short-term business) | Enum | Always | Applicant declaration; drives document set |
| Passport number, type, nationality | String | Always | Passport |
| Date of arrival / departure (DD/MM/YYYY) | Date | Always | Flight/ship itinerary |
| Flight/ship number & itinerary | String | Always | Booking |
| Itinerary in Japan / schedule of stay (滞在予定表) | Structured day-by-day | Always (esp. visiting/business) | MOFA "Travel itinerary" template |
| Guarantor (身元保証人) — name, address, relationship, occupation, income | Person/org | Business, or visiting relatives/friends where a guarantor covers expenses | Letter of Guarantee (MOFA template); guarantor proof of funds, Juminhyo |
| Inviter (招へい人) — name, org, relationship, reason for invitation | Person/org | Visiting relatives/friends; business | Letter of Invitation (MOFA template); reason-for-invitation document |
| Relationship to inviter/guarantor | Enum + evidence | Visiting relatives/friends | Kinship: birth/marriage certificate, family register (Kosekitohon). Friends: photos, emails, call history, letters |
| Who pays travel expenses (self / inviter / guarantor) | Enum | Always | If self: applicant bank statement/income certificate. If guarantor: guarantor financial docs |
| Proof of funds | Doc | Always (self-funded) or on guarantor | Income certificate / tax return by public agency, or bank statement / balance certificate |
| Consent to accredited-agency handling of data & fee | Checkbox | When applying via accredited agency | MOFA application form |

## Documents

### Always required (all purposes) — source: MOFA single-entry checklist, application form
- **Valid passport.**
- **Visa application form ×1.**
- **Photo ×1** — **45 mm × 35 mm** (or 2 in × 1.4 in), taken within the last 6 months, plain untextured background, face centered; not a re-shot passport/licence/group photo.
- **Itinerary with flight/ship number and dates of arrival/departure.**
- **Proof of ability to pay travel/stay expenses** (self-funded: income certificate or public-agency tax return, or bank statement / balance certificate).

### Conditional — Tourism
- **Daily itinerary/schedule of stay in Japan** (滞在予定表) — MOFA "Travel itinerary" template.

### Conditional — Visiting relatives/friends
- **Document proving kinship/friendship/acquaintance** — relatives: birth/marriage certificate, family register (Kosekitohon); friends/acquaintances: photos, emails, call history, letters.
- **Letter of Invitation** (MOFA template).
- **Reason-for-invitation document** (e.g., graduation/wedding notice, medical certificate).
- **List of visa applicants** (if more than one applicant).
- **Schedule of stay in Japan.**
- **If a guarantor covers expenses:** Letter of Guarantee; guarantor proof of funds (income/taxation certificate or balance certificate; withholding-tax slip NOT accepted); Certificate of residence (Juminhyo) listing all family members' relationships; if guarantor is a foreign national, copy of both sides of Residence Card / special permanent resident certificate.

### Conditional — Short-term business
- **Document proving business purpose** (travel order from employer, letter from employer, or equivalent).
- **Certificate of employment.**
- **Invitation letter** or documents explaining activities (inter-company transaction agreement, conference materials).
- **List of visa applicants** (if multiple).
- **Schedule of stay in Japan.**
- **If a guarantor in Japan covers expenses:** Letter of Guarantee + certified copy of corporation register or Overview of company/organization (waived if listed company filing quarterly reports; individual guarantor may substitute Certificate of employment).

### Location-specific
- **China residents (Chinese nationals):** documents defined and lodged by an **approved Chinese travel agency**; applicant does not apply directly.
- **Nationality/residence-specific checklists** (single vs multiple entry, per region) linked from the MOFA short-term-stay page.
- **Per-mission variations:** the responsible mission may add documents; confirm on its page.

### Generated after submission
- **eVISA:** "Visa Issuance Notice" (QR) displayed live on a device at check-in (Route 1).
- **Consular:** visa sticker affixed in passport (Route 2).

## Portal Workflow

**JAPAN eVISA portal — publicly knowable steps:**
1. **Eligibility check** (public) — confirm ordinary passport, non-exempt nationality, eligible residence, tourism, single-entry, <90 days, air/sea entry. Portal links to the MOFA exemption list.
2. **Verify visa need & required documents** (partly public; exact doc set surfaces after residence/nationality selection).
3. **Create account / enter application information** (*login/eligibility-walled*; personal data and uploads).
4. **Examination** — mission may request an in-person interview (*walled*); result emailed.
5. **Fee payment** (*walled*; online credit card only; auto-skipped if fee-exempt).
6. **eVISA issuance** — issued electronically; no passport sticker.
7. **At boarding/entry** — display "Visa Issuance Notice" (QR) live on a device; PDF/screenshot/printout not accepted (proxy applicants excepted).

**Consular route:** Often lodged **through an accredited agency / Japan Visa Application Centre, not directly at the mission** — determined by the responsible mission. China short-term stay is agency-only. There is no single national online consular portal for these purposes; the method is specified per mission.

## Review Risks

- **Visa-exemption vs visa confusion:** The single biggest error. Many nationalities need NO visa for short-term stay; others do. Must resolve live per nationality (note per-country stay lengths and conditions, e.g., Indonesia's Visa Waiver Registration, Thailand/Indonesia 15 days). Do not apply for a visa when exempt, and do not assume exemption.
- **eVISA eligibility scope:** eVISA is **tourism-only, single-entry, ordinary passport, eligible residence**. Any of visiting relatives/friends, business, study, work, transit, or multiple-entry disqualifies the eVISA path — route to consular. Direct-online vs agency-mediated eVISA residences differ.
- **Accredited-agency-only jurisdictions:** China (all short-term purposes), and Philippines/Viet Nam packaged-tour tourism, cannot be lodged directly — must go through an approved/designated agency. Missing this produces a dead-end intake.
- **Inviter/guarantor document burden:** Visiting relatives/friends and business add the heaviest set (invitation letter, reason for invitation, guarantor letter, guarantor financials, Juminhyo, corporation register). Distinguish "who pays" (self vs guarantor).
- **Single vs multiple entry:** Different checklists, forms, and fees; multiple-entry has extra eligibility criteria.
- **Purpose-specific doc sets:** Tourism, visiting relatives/friends, and business each have a distinct item list in the checklist PDF — do not merge them.
- **Fee ambiguity:** Fees are reciprocity-based and set per mission; some categories waived by bilateral agreement. Never quote a fixed figure without confirming the responsible mission's tariff.
- **eVISA presentation trap:** eVISA must be shown live on a device at boarding; PDF/screenshot/print is rejected — a common denied-boarding cause.
- **Visa ≠ entry:** A visa (or exemption) does not guarantee entry; landing permission is decided by Immigration at the port.
