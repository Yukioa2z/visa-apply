# Australia Adapter: Visitor entry (601 ETA / 651 eVisitor / 600 Visitor visa)

Support level: `full_adapter` (rules + document-checklist depth; ImmiAccount is login-walled and not field-scriptable). Rules, fees, and document requirements verified live against immi.homeaffairs.gov.au on 2026-07-20. The 601 page's last-updated stamp is 12/08/2025.

## Metadata

- **Country/area:** Australia
- **Supported visa routes:**
  - **Subclass 601 — Electronic Travel Authority (ETA)** — tourist / family visit / business visitor activities, applied via the Australian ETA app.
  - **Subclass 651 — eVisitor** — same activities, applied via ImmiAccount, free.
  - **Subclass 600 — Visitor visa** — full visitor visa with streams: **Tourist (apply outside Australia)**, **Tourist (apply in Australia / onshore)**, **Business Visitor**, **Sponsored Family**, **Approved Destination Status (ADS)**, **Frequent Traveller**.
- **Applicant assumptions:** Nationality/passport determines route eligibility. Applicant is outside Australia for 601, 651, Tourist-overseas, Business, Sponsored Family, ADS, Frequent Traveller; onshore only for the Tourist (apply in Australia) stream. Not an Australian citizen. Purpose is a genuine short-term visit, not paid work or study >3 months.
- **Last verified date:** 2026-07-20
- **Official source IDs/URLs:** see `official-sources.json`.
- **Support level:** `full_adapter`

## Route Map

### Subclass 601 — Electronic Travel Authority (ETA)
- **Official name:** Electronic Travel Authority (subclass 601).
- **Purpose / duration:** Tourism, visit family or friends, or business-visitor activities. Study/train up to 3 months total. Valid for travel **12 months** (or passport validity if shorter), **multiple entry**, **stay up to 3 months per entry**.
- **Eligibility (passports):** Must hold a valid passport from an **ETA-eligible country/jurisdiction** (incl. Andorra, Austria, Belgium, Brunei, Canada, Denmark, Finland, France, Germany, Greece, Hong Kong SAR, Iceland, Ireland, Italy, Japan, Liechtenstein, Luxembourg, Malaysia, Malta, Monaco, Norway, Portugal, San Marino, Singapore, South Korea, Spain, Sweden, Switzerland, Taiwan (non-official/diplomatic), Netherlands, UK–British Citizen, UK–British National (Overseas), USA, Vatican City). No non-citizen passport / certificate of identity / Titre de Voyage. Australian citizens ineligible.
- **Application authority / process:** Department of Home Affairs, via the **Australian ETA app** (iOS/Android) — scan passport, live photo, answer questions (incl. criminal-conviction declaration), pay, submit. Not applied through ImmiAccount.
- **Fee:** **No Visa Application Charge; AUD 20 service charge to use the Australian ETA app.**
- **Health/character routing:** If the applicant has previously failed the health requirement, has a criminal conviction, or will enter health-care/hospital environments (or train as doctor/dentist/nurse/paramedic/childcare) → **do not use ETA; apply subclass 600.**
- **Freshness trigger:** ETA is linked to the passport used; **ETA ceases if that passport expires or is replaced** — must re-apply. Verify fee/eligible-passport list each cycle (page last updated 12/08/2025).
- **Timatic/carrier note:** Digitally linked to passport, no label; carriers verify at check-in. Do not book travel until granted.

### Subclass 651 — eVisitor
- **Official name:** eVisitor (subclass 651).
- **Purpose / duration:** Same activities as ETA. Valid for travel **12 months from grant**, **multiple entry**, **stay up to 3 months per entry**.
- **Eligibility (passports):** Must be a **citizen of and hold a passport from a European eligible country** (Andorra, Austria, Belgium, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Iceland, Ireland, Italy, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Monaco, Netherlands, Norway, Poland, Portugal, Romania, San Marino, Slovakia, Slovenia, Spain, Sweden, Switzerland, UK–British Citizen, Vatican City). Cannot apply with a non-citizen passport/CoI/Titre de Voyage, or BN(O)/British Dependent Territories/British Overseas Citizen/British Protected Person/British Subject passports. Australian citizens ineligible.
- **Application authority / process:** Department of Home Affairs via **ImmiAccount** (online); form ID **`TV-AP-651`**.
- **Fee:** **Free.**
- **Health/character routing:** As for 601 — criminal conviction / prior health failure / health-care environments → **apply subclass 600 instead.** May be asked for a police certificate.
- **Timatic/carrier note:** No label; carriers verify at check-in. Applicant must be outside Australia at grant.

