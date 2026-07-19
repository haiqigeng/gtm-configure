# Naming and reuse

## Follow type, owner, and purpose

Preserve an established compatible container convention. Otherwise use:

| Object type | Pattern | Example |
| --- | --- | --- |
| Tag | Vendor - type - event/qualifier | `GA4 - Event - page_view`, `Meta - Event - Purchase` |
| Config/base tag | Vendor - Config | `GA4 - Config`, `Meta - Config` |
| Normal trigger | Trigger type - value | `CE - purchase`, `Click - newsletter_cta` |
| Blocking trigger | Block - CMP - vendor denied | `Block - Didomi - Meta denied` |
| DataLayer variable | DLV - actual source value/path | `DLV - ecommerce.items` |
| Constant | CST - semantic value | `CST - GA4 measurement_id`, `CST - currency` |
| Custom JavaScript | CJS - vendor - output | `CJS - Meta - contents` |
| Lookup table | LUT - purpose | `LUT - currency by hostname` |
| Regex lookup table | RLT - purpose | `RLT - environment by hostname` |
| Google settings variable | Vendor - setting type | `GA4 - Config Setting`, `GA4 - Event Setting` |

Keep vendor/platform first for tags and vendor-owned special settings. Keep variable type first for ordinary variables. Use snake_case for source event names and field-oriented values. Preserve official destination event casing when the vendor requires another form.

Use a short stable acronym only when the full type/vendor name is unwieldy and the container recognizes it. Do not invent prefixes such as `GCS` for GA4 configuration.

## Name source and destination independently

Name a DLV after the actual source key, including an intentional source typo if that is the real contract. Use the official destination name in the tag field, not in a misleading DLV rename.

Name a vendor transformation after its output, not its input. For example, use `CJS - Meta - contents` for the Meta-formatted result.

## Reuse by semantic equivalence

Before creating an object, inspect candidates and all their consumers. Reuse only when these dimensions align:

- object type and terminal output;
- business and vendor ownership;
- data type, shape, and null behavior;
- source timing and event scope;
- normal and consent firing behavior;
- template/version and destination compatibility;
- environment/hostname scope;
- expected future change path.

Matching names or values alone are insufficient. Two IDs with the same current string can require separate constants when they belong to different destinations or owners. Conversely, do not duplicate a compatible object merely because its name is imperfect; reuse it and report naming debt unless renaming is authorized.

## Prefer references over repeated literals

Use a constant or settings variable when it makes a stable value visible, reusable, and safer to change. Typical candidates include measurement IDs, pixel IDs, UET IDs, conversion IDs/labels, and a genuinely fixed currency.

Do not force a constant for every literal. Keep an event-specific value on the tag when a reference adds indirection without reuse or clarity.

## Use lookup tables only when applicable

Create a LUT/RLT only when:

- multiple real input scenarios exist;
- the mapping is deterministic;
- default/no-match behavior is safe and explicit;
- it reduces duplication or clarifies environment/vendor mapping;
- representative cases can be tested.

Apply the same rule to analytics and media. Do not use a table for a single mapping or force unrelated scenarios together.

## Organize folders sparingly

Follow the container's existing folder model. When no useful model exists and the change is large enough to benefit, prefer a shallow structure by vendor/platform or implementation workstream.

Do not create a folder for one isolated object. Do not move unrelated existing objects merely to make the new workspace look tidy; that is cleanup scope.

## Add notes where they preserve non-obvious decisions

Use object notes/descriptions when supported to record a critical source event, vendor schema decision, consent exception, template dependency, or temporary blocker. Keep notes concise and free of client secrets or personal data.

Do not duplicate the entire handoff inside every object.
