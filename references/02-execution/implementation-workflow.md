# Implementation workflow

## Contents

- [1. Orient and authorize](#1-orient-and-authorize)
- [2. Select the requirement route](#2-select-the-requirement-route)
- [3. Resolve the workspace](#3-resolve-the-workspace)
- [4. Form the implementation contract](#4-form-the-implementation-contract)
- [5. Inspect before designing](#5-inspect-before-designing)
- [6. Validate the source contract](#6-validate-the-source-contract)
- [7. Research each destination and CMP](#7-research-each-destination-and-cmp)
- [8. Decide consent architecture](#8-decide-consent-architecture)
- [9. Design the object graph](#9-design-the-object-graph)
- [10. Present the plan when risk requires it](#10-present-the-plan-when-risk-requires-it)
- [11. Mutate only the approved scope](#11-mutate-only-the-approved-scope)
- [12. Validate and hand off](#12-validate-and-hand-off)

## 1. Orient and authorize

Confirm:

- target account, web container, environment, and requested workspace;
- read-only, planning, or explicitly authorized mutation;
- analytics, media, consent, or combined scope;
- current client-side work versus deferred server-side/deduplication work;
- requested advertising-platform changes outside GTM, if any, and keep them outside scope unless separately authorized.

Do not mutate for a review or planning request.

## 2. Select the requirement route

For analytics, treat the approved tracking plan or direct analytics requirement as the primary business input.

For media, treat the media-team brief as the primary business input. Capture at least the platform, requested business action, intended use, and destination identity or identify which of these is still blocking. Use any tracking plan only to discover reusable business events and source fields.

Do not require the media event to exist in the analytics plan. Do not copy a GA4 destination name into another platform.

## 3. Resolve the workspace

For authorized changes:

1. Reuse a dedicated workspace with the same owner and scope when compatible.
2. Otherwise create a dedicated implementation workspace when permitted.
3. Record workspace name/ID, owner, scope, and pre-existing changes.
4. Detect workspace conflicts before mutation.
5. Use the Default Workspace only after explaining why a dedicated workspace is unavailable and obtaining analyst approval.

Do not create a workspace for a read-only request.

## 4. Form the implementation contract

Capture:

- business action, success moment, and expected destination use;
- vendor-neutral source event and exact timing;
- source fields, types, cardinality, null behavior, and representative payloads;
- destination platform, product, account/pixel/tag ID, template, and version;
- official event or conversion action and complete destination field schema;
- base/configuration behavior and whether it sends any automatic event;
- CMP, vendor identity, approved consent model, and denied/unknown behavior;
- optional first-party user-data feature and its explicit authorization;
- acceptance criteria and runtime tests still required.

Classify every missing input as discoverable, unnecessary for the selected route, or critical and blocking.

## 5. Inspect before designing

Inventory relevant:

- tags, normal triggers, blocking/exception triggers, and sequencing;
- DLVs, constants, tables, Custom JavaScript, Google tag settings, and user-data variables;
- folders, notes, templates, template permissions/versions, and destinations;
- CMP tags, consent defaults/updates, built-in checks, and additional checks;
- automatic/enhanced measurement, Event Builder, auto-event, and duplicate browser installations;
- workspace conflicts and consumers of reusable objects.

Compare semantics, timing, output, ownership, consent behavior, and consumers rather than names alone.

## 6. Validate the source contract

For every required source value:

1. Verify the exact dataLayer key and event where it becomes available.
2. Verify type, format, cardinality, null/undefined behavior, and stale-state risk.
3. Test empty, one-item, and multi-item ecommerce payloads when applicable.
4. Distinguish the source key from the DLV name, template field, and destination parameter.
5. Record missing or incompatible values as a dataLayer requirement/blocker; do not develop the site or invent a fallback.

Prefer the clean dataLayer contract over DOM scraping, click-text inference, URL inference, or brittle selectors.

## 7. Research each destination and CMP

Open current official documentation and verify:

- standard versus custom event choice and reserved/deprecated names;
- required, recommended, optional, and conditional fields;
- types, formats, enumerations, arrays/objects, and accepted identifiers;
- base tag, event tag, conversion, remarketing, or settings behavior;
- template field mapping and permissions;
- native consent capability and basic versus advanced behavior;
- exact per-product consent classification: strict/basic blocked, native stop/hold, advanced consent-aware, adaptive/anonymous analytics, or unverified;
- CMP lifecycle event, consent-state source, vendor identity, and actual value format.

Record the research evidence before mutation.

## 8. Decide consent architecture

Default to strict/basic behavior:

- create or reuse one shared CMP blocking trigger per vendor/platform;
- make unknown, undefined, uninitialized, and denied states block;
- use the CMP's documented state variable directly in a native GTM condition when it can express the policy safely;
- treat a CMP value outside its documented contract as an integration defect to resolve, not a reason to invent a consent helper variable;
- verify that the block's event matcher can activate on every normal firing event used by its consumer tags;
- attach it to every in-scope base/configuration and event tag for that vendor;
- give each base/configuration tag a verified normal-trigger opportunity after both an initial grant and a later grant; an exception that blocks a page-load trigger does not make that trigger run again;
- prove the final firing logic rather than merely observing consent state.

Use advanced/native consent only when explicitly requested and approved. In that route, configure documented defaults and updates, preserve the vendor's intended denied-state behavior, and remove/avoid any blocking logic that would defeat it.

Make that decision for each browser product, not only for the parent vendor. Use the vendor consent-mode capability reference. If the official sources do not establish the denied-state request, storage, fields, and data-use behavior, retain strict/basic blocking or mark the advanced request blocked.

## 9. Design the object graph

Keep configuration/base tags from sending an automatic page view by default.

Default to:

- one vendor-neutral Custom Event trigger per business action;
- separate destination tags that consume the same event where semantics match;
- a separate page-view event instead of an automatic page view from a config/base tag;
- reusable constants for stable IDs or values where a reference is clearer;
- direct DLVs for compatible source values;
- lookup or regex tables only for real deterministic multi-scenario mappings;
- Custom JavaScript only for a necessary, documented transformation;
- explicit tag sequencing only when the template/vendor lifecycle requires it.

Justify every new object by a current requirement, a documented destination/template constraint, or the absence of a semantically compatible existing object. Do not create a helper variable, settings object, trigger, base tag, or page-view tag merely to normalize the container or anticipate a hypothetical future need.

Check duplicate automatic/manual events and page-view timing before finalizing.

## 10. Present the plan when risk requires it

Before mutation, surface decisions that materially affect data collection or architecture, including:

- advanced consent instead of the default strict/basic route;
- automatic or manual first-party user-data collection;
- adding/updating a community template or accepting new permissions;
- a non-dataLayer trigger fallback;
- use of the Default Workspace;
- unresolved automatic-event or page-view duplication.

Obtain the necessary approval; do not broaden the original authorization.

## 11. Mutate only the approved scope

Prefer a purpose-built GTM MCP or API. Use UI only when a required operation is unavailable or for visual verification.

Apply dependency order:

1. folders or templates when approved;
2. constants, DLVs, tables, settings variables, and transformations;
3. normal and blocking triggers;
4. base/configuration tags;
5. event/conversion/remarketing tags;
6. sequencing and consent settings.

Re-read every saved object, inspect references, preserve unrelated changes, and record created, modified, reused, and untouched objects. Never publish or create a version.

## 12. Validate and hand off

Apply the acceptance reference. Separate:

- documentation- and configuration-verified behavior;
- runtime Preview/network/vendor tests still required;
- blockers and missing dataLayer requirements;
- explicitly deferred server-side or deduplication work.

If no mutation tool is available, return the complete object-level specification and state clearly that no live configuration changed.
