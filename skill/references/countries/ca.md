# Canada Adapter: Temporary Resident Visa (visitor visa) via IRCC

Support level: `full_adapter` (rules + document-checklist depth; the IRCC secure account is login-walled and not field-scriptable). Verified against IRCC / canada.ca on 2026-07-20. A few specifics are marked **pending exact-page reconfirmation** because those pages 404'd or dropped the connection on the verification date.

## Metadata

- **Country/area:** Canada
- **Supported visa routes:**
  - **Temporary Resident Visa (TRV) / visitor visa** — the primary route this adapter scripts.
  - **eTA (Electronic Travel Authorization)** — a *separate, simpler* route for visa-exempt foreign nationals arriving **by air**. Not a visa. Determines whether the visa workflow applies at all.
  - **Super Visa** — long-validity multiple-entry visa for parents/grandparents of Canadian citizens/PRs/registered Indians. A TRV variant with extra insurance + host-income requirements.
- **Applicant assumptions:** Nationality- and residence-agnostic. The responsible visa office is the IRCC visa office / VAC network servicing the applicant's country of residence; country-specific instructions attach to the online personalized document checklist. Applicant is assumed to be **outside Canada** at time of application.
- **Last verified date:** 2026-07-20
- **Official source IDs/URLs:** see `official-sources.json`.
- **Support level:** `full_adapter`

## Route Map

### Branch A — eTA (visa-exempt air travelers) — NOT a visa workflow
- **Official name:** Electronic Travel Authorization (eTA).
- **Applies to:** Visa-exempt foreign nationals flying to or transiting through a Canadian airport. Visa-exempt travelers "do not need an eTA when arriving by car, bus, train or boat (including a cruise ship)."
- **Exempt from eTA (carry other ID instead):** U.S. citizens (carry valid U.S. passport); U.S. lawful permanent residents (carry valid PR card [I-551] or re-entry permit [I-327] **plus** a valid passport of nationality); Canadian citizens/dual citizens (Canadian passport); Canadian PRs (PR card / PR travel document).
- **Duration/validity:** Valid up to five years or until the passport expires, electronically linked to the passport. Does not guarantee entry.
- **Split rule (load-bearing):** Visa-exempt + air → **use the eTA route, not this TRV workflow.** Visa-exempt + land/sea → nothing needed. Some visa-required nationals may be eTA-eligible for air travel but **still need a TRV for land/sea entry.**
- **Fee:** eTA is CAD $7 (confirm on the eTA facts page at apply time — the facts page opened on 2026-07-20 did not restate the amount, so treat as **pending exact-page reconfirmation**).
- **Timatic/carrier cross-check:** Airlines validate eTA/visa status at boarding against IRCC systems; mismatch = denied boarding. Cross-check nationality + arrival mode against the eTA-vs-TRV decision before assuming the visa workflow applies.

### Branch B — Temporary Resident Visa (visitor visa)
- **Official name:** Temporary Resident Visa (TRV), commonly "visitor visa."
- **Purpose/duration boundary:** Tourism, visiting family/friends, business visits, transit, event attendance (incl. FIFA World Cup 2026 match attendance). Standard authorized stay on entry is up to 6 months (determined by the border officer, not the visa). Stays intended >6 months trigger medical-exam rules.
- **Eligibility inputs:** valid passport/travel document; "good health"; "no criminal or immigration-related convictions"; must convince an officer of ties (job, home, financial assets, family) that will take you back; must convince an officer you will leave at the end of the visit; enough money for the stay; not otherwise inadmissible.
- **Application authority & responsible office:** IRCC. Visa is printed by a visa office outside Canada; country-specific document instructions attach via the online personalized checklist. VAC handles logistics (biometrics, document intake) only.
- **Process:** Apply **online** via the IRCC account. Two online options: **IRCC Portal** and **IRCC Portal – New version** (new version limited to applicants 18+, applying alone, first-time, not using a representative). Applicants may also use the **IRCC secure account**. Paper only if unable to apply online (disability, or refugee/stateless/non-citizen travel documents).
- **Form/portal:** Guide **5256**; core form **IMM 5257** (Application for TRV / Details of Visit); supporting IMM 5645 (Family Information), IMM 5476 (Use of a Representative), IMM 5475 (Authority to Release Personal Information), IMM 5484 (Document Checklist).
- **Fee (CAD):** Visitor visa processing — **$100 individual**; **$500 family (5+)**. Biometrics — **$85 individual**; **$170 family maximum**. Some applicants may be exempt. Payment: Visa, MasterCard, Amex, JCB, UnionPay (online), Visa Debit; cardholder need not be the applicant.
- **Biometrics:** Required for temporary residence "except US nationals," unless exempt (children under 14, applicants over 79). **10-year reuse:** biometrics are valid for 10 years; if given within the last 10 years and still valid, generally not repeated for a new TR application. *(Exact reuse wording could not be opened on a single live page on 2026-07-20 — treat the 10-year figure as pending exact-page reconfirmation; the facts page confirmed the fee/exemption structure.)*
- **Appointment:** After submitting, applicant receives a **Biometrics Instruction Letter (BIL)** and books biometrics at a VAC promptly.
- **Visa validity:** May be issued for up to 10 years or until the expiry of the passport or biometrics, whichever comes first. Renewing biometrics does not automatically extend the visa to 10 years.
- **Medical exam triggers:** Stays **≤6 months** — generally not required, except jobs in close contact with people (health care, clinical lab, childcare, medical students) and certain agricultural workers who lived in/visited a designated country 6+ consecutive months in the prior year. Stays **>6 months** — required if at least one applies: lived in/traveled to a designated country for 6+ consecutive months in the year before coming; OR coming to work a public-health-sensitive job; OR applying for a parent/grandparent super visa. The designated-country list was updated **November 3, 2025** — re-check the current list.
- **Policy freshness trigger:** Re-verify each cycle: fee schedule, biometrics fee/exemptions, medical designated-country list (last change 2025-11-03), and LICO income tables (annual).

