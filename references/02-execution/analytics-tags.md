# Analytics tags

## Map the tracking plan to the destination schema

For each analytics destination, make a field-level map:

| Tracking-plan item | Destination decision |
| --- | --- |
| Business action | Use the current official event when one exists; use a custom event only when no suitable official event applies. |
| dataLayer event | Use it as the normal Custom Event trigger by default. Keep it vendor-neutral. |
| Source field | Create or reuse the appropriate DLV, constant, lookup, or transformation. |
| Destination parameter | Use the exact official platform parameter name and documented type. |
| Common value | Consider a shared configuration/event settings variable only when it is genuinely shared and reduces complexity. |
| Consent | Attach the verified vendor/platform gate; do not place consent status in a payload field and call it gating. |

Never create a custom destination parameter just because the incoming dataLayer key has that name. Map the source key to the official destination parameter when one exists.

## GA4 and Google tag configuration

Use current Google documentation to distinguish:

- the Google tag/configuration itself;
- a Google tag Configuration Settings variable;
- a Google tag Event Settings variable;
- GA4 event tags and their event-specific parameters.

Name the primary Google tag configuration "GA4 - Config", or "GA4 - Config - main" where several configurations need a clear qualifier. Do not use an invented prefix such as "GCS".

Create "GA4 - Event Setting" only when a small, coherent set of parameters or user properties is used across relevant events and the settings variable makes the design simpler. Do not use it as a dumping ground, and do not create it solely because the feature exists.

Keep event-specific values, especially transaction, item, search, form, and conversion details, on the applicable event tag unless a documented, limited shared use case justifies otherwise.

## GA4 events and parameters

Before configuring a GA4 tag:

1. Check whether the desired behavior is automatic, enhanced measurement, recommended, ecommerce, or custom.
2. Confirm the current official event name and each parameter name.
3. Confirm required/optional status, type, multiplicity, and accepted value format.
4. Map each parameter from a named GTM variable, lookup table, or documented transformation.
5. Validate the final tag payload against a representative dataLayer event.

For example, a tracking plan may expose "page_location", "page_referrer", and a site-specific path field. Use the documented GA4 names for the destination. Do not automatically send "page_path" as a GA4 page_view parameter merely because the plan contains it; GA4 normally derives page path reporting from location. Retain a path field only when a documented/approved custom use case requires it.

If a plan contains a misspelled source key such as "page_refferrer", treat it as a source-contract issue. Verify whether that key truly exists in runtime data and map it deliberately to the correctly named destination field; do not propagate the typo into the GA4 parameter name.

## Page-view implementation

Decide page-view behavior deliberately before creating a tag:

- inspect whether the Google tag sends page views automatically;
- inspect Enhanced Measurement and, for SPAs, history-change behavior;
- choose manual page_view only when the implementation needs it;
- prevent a manual event from duplicating an automatic/enhanced event;
- document the page-view trigger's timing relative to CMP initialization.

For a strict CMP-gated manual page view, the initial page event can precede consent initialization. Use the CMP's documented event that has the required one-time semantics, plus a verified consent check. Do not use a generic CMP event that can fire repeatedly unless duplicate prevention and later-consent behavior are explicitly designed and approved.

## Naming examples

| Object | Example |
| --- | --- |
| Google tag configuration | "GA4 - Config" |
| Qualified configuration | "GA4 - Config - main" |
| Event settings variable, when justified | "GA4 - Event Setting" |
| GA4 event tag | "GA4 - Event - page_view" |
| GA4 ecommerce event tag | "GA4 - Event - purchase" |
| Source dataLayer variable | "DLV - page_location" |
| Measurement ID constant, when appropriate | "CST - GA4 measurement_id" |
| Custom Event trigger | "CE - page_view" |
