# Implementation workflow

## Contents

- [1. Orient and authorize](#1-orient-and-authorize)
- [2. Select the requirement route](#2-select-the-requirement-route)
- [3. Resolve the workspace](#3-resolve-the-workspace)
- [4. Form the implementation contract](#4-form-the-implementation-contract)
- [5. Inspect the container as integration evidence](#5-inspect-the-container-as-integration-evidence)
- [6. Validate the source contract](#6-validate-the-source-contract)
- [7. Research, validate, and classify discrepancies](#7-research-validate-and-classify-discrepancies)
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

For an approved tracking plan, preserve its exact in-scope event names, outgoing fields, literals,
source mappings, and business timing. Do not optimize or redesign it. When a direct analytics request
does not yet contain an exact collection decision, present the documented choices and obtain the
analyst's decision before mutation.

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

Use the configuration-contract reference and capture:

- a source-scope manifest covering included, reference-only, excluded, and ambiguous source items;
- the approved collection contract separately from the technical implementation contract;
- business action, success moment, and expected destination use;
- vendor-neutral source event and exact timing;
- source fields, types, cardinality, null behavior, state lifetime, representative payloads, and evidence grades;
- destination platform, product, account/pixel/tag ID, template, and version;
- official event or conversion action and complete destination field schema;
- base/configuration behavior and whether it sends any automatic event;
- CMP, vendor identity, approved consent model, and denied/unknown behavior;
- optional first-party user-data feature and its explicit authorization;
- object change manifest, external dependencies, result status, and static acceptance criteria.
- the applicable skill reference architecture, preflight discrepancy report, and approved-to-intended conformance result.

Classify every missing input as discoverable, unnecessary for the selected route, or critical and blocking.

## 5. Inspect the container as integration evidence

Inventory relevant:

- tags, normal triggers, blocking/exception triggers, and sequencing;
- DLVs, constants, tables, Custom JavaScript, Google tag settings, and user-data variables;
- folders, notes, templates, template permissions/versions, and destinations;
- CMP tags, consent defaults/updates, built-in checks, and additional checks;
- automatic/enhanced measurement, Event Builder, auto-event, and duplicate browser installations;
- workspace conflicts and consumers of reusable objects.

Compare semantics, timing, output, ownership, consent behavior, and consumers rather than names alone.
When hard-coded code, CMS plugins, CMP configuration, or platform settings cannot be established from the available static evidence, record the external dependency or blocker instead of claiming that no duplicate or conflict exists.

Do not infer the target architecture from the most common or nearest existing pattern. Existing
container state can establish capabilities, template versions, IDs, consumers, conflicts, duplicate
risk, saved fields, and candidates for reuse. It cannot establish best practice merely because an
object already exists.

Use the applicable skill playbook and current official documentation to select the target pattern.
Classify each reuse candidate as conformant, conformant with harmless naming debt, nonconformant,
conflicting, or unknown. Reuse only the first two classes. Do not reproduce a legacy helper, trigger,
consent model, page-view pattern, or tag architecture without passing the current static criteria.

## 6. Validate the source contract

For every required source value:

1. Establish the exact dataLayer key and event where it becomes available from the approved source contract.
2. Establish type, format, cardinality, null/undefined behavior, state lifetime, stale-state risk, and evidence grade.
3. Validate supplied empty, one-item, and multi-item ecommerce examples when applicable; require representative examples when a transformation depends on shape.
4. Distinguish the source key from the DLV name, template field, and destination parameter.
5. Record missing or incompatible values as a dataLayer requirement/blocker; do not develop the site or invent a fallback.

For analytics, validate that the intended source event, source paths, literals, business filters, and
timing exactly match the approved collection contract. Do not add a source field merely because an
official optional or recommended destination parameter could consume it.

Prefer the clean dataLayer contract over DOM scraping, click-text inference, URL inference, or brittle selectors.

## 7. Research, validate, and classify discrepancies

Open current official documentation and verify:

- standard versus custom event choice and reserved/deprecated names;
- required, recommended, optional, and conditional fields;
- types, formats, enumerations, arrays/objects, and accepted identifiers;
- base tag, event tag, conversion, remarketing, or settings behavior;
- template field mapping and permissions;
- native consent capability and basic versus advanced behavior;
- exact per-product consent classification: strict/basic blocked, native stop/hold, advanced consent-aware, adaptive/anonymous analytics, or unverified;
- CMP lifecycle event, consent-state source, vendor identity, approved predicate, and documented value format.

Record the research evidence before mutation.

For an approved analytics plan, compare the official findings with the exact approved collection
contract. Classify every difference as:

- `blocking-error` when the plan is invalid, reserved, missing a required field, type/shape
  incompatible, unsupported, or impossible to implement safely;
- `advisory` when the approved choice remains valid but a recommended event, field, or convention
  may be more appropriate;
- `implementation-note` when documentation guides GTM/template mechanics without changing the
  collection contract.

Never substitute a recommended event or add a recommended/optional parameter automatically. Stop
the affected requirement for a blocking error. Preserve the approved contract for an advisory unless
the analyst explicitly amends it.

## 8. Decide consent architecture

Default to strict/basic behavior:

- create or reuse the smallest shared set of CMP blocking triggers that expresses the approved category/purpose, vendor, product, and initialization predicate;
- make unknown, undefined, uninitialized, and denied states block;
- use the CMP's documented state variable directly in a native GTM condition when it can express the policy safely;
- treat a CMP value outside its documented contract as an integration defect to resolve, not a reason to invent a consent helper variable;
- verify that the block's event matcher can activate on every normal firing event used by its consumer tags;
- attach it to every in-scope base/configuration and event tag for that vendor;
- give each base/configuration tag a verified normal-trigger opportunity after both an initial grant and a later grant; an exception that blocks a page-load trigger does not make that trigger run again;
- prove the expected firing logic from GTM trigger semantics, the approved CMP contract, and the planned object graph without presenting it as runtime observation.

Use advanced/native consent only when explicitly requested and approved. In that route, configure documented defaults and updates, preserve the vendor's intended denied-state behavior, and remove/avoid any blocking logic that would defeat it.

Make that decision for each browser product, not only for the parent vendor. Use the vendor consent-mode capability reference. If the official sources do not establish the denied-state request, storage, fields, and data-use behavior, retain strict/basic blocking or mark the advanced request blocked.

## 9. Design the object graph

Select the smallest best-practice reference architecture from the applicable skill playbooks,
approved consent policy, source contract, installed-template capabilities, and current official
documentation. Reconcile it with container integration constraints only after selecting that target.

Keep configuration/base tags from sending an automatic page view by default.

Default to:

- one exact approved Custom Event trigger per business action; when the approved input authorizes a new source contract, default to a vendor-neutral event;
- separate destination tags that consume the same event where semantics match;
- a separate page-view event instead of an automatic page view from a config/base tag;
- reusable constants for stable IDs or values where a reference is clearer;
- direct DLVs for compatible source values;
- lookup or regex tables only for real deterministic multi-scenario mappings;
- Custom JavaScript only for a necessary, documented transformation;
- explicit tag sequencing only when the template/vendor lifecycle requires it.

Justify every new object by a current requirement, a documented destination/template constraint, or the absence of a semantically compatible existing object. Do not create a helper variable, settings object, trigger, base tag, or page-view tag merely to normalize the container or anticipate a hypothetical future need.

For every reused object, prove that architecture, terminal output, source, type/shape, timing,
consent, consumers, template/version, environment, and future change path remain compatible. A name
or current value match is insufficient. If a nonconformant existing object would conflict with the
best-practice implementation, update or disable it only when authorized; otherwise block the
affected requirement. Never knowingly add a parallel duplicate.

Check duplicate automatic/manual events and page-view timing before finalizing.

## 10. Present the plan when risk requires it

For every analytics tracking-plan implementation, present the concise discrepancy report before the
first write. A zero-discrepancy result needs no additional approval. An advisory states that the
default is faithful implementation. A blocking error stops the affected requirement until an amended
approved input is supplied.

Run the approved-to-intended collection-contract conformance check before mutation. Require identical
scope, requirement IDs, events, business timing, fields, sources, and literals, with zero unauthorized
additions, removals, or substitutions. Keep implementation infrastructure in a separate manifest.

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

Before the first write, finalize the object change manifest, capture IDs/fingerprints and exact pre-change state for modified objects, record pre-existing workspace changes, inspect workspace synchronization/conflicts, and confirm that rerunning the same contract will not create duplicates.

Apply dependency order:

1. folders or templates when approved;
2. constants, DLVs, tables, settings variables, and transformations;
3. normal and blocking triggers;
4. base/configuration tags;
5. event/conversion/remarketing tags;
6. sequencing and consent settings.

Re-read every saved object, compare it with the manifest, inspect references, preserve unrelated changes, and record current-run created, modified, reused, and untouched objects separately from pre-existing workspace changes and final workspace totals. Re-evaluate the manifest after an unexpected saved field, consumer, or fingerprint. Never publish or create a version.

## 12. Validate and hand off

Apply the acceptance reference. Separate:

- approved-to-intended and approved-to-saved collection-contract conformance results;
- source-scope classifications, blocking errors, advisories, and implementation notes;
- pre-existing workspace changes, current-run changes, and final workspace totals;
- documentation- and static configuration-verified assertions;
- the explicit boundary that runtime validation was not performed or claimed;
- blockers and missing dataLayer requirements;
- external site, CMP, GA4-administration, and advertising-platform dependencies;
- explicitly deferred server-side or deduplication work.

If no mutation tool is available, return the complete object-level specification as `Specification complete` and state clearly that no live configuration changed.