### Branch C — Super Visa (parents & grandparents)
- **Who:** Parents/grandparents (biological or adopted) of a child/grandchild who is a Canadian citizen, PR, or registered Indian, aged 18+ and living in Canada. Cannot include dependants.
- **Duration:** Multiple entry, valid up to 10 years; each stay up to 5 years at a time.
- **Fee:** From CAD $100 (+ biometrics).
- **Extra requirements:** mandatory medical exam; **$100,000** minimum private medical insurance covering health care, hospitalization, and repatriation, valid ≥1 year from date of entry; host must meet or exceed **minimum necessary income (LICO)**; signed host letter of invitation.

## Question Overlay
(Fields BEYOND a universal core intake of name/DOB/nationality/passport/contact. IMM 5257 / Details of Visit order where known.)

| # | Field label | Expected format | Conditional trigger | Evidence source |
|---|---|---|---|---|
| 1 | Purpose of visit | Enum: tourism / visit family / business / transit / study<6mo / other + free text | Always | IMM 5257; apply-page purpose router |
| 2 | Intended arrival / departure dates & duration | Dates; duration | Always; >6 months flags medical | IMM 5257; medical-exam rules |
| 3 | Funds available during stay | Amount in CAD | Always | Guide 5256 |
| 4 | Who is paying / funds source | Self / host / employer + relationship | Always | Guide 5256 |
| 5 | Ties to home country | Free text + evidence: job, home, assets, family | Always (officer-weighted) | Eligibility page |
| 6 | Family in Canada | Names, status, relationship, address | If any relative in Canada | IMM 5645; invitation logic |
| 7 | Host / invitation | Host name, status, address; invitation letter | If visiting a person or business | Apply page |
| 8 | Previous travel history (10 yr) | Countries, dates, prior passports/visas/permits | Always | Apply page |
| 9 | Previous Canada applications / permits | UCI, prior TRV/study/work/PR, dates | If ever applied to Canada | IRCC account linking; IMM 5257 |
| 10 | Prior refusals / removals (any country incl. US) | Yes/No + details | Always — must disclose | Eligibility (admissibility) |
| 11 | Criminal / immigration convictions | Yes/No + details | Always | Eligibility |
| 12 | Occupation / employer | Employer, role, salary, contact | If employed | Apply page (employer letter ≤3 months old) |
| 13 | Representative used | Yes/No + rep details | If using paid/unpaid rep | IMM 5476 |
| 14 | Minor traveling | Custody, parental authorization letter | If applicant/accompanied child is a minor | Guide 5256 |
| 15 | Biometrics given in last 10 years? | Yes/No + prior UCI/date | Determines whether biometrics repeat needed | Biometrics facts (reuse — pending exact-page reconfirm) |
| 16 *(Super Visa)* | Host income (LICO) | Host income vs. LICO for family size | Super Visa only | Super Visa manual |
| 17 *(Super Visa)* | Medical insurance policy | Insurer, coverage amount, validity dates | Super Visa only | Super Visa manual ($100k / 1yr) |

## Documents

### Always required (TRV)
- **Valid passport / travel document** — valid at least 6 months beyond travel date; color copy of the bio page plus all pages with stamps/visas. Not accepted: Somali passports, non-machine-readable Czech passports, temporary South African passports, provisional Venezuelan passports.
- **Digital photo** — meeting IRCC visa photo specifications (or none in-app if a biometrics photo is being captured). *Exact spec (frame 35×45 mm, chin-to-crown ~31–36 mm, within 6 months, plain light background) is standard IRCC but the dedicated photo-spec page 404'd on 2026-07-20 — treat exact numeric spec as pending exact-page reconfirmation via the visa photo appendix linked from Guide 5256.*
- **Proof of funds** — enough money to maintain yourself and to return home; typically bank statements with at least 6 months of account details/balances.
- **Purpose-of-visit evidence / itinerary** — flight details, accommodation, event registration.
- **Family Information (IMM 5645)** and, if using one, **Use of a Representative (IMM 5476)**.

