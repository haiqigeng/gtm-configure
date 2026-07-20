# Analytics tags

## Contents

- [Use the analytics requirement as the business contract](#use-the-analytics-requirement-as-the-business-contract)
- [Configure the Google tag deliberately](#configure-the-google-tag-deliberately)
- [Keep page view separate by default](#keep-page-view-separate-by-default)
- [Configure events from the official schema](#configure-events-from-the-official-schema)
- [Govern user properties and identifiers](#govern-user-properties-and-identifiers)
- [Record external Google and GA4 administration](#record-external-google-and-ga4-administration)
- [Apply consent](#apply-consent)
- [Naming examples](#naming-examples)

## Use the analytics requirement as the business contract

Treat an approved tracking plan or direct analytics requirement as the primary analytics input. Resolve destination semantics from current official documentation.

For each event, map:

| Requirement layer | Required decision |
| --- | --- |
| Business action | Confirm the exact success moment and intended analysis. |
| Source event | Use the vendor-neutral dataLayer Custom Event by default. |
| Source values | Verify key, event timing, type, cardinality, and sample output. |
| GA4 event | Prefer the current automatic, enhanced-measurement, recommended, or ecommerce event when applicable; use custom only when none fits. |
| GA4 parameters | Use exact official names, types, and item/event scope. |
| GTM variables | Reuse or create DLVs, constants, settings, tables, or documented transformations. |
| Consent | Apply strict/basic CMP blocking by default; route explicitly approved advanced Google Consent Mode separately. |

Never copy a source key into GA4 merely because the names look plausible. Map the source field deliberately to an official destination parameter or an approved custom parameter.

## Configure the Google tag deliberately

Use current Google documentation to distinguish:

- the Google tag/configuration tag;
- a Google tag Configuration Settings variable;
- a Google tag Event Settings variable;
- GA4 event tags and event-specific parameters;
- settings managed in the GA4 data stream or Google tag destination UI.

Use these naming patterns when compatible with the container:

| Object | Name |
| --- | --- |
| Primary Google tag | `GA4 - Config` |
| Qualified Google tag | `GA4 - Config - main` |
| Configuration Settings variable, when justified | `GA4 - Config Setting` |
| Event Settings variable, when justified | `GA4 - Event Setting` |
| Measurement ID constant | `CST - GA4 measurement_id` |

Reference the measurement ID through a compatible constant rather than hard-coding it repeatedly. Do not create a settings variable merely because GTM offers one.

Use a Configuration Settings variable only for a coherent set of configuration-level values reused across applicable Google tags. Use an Event Settings variable only for a coherent set of event parameters or user properties genuinely shared across applicable events. Keep transaction, item, search, form, and other event-specific values on the event tag.

Inspect consumers before changing either settings variable because one edit may affect many tags and destinations.

## Keep page view separate by default

When page-view configuration is in the approved scope, keep the Google tag from sending an automatic page view by default. Verify the current `send_page_view` behavior and set it to `false` only where a separately managed page-view event is required. Do not alter an existing compatible page-view architecture merely to impose this preference during an unrelated event change.

When the approved requirement includes a manually managed page view and no compatible tag already supplies it, create `GA4 - Event - page_view` with the approved source values and trigger. Before doing so:

1. Inspect existing Google tags and any supplied evidence of hard-coded or partner installations; record unknown outside-container installation as an external dependency.
2. Inspect Enhanced Measurement page-load and browser-history behavior.
3. Disable or avoid overlapping automatic behavior.
4. Verify page-load and SPA navigation semantics separately.
5. Design CMP timing so the initial page view is not lost or duplicated.

If the normal `page_view` dataLayer event occurs before CMP state is ready under strict/basic gating, use the CMP's officially documented one-time readiness event and a verified vendor gate. Do not use a repeatable consent-change event without an explicit duplicate and late-consent policy.

When the tag fires on a CMP event instead of the original `page_view` event, revalidate every page parameter at that later event. Use browser built-ins or retained dataLayer state only when the approved source contract establishes that the value is current and in scope; never assume an earlier event-scoped payload remains available. If a required value is missing or stale under the contract, block the page-view implementation and request a CMP-safe application event or source contract.

## Configure events from the official schema

For each GA4 event:

1. Open the current GA4 event reference.
2. Confirm automatic, enhanced-measurement, recommended, ecommerce, or custom classification.
3. Extract each parameter's exact name, requirement status, type, scope, cardinality, and limits.
4. Validate event-level and item-level placement.
5. Map each destination parameter to a named GTM variable or documented transformation.
6. Validate a representative resolved event, including all ecommerce items.

When a source key is misspelled, verify that the approved source contract uses that exact key. Name the DLV for the actual source key, then map it to the correctly spelled official GA4 parameter. Do not propagate source typos into destination fields.

Treat `value` and `currency`, transaction identifiers, and `items` according to the exact event reference. Never infer an item parameter from a similarly named event parameter.

## Govern user properties and identifiers

Add a user property only when it is an approved, stable user attribute with a valid analysis use and current GA4 documentation permits it. Keep it in an Event Settings variable only when it genuinely applies across the intended events.

Treat `user_id` as a separately approved identifier contract, not a routine event parameter or user property. Establish its source, authentication lifecycle, reset behavior, consent, and current official requirements before configuration.

Do not send personally identifiable information to GA4. Do not repurpose media advanced-matching fields as GA4 parameters or user properties.

## Record external Google and GA4 administration

For every collected field or event, determine whether the approved reporting use also requires work outside the authorized GTM change. Record, without silently changing:

- GA4 custom dimensions or metrics for custom event, item, or user fields;
- GA4 key-event designation;
- data-stream or Enhanced Measurement settings that can duplicate or alter the selected event;
- Google tag destinations, shared settings, cross-domain configuration, unwanted-referral handling, or other current administration surfaces;
- advertising or audience activation settings owned outside GTM.

Resolve the current configuration surface from official documentation. Classify each dependency as already confirmed, separately authorized, required external work, intentionally untouched, or blocking.

## Apply consent

Use strict/basic gating by default:

- create or reuse `Block - <CMP> - GA4 denied`;
- block unknown, uninitialized, and denied states;
- apply the gate to the config and all GA4 event tags in scope only after confirming that any shared Google tag destinations require a compatible basic route.

Use advanced Google Consent Mode only when explicitly requested and approved. In that route, follow the dedicated consent reference and do not attach a blocking trigger that suppresses the documented denied-state behavior.

If a Google tag also serves Google Ads, Floodlight, or another destination with a different consent route, follow the shared-execution-unit rule in the Google consent reference. Do not let a GA4 block silently disable an approved advanced destination or let that destination's advanced route expose GA4 contrary to its selected basic policy.

## Naming examples

| Object | Example |
| --- | --- |
| Google tag | `GA4 - Config` |
| GA4 event | `GA4 - Event - generate_lead` |
| GA4 ecommerce event | `GA4 - Event - purchase` |
| Source DLV | `DLV - page_location` |
| Measurement ID | `CST - GA4 measurement_id` |
| Custom Event trigger | `CE - generate_lead` |
| Consent exception | `Block - Didomi - GA4 denied` |
