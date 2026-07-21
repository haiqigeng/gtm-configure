# Utility contract

## Contents

- [Audience](#audience)
- [Objective](#objective)
- [Current use cases](#current-use-cases)
- [Requirement authority](#requirement-authority)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Authority and workspace policy](#authority-and-workspace-policy)
- [Boundaries](#boundaries)

## Audience

Serve an expert web analyst who uses an AI agent such as Codex, Claude, or another capable agent to configure tag management, especially client-side Google Tag Manager. Keep the analyst responsible for business intent, authorization, measurement decisions, and the client-approved consent policy. Make the agent responsible for evidence-backed design, scoped configuration, validation, and traceable reporting.

## Objective

Convert an approved analytics tracking plan, direct analytics requirement, or media-team implementation brief into the smallest authorized, statically verifiable, best-practice, officially documented, and consent-controlled client-side GTM change set.

Cover Google tag/GA4 analytics, supported browser media platforms, or both. Preserve the approved analytics collection contract exactly, detect documentation discrepancies without redesigning the tracking plan, and optimize implementation correctness, maintainability, and traceability. Do not claim legal compliance, make the client's legal decisions, require runtime access, or describe static configuration as observed browser behavior.

## Current use cases

Support these client-side use cases:

- create or modify tags, triggers, blocking triggers, variables, Google tag settings, and transformations;
- configure Google tag and GA4 events from an analytics tracking plan or direct human requirement;
- normalize approved analytics scope, report plan/documentation discrepancies, and prove exact pre-write and saved-state collection-contract conformance;
- configure Google Ads, Microsoft Advertising, Meta, TikTok, Snapchat, and other browser media tags from a media-team brief;
- map standard and custom destination events against current official vendor schemas;
- configure base/configuration tags, event tags, conversion tags, remarketing tags, and documented browser-side matching features;
- implement strict/basic CMP gating by default and explicitly approved per-product advanced/native, cookieless, or anonymous consent behavior when supported;
- validate the available dataLayer contract without developing the website or dataLayer;
- create an implementation specification when live mutation is unavailable or unauthorized.

## Requirement authority

Use different primary inputs for analytics and media:

| Route | Primary business input | Supporting evidence | Technical authority |
| --- | --- | --- | --- |
| Analytics | Approved tracking plan or exact direct analytics requirement | Approved dataLayer contract and representative payloads | Skill reference architecture, current official Google tag/GA4/GTM documentation, and installed-template capabilities; use them to validate and implement, not to silently rewrite the approved collection contract |
| Media | Human media-team brief | Tracking plan, approved source contract, existing business events, representative payloads, and target container | Current official media-vendor documentation and installed template |

Do not assume that a requested media event appears in the analytics tracking plan or should use the corresponding GA4 destination name. Reuse a vendor-neutral source event where semantics and timing match, but establish each destination schema independently.

Treat a tracking plan as supporting evidence for reusable business events and source values in the media route, not as the authority for the media destination schema.

For the analytics route, keep measurement optimization outside this skill. Preserve every approved
event, outgoing field, literal, source mapping, and business success moment when technically valid.
Classify a valid recommended alternative as advisory. Block an invalid, reserved, missing-required,
type/shape-incompatible, or unsupported requirement instead of substituting or enriching it.

Use existing container and workspace state only to establish integration constraints, consumers,
conflicts, saved fields, and candidates for reuse. Never treat a local legacy pattern as technical
authority or proof of best practice.

## Inputs

Accept incomplete intake. Discover safely derivable information before asking the analyst.

| Input class | Examples | Agent behavior |
| --- | --- | --- |
| Analytics requirement | Approved tracking-plan row or exact direct analytics contract | Preserve the approved collection contract; use official documentation to validate it and report discrepancies before mutation. |
| Media brief | Platform, pixel/account/destination, requested action, optimization or audience use, conversion label | Treat as media intent; do not treat its informal event label as an official schema. |
| Target and authority | Account, container, environment, workspace, read/write authorization | Confirm before mutation. |
| Discoverable configuration | Existing objects, folders, templates, workspace state, destination IDs | Inspect as integration evidence; reuse only after the object passes the selected best-practice architecture and static acceptance checks. |
| Source contract | dataLayer event, fields, types, cardinality, timing, state lifetime, representative payloads | Require an explicit approved contract or sample for every critical value. |
| Consent | CMP, client-approved product policy, CMP signal contract, basic/strict or explicitly approved advanced/native behavior | Classify each browser product from official documentation, installed template, approved CMP contract, and target-container state. |
| Conditional media details | Conversion ID/label, feed/business vertical, catalog IDs, first-party user data, advanced matching | Require only when the chosen product or feature needs them. |

Classify a missing input as discoverable, optional for the selected route, or critical. Block only when the missing value affects authorization, business meaning, destination identity/schema, data handling, consent behavior, or another decision that cannot be established safely.

## Outputs

For authorized configuration, produce:

- configured objects in a dedicated workspace whenever possible;
- one adapter-neutral configuration contract covering every requirement;
- normalized source-scope manifest and preflight discrepancy report for analytics inputs;
- exact approved-to-intended and approved-to-saved collection-contract conformance results;
- target account, container, environment, and workspace;
- requirement-to-object and source-to-destination maps;
- pre-existing workspace changes, current-run created/modified/reused/untouched objects, and final workspace totals reported separately;
- for every destination field: official name, requirement status, type/shape, source, transformation, and representative resolved value;
- installed template identity/version and relevant permissions;
- official source URLs, titles, access dates, and decisions;
- final normal trigger, blocking trigger or consent mechanism, and denied/unknown behavior per browser product/vendor;
- evidence grades, static validation results, blockers, external dependencies, and deferred capabilities;
- confirmation that no publication or GTM version occurred.

For planning, read-only, unavailable-tool, or blocked work, return the same object-level specification without claiming live mutation. Classify results as `Configured`, `Specification complete`, `Partial`, `Blocked`, or `Deferred`; never make runtime execution a completion requirement.

## Authority and workspace policy

Classify authority before mutation:

| Request state | Permitted result |
| --- | --- |
| Review, design, or implementation plan | Read-only inventory, object graph, blockers, and acceptance matrix. |
| Explicitly authorized create or modify request | Changes limited to the approved container, workspace, vendors, and business actions. |
| Unclear authority, destination, data handling, or consent model | Complete the safe design work, then request the missing decision before mutation. |

For authorized changes:

1. Reuse a compatible dedicated workspace assigned to the same requirement.
2. Otherwise create a dedicated workspace with a clear implementation name when permitted.
3. Avoid the Default Workspace whenever possible.
4. Explain the constraint and obtain approval before falling back to the Default Workspace.
5. Never publish, create a version, change an advertising-platform setting, or expand to another container without explicit authorization.

## Boundaries

Do not use this skill for:

- creating, optimizing, or redesigning an analytics tracking plan;
- developing the website or its dataLayer;
- auditing, cleaning, or broadly refactoring a container;
- executing a full interactive GTM Preview recette;
- certifying browser, network, CMP, or vendor-platform runtime behavior;
- deciding legal basis, consent categories, regional law, or privacy policy;
- publishing or creating a GTM version.

Keep server-side GTM, Conversions API, browser/server deduplication, and event-ID architecture deferred in the current client-side version. Record them as future work when encountered; do not treat them as permanent exclusions from the skill.

The cross-vendor consent-capability map is a research and classification aid. It does not add an analytics tag-configuration route beyond the current Google tag/GA4 scope. For Matomo, Piwik PRO, or another analytics product without an approved playbook in this skill, report the scope gap and do not create or modify its tags unless that capability is added explicitly.
