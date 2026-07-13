# Media tags

## Configure from the vendor schema, not by analogy

Media platforms differ in browser tag templates, event names, required fields, accepted formats, matching rules, and consent/vendor identity. For every vendor:

1. Retrieve the current official browser/pixel/tag documentation and the installed GTM template's field definitions.
2. Establish the official event and parameter schema for the requested business action.
3. Map the vendor-neutral dataLayer event to that schema.
4. Use a normal business trigger and the verified vendor gate.
5. Validate the resolved browser payload with representative data.

Do not copy GA4 names, types, or transformations into a media tag unless that vendor's official documentation requires the same shape.

## Build a vendor mapping sheet

Capture these decisions before configuration:

| Field | Record |
| --- | --- |
| Vendor and browser tag/template | Exact product and template version. |
| Official event | Exact vendor event name and classification. |
| Parameter schema | Required/optional status, type, enum, and shape. |
| Source | dataLayer key, existing variable, or constant. |
| Transformation | Exact logic, null behavior, and representative output. |
| Consent | CMP vendor identity and the shared blocking trigger. |
| Validation | Expected payload for zero, one, and many items where applicable. |

## Transform only when the schema requires it

Prefer a DLV, constant, lookup table, or regex lookup table when it produces the documented result clearly. Use Custom JavaScript only when the vendor requires a data shape or logic that the built-in variables cannot express cleanly.

Write Custom JavaScript to be:

- deterministic and null-safe;
- limited to one well-defined transformation;
- free of invented fallback values;
- validated with representative dataLayer input;
- named for its vendor-specific output.

For example, name a Meta contents transformation "CJS - Meta - contents", not a generic or ambiguous name.

## Ecommerce and multi-item payloads

Preserve every line item. When vendor documentation requires arrays:

- return an array even for a single item;
- map every eligible item, not only the first one;
- produce the vendor's required object keys and numeric/string types;
- decide documented behavior for missing item IDs, quantities, prices, or currency;
- test empty, one-item, and multi-item inputs.

For Meta-style ecommerce mappings, "content_ids" and "contents" are different fields with different shapes. When the official schema requires them, ensure "content_ids" is an array of strings and "contents" is an array of objects. Do not flatten the array, stringify it, or select only item zero.

## V1 implementation boundary

This V1 configures browser/client-side tags only. Server-side GTM, Conversions API, browser/server deduplication, transport URL, and related routing are deferred capabilities of this same skill. When requested in V1, record them as deferred and do not add a server-specific parameter or event-ID variable.

## Naming examples

| Object | Example |
| --- | --- |
| Media event tag | "Meta - Event - purchase" |
| Vendor transformation | "CJS - Meta - contents" |
| Vendor constant | "CST - Meta pixel_id" |
| Shared Custom Event trigger | "CE - purchase" |
| Vendor consent exception | "Block - Didomi - Meta denied" |
