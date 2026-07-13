# Utility contract

## Audience

Serve an expert web analyst who uses an AI agent such as Codex, Claude, or another capable agent to manage tag configuration. The analyst remains responsible for business intent, the approved measurement requirement, and the client consent policy. The agent is responsible for evidence-backed configuration work and traceable reporting.

## Objective

Convert an approved tracking plan or direct human measurement requirement into a clean, minimal, reusable, officially documented, and consent-gated client-side GTM configuration.

The configuration may cover analytics tools, media platforms, or both. The objective is implementation quality and traceability, not a claim of legal compliance.

## Current use cases

Support these V1 use cases:

- create GTM tags, triggers, variables, settings variables, and transformations from an approved requirement;
- modify existing GTM objects for a new or changed requirement;
- configure analytics tags, including Google tag and GA4 event configuration;
- configure client-side media tags and vendor-specific payload transformations;
- implement or adjust CMP consent gates for configured vendors.

Additional use cases may be added later without changing this core contract.

## Inputs

Inputs may be provided by the analyst, discovered by the agent, or conditional to the request. Do not assume that every input is available at intake.

| Input class | Examples | Agent behavior |
| --- | --- | --- |
| User-provided | Tracking-plan row, direct human requirement, target container, desired scope, consent policy | Treat as business intent and authorization context. |
| Discoverable | Existing tags, triggers, variables, templates, folders, workspace state, current official documentation | Inspect and record before designing. |
| Runtime evidence | DataLayer events, field values, CMP event order, preview state, site source | Obtain when timing, shape, or actual value format matters. |
| Conditional | Sample ecommerce payload, vendor ID, template version, region or hostname mapping | Require or derive only when the selected implementation needs it. |

When an input is missing, first determine whether it can be safely derived. Block only when the missing information affects authorization, business meaning, destination schema, consent behavior, or another critical decision that cannot be established from available evidence.

## Outputs

For an authorized configuration request, produce:

- the configured objects in a dedicated workspace whenever possible;
- the target container and workspace used;
- a requirement-to-object map;
- created, modified, reused, and intentionally untouched objects;
- official sources and platform decisions;
- final firing and consent-gating behavior per vendor;
- validation results, unresolved blockers, deferred future capabilities, and remaining runtime QA;
- confirmation that no publication occurred.

For a read-only, planning, or blocked request, produce the same object-level specification without claiming that live changes were made.

## Authority and workspace policy

Classify the request before mutation:

| Request state | Permitted result |
| --- | --- |
| Review or implementation plan | Read-only inventory, design, blockers, and acceptance matrix. |
| Explicitly authorized create or modify request | Configuration changes limited to the approved scope. |
| Unclear authority or destination | Object-level plan and approval request before mutation. |

For authorized changes:

1. Reuse a compatible existing dedicated workspace when it has the same scope.
2. Otherwise create a dedicated workspace, using a clear implementation-oriented name such as "Implementation - <requirement> - <date>" when the platform allows it.
3. Avoid the Default Workspace whenever possible.
4. If a dedicated workspace cannot be created or reused, explain the reason and obtain approval before using the Default Workspace.
5. Never publish, create a version, or expand to another container without explicit authorization.

## Boundaries

Do not use this skill for:

- creating or redesigning a tracking plan;
- developing the website or its dataLayer;
- container audit, cleanup, or hygiene work;
- full interactive GTM Preview recette execution;
- deciding legal basis, consent categories, or the client's privacy policy;
- publishing a GTM version.

Server-side GTM, Conversions API, browser/server deduplication, and related routing are not implemented in V1. They are deferred capabilities of this same skill, not permanent exclusions or automatic handoffs to another skill.
