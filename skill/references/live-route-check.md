# Live Visa-Need And Entry Route Check

Run this check for every new application before collecting detailed form answers. Never infer a current visa requirement from the cached registry, general knowledge, a search snippet, or a prior trip.

## Route Key

Collect these facts first:

- destination and every transit country
- nationality or stateless/refugee status
- travel-document type, issuer, issue/expiry dates
- legal residence, residence status/expiry, and application location
- purpose, arrival date, duration, entries, arrival mode, and entry point
- self-transfer, overnight transit, airport change, or baggage recheck
- existing visas, residence permits, diplomatic/official status, or crew status
- age and accompanying guardian when minor rules may apply

## Mandatory Live Sources

1. Destination immigration authority or foreign ministry.
2. Destination embassy/consulate responsible for the application location.
3. Official ETA/eVisa/application portal when applicable.
4. Official sources for every transit country.
5. IATA Travel Centre/Timatic or the operating carrier for boarding-document cross-checks.

Government sources determine the legal rule. Timatic and carriers are operational cross-checks and may reveal boarding implementation, but they do not override the destination government. Delegated visa centres establish submission logistics only.

Use Browser/Web search on every run. Open the official page itself; do not rely on search-result text. Record the exact URL, authority, checked timestamp, page update/effective date when shown, and the applicant facts used for the lookup.

## Verdict Values

Use one of:

- `visa_free`
- `eta`
- `evisa`
- `visa_on_arrival`
- `consular_visa`
- `transit_authorization`
- `residence_route`
- `mixed`
- `unresolved`

`mixed` means the itinerary contains different routes, such as visa-free destination entry plus a transit authorization. `Unresolved` is valid only when the conflict and next verification action are visible.

## Required Findings

Capture all applicable conditions:

- eligible travel document and nationality/residence exceptions
- allowed purposes and work/study restrictions
- maximum stay, number of entries, validity window, and extension rules
- policy start/end dates or temporary-program dates
- passport validity, blank pages, damage, and emergency-document restrictions
- required arrival mode, approved ports, pre-registration, or invitation
- onward/return travel, funds, accommodation, insurance, vaccination/health, and registration
- ETA/eVisa/VOA fee, processing time, payment method, and issuance format
- transit airside/landside rules, self-transfer, airport change, and overnight stay
- minor, diplomatic/official passport, crew, refugee-document, and stateless-person exceptions
- existing visa or residence-permit substitutions

## Freshness Rules

- Check live sources on the day detailed intake starts.
- Recheck immediately before application submission or payment.
- Refresh when the route check is more than 7 days old, the itinerary changes, or a policy has a future effective date.
- Recheck entry and carrier requirements within 72 hours before departure.
- Never claim “latest” without a checked timestamp.

## Conflict Handling

If official pages disagree, keep the verdict `unresolved`, record both sources and dates, and seek clarification from the responsible mission or immigration authority. Do not choose the more convenient rule. If Timatic conflicts with a government source, record the carrier risk and contact the operating carrier before travel.

## Gate

Do not begin detailed form intake until the HTML shows the verdict, official basis, conditions, transit result, checked timestamp, and recheck deadline. Visa-free or ETA results may end the visa-form workflow and switch the dossier to entry-readiness tracking.
