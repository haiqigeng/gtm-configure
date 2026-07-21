# Data contract and transformations

## Contents

- [Establish the source event contract](#establish-the-source-event-contract)
- [Keep mapping layers distinct](#keep-mapping-layers-distinct)
- [Validate before transforming](#validate-before-transforming)
- [Prefer the least-complex mapping](#prefer-the-least-complex-mapping)
- [Preserve arrays and object schemas](#preserve-arrays-and-object-schemas)
- [Write narrow Custom JavaScript](#write-narrow-custom-javascript)
- [Test transformations](#test-transformations)
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
- item identifiers and catalog/feed alignment;
- duplicate or stale ecommerce state;
- SPA navigation timing.

If a critical required value is unavailable or incompatible, block the affected tag design and specify the required dataLayer change. Do not develop the site within this skill.

## Prefer the least-complex mapping

Select the target mapping from the approved collection contract, applicable skill playbook, and
current official/template documentation before considering local container patterns. Use this order:

1. direct template field or DLV for an already compatible approved source;
2. constant for a stable configuration value or approved fixed semantic value;
3. supported settings variable for a coherent set of genuinely shared fields;
4. lookup/regex table for a real deterministic multi-scenario mapping;
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

## Test transformations

Use supplied non-sensitive payloads as static test vectors and record at least:

| Input case | Required check |
| --- | --- |
| Missing source | No invented value; affected field/tag follows the approved missing-data rule. |
| Empty array | Output matches documented empty behavior. |
| One item | Required array/object shape and types remain correct. |
| Multiple items | Every item is retained and correctly mapped. |
| Zero value/quantity | Zero is not mistaken for missing. |
| Invalid type | Transformation fails safely and visibly. |

## Defer event-ID architecture

Do not create a browser/server event ID, transaction-based deduplication map, or `gtm.start`/`gtm.uniqueEventId` Custom JavaScript variable in the current client-side-only scope. Add that architecture when server-side/deduplication support is intentionally introduced.
