# Operational implementation workflow

## Contents

- [1. Resolve only blocking inputs](#1-resolve-only-blocking-inputs)
- [2. Create or reuse the workspace](#2-create-or-reuse-the-workspace)
- [3. Research the product and installed template](#3-research-the-product-and-installed-template)
- [4. Inspect relevant container integration](#4-inspect-relevant-container-integration)
- [5. Build the configuration map](#5-build-the-configuration-map)
- [6. Design and preflight the object graph](#6-design-and-preflight-the-object-graph)
- [7. Mutate in dependency order](#7-mutate-in-dependency-order)
- [8. Read back, correct, and hand off](#8-read-back-correct-and-hand-off)

Use this single internal workflow for every actual configuration. Analytics, media, ecommerce,
first-party data, and consent are conditional configuration requirements, not different operating
modes. Work continuously unless a critical input, conflict, or mutation failure blocks the affected
objects.

## 1. Resolve only blocking inputs

Confirm the target account and web container, then derive or request the applicable business input:

- For analytics, use the approved tracking plan or exact direct analytics requirement. Preserve the
  selected event, outgoing fields, literals, source mappings, filters, and business timing.
- For media, use the explicit human brief for platform, business action, intended use, and
  destination identity. Use a tracking plan only for compatible source events and values.
- For consent, default to strict/basic CMP blocking. Detect the installed CMP and its documented
  state where possible. Require an explicit request for advanced/native behavior.

Discover destination IDs, installed templates, CMP objects, source variables, folders, and other
safe container facts before asking. Ask only for a critical fact that cannot be established and
changes the configuration. Do not ask for a read-only, planning, or test mode.

Limit the source artifact to its relevant configuration scope. Resolve an ambiguous sheet, row,
event, media objective, or consent identity before mutating the dependent object; do not turn the
exercise into a tracking-plan or container audit.

## 2. Create or reuse the workspace

For the requested configuration:

1. Reuse a compatible dedicated workspace for the same owner and scope, or create a clearly named
   dedicated workspace.
2. Resolve it by stable ID and record its pre-existing changes, synchronization state, and
   conflicts.
3. Use the Default Workspace only after the analyst explicitly accepts why a dedicated workspace is
   unavailable.
4. Keep the same account, container, and workspace across MCP, API, export/import, and UI tools.

Never publish, Submit, or create a GTM version.

## 3. Research the product and installed template

Before designing a tag or transformation, open current official documentation for the exact
client-side product and establish:

- official event/conversion classification and exact field schema;
- required, recommended, optional, and conditional fields;
- types, formats, enums, arrays, objects, identifiers, and cardinality;
- base/configuration, automatic-event, page-view, and matching behavior;
- supported basic, advanced, native, cookieless, or limited-data consent behavior;
- external platform requirements such as conversion actions, catalogs, feeds, or terms.

Then inspect the installed template's exact identity/version, publisher, permissions, visible fields,
defaults, and hidden automatic behavior. The official documentation establishes the technical
contract; the installed version establishes whether that contract can be configured in this
container. Block an unresolved mismatch instead of forcing a field or designing for a newer template
that is not installed.

For analytics, compare documentation with the approved collection contract. Preserve a technically
valid advisory by default and stop only an invalid, reserved, required-field, type/shape,
unsupported, or unsafe requirement. For media, official vendor documentation establishes the
destination schema; never infer it from GA4 or another media platform.

## 4. Inspect relevant container integration

Inspect only objects that can supply, consume, duplicate, block, or conflict with the requested
configuration:

- destination/configuration and event tags, triggers, exceptions, sequencing, and advanced settings;
- source DLVs, constants, settings variables, LUTs, RLTs, transformations, and their consumers;
- folders and naming conventions for the relevant object family;
- CMP tags, readiness/update events, state variables, consent defaults, and additional checks;
- installed template consumers, versions, and permissions;
- known automatic, Enhanced Measurement, Event Builder, SPA, partner, plugin, or hard-coded paths;
- workspace conflicts, stable IDs, fingerprints, and pre-existing changes.

Use the applicable playbook and current official documentation to select the target architecture
before evaluating local reuse. Reuse only a semantically compatible object. Do not reproduce a
legacy pattern, inventory unrelated objects, move unrelated objects, or add a clean parallel tag
around a known conflict.

When outside-container code or platform settings cannot be established from supplied static
evidence, record the exact external dependency. Do not claim that no duplicate exists.

## 5. Build the configuration map

Use the configuration-contract reference as a concise internal mutation map. For every independent
business action and destination, establish:

- approved event/action and exact success moment;
- source event, required paths, type/shape, timing, lifetime, and missing-data behavior;
- destination product, identity, official event/conversion, and complete configured field set;
- GTM resolution for each field: direct value, DLV, constant, settings variable, LUT/RLT, or
  necessary transformation;
- installed-template field and version;
- normal trigger, basic block or explicitly approved advanced consent mechanism, and firing option;
- object action (`create`, `update`, `reuse`, or `untouched`), dependencies, folder, and intended
  saved fields;
- relevant external dependency or blocker.

Do not demand a separate source-contract document when approved inputs establish these facts. When
a required value is absent or incompatible, record the precise dataLayer obligation and block the
affected object. Do not develop the site, scrape the DOM, infer a click/URL success, coerce an
unapproved type, or invent a fallback.

## 6. Design and preflight the object graph

Choose the smallest understandable architecture that satisfies the approved requirement:

Justify every create or update by a current approved requirement or documented implementation
constraint. Do not create speculative future helpers.

1. Reuse or create a shallow folder when several related objects benefit from grouping.
2. Prefer direct template fields/DLVs, then clear constants or shared settings variables.
3. Use LUTs or RLTs for real deterministic multi-scenario mappings with a safe no-match result.
4. Use narrow Custom JavaScript only for a required array/object or multi-step conversion.
5. Create precise normal triggers and the smallest reusable basic-consent block set.
6. Create or update one compatible initialization path and separate requested event tags.
7. Reconcile automatic/manual page views and business events before adding another event source.

For ecommerce, preserve every required item and exact destination type/shape. Establish catalog/feed
identifier mapping explicitly. Do not silently drop invalid items. A transformation that returns
`undefined`, `{}`, or `[]` does not itself stop a tag; add the smallest explicit native eligibility
condition or narrow validity guard when the tag could otherwise send an invalid required payload.

Follow the default naming convention unless the analyst supplied another clear convention. An
existing coherent convention may be retained for presentation, never for architecture.

Before the first write:

- report analytics documentation discrepancies concisely;
- surface advanced consent, first-party data, new template permissions, Default Workspace use,
  non-dataLayer fallbacks, and unresolved duplicate architecture for the required decision;
- compare the approved analytics contract with the intended event and field set and require zero
  unauthorized additions, removals, substitutions, or timing changes;
- capture stable IDs, fingerprints, pre-change state for updates, and mutation dependencies.

## 7. Mutate in dependency order

Prefer a purpose-built GTM MCP, then the GTM API, and use the UI only for unavailable semantic fields
or controlled fallback. Discover the adapter's actual actions, pagination, limits, returned fields,
and conflict behavior before mutation.

Apply only the requested configuration in this order:

1. approved templates and folders;
2. constants, DLVs, settings variables, LUTs/RLTs, transformations, and validity variables;
3. normal and blocking triggers;
4. base/configuration tags;
5. event, conversion, and remarketing tags;
6. sequencing, firing settings, and consent settings.

After each logical save, re-read the object and compare its stored fields and references. Stop
dependent writes on an unexpected fingerprint, consumer, normalized field, template change,
conflict, authentication failure, or partial write. Never retry an uncertain create blindly; first
read back by stable parent, identity, and semantics to avoid a duplicate.

## 8. Read back, correct, and hand off

Before `Configured`:

- re-read every created, updated, and reused object from the target workspace;
- prove analytics approved-to-saved event, timing, field, source, and literal equality;
- prove media brief-to-official-schema and source-to-template mappings;
- confirm normal triggers, consent blocks/settings, firing options, sequencing, folders, naming, and
  template fields;
- resolve every GTM reference and known in-scope duplicate/conflict;
- distinguish pre-existing workspace changes from current-run writes and final totals;
- recompute the intended actions so an identical rerun is entirely `reuse` or `untouched`.

Correct safe current-operation differences before finishing. Use `Partial` for an exact saved partial
state and stop its dependent writes. Use `Blocked` when a critical input or mutation path prevents
configuration. Use `Deferred` only for the explicitly future server-side/deduplication capability.

Return a concise handoff containing the workspace, configured objects, conformance result,
discrepancies, blockers/partial state, and external dependencies. State that runtime recette was not
performed and that no publication or version action occurred.