### Subclass 600 — Visitor visa (streams)
- **Official name:** Visitor visa (subclass 600).
- **Purpose:** For everyone not eligible/able to use 601 or 651, or with longer/specific-purpose needs (criminal conviction, prior health-requirement failure, health-care environments, sponsored family visits, ADS tour groups, long-validity frequent travel).
- **Application authority / process:** Department of Home Affairs via **ImmiAccount**. **All streams use form ID `VSS-AP-600`.**
- **Streams — duration, location, base Visa Application Charge (VAC, current AUD):**

  | Stream | Location | Stay | Base VAC (AUD) | Notes |
  |---|---|---|---|---|
  | Tourist — apply outside Australia | Offshore | 3, 6 or 12 months | **from 250** | Tourism/family/friends |
  | Tourist — apply in Australia (onshore) | Onshore | up to 12 months | **from 630** | Stay/extend from within Australia |
  | Business Visitor | Offshore | up to 3 months | **250** | Business-visitor activities only; ABTC interaction |
  | Sponsored Family | Offshore | up to 12 months | **250** | Requires eligible sponsor; **sponsor may pay a security bond** |
  | Approved Destination Status (ADS) | Offshore | as granted | **250** | PRC citizens (excl. SARs) on organised tour group |
  | Frequent Traveller | Offshore | validity up to **10 years**, 3 months/entry | **1,845** | Citizens of PRC, Brunei, Cambodia, Philippines, Laos, Indonesia, Malaysia, Singapore, Thailand, Vietnam, Timor-Leste |

  **Cost concession:** From 1 July 2026 a lower visa cost applies to eligible Pacific Island and Timor-Leste citizens (recognised by passport in ImmiAccount). Use the **Visa Pricing Estimator** for the exact charge — the base VAC excludes second-instalment and subsequent-family-member charges.
- **Biometrics/health:** Health examinations may be required (before applying or when requested; mandatory-context for health-care/hospital environments, long stays, parents seeking longer visas). Biometrics if requested. Police certificate(s) if requested / where character concerns.
- **Freshness trigger:** Fees change on the annual 1 July cycle (1 July 2026 concession confirmed; PNG passport arrangements from 1 July 2026). Re-verify all VAC figures via the Visa Pricing Estimator each cycle.
- **Timatic/carrier note:** Digitally linked to passport, no label; carriers verify at check-in.

## Question Overlay

ImmiAccount is login-walled, so field-level scripting is not reproducible. The subclass 600 form (`VSS-AP-600`) follows this general information order (from official Step-by-step / Eligibility content; not literal in-portal labels):

| Field / topic | Format | Conditional trigger | Evidence source |
|---|---|---|---|
| Identity — passport bio page | Passport scan/photo, colour | Always | 600 Tourist (Identity documents) |
| National identity card | Scan | If held | 600 Tourist |
| Change-of-name proof | Marriage/divorce/name-change docs | If name differs from passport | 600 Tourist |
| Other passports / other names | Declaration | If applicable | 601 / 600 |
| Purpose of visit / plans in Australia | Free-text + itinerary | Always | 600 Tourist (Genuine visitor) |
| Funds / access to money | Bank statements (3 months), pay slips, tax records, term deposits | Always | 600 Tourist (Have enough money) |
| Invitation from relative/friend | Letter (relationship, purpose, length, accommodation; + their funds if they pay) | If visiting/staying with someone | 600 Tourist |
| Ties to home country / intent to return | Employer letter, study proof, family, assets | Always | 600 Tourist |
| Genuine visitor / genuine temporary entrant declaration | Declaration | Always | 600 Tourist |
| Sponsor details | Sponsor identity + relationship evidence | Sponsored Family stream only | 600 Sponsored |
| Security bond | Payable by sponsor if requested | Sponsored Family, if requested | 600 Sponsored |
| Health declarations / examinations | Panel-physician exam if triggered | Long stay, health-care/hospital, prior health failure, or if requested | 600 Tourist; Health req |
| Character declarations | Criminal-conviction declaration; military service; police certificate | Always declare; certificate if requested | 600 Tourist; Character req |
| Previous travel / visa refusals | Declaration | Always | 601/651 (accurate info) |
| Longer-visa request | Reason + evidence | If requesting >standard stay / parent applicants | 600 Tourist |
| Minor (under 18) details + consent | Birth cert / family book / court docs; Form 1229 or statutory declaration; Form 1257 if not staying with relative/guardian | Applicant under 18 | 600 Tourist |

For **601 (ETA app)** the in-app flow captures: passport scan, live photo, criminal-conviction declaration, prior names, Australian contact details, other passports, payment. For **651** the key checks are name spelling, eligible-passport confirmation, DOB, email, criminal-conduct declaration.

## Documents

Cite official source per mandatory item. "601/651/600" indicate which route(s) the item applies to.

**Always required**
- **Valid passport** (bio/photo page; for 600 provide photo, personal-details and issue/expiry pages). 601/651/600.
- **Live facial image / photo** — captured in the ETA app (601); standard identity for 651/600.
- **Evidence of sufficient funds** (600: itemised personal bank statements for a 3-month period, pay slips, audited accounts, tax records, term deposits). 651 requires an "enough money" declaration; 600 requires documentary proof.
- **Genuine-visitor / intent-to-return evidence** (600: employer letter, study proof, family in home country, property/assets).

