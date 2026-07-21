---
name: configure-gtm
description: "Create and modify statically verifiable client-side Google Tag Manager web-container configurations for an expert web analyst using an AI agent. Faithfully translate approved analytics tracking plans or direct requirements, and media-team implementation briefs, into minimal, best-practice, officially documented, consent-controlled tags, triggers, variables, settings, and transformations. Detect and report tracking-plan/documentation discrepancies without silently redesigning analytics. Use for GA4, Google Ads, Microsoft Advertising, Meta, TikTok, Snapchat, other browser media tags, CMP gating, basic consent by default, or explicitly approved advanced consent through a GTM MCP, API, export, or UI. Do not use for tracking-plan creation or optimization, container audit or cleanup, site/dataLayer development, legal decisions, runtime recette, publication, or runtime certification. Server-side GTM and browser/server deduplication are future extensions not implemented in the current client-side scope."
---

# Configure Google Tag Manager

Convert an approved implementation requirement into the smallest authorized, statically verifiable, traceable, and consent-controlled client-side GTM change set. Do not require or claim runtime execution. Keep this entrypoint small and load only the references required by the selected route.

## 01 - Orientation

Read for every request:

- [utility-contract.md](references/01-orientation/utility-contract.md)
- [official-source-policy.md](references/01-orientation/official-source-policy.md)

## 02 - Execution

Read [implementation-workflow.md](references/02-execution/implementation-workflow.md) for every request. Then load the applicable references:

- Read [configuration-contract.md](references/02-execution/configuration-contract.md) for every request and use it as the common source for planning, mutation, verification, and handoff.

| Request component | Read |
| --- | --- |
| Approved analytics tracking plan, direct analytics contract, source-scope selection, or exact conformance | [tracking-plan-fidelity-and-conformance.md](references/02-execution/tracking-plan-fidelity-and-conformance.md) |
| GA4 or Google tag analytics | [analytics-tags.md](references/02-execution/analytics-tags.md) |
| Any browser media implementation | [media-tags.md](references/02-execution/media-tags.md) |
| Google Ads | [media-google-ads.md](references/02-execution/media-google-ads.md) |
| Microsoft Advertising or Bing Ads | [media-microsoft-ads.md](references/02-execution/media-microsoft-ads.md) |
| Meta Pixel | [media-meta.md](references/02-execution/media-meta.md) |
| TikTok Pixel | [media-tiktok.md](references/02-execution/media-tiktok.md) |
| Snap Pixel | [media-snapchat.md](references/02-execution/media-snapchat.md) |
| CMP gating or consent behavior | [cmp-consent.md](references/02-execution/cmp-consent.md) |
| Any advanced, native, cookieless, anonymous, or limited-data consent behavior | [vendor-consent-modes.md](references/02-execution/vendor-consent-modes.md) |
| Google basic or advanced Consent Mode | [google-consent-mode.md](references/02-execution/google-consent-mode.md) |
| First-party user data, enhanced conversions, or advanced matching | [first-party-data.md](references/02-execution/first-party-data.md) |
| dataLayer contracts, ecommerce arrays, or transformations | [data-contract-and-transformations.md](references/02-execution/data-contract-and-transformations.md) |
| Trigger, variable, SPA, or sequencing design | [triggers-and-variables.md](references/02-execution/triggers-and-variables.md) |
| Native, official, community, or custom templates | [template-governance.md](references/02-execution/template-governance.md) |
| MCP, API, export, or UI execution | [tool-adapters.md](references/02-execution/tool-adapters.md) |
| Naming, folders, constants, lookup tables, or reuse | [naming-and-reuse.md](references/02-execution/naming-and-reuse.md) |

## 03 - Judgement

Read [acceptance-and-handoff.md](references/03-judgement/acceptance-and-handoff.md) for every request. Classify each requirement as configured, specification complete, partial, blocked, or deferred.

## Core operating rules

- Implement an approved analytics tracking plan faithfully. Do not rename events, add or remove payload fields, change business timing, or substitute a recommended design unless the analyst first amends the approved input explicitly.
- Use current official documentation to validate analytics appropriateness and technical feasibility. Report advisory differences before mutation; block invalid, reserved, required-field, type/shape, or unsupported conflicts. Never treat documentation as authorization to redesign the tracking plan.
- Treat the media-team brief as the primary media business input. Use a tracking plan only as supporting evidence for reusable business events and source values.
- Use current official documentation and the installed template to establish media destination schemas, validate approved analytics schemas, and determine technical field types, shapes, consent features, and template settings; never translate by analogy from another platform.
- Assign an evidence grade to every critical fact. Use approved inputs, current official sources, target-container state, and supplied source contracts. Runtime evidence is outside this skill.
- Select the target GTM architecture from the applicable skill playbooks, approved consent policy, source contract, installed-template capabilities, and current official documentation. Treat existing container state only as integration evidence for capabilities, consumers, conflicts, and reuse candidates; never as proof of best practice.
- Use the exact approved source event and timing. When an approved input authorizes a new source contract, default to one vendor-neutral Custom Event dataLayer event per business action; use another trigger type only as an approved, evidence-backed fallback.
- Prefer relative references: reuse or create constants and variables for stable IDs, currency, and other values when that is clearer than hard-coding.
- Default to strict/basic CMP gating for every in-scope analytics and media product. Use the smallest reusable set of blocking triggers that expresses the approved category/purpose, vendor, product, and initialization predicate; make unknown, undefined, and denied states block.
- Classify consent behavior per browser product, not only per vendor. Reconcile those decisions with the actual executable tag or helper: never attach incompatible basic and advanced policies to one shared execution unit. Configure advanced/native, cookieless, anonymous, or limited-data behavior only when explicitly requested, approved, and proven by current official documentation. Do not attach a blocking trigger that defeats the exact authorized denied-state behavior.
- Keep configuration/base tags from sending an automatic page view by default. Implement page views as separate events unless current official vendor behavior requires a documented exception.
- Preserve every item in vendor-required arrays and validate zero-, one-, and multi-item payloads.
- Prefer a dedicated GTM workspace. Avoid the Default Workspace whenever a dedicated workspace can be created or reused safely.
- Create an object only for a current requirement or documented platform/template constraint. Select the least-complex best-practice pattern first, then reuse an existing object only when it passes the same architecture, semantics, source, consent, consumer, and static-acceptance checks as a new object.
- Never copy a legacy pattern or add a parallel implementation around a known conflict. Resolve the conflict within authority or block the affected requirement. Inspect before creating, verify every mutation, and never publish or create a GTM version.
- Treat server-side GTM, Conversions API, browser/server deduplication, and event-ID design as deferred current-scope capabilities, not permanent exclusions. They remain future extensions of this skill.
