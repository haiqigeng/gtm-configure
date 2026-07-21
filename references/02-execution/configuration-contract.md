# Configuration contract

## Contents

- [Purpose and priority](#purpose-and-priority)
- [Collection and implementation contracts](#collection-and-implementation-contracts)
- [Source scope and discrepancies](#source-scope-and-discrepancies)
- [Evidence grades](#evidence-grades)
- [Requirement record](#requirement-record)
- [Field mapping](#field-mapping)
- [Object change manifest](#object-change-manifest)
- [Contract conformance](#contract-conformance)
- [Consent and external dependencies](#consent-and-external-dependencies)
- [Result statuses](#result-statuses)
- [Static completion invariants](#static-completion-invariants)

## Purpose and priority

Translate every approved requirement into one adapter-neutral configuration contract before
creating or modifying GTM objects. Use the contract as the common source for the human plan,
MCP/API/UI mutations, saved-object verification, and handoff.

Resolve tradeoffs in this order:

1. authorization, data handling, and consent safety;
2. exact fidelity to the approved analytics collection contract or media business authority;
3. technical validity against current official destination and template documentation;
4. the applicable skill reference architecture and smallest semantically correct GTM object graph;
5. conformant reuse, maintainability, and field-level traceability;
6. completion of the authorized static configuration.

Do not weaken a higher-priority requirement to obtain a tidier container or a more complete
change set.

For analytics, a conflict between fidelity and critical technical validity does not authorize an
automatic redesign. Block the affected requirement, report the discrepancy, and wait for an amended
approved input. A documented recommended alternative to a still-valid approved event or field is an
advisory, not a substitution instruction.

## Collection and implementation contracts

Keep two layers in the same configuration record:

| Layer | Authority | Contents |
| --- | --- | --- |
| Collection contract | Approved tracking plan or exact direct analytics decision; media brief plus official media schema for the media route | In-scope business action, destination event, outgoing fields/literals, source event and paths, success timing, repeatability, and business filters. |
| Implementation contract | Applicable skill playbook, current official documentation, installed template, approved consent/source contracts, and confirmed integration constraints | Workspace, destination identity, GTM objects/references, DLV version, consent, firing options, sequencing, adapter operations, and validation. |

Do not use an implementation source to add or change an analytics collection field. A technical ID,
trigger reference, consent setting, or template field is not payload enrichment, but it still needs a
current requirement or documented implementation constraint.

## Source scope and discrepancies

For a workbook or multi-part input, record every relevant sheet, table, row group, or requirement as
`included`, `reference-only`, `excluded`, or `ambiguous`, with its source reference and reason. Do not
infer scope from visibility alone. Preserve an explicit analyst scope decision as `approved-input`.

For each tracking-plan/documentation difference, record:

- approved value and source reference;
- current official finding, URL, title, access date, and installed-template relevance;
- class: `blocking-error`, `advisory`, or `implementation-note`;
- impact, default action, analyst decision when supplied, and resulting requirement status.

Report discrepancies before the first write. Preserve valid approved analytics choices for
advisories. Stop invalid, reserved, missing-required, type/shape-incompatible, or unsupported
requirements instead of inventing, omitting, or substituting collection semantics.

## Evidence grades

Assign an evidence grade to every fact that affects a configuration decision:

| Grade | Meaning | Permitted use |
| --- | --- | --- |
| `approved-input` | Approved tracking plan, direct analytics requirement, media brief, client consent policy, or explicit analyst decision. | Establish business intent, authorization, destination use, and approved policy. |
| `official-current` | Current official platform, GTM, CMP, or installed-template documentation inspected for this implementation. | Establish destination schema, template behavior, and supported consent capability. |
| `container-confirmed` | Current target-container/workspace object, export, API/MCP response, template definition, ID, fingerprint, or consumer graph. | Establish integration constraints, reuse evidence, stored fields, conflicts, consumers, and mutation preconditions. Never establish best practice merely because a pattern exists. |
| `contract-sample` | Analyst-supplied dataLayer specification or representative payload, including type, timing, cardinality, and null behavior. | Establish the static source contract when it is sufficiently explicit. |
| `assumption` | Inference not established by an approved, official, container, or sample source. | Record for non-critical context only. Never use for a critical mutation decision. |

Runtime execution is outside this skill. Configure from the approved source contract and state any
external site dependency without requesting runtime access or treating runtime QA as an unfinished
configuration status.

## Requirement record

Create one record per independently judgeable business action and destination family. Capture:

- stable requirement ID;
- source-scope classification and exact workbook sheet/cell, table, row, or direct-decision reference;
- route: analytics, media, consent, or combined;
- primary business authority and authorization state;
- business action, exact success moment, intended reporting/optimization/audience use;
- source `event`, timing contract, repeatability, state-reset behavior, and representative payload;
- source fields with paths, types, formats, scopes, cardinality, null/undefined rules, and evidence;
- destination product, account/tag/pixel/dataset identity, environment, template, and version;
- exact approved analytics destination event and fields, plus official standard, custom, reserved, deprecated, required, recommended, optional, or conditional findings and discrepancy class;
- base/configuration and automatic-event behavior;
- consent product, selected mode, approved policy source, CMP signal, and expected static logic;
- first-party user-data scope and authorization when applicable;
- external platform/site dependencies and explicitly untouched settings;
- result status and exact blocker or deferral reason.

Do not merge requirements merely because they currently share an event name. Keep them separate
when business meaning, destination, consent, environment, ownership, or future change path differs.

## Field mapping

Map every configured destination field through these layers:

| Layer | Required record |
| --- | --- |
| Business meaning | Why the value is needed for the approved use. |
| Source contract | Exact dataLayer/configuration path, event, evidence grade, and representative input. |
| GTM resolution | DLV, constant, settings variable, table, transformation, or direct literal with output type and null behavior. |
| Template field | Exact visible field and installed template/version. |
| Destination contract | Official parameter name, requirement status, type, format, enum, scope, and cardinality. |
| Representative result | Static resolved value or shape using non-sensitive sample data. |

Classify a destination field as `mapped`, `intentionally omitted`, `external`, or `blocked`.
Preserve zero and `false` when valid. Do not convert an absent required value into an empty
string, placeholder, guessed identifier, or invented default.

For an approved analytics tracking plan, the outgoing field set must equal the approved field set.
Do not add an official recommended or optional field that the plan omits. If current documentation
requires a missing field, classify the affected requirement as a blocking discrepancy; do not add it
without a new approved decision.

## Object change manifest

Create the complete object graph before mutation. For every relevant object, record:

- action: `create`, `update`, `reuse`, `untouched`, or explicitly authorized `remove`;
- object type, intended name, existing ID/path and fingerprint when applicable;
- requirement or documented constraint that justifies the object;
- exact intended fields and references;
- dependencies, consumers, environment/hostname scope, and consent route;
- pre-change state for every modified existing object;
- dependency order and expected saved-object verification;
- reason a similar existing object is or is not semantically compatible;
- selected skill reference architecture and the conformance gate result for every reused object;
- pre-existing workspace changes, current-operation mutations, and expected final workspace totals as separate records.

A second execution against the same saved state must produce `reuse` or `untouched`, not duplicate
objects. Treat that idempotency check as part of adapter design.

Select the target pattern before adopting local implementation choices. Reuse only when the object
passes the same architecture, source, type/shape, timing, consent, consumer, template, environment,
and static-acceptance checks as a new object. Harmless naming debt may remain when behavior is fully
conformant. Do not reuse a nonconformant object or create a parallel implementation around a known
duplicate; update/disable within authority or block the affected requirement.

## Contract conformance

Before mutation, compare the normalized approved collection contract with the intended object graph.
After mutation, compare it with authoritative current-workspace readback. Record:

- expected and actual requirement counts;
- missing and extra requirement IDs;
- source-scope differences;
- event-name, source-event, timing, business-filter, parameter, source-path, literal, and type/shape mismatches;
- zero unauthorized additions, removals, substitutions, or hidden-scope inclusions;
- the separate implementation manifest and infrastructure justifications.

Use `scripts/validate_contract_conformance.py` when normalized JSON is available. The agent interprets
the client-specific source; the script verifies equality and must not guess workbook semantics. A
non-zero semantic difference blocks the affected mutation unless an explicit approved decision
updates the collection contract.

## Consent and external dependencies

Express the approved consent predicate before translating it into GTM triggers or consent APIs.
Include every applicable CMP initialization state, category/purpose, vendor identity, Google or
vendor consent type, product-specific mode, and environment/region decision supplied by the
approved policy.

Record external dependencies separately, including:

- site/dataLayer delivery obligations;
- GA4 custom definitions, key-event designation, data-stream, Enhanced Measurement, Google tag,
  or other administration outside the authorized GTM change;
- advertising-platform conversion goals/actions, custom conversions, feeds/catalogs, account
  options, and terms/settings;
- CMP configuration or website code changes;
- publication.

Do not silently treat an external dependency as completed GTM work.

## Result statuses

Apply one status per requirement or tag family:

| Status | Meaning |
| --- | --- |
| `Configured` | Authoritative current-workspace readback proves the saved state already matched the approved contract or that authorized changes were applied; every relevant saved object passes the static invariants. |
| `Specification complete` | The object-level contract is complete, but mutation was not authorized or no mutation path was available. No live-change claim is made. |
| `Partial` | The current authorized operation changed some objects but could not finish. The exact saved partial state and recovery boundary are recorded. |
| `Blocked` | A critical authorization, business, destination, source, template, consent, or mutation fact cannot be established safely. |
| `Deferred` | The requirement belongs to an intentionally future capability such as server-side GTM, CAPI, or browser/server deduplication. |

Do not use `Complete` as a synonym for browser-validated. This skill establishes static GTM
configuration; it does not execute or certify runtime behavior.

## Static completion invariants

Before assigning `Configured` or `Specification complete`, prove from the contract and available
static evidence that:

1. every approved requirement has one explicit status;
2. every critical fact has a non-assumption evidence grade;
3. the source-scope manifest has no unresolved in-scope ambiguity and every destination field is mapped, intentionally omitted, external, or blocked;
4. every source type, shape, scope, cardinality, and null rule is compatible with its destination;
5. every tag has a valid normal trigger and selected consent mechanism;
6. every reference resolves to an existing, reused, or planned dependency;
7. every created, updated, or reused object conforms to the selected skill reference architecture, has a current justification, and has a compatible consumer graph;
8. known automatic/manual, base-tag, environment, and destination duplicates are resolved;
9. first-party user data remains limited to the explicitly approved destinations and sources;
10. approved-to-intended and approved-to-saved collection-contract comparisons show no missing, extra, substituted, or mismatched semantics for `Configured`;
11. authoritative current-workspace readback matches the intended implementation fields for `Configured`, including after any mutation;
12. pre-existing workspace changes, current-run changes, and final workspace totals are distinguished;
13. blockers, advisories, external dependencies, and untouched settings are explicit;
14. no publish, Submit, or GTM version action occurred.

Describe these as configuration assertions. Never present them as observed browser, network, CMP,
or vendor-platform behavior unless such evidence was separately supplied.
