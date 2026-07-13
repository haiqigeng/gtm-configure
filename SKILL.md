---
name: configure-gtm
description: "Create and modify client-side Google Tag Manager web-container configuration for an expert web analyst using an AI agent, from an approved tracking plan or direct human measurement requirement. Cover analytics tools, media platforms, or both with clean, minimal, reusable, officially documented, and consent-gated configuration. Use through a GTM MCP, API, export, or UI. Scope excludes tracking-plan creation, container audit or cleanup, site/dataLayer development, legal consent decisions, and publishing. Server-side GTM and deduplication are future extensions of this skill and are not implemented by V1."
---

# Configure Google Tag Manager

Convert an approved tracking requirement into a traceable GTM configuration for an expert web analyst. Keep the entrypoint small and route orientation, execution, domain details, and judgement to the appropriate reference.

## 01 - Orientation

Read these for every request:

- [utility-contract.md](references/01-orientation/utility-contract.md)
- [official-source-policy.md](references/01-orientation/official-source-policy.md)

The utility contract defines the audience, objective, use cases, inputs, outputs, authority, workspace policy, and boundaries.

## 02 - Execution

Read [implementation-workflow.md](references/02-execution/implementation-workflow.md) for every configuration request.

Then load only the relevant domain references:

| Request component | Read |
| --- | --- |
| GA4, Google tag, or analytics implementation | [analytics-tags.md](references/02-execution/analytics-tags.md) |
| Meta or another media/vendor tag | [media-tags.md](references/02-execution/media-tags.md) |
| CMP integration, consent settings, firing conditions, or exception triggers | [cmp-consent.md](references/02-execution/cmp-consent.md) |
| Naming, reuse, constants, lookup tables, or transformations | [naming-and-reuse.md](references/02-execution/naming-and-reuse.md) |

## 03 - Judgement

Read [acceptance-and-handoff.md](references/03-judgement/acceptance-and-handoff.md) for every request. Use it to decide whether the work is complete, blocked, deferred, or still requires runtime QA.

## Core operating rules

- Default to one vendor-neutral Custom Event dataLayer event per business action. One event may feed several destination tags.
- Accept direct human input as a valid requirement source; a tracking plan is not mandatory.
- Treat user-provided inputs as potentially incomplete. Discover missing values from the target container, installed templates, official documentation, and runtime evidence when possible.
- Prefer a dedicated GTM workspace for authorized configuration. Avoid the Default Workspace whenever a dedicated workspace can be created or reused safely.
- Use official vendor and CMP documentation for event names, parameters, data shapes, template fields, consent signals, and vendor identifiers.
- A consent check is not a consent gate unless the final GTM logic prevents firing under the required denied or unknown states.
- Preserve every item in vendor-required ecommerce arrays; never reduce a multi-item payload to item zero.
- Do not publish or create a release/version as part of this skill.
- Server-side GTM, Conversions API, browser/server deduplication, and related routing are deferred capabilities for a future version of this skill. Record them as deferred when encountered in V1.