### Conditional (TRV)
- **Letter of invitation** — from a Canadian person or business, if visiting someone/an organization.
- **Employer letter** — on letterhead, dated ≤3 months before applying, confirming job/salary/manager contact, if employed.
- **Travel history** — prior passports/visas/permits used within the last 10 years.
- **Minor authorization letter** — for a minor traveling alone or with one parent; signed by both parents/legal guardians.
- **Medical exam (eMedical) results** — if a medical trigger applies.
- **Authority to Release Personal Information (IMM 5475)** — if authorizing release to a third party.

### Location-specific
- **Personalized document checklist** — generated online per applicant; the responsible visa office attaches country-specific instructions and may require additional documents.

### Super Visa additional (mandatory for Branch C)
- **Private medical insurance** — minimum **$100,000** emergency coverage; must cover health care, hospitalization and repatriation; valid for a minimum of 1 year from the date of entry and for each entry; from a Canadian insurer or an OSFI-listed/minister-approved foreign insurer; **quotes are not accepted.**
- **Host letter of invitation + proof of host income at/above LICO** — LICO figures track Statistics Canada low-income cut-offs and change annually; pull the current table at application time.
- **Immigration medical exam** — mandatory for super visa.

### Generated after submission
- **Biometrics Instruction Letter (BIL)** — issued in-account after submission; book VAC appointment promptly.
- **Personalized document checklist** — produced by the online questionnaire.
- **Correspondence / decision letter & (if approved) visa counterfoil** — delivered via IRCC account; passport submitted to VAC for visa printing.

## Portal Workflow (IRCC secure account / IRCC Portal)

**Publicly knowable (no login):**
- **Account options / sign-in:** GCKey (reusable username/password) or a Canadian Interac® Sign-In Partner. New users create a new account in the IRCC secure account.
- **Two-factor authentication:** choose a second authentication method to use each sign-in; save recovery codes.
- **Application options:** IRCC Portal, IRCC Portal – New version (18+, applying alone, first-time, no representative), or IRCC secure account.
- **Personal reference code:** from the "Come to Canada" eligibility tool; expires 60 days after issue; used to start/link an application.
- **Linking applications:** if items are missing you may link the application to your account.
- **Fee payment:** paid online at the end via credit/debit; cardholder need not be the applicant.
- **Biometrics:** BIL issued after submission; biometrics given at a VAC.

**Login-walled (not publicly scrapable — do NOT attempt field-level scripting):**
- The authenticated dashboard, the actual application forms/upload slots, personalized document checklist contents, message centre, application status, and the biometrics letter itself all sit behind GCKey/Sign-In-Partner authentication. This adapter is rules + checklist depth only.

## Review Risks

1. **eTA-vs-TRV confusion (highest-impact):** Confirm nationality **and** arrival mode before assuming the visa workflow. Visa-exempt + air → eTA (not TRV). Visa-exempt + land/sea → nothing. U.S. citizens/green-card holders → neither eTA nor TRV (carry ID). Visa-required + air → may be eTA-eligible but still needs a TRV for land/sea. Wrong route = denied boarding.
2. **Biometrics reuse window:** Check for valid biometrics given in the last 10 years before paying the $85/$170 fee or booking a VAC slot. (Reuse rule wording is pending exact-page reconfirmation.)
3. **Proof-of-funds sufficiency:** No fixed IRCC dollar figure for visitors — officer-assessed against trip length and accommodation. Under-documented funds are a leading refusal reason; recommend ~6 months of statements plus a funds-source narrative.
4. **Refusal-history disclosure:** All prior refusals/removals from any country (notably the U.S.) must be disclosed. Non-disclosure risks misrepresentation findings (potential multi-year inadmissibility).
5. **Dual intent:** Visiting while also pursuing PR is permissible, but the applicant must still satisfy the officer they will leave at the end of the visit. Ties evidence must be genuine and specific.
6. **Minors / custody:** Minors traveling alone or with one parent need an authorization letter signed by both parents/legal guardians; custody/consent gaps trigger scrutiny.
7. **Super Visa specifics:** Insurance must be a purchased policy of ≥$100,000 valid ≥1 year (quotes rejected); host income must meet current-year LICO; medical exam is mandatory. Any missing = refusal.
8. **Freshness:** Medical designated-country list changed 2025-11-03; LICO and fees update periodically — re-verify at application time.
