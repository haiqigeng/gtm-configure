---
name: configure-gtm
description: "Create and modify statically verifiable client-side Google Tag Manager web-container configurations for an expert web analyst using an AI agent. Translate approved analytics tracking plans or direct human requirements, and media-team implementation briefs, into minimal, reusable, officially documented, and consent-controlled tags, triggers, variables, settings, and transformations. Use for GA4, Google Ads, Microsoft Advertising, Meta, TikTok, Snapchat, other browser media tags, CMP gating, basic consent by default, or explicitly approved advanced consent through a GTM MCP, API, export, or UI. Do not use for tracking-plan creation, container audit or cleanup, site/dataLayer development, legal decisions, runtime recette, publication, or runtime certification. Server-side GTM and browser/server deduplication are future extensions not implemented in the current client-side scope."
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

- Treat an analytics tracking plan or direct analytics requirement as the primary analytics input.
- Treat the media-team brief as the primary media business input. Use a tracking plan only as supporting evidence for reusable business events and source values.
- Determine every destination event, field, type, shape, consent feature, and template setting from current official documentation and the installed template; never translate by analogy from another platform.
- Assign an evidence grade to every critical fact. Use approved inputs, current official sources, target-container state, and supplied source contracts. Runtime evidence is outside this skill.
- Default to one vendor-neutral Custom Event dataLayer event per business action. Use another trigger type only as an approved, evidence-backed fallback.
- Prefer relative references: reuse or create constants and variables for stable IDs, currency, and other values when that is clearer than hard-coding.
- Default to strict/basic CMP gating for every in-scope analytics and media product. Use the smallest reusable set of blocking triggers that expresses the approved category/purpose, vendor, product, and initialization predicate; make unknown, undefined, and denied states block.
- Classify consent behavior per browser product, not only per vendor. Reconcile those decisions with the actual executable tag or helper: never attach incompatible basic and advanced policies to one shared execution unit. Configure advanced/native, cookieless, anonymous, or limited-data behavior only when explicitly requested, approved, and proven by current official documentation. Do not attach a blocking trigger that defeats the exact authorized denied-state behavior.
- Keep configuration/base tags from sending an automatic page view by default. Implement page views as separate events unless current official vendor behavior requires a documented exception.
- Preserve every item in vendor-required arrays and validate zero-, one-, and multi-item payloads.
- Prefer a dedicated GTM workspace. Avoid the Default Workspace whenever a dedicated workspace can be created or reused safely.
- Create an object only for a current requirement or documented platform/template constraint. Reuse a semantically compatible object and prefer a direct field or DLV over a helper variable; do not add speculative objects for possible future cases.
- Inspect before creating, reuse semantically compatible objects, verify every mutation, and never publish or create a GTM version.
- Treat server-side GTM, Conversions API, browser/server deduplication, and event-ID design as deferred current-scope capabilities, not permanent exclusions. They remain future extensions of this skill.
