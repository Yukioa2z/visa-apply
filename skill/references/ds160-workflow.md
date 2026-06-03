# DS-160 Visa Dossier Workflow

## Ground Rules

- The local HTML dossier is the single source of truth.
- Store sensitive data only after the user agrees to a local complete copy.
- Use official sources for current requirements, fees, appointment process, photo rules, and visa-category guidance.
- The applicant performs final review, certification, signature, and submission.
- Do not bypass CAPTCHA, anti-automation locks, or identity checks.
- Do not invent unknown facts. Mark them `Pending`, `Unknown`, or `Does Not Apply` only when the official form supports that answer and the user confirms it.

## Official Source Starting Points

- State Department DS-160 overview: https://travel.state.gov/content/travel/en/us-visas/visa-information-resources/forms/ds-160-online-nonimmigrant-visa-application.html
- DS-160 FAQ: https://travel.state.gov/content/travel/en/us-visas/visa-information-resources/forms/ds-160-online-nonimmigrant-visa-application/ds-160-faqs.html.html
- CEAC DS-160 start/retrieve page: https://ceac.state.gov/genniv/
- State Department visitor visa page: https://travel.state.gov/content/travel/en/us-visas/tourism-visit/visitor.html

For country scheduling and fee payment, find the currently official embassy/consulate or visa scheduling portal for the applicant's interview country.

## Intake Order

Ask in DS-160 order unless the user is actively filling a different page.

Before detailed intake, create a visa-type branch:

- Core DS-160 questions are always required.
- B-1, B-2, or B-1/B-2: travel purpose, itinerary, U.S. address/contact, trip payer, tourism/business boundary, employment/ties, and whether any work/study will occur.
- F or M: school/program, SEVIS ID, I-20 details, funding, prior study/status history, and intended course of study.
- J: exchange program, DS-2019 details, SEVIS ID, sponsor, funding, field/category, and two-year home residency relevance if prompted by the form.
- H, L, O, P, Q, R, or similar petition-based work categories: petition/receipt details, petitioner/employer, job title, worksite, duties, and dates.
- E treaty trader/investor: enterprise, investment/trade facts, role, ownership, and supporting business details.
- C, D, or C-1/D: transit, vessel/airline, crew role, onward travel, and short-stay logistics.
- A, G, NATO, or official categories: official position, mission/organization, diplomatic/official travel purpose, and assignment details.
- K categories: petitioner/beneficiary relationship, petition details, consular case details, and relationship timeline.

If the selected visa class does not fit one of these examples, search official State Department and consular sources for that category and add the resulting branch to the HTML coverage map before asking detailed questions.

1. Privacy and logistics
   - Local complete copy or redacted copy?
   - Visa class and purpose of travel.
   - Application location and intended interview post.
   - CEAC application ID, security question, and save/retrieve details if already created.
2. Personal information
   - Passport name, native alphabet name, telecodes if applicable.
   - Sex, marital status, date/place/country of birth.
   - Nationality, other nationality, permanent residence elsewhere.
   - National ID, SSN, ITIN, if applicable.
3. Travel information
   - Arrival and departure dates or intended dates.
   - Cities/places to visit.
   - U.S. address.
   - Trip payer.
   - Travel companions.
4. Previous U.S. travel and visas
   - Prior visits, I-94 entries, prior visa details.
   - Refusals, cancellations, revocations, lost/stolen visa or passport.
   - Driver license and U.S. identifiers when requested.
5. Address, phone, email, social media
   - Current home address and mailing address.
   - Phone numbers, email addresses.
   - Social media identifiers for the requested period.
6. Passport information
   - Passport number, book number if present, issuance/expiration date, issuing city/state/country.
   - Lost/stolen passport history.
7. U.S. contact
   - Person or organization in the U.S.
   - Relationship, address, phone, email if available.
8. Family
   - Parents' names/dates of birth or unknown status.
   - Spouse/former spouse if applicable.
   - Relatives in the United States.
9. Present work, education, and training
   - Current employment or study.
   - Employer/school address and phone.
   - Salary, start date, duties.
10. Previous work, education, travel
   - Past work history required by DS-160.
   - Education after elementary level.
   - Recent travel to other countries.
   - Languages, organizations, specialized skills or training, military/government/security service.
11. Security and background
   - Ask the official security pages carefully.
   - Group all clear "No" responses only after the user explicitly confirms.
12. Review and submission
   - Photo status.
   - Final preview complete.
   - Applicant review complete.
   - Submission/confirmation number backfilled.
13. Fee, appointment, and status
   - Payment status and receipt number.
   - Appointment date/time and location.
   - Visa status or passport return status.

## HTML Update Rules

- Update `Visa Process Progress` whenever a milestone changes.
- Update `Current Filing Status` with a plain-language summary.
- Update `Final DS-160 Filled Preview` with cleaned values only.
- Update `Source: Collected Answers` with raw answers and provenance.
- Update `DS-160 Coverage Map` so missing sections are obvious.
- Keep placeholders visible instead of deleting unresolved fields.
- Use `Pending user confirmation` for inferred values until the user confirms.

## Browser And Computer Use

Use Browser when the task is in the Codex in-app browser, local HTML, localhost, or another local target. Use Computer Use when interacting with the user's real browser session, authenticated pages, installed extensions, profile cookies, native file pickers, or desktop dialogs.

If the agent runtime is not Codex, translate this step to the equivalent browser-use or computer-use capability in that environment. Claude Code, Hermes, OpenClaw, and similar agents may require another skill or plugin, such as Peekaboo or an environment-specific browser/computer-control skill. Keep the same safety boundaries regardless of tool choice.

Before entering official form data:

1. Open the local dossier and final preview.
2. Ask the user to confirm the final preview is ready for form entry.
3. Fill fields page by page from the final preview.
4. After each page, use the official form's own navigation/save controls.
5. Let the user handle CAPTCHA, passwords, final certification, signature, and submission.
6. Backfill generated IDs and milestones into the HTML.

## Review Gate Checklist

- All final fields have a value, `Does Not Apply`, or clear `Pending` note.
- Travel purpose matches the visa class.
- U.S. address and contact are consistent.
- Current work/school data is current.
- Previous U.S. visa/travel data is consistent with documents.
- Security/background answers are confirmed by the user.
- Photo is ready and meets current official requirements.
- The user understands that official submission is their act, not the agent's.
