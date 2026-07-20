# United Kingdom Adapter: Standard Visitor visa (and the ETA branch)

Support level: `full_adapter` (rules + document-checklist depth; the UKVI apply portal is login-walled and not field-scriptable). All fees, rules, and the full TB country list verified live against gov.uk on 2026-07-20.

## Metadata

- **Country/area:** United Kingdom (England, Scotland, Wales, Northern Ireland; ETA also covers Jersey, Guernsey, Isle of Man)
- **Supported visa routes:**
  - **Standard Visitor visa** — for nationals who must hold a visa before travel. Sub-purposes within the same route: tourism, family/friends, business activities, study (courses ≤6 months), Permitted Paid Engagement, academic/senior doctor/dentist, medical treatment. **Marriage/civil partnership is *not* covered** — a separate Marriage Visitor visa is required.
  - **ETA branch (Electronic Travel Authorisation)** — for visa-exempt nationals who still need pre-travel authorisation. **An ETA is not a visa** and does not use the visa-application workflow.
- **Applicant assumptions:** Nationality- and residence-agnostic. Whether a person needs a Standard Visitor visa, an ETA, or nothing is determined solely by nationality + purpose via the official "Check if you need a UK visa" tool. This adapter drives the visa-form workflow **only when the applicant needs a Standard Visitor visa**; ETA applicants are routed to the ETA app/online flow instead.
- **Last verified date:** 2026-07-20
- **Official source IDs/URLs:** see `official-sources.json` (all gov.uk / Home Office).
- **Support level:** `full_adapter`

## Route Map

### Branch selector (run first)
Determine, from nationality + purpose, which of three states applies (source: gov.uk/standard-visitor, gov.uk/eta):
1. **Needs a Standard Visitor visa** → run the visa workflow below.
2. **Needs an ETA** (visa-exempt but authorisation-required: typically Europe, USA, Australia, Canada and certain others) → run the ETA flow. **Not a visa.**
3. **Needs neither** (e.g., British/Irish passport holders, or those with existing UK permission) → no pre-travel document; must still meet visitor eligibility at the border.

Authoritative selector tool: "Check if you need a UK visa" — https://www.gov.uk/check-uk-visa

> Note: Even someone who only *needs* an ETA (or nothing) **may choose to apply for a Standard Visitor visa** if they have a prior UK refusal or a criminal record (gov.uk/standard-visitor).

### Standard Visitor visa
- **Official name:** Standard Visitor visa (UK Visas and Immigration / UKVI, Home Office).
- **Purpose/duration:** Visits for tourism, business, short study (≤6 months), permitted paid engagements, medical, academic. Usual max stay **6 months** per visit.
- **Eligibility (source: gov.uk/standard-visitor):** passport/travel document valid for the whole stay; will leave at end of visit; can support self + dependants (or funded by someone); can pay for return/onward journey; will not make the UK a main home via frequent/successive visits.
- **Application authority:** UKVI, applied for **online** before travel; biometrics at a Visa Application Centre (VAC).
- **Form/portal:** Online apply (login-walled) via gov.uk "Apply now" → https://www.gov.uk/standard-visitor/apply-standard-visitor-visa
- **Fees (current, GBP — source: gov.uk/standard-visitor/apply-standard-visitor-visa):**

  | Product | Fee | Max stay |
  |---|---|---|
  | Standard Visitor visa | **£135** | 6 months |
  | Standard Visitor (medical reasons) | £234 | 11 months |
  | Standard Visitor (academics) | £234 | 12 months |
  | Long-term 2-year | £506 | 6 months/visit |
  | Long-term 5-year | £903 | 6 months/visit |
  | Long-term 10-year | £1,128 | 6 months/visit |
  | Visitor in Transit (transit-only) | £74.50 | — |

