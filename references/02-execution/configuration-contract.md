# Operational configuration map

## Contents

- [Purpose and priority](#purpose-and-priority)
- [Keep business and implementation decisions separate](#keep-business-and-implementation-decisions-separate)
- [Use one concise record per requirement](#use-one-concise-record-per-requirement)
- [Retain critical provenance](#retain-critical-provenance)
- [Map fields and event eligibility](#map-fields-and-event-eligibility)
- [Map GTM object actions](#map-gtm-object-actions)
- [Prove analytics conformance](#prove-analytics-conformance)
- [Record consent and external dependencies](#record-consent-and-external-dependencies)
- [Apply operational statuses](#apply-operational-statuses)
- [Completion invariants](#completion-invariants)

## Purpose and priority

Build a concise internal requirement-to-object map before the first write. Use the same map for
MCP/API/UI mutation, saved-object comparison, idempotency, and the concise handoff. It is an
operational control, not a separate planning deliverable.

Resolve tradeoffs in this order:

1. data handling and consent safety;
2. exact fidelity to the approved analytics contract or explicit media business authority;
3. technical validity against current official product and installed-template documentation;
4. the smallest clean and maintainable best-practice GTM object graph;
5. compatible reuse, organization, and critical traceability;
6. completion of the saved client-side configuration.

Do not weaken a higher priority to obtain a tidier container or a more complete-looking result.
When a technically invalid analytics requirement conflicts with fidelity, stop that requirement and
request an amended approved input; never redesign it automatically.

## Keep business and implementation decisions separate

| Layer | Authority | Contents |
| --- | --- | --- |
| Approved collection decision | Analytics tracking plan or exact direct analytics requirement; for media, explicit brief plus the current official destination schema | Business action, event/conversion, outgoing fields and literals, source event/paths, success timing, repeatability, and business filters. |
| GTM implementation decision | Applicable playbook, current official documentation, installed template, source values, consent requirement, and relevant container integration | Workspace, object actions, names/folders, DLV version, mappings, triggers, consent, firing settings, sequencing, adapter fields, and readback. |

Do not use implementation infrastructure to add or change an analytics payload. Technical IDs,
folder references, consent settings, trigger references, and template mechanics are not payload
enrichment, but each must serve the current configuration or a documented product constraint.

## Use one concise record per requirement

Create one record per independently configurable business action and destination. Keep separate
records when destination, business meaning, consent route, source timing, environment, ownership, or
future change path differs.

Capture only what mutation and verification need:

- stable requirement/source reference and `included`, `reference-only`, `excluded`, or `ambiguous`
  scope when the supplied artifact contains multiple relevant parts;
- analytics tracking-plan decision or media objective and exact success moment;
- source event and required fields with type/shape, timing, lifetime, and missing-data rule;
- destination product/ID, official event or conversion, configured outgoing field set, and intended
  use;
- installed tag/template identity, version, fields, defaults, and relevant permissions;
- GTM field resolution, normal trigger, consent mechanism, firing option, and folder;
- object actions and dependencies;
- discrepancy, blocker, external dependency, and final operational status.

Do not force a large worksheet-style record for a direct one-field mapping. Add detail in proportion
to transformation, consent, shared-consumer, template, or mutation risk.

## Retain critical provenance

Keep source attribution for facts that determine a write:

| Provenance | Permitted decision |
| --- | --- |
| `approved-input` | Analytics semantics, media objective, client policy, and explicit analyst decisions. |
| `official-current` | Destination schema, GTM behavior, template expectations, and supported consent capability. |
| `container-confirmed` | Installed objects/templates, stable IDs, consumers, conflicts, fingerprints, and saved fields. It never proves best practice. |
| `contract-sample` | dataLayer/source timing, type, shape, cardinality, null behavior, and representative transformation input. |

An assumption may explain non-critical context but may not supply a destination ID, required source,
field type/shape, consent predicate, template capability, or mutation target. Ask for or discover the
critical fact instead. Preserve official URLs, titles, and access dates for schema, discrepancy,
template, and consent decisions; do not produce a citation ledger for routine self-evident object
names.

## Map fields and event eligibility

For every outgoing field, preserve these distinct layers:

| Layer | Required decision |
| --- | --- |
| Source | Exact dataLayer/configuration path, event timing, type/shape, and representative value when needed. |
| GTM resolution | Direct value, DLV, constant, settings variable, LUT/RLT, or narrow transformation with missing-data behavior. |
| Template | Exact installed-template field and stored type. |
| Destination | Official parameter, requirement status, type, format, enum, scope, and cardinality. |

Use `mapped`, `intentionally omitted`, `external`, or `blocked` for exceptional field states. Preserve
valid zero and `false`. Never turn an absent required value into an empty string, placeholder,
guessed ID, invented literal, or silent item omission.

Define tag eligibility separately from transformation output. If a required event-level value or
required item contract is invalid and the tag could still execute, add the smallest explicit native
trigger condition/exception. Use a narrow validity variable only when native source conditions
cannot express the documented rule cleanly. Returning `undefined`, `{}`, or `[]` from another
variable does not prove that the tag is ineligible.

For arrays, define the empty, one-item, multi-item, and invalid-item result. Preserve every required
item. Default to failing the complete affected media event when a required item identifier is absent
unless current official documentation and the explicit media requirement authorize partial-item
delivery.

## Map GTM object actions

Create the complete in-scope object graph before mutation. For each object record:

- `create`, `update`, `reuse`, or `untouched`;
- object type, intended name/folder, stable existing ID/path, and fingerprint when applicable;
- requirement or documented constraint that justifies it;
- exact intended fields, references, consent route, and dependencies;
- compatible consumers and relevant environment/hostname scope;
- exact pre-change representation for an update;
- expected saved-object comparison.

Use `remove` only after explicit destructive authorization and confirmed ownership. A repeated run
against the final saved state must resolve every completed object to `reuse` or `untouched`.

Select the target architecture before reuse. A matching name or current value is insufficient.
Require compatible output, source, type/shape, timing, consent, consumers, template/version,
environment, and future change path. Keep harmless naming debt when reuse is otherwise correct; do
not inherit functional debt or add a parallel duplicate.

## Prove analytics conformance

Before the first analytics write, compare the approved contract with the intended event tags. After
mutation, compare it with authoritative workspace readback. Require:

- identical included requirement IDs;
- identical destination and source events;
- identical business timing and filters;
- exact outgoing parameter/property/item-field set equality;
- exact approved source or literal for every field;
- zero unauthorized additions, removals, substitutions, or hidden-scope inclusions.

Use `scripts/validate_contract_conformance.py` when the approved, intended, or saved representations
can be normalized to JSON. Keep implementation metadata outside `scope` and `requirements`. A
non-zero semantic difference blocks the affected write or `Configured` result until corrected or
supported by an explicit amended analytics decision.

## Record consent and external dependencies

For each browser product, record the normal trigger and either:

- strict/basic CMP block predicate, event scope, unknown/denied behavior, and initial/later grant
  opportunity; or
- explicitly approved advanced/native feature, defaults/updates, denied-state behavior, template
  fields, and product-specific official evidence.

Keep independent CMP grants as OR-denial across the smallest reusable block set. Reconcile consent
with every consumer of a shared execution unit.

Record but do not silently perform external work, including site/dataLayer changes, CMP setup, GA4
custom definitions or key events, Google tag/data-stream settings, advertising conversion actions,
catalog/feed work, platform account settings, publication, and server-side/deduplication work.

## Apply operational statuses

Use one status per requirement or tag family:

| Status | Meaning |
| --- | --- |
| `Configured` | Authoritative current-workspace readback proves that the saved object graph matches the approved requirement and all applicable completion invariants. The graph may have already matched without a write. |
| `Partial` | This run saved some in-scope objects but could not complete their dependent graph; the exact saved state and recovery boundary are known. |
| `Blocked` | A critical business, source, destination, template, consent, conflict, access, or mutation fact prevents safe configuration. No specification status substitutes for the missing write path. |
| `Deferred` | The requirement belongs to the intentionally future server-side GTM, CAPI, browser/server deduplication, or event-ID capability. |

Do not use `Configured` as a synonym for runtime-tested or published. Runtime recette and publication
remain separate.

## Completion invariants

Before `Configured`, prove from current workspace readback that:

1. every included requirement has an accurate status and no unresolved in-scope ambiguity;
2. every critical mutation fact has approved, official, container, or supplied-source provenance;
3. analytics collection semantics match exactly, or media fields match the explicit brief and
   current official destination schema;
4. every required source type/shape/timing and eligibility rule is compatible with the destination;
5. every tag has the intended normal trigger, consent route, firing option, and initialization path;
6. every GTM reference resolves and every reused consumer remains compatible;
7. known in-scope automatic/manual, destination, environment, and conflict duplicates are resolved;
8. first-party data remains limited to explicitly approved fields, sources, destinations, and
   consent states;
9. intended and saved fields match after every mutation, and an identical rerun is a no-op;
10. pre-existing workspace changes and current-run writes are distinguished;
11. blockers, external dependencies, and partial or deferred work are explicit;
12. no runtime claim, publication, Submit, or GTM version action occurred.
