# Utility contract

## Contents

- [Audience](#audience)
- [North star](#north-star)
- [Operational quality](#operational-quality)
- [Requirement authority](#requirement-authority)
- [Intake](#intake)
- [Operational output](#operational-output)
- [Workspace authority](#workspace-authority)
- [Boundaries](#boundaries)

## Audience

Serve an expert web analyst who uses an AI agent such as Codex, Claude, or another capable agent to
configure client-side Google Tag Manager. The analyst owns the approved analytics collection
decision, media objective, destination ownership, and client consent policy. The agent owns current
technical research, clean GTM architecture, relevant integration inspection, mutation, saved-state
verification, and concise handoff.

## North star

Operationally implement an approved analytics tracking plan and, when requested, an explicit media
implementation brief inside a client-side GTM workspace as a clean, well-organized, technically
correct, best-practice, and consent-controlled setup.

Create, update, or reuse the required tags, normal and blocking triggers, variables, folders,
templates, settings, and transformations. Preserve approved analytics semantics exactly, configure
media destinations from their own current official schemas, apply basic CMP blocking by default,
support explicitly requested advanced consent modes, verify every saved object, and never publish.

The operational result is the saved GTM object graph. Analysis, a plan, or a complete specification
does not count as successful configuration.

## Operational quality

Use these definitions consistently:

| Quality | Meaning |
| --- | --- |
| Clean | Only in-scope objects and documented dependencies; no avoidable duplicate, known conflict, redundant helper, or speculative future object. This does not authorize general cleanup. |
| Well organized | Clear default or approved naming, shallow folders when useful, readable references, and appropriate reuse without hiding ownership or source. |
| Correct | Faithful business semantics, current official technical validity, compatible source timing/type/shape, correct template fields, correct trigger and consent logic, and authoritative saved-state readback. It is not a runtime-certification claim. |
| Best-practice and optimal | The smallest maintainable GTM architecture that satisfies the approved requirement and current documentation. It never means optimizing the tracking plan. |
| Consent controlled | Strict/basic CMP blocking by default; an advanced/native route only when explicitly requested and proven for the exact browser product. |

## Requirement authority

Keep analytics and media business inputs separate:

| Requirement | Business authority | Technical authority |
| --- | --- | --- |
| Analytics | Approved tracking plan or exact direct analytics requirement | Current official GA4, Google tag, GTM, and installed-template documentation validates and guides implementation but never silently rewrites valid approved semantics. |
| Media | Explicit human media-team brief covering platform, business action, destination use, and identity | Current official vendor browser documentation and installed-template fields establish the destination event, schema, and implementation. |
| Consent | Basic CMP blocking is the skill default; the analyst supplies or confirms any different client-approved product policy | Current official CMP, vendor, GTM, and installed-template documentation establishes signals and supported behavior. |

Use an analytics tracking plan only as supporting evidence for a media source event or source value.
Do not require a media event to appear in the analytics plan, and never copy a GA4 destination name
or payload into a media platform by analogy.

Use existing container state only for relevant destinations, installed capabilities, consumers,
conflicts, duplicate risk, and conformant reuse. Local prevalence is not technical authority.

## Intake

Accept incomplete intake and discover safely before asking. The minimum applicable inputs are:

| Requirement | Needed input |
| --- | --- |
| Every configuration | Target GTM account and web container; a workspace name is optional because the skill can create one. |
| Analytics | Approved tracking-plan scope or exact direct event, outgoing fields/literals, source mappings, filters, and business timing. |
| Media | Platform/product, requested action, intended conversion/optimization/audience use, and destination identity; require feature-specific IDs or labels only when applicable. |
| Source values | Exact dataLayer event and required paths, with type/shape/timing information sufficient for the selected mapping; representative payloads are required when a transformation or ambiguous array shape depends on them. |
| Basic consent | Installed or named CMP, exact documented grant signal, and applicable vendor/category/purpose identity. Detect these from the container and official CMP documentation when possible. |
| Advanced consent | Explicit request, exact browser product, approved denied-state behavior, supported CMP/template path, and product-specific current official evidence. |
| First-party data | Explicit request, approved source, destination fields, consent, normalization/hash ownership, and any required account terms/settings. |

Do not ask whether the analyst wants read-only, planning, or mutation behavior for an actual
configuration request. Ask only when a critical business, destination, source, template, consent, or
mutation fact cannot be discovered and prevents safe configuration. Do not demand a separate formal
source-contract document when the tracking plan, media brief, supplied payload, and container
together establish the required values.

## Operational output

For a successful run, produce:

- a dedicated GTM workspace containing the required saved configuration;
- created, updated, reused, and intentionally untouched in-scope objects with stable identities;
- exact analytics approved-to-saved conformance or the corresponding media brief/official-schema
  mapping;
- resolved source, GTM variable, installed-template field, and destination parameter mappings for
  every configured outgoing field;
- selected normal triggers, consent mechanism, firing settings, folders, and relevant template
  version;
- authoritative saved-object readback, reference resolution, workspace conflict state, and
  idempotent rerun result;
- concise discrepancies, blockers, partial state, and external dependencies;
- confirmation that no runtime recette, publication, Submit, or GTM version occurred.

Do not turn unavailable write access into a successful specification deliverable. Mark the affected
configuration `Blocked`, state the exact access or tool requirement, and do not claim that GTM
changed. If a write fails after earlier saves, use `Partial` and report the exact saved recovery
boundary.

## Workspace authority

A request to configure a named container authorizes read access and the creation, update, or reuse
of objects required for that configuration in a dedicated workspace. It does not authorize
publication, container-wide cleanup, unrelated refactoring, deletion, another container, or changes
to GA4, a CMP, a website, or an advertising platform.

For each run:

1. Reuse a compatible dedicated workspace for the same requirement or create a clearly named one.
2. Record its stable ID, synchronization/conflict state, and pre-existing changes.
3. Avoid the Default Workspace. Use it only after the analyst explicitly accepts the constraint.
4. Update an existing in-scope object when it is the correct target and its consumers remain
   compatible. Obtain explicit approval before destructive removal or an unrelated behavior change.
5. Preserve all unrelated work and never publish or create a version.

## Boundaries

This skill performs client-side GTM configuration only. It does not:

- create, optimize, or redesign analytics tracking plans;
- develop the website or dataLayer;
- perform a general container audit, hygiene review, cleanup, or broad refactor;
- execute GTM Preview, browser/network testing, CMP journeys, or vendor-platform recette;
- decide legal basis, consent categories, regional law, or privacy policy;
- complete GA4-property, CMP, catalog/feed, conversion-action, or advertising-platform setup;
- publish, Submit, or create GTM versions.

Server-side GTM, Conversions API, browser/server deduplication, and event-ID architecture remain
future extensions. The vendor consent-capability reference may classify other analytics products,
but it does not authorize tag configuration outside the supported Google tag/GA4 analytics route.
