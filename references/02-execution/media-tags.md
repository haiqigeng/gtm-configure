# Media tags

## Contents

- [Treat the media brief as the primary business input](#treat-the-media-brief-as-the-primary-business-input)
- [Normalize the media brief](#normalize-the-media-brief)
- [Use a four-authority model](#use-a-four-authority-model)
- [Build a field-level implementation map](#build-a-field-level-implementation-map)
- [Choose standard versus custom events](#choose-standard-versus-custom-events)
- [Separate base/configuration and event behavior](#separate-baseconfiguration-and-event-behavior)
- [Transform only for the documented schema](#transform-only-for-the-documented-schema)
- [Preserve ecommerce cardinality](#preserve-ecommerce-cardinality)
- [Govern first-party user data](#govern-first-party-user-data)
- [Apply consent](#apply-consent)
- [Handle an undocumented vendor](#handle-an-undocumented-vendor)
- [Current client-side boundary](#current-client-side-boundary)

## Treat the media brief as the primary business input

Expect media implementation requests to arrive directly from a media team rather than from an analytics tracking plan. Treat the brief as the authority for platform, business action, optimization/conversion use, audience use, and destination account.

Use any tracking plan only to discover reusable business events and source fields. Do not require the requested media event to appear in that plan, and do not assume that a media event should use a GA4 name or schema.

## Normalize the media brief

Derive or request only what the selected feature needs:

- vendor, browser product, account/pixel/tag/dataset identity, and environment;
- requested business action and exact success moment;
- optimization, conversion reporting, remarketing, catalog, or audience purpose;
- requested standard event, custom event, or conversion action when already decided;
- conversion ID/label, UET tag ID, pixel ID, feed/business vertical, or catalog identity as applicable;
- value, currency, transaction/order ID, product identifiers, and item details when applicable;
- first-party user-data or advanced-matching request, if any;
- client-approved CMP and consent model;
- existing dataLayer event and representative payload.

Do not create a tag from an informal label such as "purchase pixel" or "lead conversion" alone. Establish the destination identity and official event contract first.

## Use a four-authority model

1. Use the media brief for business intent and requested destination use.
2. Use current official vendor documentation for the destination event and parameter schema.
3. Use the existing dataLayer, tracking plan, and runtime evidence for source availability and timing.
4. Use the installed GTM template/version for actual UI fields and execution behavior.

Never configure one media platform by analogy with GA4 or another media vendor.

## Build a field-level implementation map

Record before mutation:

| Field | Record |
| --- | --- |
| Business action | Human-readable action and exact success moment. |
| Destination | Vendor, browser product, account/pixel/tag ID, and conversion action where applicable. |
| Official event | Exact name and standard, custom, reserved, or deprecated status. |
| Vendor parameter | Exact destination name. |
| Requirement | Required, recommended, optional, or conditionally required. |
| Contract | Type, format, enum, item/event scope, and cardinality. |
| Source | dataLayer key, existing GTM variable, constant, or approved fallback. |
| Transformation | Exact logic, null behavior, and zero/one/many output. |
| Template UI field | Visible field in the installed template/version. |
| Consent | CMP vendor identity, strict/basic block or explicitly approved native advanced behavior. |
| Evidence | Official URL, title, access date, and representative resolved payload. |

Do not conflate a dataLayer key, GTM variable, template UI field, and network parameter even when they share a label.

## Choose standard versus custom events

Prefer a current official standard event when its documented meaning matches the business action. Use a custom event only when:

- no standard event represents the action;
- the media team explicitly needs a separate custom event and the vendor permits it; or
- a documented product requirement needs a custom name.

Check reserved names, naming limits, reporting/optimization eligibility, and platform-side configuration requirements. Do not assume that sending a browser event automatically creates or configures a conversion action in the advertising platform.

## Separate base/configuration and event behavior

Configure base or initialization tags only for documented initialization and shared settings. Do not make a base/configuration tag send a page view by default.

First establish whether a compatible GTM tag, hard-coded implementation, partner integration, or template behavior already supplies initialization. Create a GTM base/configuration tag only when initialization is in scope and no compatible path exists.

Create page-view and business-event tags separately unless the current official template requires an inseparable documented base event. Where a base tag inherently emits a page-load event, document that exception and prevent any duplicate manual page-view tag.

Inspect automatic event detection, Event Builder rules, CMS plugins, hard-coded pixels, and existing templates before adding manual events.

## Transform only for the documented schema

Prefer a direct DLV, constant, lookup table, or regex table when it yields the exact required output. Use Custom JavaScript only when built-in variables cannot express the required array/object structure or deterministic transformation cleanly.

Make each Custom JavaScript variable deterministic, null-safe, narrowly scoped, free of invented fallbacks, and tested with representative source data. Name it for the vendor and output, for example `CJS - Meta - contents`.

## Preserve ecommerce cardinality

When the vendor requires an array:

- return an array even for one item when the schema requires it;
- map every eligible item rather than selecting item zero;
- preserve the required object keys and exact number/string types;
- handle missing IDs, quantities, prices, and currency according to documentation;
- test empty, one-item, and multi-item payloads.

Treat similarly named fields such as `content_id`, `content_ids`, `contents`, `items`, and product arrays as separate vendor contracts. Never flatten, stringify, or reshape them by analogy.

## Govern first-party user data

Do not enable enhanced conversions, advanced matching, automatic matching, DOM scanning, or user-provided data merely because the template offers it. Require explicit request/approval, verify current vendor policy and accepted fields, verify consent, and follow the first-party-data reference.

## Apply consent

Use strict/basic CMP gating by default for both base and event tags. Prefer one shared block per vendor/platform. Configure a native advanced consent mode only when the media team/analyst explicitly requests it, the vendor officially supports it, and its denied-state transmission is understood and approved.

## Handle an undocumented vendor

If no dedicated playbook exists:

1. Locate the current official browser implementation, event reference, parameter reference, consent, matching, and GTM/template documentation.
2. Apply this generic mapping contract.
3. Inspect template identity, version, permissions, and field definitions.
4. Block any critical field or behavior that official documentation does not establish.

Lack of a dedicated skill file never permits memory-based configuration.

## Current client-side boundary

Do not add event IDs or deduplication logic for a browser-only request. Record server-side GTM, Conversions API, and browser/server deduplication as deferred when encountered.