**Conditional**
- **Letter of invitation** from Australian relative/friend (+ proof of their funds if they will pay). Trigger: visiting/staying with someone; also the without-sponsor alternative to the Sponsored Family stream.
- **Sponsorship documents + sponsor** — Sponsored Family stream only; sponsor must be eligible; relationship evidence; **security bond** if the Department requests.
- **Police certificate(s)** — where character concerns / criminal conviction, or if requested. An ETA/eVisitor applicant with a criminal conviction in any country should apply **subclass 600.**
- **Military service record / discharge papers** — 600, if applicable.
- **Health examinations** — panel-physician exams if triggered (long stay, health-care/hospital environments, prior health-requirement failure, or if requested).
- **Change-of-name / national ID** documents — if name differs or held.
- **Longer-visa evidence** — e.g. proof child is AU citizen/PR (parents).

**Minors (under 18) — conditional**
- Birth certificate showing both parents (or family book / government ID / court document / family census register).
- Guardianship/adoption proof if not biological parents.
- **Form 1229** (consent to grant a visa to a child under 18) or a statutory declaration of consent, plus signed/photo ID of the consenter.
- **Form 1257** (Undertaking declaration) if the child is not staying with a relative/legal guardian.

**Location-specific / representation**
- Non-English documents must be translated to English; in-Australia translators must be NAATI-accredited; overseas translators must state name, address/phone, qualifications (in English).
- Documents scanned/photographed in colour, clear, multi-page saved as one file.
- **Form 956A** (authorised recipient) / **Form 956** (registered migration agent, legal practitioner, exempt person) if using a representative.

**Generated after submission**
- **Visa grant notice** (grant number, start date, conditions) or refusal notice with review rights — issued in writing.
- **Form 1554** (ETA Request for further processing) — only if the Department requests further ETA processing.

## Portal Workflow

### Australian ETA app (subclass 601)
1. Check passport validity; **download the Australian ETA app** (Apple Store / Google Play).
2. Device requirements: camera, **NFC enabled**, location services enabled, valid email, valid payment method.
3. In-app: **scan passport → take a live photo → answer questions** (criminal convictions, prior names, Australian contact details, other passports).
4. **Pay AUD 20 service fee** in-app and submit. Each person needs a separate application.
5. Result usually immediate by email; do not book travel until granted.
6. Post-grant: check status via **VEVO** or the app's "Visa check"; ETA is linked to the passport (no label). If further processing is needed, the Department sends a link to submit an online form in ImmiAccount + **Form 1554**.

*(In-app screens are login-walled/device-side; steps above are the publicly documented flow.)*

### ImmiAccount (subclass 651 and 600)
1. **Create / log in to ImmiAccount.** *[account creation public; the application editor is login-walled]*
2. Start a new application: 651 → form **`TV-AP-651`**; 600 (any stream) → form **`VSS-AP-600`**.
3. Complete the online form (identity, purpose, funds, genuine-visitor, character/health declarations, sponsor if Sponsored Family). *[login-walled]*
4. **Attach documents** (colour scans; translations where needed); submit family applications together where applicable. *[login-walled]*
5. **Pay the Visa Application Charge** — none for 651; for 600 the base VAC per stream. Application not processed until paid. *[login-walled]*
6. **Biometrics** — provide if the Department notifies you. *[triggered]*
7. **Health examinations** — complete before applying or when requested. *[triggered]*
8. **Outcome** — written grant notice or refusal with review rights.
9. Post-grant: check details/conditions and prove your visa via **VEVO**; complete an Incoming Passenger Card at the border.

## Review Risks

- **Route selection (601 vs 651 vs 600):** ETA (601) is app-only and limited to the ETA-eligible passport list. eVisitor (651) is ImmiAccount-only, free, for the European eligible list (UK only British Citizen; **BN(O) qualifies for ETA but NOT eVisitor**; British Protected Person/Subject qualify for neither). Overlap exists (several EU states on both) — 651 is free while 601 costs AUD 20. Everyone else, or anyone with a **criminal conviction, prior health-requirement failure, health-care/hospital environment intent, sponsored-family visit, ADS tour, or need for >3-month/long-validity stay**, must use **subclass 600.**
- **Genuine-visitor / genuine-temporary-entrant test:** All routes require genuine temporary intent. Frequent/long stays can prompt questioning and possible cancellation. 600 requires documentary evidence of ties and intent to return.
- **Health & character triggers:** Any criminal conviction (any country) or prior health-requirement failure routes the applicant off 601/651 onto 600. Health exams/police certificates are request-driven.
- **Funds:** 600 expects itemised 3-month bank statements plus supporting financial evidence; thin or unexplained funds are a common refusal driver.
- **Sponsored streams:** Sponsored Family (600) needs an eligible sponsor and relationship evidence; the Department may require a **security bond** from the sponsor. The Tourist stream (invitation letter instead of sponsor) is often simpler.
- **Minors:** Consent (Form 1229 or statutory declaration), guardianship proof, and Form 1257 (if not staying with relative/guardian) are frequent gaps.
- **Fee freshness:** VAC figures change on the 1 July annual cycle; a Pacific Island / Timor-Leste concession and PNG passport arrangements take effect 1 July 2026. Always re-confirm via the Visa Pricing Estimator.
- **Passport linkage:** ETA/eVisitor/600 grants are digitally linked to the passport. A new/expired passport **ceases an ETA** and requires re-application.
