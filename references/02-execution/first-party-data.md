# First-party user data

## Treat matching features as opt-in scope

Apply this reference to Google Ads enhanced conversions, Meta Advanced Matching, TikTok Advanced Matching, Snap matching, Microsoft user-data features, or another vendor feature that uses email, phone, name, address, external/customer ID, or similar identifiers.

Do not enable automatic or manual collection by default. Require:

- an explicit implementation request and authorization;
- the client-approved purpose and consent policy;
- confirmation that required vendor terms/settings are completed outside GTM where applicable;
- current official browser documentation for supported fields and handling;
- an approved source contract, evidence grade, and representative non-production test data.

Do not make the legal decision. Stop when the analyst cannot establish approved data use.

## Prefer controlled sources

Use this source priority unless the approved implementation requires otherwise:

1. a deliberate dataLayer field available at the correct event;
2. an existing controlled JavaScript variable or first-party source;
3. a stable DOM element or selector only when documented and approved;
4. automatic DOM scanning only when explicitly enabled and its collection scope is understood.

Do not enable automatic collection merely because a template recommends it. Document every page and field type the feature can inspect.

Never send placeholder values, test identities, authentication secrets, or sensitive-category data.

## Follow the vendor's field contract

For every identifier, record:

- official vendor field and browser support;
- raw or pre-hashed input requirement;
- required normalization steps;
- hashing algorithm and whether the vendor/template performs it;
- accepted array/single-value shape;
- null, empty, invalid, and multiple-value behavior;
- GTM source variable and consent requirement.

Normalize and hash only as current official documentation requires. Do not double-hash a value when the selected template performs hashing. Do not send a raw value where pre-hashing is required.

## Separate analytics identifiers from advertising matching

Do not send email, phone, name, postal address, or other personally identifiable information to GA4 event parameters, user properties, URLs, titles, or debug fields.

Do not reuse an advertising matching variable in an analytics tag without independently validating that the analytics destination permits that value.

## Design safe GTM objects

- Give each user-data variable a clear vendor/purpose owner.
- Keep normalization transformations narrow and null-safe.
- Do not persist user data in a GTM constant, lookup table, cookie, local storage, or debug log.
- Avoid exposing resolved personal data in handoff screenshots or reports.
- Do not broaden an existing shared variable's consumers without checking its data-handling contract.
- Use template-native user-data variables when current official documentation requires them.

## Apply consent before collection and transmission

Map each identifier feature to the client-approved consent state and current vendor requirement. Under the default strict/basic route, block both the base tag and matching-enabled event tag until the required vendor consent is granted.

For explicitly approved advanced/native consent, verify whether denied-state requests can contain user-provided data. Configure the vendor controls so disallowed identifiers are not collected or transmitted under denied state.

Do not assume that hashing replaces consent or makes a value anonymous.

## Validate without leaking data

Use synthetic test values when possible. Verify:

- source availability at the exact event according to the approved contract;
- normalization and hash ownership;
- template field resolution;
- configured collection fields remain ineligible before required consent;
- configured denied-state routes omit user data when prohibited by the approved contract;
- no PII in GA4, URLs, logs, reports, or unrelated tags;
- missing input produces no invented fallback.

Record validation results without reproducing real personal data.

## Current client-side boundary

Configure only the browser-side feature explicitly requested. Do not add server-side user-data events, Conversions API, enhanced conversions for leads uploads, offline conversion uploads, or browser/server deduplication in the current scope.