- **Biometrics / BRP-vs-eVisa:** Fingerprints + photo taken at the VAC (or, for some, verified via the UK Immigration: ID Check app). The UK has **moved to eVisas** — a digital immigration status in a UKVI account — replacing physical BRPs/documents. Any passport vignette (sticker) issued remains valid until it expires. (Source: https://www.gov.uk/evisa)
- **Appointment:** Booked as part of the online application; attend at a VAC. Passport returned same day; other documents may be retained during processing.
- **Timing:** Earliest apply = **3 months** before travel. Decision **usually within 3 weeks**.
- **Freshness trigger:** Re-verify if fee table changes, if eVisa rollout status changes, or if the visa/ETA nationality mapping changes. Re-check the visa-fees.homeoffice.gov.uk calculator and gov.uk/standard-visitor.
- **Timatic/carrier note:** Carriers check pre-travel authorisation status. For visa nationals, the vignette/eVisa is the credential; for ETA nationals, the ETA is linked to the passport (no document shown beyond the passport).

### ETA branch
- **Official name:** Electronic Travel Authorisation (ETA), UKVI/Home Office. **Not a visa.**
- **Who needs it:** Visa-exempt visitors "usually from Europe, the USA, Australia, Canada or certain other countries" (source: gov.uk/eta). Confirm per nationality via the check tool.
- **Who does not:** British/Irish passport holders; anyone with existing permission to live/work/study in the UK. Every traveller including babies/children needs their own ETA. Also required for **landside transit** through a UK airport.
- **Fee:** **£20** (source: gov.uk/eta/apply). Beware imitation sites charging more.
- **Validity:** **2 years or until passport expires, whichever is sooner**; multiple visits, each up to 6 months.
- **Apply:** UK ETA **app** (scan passport + face) or **online** (upload passport photo + face photo). Needs passport, email, card/Apple Pay/Google Pay. Decision **usually within a day**, allow up to **3 working days**. A 16-digit ETA reference is emailed; ETA is linked to the passport. (Source: https://www.gov.uk/eta/apply)
- **Does not guarantee entry.**

## Question Overlay

Field order below reflects gov.uk's stated "Documents and information you'll need" (source: gov.uk/standard-visitor/apply-standard-visitor-visa). The actual multi-step portal is login-walled; exact widget order is not publicly scrapable.

**Always asked (core intake):**

| Field | Format | Trigger | Evidence source |
|---|---|---|---|
| Planned travel dates to UK | Date range | Always | Applicant plan |
| Where you'll stay in the UK | Address/text | Always | Booking / host address |
| Estimated trip cost | Amount (GBP) | Always | Applicant estimate |
| Current home address + duration there | Address + years | Always | Proof of residence |
| Parents' names + DOB (if known) | Names/dates | Always | — |
| Annual income (if any) | Amount | Always | Payslips/bank |
| Criminal / civil / immigration offences | Declaration | Always | Applicant declaration |

**Conditional:**

| Field | Trigger | Evidence source |
|---|---|---|
| Travel history for past 10 years | If applicable to circumstances | Passport stamps/visas |
| Employer address + phone | If employed | Employer |
| Partner name, DOB, passport number | If has partner | Partner passport |
| Name/address of anyone paying for the trip | If third-party funded | Sponsor |
| Name/address/passport of UK-based family | If family in UK | Relative documents |
| TB certificate | Only if visiting **6+ months** and lived in a listed country (see Documents) | Approved TB clinic |
| Accompanying adult(s) — up to 2 named | If applicant is under 18 | Adult passports; names appear on the visa |
| Extra evidence for study / academic / PPE / medical sub-purposes | If that sub-purpose | Sub-purpose docs |

Non-English/Welsh documents require **certified translations**.

## Documents

### Always (Standard Visitor)
- **Passport / travel document** valid for the whole stay (source: gov.uk/standard-visitor, /apply-standard-visitor-visa). *Mandatory.*
- **Biometrics** — fingerprints + photo taken at the VAC (source: /apply-standard-visitor-visa). *Mandatory.*
- Evidence supporting eligibility: funds to support self/dependants, ability to pay return/onward journey, intent to leave (source: gov.uk/standard-visitor eligibility section). *Mandatory to demonstrate.*

### Conditional
- **Funds / income evidence** (bank statements, payslips) — to show maintenance and return-journey funds. (gov.uk/standard-visitor eligibility)
- **Accommodation & travel plan** — where you'll stay, trip dates, cost. (/apply-standard-visitor-visa)
- **Employment / purpose evidence** — employer details; for study/academic/PPE/medical, "additional documents" are required per sub-purpose. (/apply-standard-visitor-visa)
- **Sponsor / third-party funder details** — name and address of anyone paying. (/apply-standard-visitor-visa)
- **Minors (under 18):** written parental/guardian consent to travel (if travelling alone) + full contact details; proof of suitable accommodation; identification of up to 2 accompanying adults in the application; possible local-authority notification for private foster care. (Source: https://www.gov.uk/standard-visitor/if-youre-under-18)
- **Certified translations** for any non-English/Welsh document. (/apply-standard-visitor-visa)

### Location-specific — TB test certificate
Required **only if** all are true: coming to the UK for **6 months or more**, AND lived 6+ months in a listed country, AND lived there (or another listed country) within the last 6 months. (Source: https://www.gov.uk/tb-test-visa)

> Practical note: a **standard 6-month Standard Visitor visa does not trigger the TB requirement** (it applies at "6 months or more" stays). It becomes relevant for the 11-month medical and 12-month academic visitor variants. Certificate valid **6 months** from x-ray date. Full authoritative country list: gov.uk/tb-test-visa/countries-where-you-need-a-tb-test.

### Generated after submission
- **Decision email** from the Home Office (next-steps instructions).
- **Visa vignette (sticker)** in passport where issued, and/or **eVisa** — a digital status accessed via a UKVI account; used to generate a share code to prove status (source: gov.uk/evisa). Physical BRPs have been replaced by eVisas.

### ETA (documents)
- Passport to be travelled with; a face photo (and passport photo if applying online for another person). No supporting-document upload beyond photos. (gov.uk/eta/apply)

## Portal Workflow

### Standard Visitor (gov.uk apply flow)
1. **Check** you need a visa (public) — https://www.gov.uk/check-uk-visa
2. **Start application** online via "Apply now" (public entry point; **login-walled** thereafter) — /apply-standard-visitor-visa. Can save and resume.
3. **Complete the online form** (login-walled) — intake fields per Question Overlay.
4. **Pay the fee** (login-walled). £135 for 6-month visit; other products per fee table.
5. **Book biometrics appointment** at a VAC as part of the application (login-walled booking).
6. **Attend the VAC** (or use the UK Immigration: ID Check app where offered) — prove identity, give fingerprints + photo, submit required documents. Passport returned same day.
7. **Decision** by email (usually ≤3 weeks).
8. **eVisa / UKVI account** — set up/access the UKVI account to view the digital status and generate share codes (public guidance: gov.uk/evisa; account access is login-walled).

*Family members each need a separate application, fee, and appointment; a parent/partner may apply on behalf of a child/partner who cannot apply themselves.*

### ETA flow (not the visa workflow)
1. Confirm ETA (not visa) is required via the check tool.
2. Apply via UK ETA app (scan passport + face) or online (upload photos). Pay £20.
3. Await email decision (usually within a day; up to 3 working days) with 16-digit reference. ETA is linked to the passport.

## Review Risks
- **ETA-vs-visa confusion (highest risk):** An ETA is **not a visa** and uses a different app/online flow. Routing an ETA-eligible national into the Standard Visitor visa workflow (or vice versa) is the primary failure mode. Always run the check tool first, keyed on nationality **and** purpose.
- **TB certificate by country/duration:** Only triggers at **6+ month** stays for listed countries — so it generally does **not** apply to the standard 6-month visitor visa, but **does** apply to the 11-month medical and 12-month academic variants. Watch the "get tested in another country" exceptions and the 6-month certificate validity.
- **Funds sufficiency & intent to leave:** Weak maintenance evidence or a travel pattern suggesting the UK as a main home is a common refusal ground; long-term visas can be cancelled for repeated extended residence.
- **eVisa transition:** No physical BRP for new grants; applicants must set up a UKVI account and use share codes to prove status. Legacy vignettes remain valid until expiry.
- **Refusal / criminal history:** Must be declared. Prior refusal or a criminal record may make it advisable to apply for a Standard Visitor visa even when only an ETA/nothing is otherwise required.
- **Minors:** Consent letters, accompanying-adult identification (max 2, named on the visa), and possible local-authority notification for private foster care are easy to miss.
