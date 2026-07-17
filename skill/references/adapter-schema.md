# Country Adapter Schema

Create an adapter only from current official sources.

## Metadata

- Country or area
- Supported visa routes
- Applicant nationality or stateless/refugee status, travel-document issuer, legal residence, residence status, and application-location assumptions
- Last verified date
- Official source IDs from `official-sources.json`
- Support level: `full_adapter`, `source_seeded`, or `discovered`

## Route Map

For each route record:

- official visa or authorization name
- purpose and duration boundary
- eligibility inputs
- application authority and responsible post
- online, paper, in-person, or hybrid process
- form/application portal
- fee, biometrics, appointment, interview, and status channels
- visa-free, ETA, eVisa, visa-on-arrival, transit, and residence-permit substitution branches
- policy effective dates, freshness trigger, and carrier/Timatic operational cross-check

## Question Overlay

List only questions beyond `core-intake.md`, in official form order when known. Each question should include:

- field label
- expected format
- conditional trigger
- evidence source
- official source URL or registry source label

## Documents

Separate documents into:

- always required
- conditional
- location-specific
- generated after submission

Do not call a document mandatory unless the relevant official source says so for the applicant's route and place of application.

## Portal Workflow

Record the page order, save/retrieve behavior, generated identifiers, upload constraints, payment, appointment, and status steps. Include automation limits and applicant-only declaration/signature steps.

## Review Risks

Record unresolved source conflicts, translation/legalization rules, passport validity rules, residence-jurisdiction limits, and facts that require applicant confirmation.
