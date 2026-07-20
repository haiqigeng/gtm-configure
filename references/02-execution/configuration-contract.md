# Configuration contract

## Contents

- [Purpose and priority](#purpose-and-priority)
- [Evidence grades](#evidence-grades)
- [Requirement record](#requirement-record)
- [Field mapping](#field-mapping)
- [Object change manifest](#object-change-manifest)
- [Consent and external dependencies](#consent-and-external-dependencies)
- [Result statuses](#result-statuses)
- [Static completion invariants](#static-completion-invariants)

## Purpose and priority

Translate every approved requirement into one adapter-neutral configuration contract before
creating or modifying GTM objects. Use the contract as the common source for the human plan,
MCP/API/UI mutations, saved-object verification, and handoff.

Resolve tradeoffs in this order:

1. authorization, data handling, and consent safety;
2. fidelity to the approved business requirement;
3. correctness against current official destination and template documentation;
4. the smallest semantically correct GTM object graph;
5. reuse, maintainability, and field-level traceability;
6. completion of the authorized static configuration.

Do not weaken a higher-priority requirement to obtain a tidier container or a more complete
change set.

## Evidence grades

Assign an evidence grade to every fact that affects a configuration decision:

| Grade | Meaning | Permitted use |
| --- | --- | --- |
| `approved-input` | Approved tracking plan, direct analytics requirement, media brief, client consent policy, or explicit analyst decision. | Establish business intent, authorization, destination use, and approved policy. |
| `official-current` | Current official platform, GTM, CMP, or installed-template documentation inspected for this implementation. | Establish destination schema, template behavior, and supported consent capability. |
| `container-confirmed` | Current target-container/workspace object, export, API/MCP response, template definition, ID, fingerprint, or consumer graph. | Establish existing architecture, reuse, stored fields, and mutation preconditions. |
| `contract-sample` | Analyst-supplied dataLayer specification or representative payload, including type, timing, cardinality, and null behavior. | Establish the static source contract when it is sufficiently explicit. |
| `assumption` | Inference not established by an approved, official, container, or sample source. | Record for non-critical context only. Never use for a critical mutation decision. |

Runtime execution is outside this skill. Configure from the approved source contract and state any
external site dependency without requesting runtime access or treating runtime QA as an unfinished
configuration status.

## Requirement record

Create one record per independently judgeable business action and destination family. Capture:

- stable requirement ID;
- route: analytics, media, consent, or combined;
- primary business authority and authorization state;
- business action, exact success moment, intended reporting/optimization/audience use;
- source `event`, timing contract, repeatability, state-reset behavior, and representative payload;
- source fields with paths, types, formats, scopes, cardinality, null/undefined rules, and evidence;
- destination product, account/tag/pixel/dataset identity, environment, template, and version;
- official destination event/conversion and standard, custom, reserved, or deprecated status;
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

## Object change manifest

Create the complete object graph before mutation. For every relevant object, record:

- action: `create`, `update`, `reuse`, `untouched`, or explicitly authorized `remove`;
- object type, intended name, existing ID/path and fingerprint when applicable;
- requirement or documented constraint that justifies the object;
- exact intended fields and references;
- dependencies, consumers, environment/hostname scope, and consent route;
- pre-change state for every modified existing object;
- dependency order and expected saved-object verification;
- reason a similar existing object is or is not semantically compatible.

A second execution against the same saved state must produce `reuse` or `untouched`, not duplicate
objects. Treat that idempotency check as part of adapter design.

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
3. every destination field is mapped, intentionally omitted, external, or blocked;
4. every source type, shape, scope, cardinality, and null rule is compatible with its destination;
5. every tag has a valid normal trigger and selected consent mechanism;
6. every reference resolves to an existing, reused, or planned dependency;
7. every created or updated object has a current justification and compatible consumer graph;
8. known automatic/manual, base-tag, environment, and destination duplicates are resolved;
9. first-party user data remains limited to the explicitly approved destinations and sources;
10. authoritative current-workspace readback matches the intended fields for `Configured`, including after any mutation;
11. blockers, external dependencies, and untouched settings are explicit;
12. no publish, Submit, or GTM version action occurred.

Describe these as configuration assertions. Never present them as observed browser, network, CMP,
or vendor-platform behavior unless such evidence was separately supplied.
