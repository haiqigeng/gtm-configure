# Meta Pixel browser tags

## Complete the media brief

Confirm or derive:

- Meta Pixel/dataset ID and environment;
- requested business action and its optimization/conversion/audience use;
- current standard event or justified custom event;
- catalog identity and product-ID convention for commerce events;
- required value, currency, order/transaction reference, and item fields;
- advanced matching request and approved user-data sources;
- CMP vendor identity and strict/basic gate.

Do not use a GA4 event name as the Meta destination name unless Meta's current official standard event has that exact name and meaning.

## Research the current Meta browser schema

Open the current official Meta Pixel event reference and the installed GTM template documentation/repository. Record:

- exact standard event spelling and meaning;
- standard, custom, reserved, or deprecated status;
- required, recommended, optional, and conditional parameters;
- accepted types, formats, arrays, and object keys;
- catalog matching rules for content identifiers;
- template fields, version, publisher, permissions, and advanced-matching behavior.

If Meta's official page is unavailable, retry or use another current official Meta source. Block critical schema decisions rather than relying on remembered standard-event lists.

## Separate initialization and PageView

Ensure one compatible Meta Pixel initialization path exists. Reuse a compatible GTM base tag, hard-coded Pixel, plugin, or partner integration; create a new GTM base/configuration tag only when initialization is in scope and no compatible path exists. Do not include `PageView` in a newly configured base tag by default. Create a separate `Meta - Event - PageView` tag only when requested and after checking hard-coded pixels, plugins, automatic event setup, and existing tags.

Use separate event tags such as `Meta - Event - <official_event>` for business actions. Trigger them from the vendor-neutral Custom Event and apply the shared Meta block.

## Map ecommerce fields without losing items

Treat each current Meta parameter as an independent contract. Where the official browser schema requires them:

- return `content_ids` in the documented array form and preserve every eligible ID;
- return `contents` as an array of documented content objects and preserve every eligible item;
- match content IDs to the catalog's actual identifier convention;
- calculate or map value and currency according to the documented event semantics;
- preserve number versus string types for item values;
- test empty, one-item, and multi-item payloads.

Do not flatten `contents`, stringify the array, or select the first item. Do not assume `content_ids` and `contents` accept the same shape.

Use names such as `CJS - Meta - content_ids` and `CJS - Meta - contents` only when a transformation is necessary. Reuse a direct DLV when it already has the exact documented shape.

## Select standard or custom events deliberately

Prefer a current Meta standard event when its meaning matches the requested action and supports the intended optimization/reporting. Use a custom event only after checking current naming and optimization limitations and confirming the media-team requirement.

Do not assume that a browser custom event automatically creates the intended Custom Conversion in Events Manager.

## Configure advanced matching only explicitly

Do not enable automatic or manual advanced matching by default. Require explicit request/approval, identify accepted browser identifiers and normalization/hashing behavior from current Meta documentation/template, verify CMP permission, and follow the first-party-data reference.

Avoid collecting user data from the DOM automatically when the agreed implementation requires controlled dataLayer sources.

## Apply consent

Use strict/basic gating by default for the Meta base and all Meta events:

- attach `Block - <CMP> - Meta denied`;
- block unknown, uninitialized, and denied state;
- verify that no Meta script or request loads before the required grant.

Use native limited-data or consent features only when explicitly requested and documented for the selected browser template. A grant/revoke command or built-in consent control does not by itself prove cookieless denied-state measurement or modeling. Follow the vendor consent-mode capability reference and do not infer Google Consent Mode behavior.

## Official entry point

- https://developers.facebook.com/docs/meta-pixel/reference/
