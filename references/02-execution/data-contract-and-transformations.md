# Data contract and transformations

## Contents

- [Establish the source event contract](#establish-the-source-event-contract)
- [Keep mapping layers distinct](#keep-mapping-layers-distinct)
- [Validate before transforming](#validate-before-transforming)
- [Prefer the least-complex mapping](#prefer-the-least-complex-mapping)
- [Preserve arrays and object schemas](#preserve-arrays-and-object-schemas)
- [Write narrow Custom JavaScript](#write-narrow-custom-javascript)
- [Make invalid events ineligible](#make-invalid-events-ineligible)
- [Statically verify transformations](#statically-verify-transformations)
- [Defer event-ID architecture](#defer-event-id-architecture)

## Establish the source event contract

For every business action, record:

- exact dataLayer `event` name;
- moment the push occurs and whether it can repeat;
- source object paths and dataLayer variable version;
- expected type, format, cardinality, and null behavior;
- sample payloads for relevant edge cases;
- whether values are event-scoped or can persist from a previous push;
- evidence grade for the event, timing, shape, and representative payload;
- source owner and required site change when a field is absent.

Use the Custom Event as the normal trigger. Do not infer a success event from a click, URL, DOM message, or form submission when a reliable business dataLayer event exists.

## Keep mapping layers distinct

Create a traceable map:

| Layer | Example role |
| --- | --- |
| dataLayer key | Actual site-owned source path. |
| GTM variable | DLV, constant, table, or transformation that resolves a value. |
| Template field | Field visible in the installed tag template. |
| Destination parameter | Official network/platform contract. |

Do not rename the source key to look official. Name the DLV after the actual key and map it to the correct official destination field.

## Validate before transforming

Require the approved source contract to place the value on the same GTM event that fires the tag, or to document its retained state and reset behavior. Check:

- string versus number versus Boolean;
- object versus array;
- empty string, zero, false, null, and undefined;
- decimal and currency formatting;
- item identifiers and explicit catalog/feed alignment;
- duplicate or stale ecommerce state;
- SPA navigation timing.

If a critical required value is unavailable or incompatible, block the affected tag design and specify the required dataLayer change. Do not develop the site within this skill.

Do not assume that an analytics `item_id` is the identifier used by a media catalog or feed. Do not
coerce a numeric string, derive a total, choose a default currency, or synthesize `content_type`
unless the approved source/media requirement and current destination documentation establish that
rule.

## Prefer the least-complex mapping

Select the target mapping from the approved collection contract, applicable skill playbook, and
current official/template documentation before considering local container patterns. Use this order:

1. direct template field or DLV for an already compatible approved source;
2. constant for a stable configuration value or approved fixed semantic value;
3. supported settings variable for a coherent set of genuinely shared fields;
4. lookup/regex table for a real deterministic multi-scenario mapping when it makes environment,
   destination, currency, event, or other configuration logic clearer than repeated conditions;
5. Custom JavaScript for a required destination transformation that built-in variables cannot express cleanly.

After selecting the target pattern, reuse an existing variable only when it implements that pattern
and passes current source, type/shape, null, timing, consumer, consent, environment, and static
acceptance checks. Do not preserve or reproduce a helper merely because the container already uses
that pattern. Harmless naming debt can remain; functional debt cannot become the new architecture.

Do not hard-code a measurement ID, pixel ID, conversion label, currency, or repeated semantic value when a clear named reference improves maintenance. Do not create a constant for a one-off literal when it adds no clarity or reuse.

Do not use Custom JavaScript to reinterpret routine CMP vendor consent when the documented CMP state can be tested directly in a native trigger condition. An undocumented or invalid CMP shape is a source-contract blocker, not a transformation requirement.

For analytics, do not create a mapping for a destination field absent from the approved collection
contract. A documented required field missing from the plan is a blocking discrepancy, while a
recommended or optional field remains omitted unless the analyst explicitly amends the input.

## Preserve arrays and object schemas

For ecommerce and content arrays:

- verify whether the destination expects one object, an array of IDs, or an array of objects;
- return an array for one item when the destination requires an array;
- map all eligible items;
- retain documented event-level versus item-level fields;
- preserve exact number/string types and allowed enums;
- calculate totals only from the documented source and rule;
- define behavior for empty arrays and missing required item fields;
- test zero-item, one-item, and multi-item payloads.

Do not silently select item zero. Do not silently drop an item with a missing required identifier and still report the event as valid; expose the data-quality failure or block the tag according to the approved rule.

Default to failing the complete affected media event when any item lacks a destination-required
identifier. Permit partial-item delivery only when current official documentation allows it and the
explicit media requirement defines that policy. Do not apply this media eligibility rule to enrich
or alter an approved analytics payload.

## Write narrow Custom JavaScript

Use one output purpose per variable. Make the function:

- deterministic and free of side effects;
- guarded for null, undefined, and wrong input type;
- explicit about string/number conversion;
- free of network calls, DOM mutation, dataLayer pushes, and invented values;
- able to return `undefined` when a critical source contract is not met;
- validated with representative inputs.

Name it `CJS - <Vendor> - <output>`, for example `CJS - Meta - contents`.

Avoid a broad `try/catch` that hides contract defects. Catch only a specifically anticipated error and preserve a visible validation failure.

## Make invalid events ineligible

A transformation output does not control tag firing by itself. Returning `undefined`, `{}`, or `[]`
can still leave the tag eligible and send value, currency, event name, or another partial payload.

When a required event-level field or item contract can be invalid:

1. Prefer a direct native trigger condition on the documented source when it expresses validity
   exactly.
2. Otherwise reuse the transformation's narrow validity result or create one narrow Boolean
   eligibility variable; do not build a generic validation framework.
3. Make the normal trigger require validity or attach an exception that activates for every invalid
   and unknown path on the same GTM event.
4. Confirm the eligibility guard covers empty arrays, invalid item IDs, wrong types, and any paired
   value/currency requirement established by current documentation.
5. Block the configuration when the required rule cannot be represented safely from the approved
   source.

Name a necessary validity variable for its vendor and purpose, for example
`CJS - Meta - purchase valid`. Keep the transformation and validity logic together only when one
narrow variable can expose the exact terminal result required by the installed template; do not
duplicate parsing across several helpers.

## Statically verify transformations

Use supplied non-sensitive payloads as small static vectors for each transformation actually
created. This is configuration verification, not a test mode or runtime recette. Check at least:

| Input case | Required check |
| --- | --- |
| Missing source | No invented value; affected field/tag follows the approved missing-data rule. |
| Empty array | Output matches documented empty behavior. |
| One item | Required array/object shape and types remain correct. |
| Multiple items | Every item is retained and correctly mapped. |
| Zero value/quantity | Zero is not mistaken for missing. |
| Invalid type | Transformation fails safely and visibly. |

Also verify that the related eligibility condition prevents the event tag from becoming eligible
when a required output is invalid. Do not claim that these static vectors prove browser execution.

## Defer event-ID architecture

Do not create a browser/server event ID, transaction-based deduplication map, or `gtm.start`/`gtm.uniqueEventId` Custom JavaScript variable in the current client-side-only scope. Add that architecture when server-side/deduplication support is intentionally introduced.
Load `transformation-patterns.md` when the same source-to-destination projection pattern recurs,
especially ecommerce item arrays, destination identifier arrays, scalar validation, or explicit
eligibility vectors. The pattern reference standardizes the function contract but current official
destination documentation still establishes every output field.
