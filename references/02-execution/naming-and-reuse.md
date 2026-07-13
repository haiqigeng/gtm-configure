# Naming and reuse

## Name by type, purpose, and owner

Follow existing container conventions where they are compatible with these rules. Keep vendor name/acronym first for vendor-specific tags and special Google tag settings.

| Object type | Pattern | Examples |
| --- | --- | --- |
| Tag | Vendor - type - event or qualifier | "GA4 - Event - page_view", "Meta - Event - purchase", "GA4 - Config - main" |
| Normal trigger | Trigger type - value | "CE - purchase", "Click - newsletter_cta" |
| Blocking trigger | Block - CMP - vendor denied | "Block - Didomi - Meta denied" |
| DataLayer variable | DLV - value | "DLV - page_location", "DLV - didomiVendorsEnabled" |
| Constant | CST - semantic value | "CST - GA4 measurement_id", "CST - currency" |
| Custom JavaScript | CJS - vendor - output | "CJS - Meta - contents" |
| Lookup table | LUT - purpose | "LUT - currency by hostname" |
| Regex lookup table | RLT - purpose | "RLT - content category" |
| GA4 setting variable | Vendor - setting type | "GA4 - Event Setting" |

Use snake_case for event names and field-oriented values. Use a short, stable acronym only when the full element type is unwieldy and the container already recognizes it. Do not invent a prefix such as "GCS" for a GA4 configuration.

## Reuse by semantic equivalence

Before creating an object, inspect all potentially related candidates. Reuse only when all relevant dimensions match:

- object type and terminal value/output;
- business/vendor purpose;
- data type and null behavior;
- trigger/event timing;
- consent/firing/blocking behavior;
- consumers and impact of future changes;
- folder/template compatibility where relevant.

Identical strings do not automatically justify reuse. For example, do not share two constants simply because both currently contain the same value if their ownership and future change paths differ.

Likewise, do not create duplicates simply because a matching object has an imperfect name. If it is semantically compatible, reuse it and report the naming debt separately unless an approved migration is in scope.

## Variable selection

Use the least complex variable that yields the documented output:

1. Reuse a compatible variable.
2. Use a DLV for direct dataLayer values.
3. Use a constant for stable configuration values where a reference is clearer than a hard-coded literal.
4. Use a lookup or regex lookup table when it meaningfully combines deterministic scenarios and has a tested default.
5. Use Custom JavaScript only for a transformation that built-in variables cannot represent clearly.

Do not force lookup tables, regex lookup tables, constants, event settings variables, or Custom JavaScript into a design. Use them for analytics and media alike only when they reduce real duplication or clarify a multi-scenario mapping.

## Lookup table decision check

Create a LUT/RLT only when all answers are yes:

- Does more than one real input scenario need a mapping?
- Is the mapping deterministic and understandable without code?
- Is there a safe default or explicit no-match behavior?
- Does it reduce duplicated configuration across tags or conditions?
- Can representative inputs and outputs be tested?

Otherwise, keep the direct variable mapping or a narrowly scoped transformation.
