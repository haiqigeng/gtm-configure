# Operational acceptance and handoff

## Contents

- [Configured means saved and verified](#configured-means-saved-and-verified)
- [Operational statuses](#operational-statuses)
- [Configuration judgement matrix](#configuration-judgement-matrix)
- [Analytics conformance proof](#analytics-conformance-proof)
- [Consent configuration proof](#consent-configuration-proof)
- [Concise handoff](#concise-handoff)

## Configured means saved and verified

Assign `Configured` only when authoritative current-workspace readback proves that the complete
in-scope GTM object graph already matched or now matches the approved requirement. Require every
applicable condition:

1. Resolve the target account, web container, environment, and dedicated workspace by stable ID;
   record conflicts and pre-existing workspace changes.
2. Use the approved tracking plan or exact direct analytics decision for analytics, the explicit
   human media brief for media, and basic CMP blocking unless an advanced route was requested.
3. Open current official documentation and inspect the installed template version before designing
   event fields, transformations, consent, or automatic behavior.
4. Inspect only relevant existing tags, triggers, variables, templates, folders, consumers,
   destinations, consent paths, automatic behavior, and duplicate/conflict risks.
5. Select the best-practice architecture before considering container reuse. Reuse only a
   semantically compatible object; do not copy legacy architecture or add a known duplicate.
6. Resolve every outgoing field from approved source to GTM variable to installed-template field to
   official destination contract. Preserve zero/false and reject invented values.
7. Preserve every required array item and establish explicit event eligibility. An empty or
   undefined transformation must not leave an invalid tag eligible.
8. Use clear naming and a shallow folder when several related objects benefit. Use DLVs, constants,
   settings variables, LUTs/RLTs, and CJS according to the least-complex mapping order.
9. Prove a valid normal trigger, firing option, initialization path, and basic block or explicitly
   approved advanced consent route for every tag.
10. Reconcile known automatic/manual event, page-view, shared-execution-unit, environment, and
    destination conflicts.
11. Re-read every created, updated, and reused object; compare intended and saved fields,
    references, consumers, template version, folder, consent, and fingerprints.
12. Prove exact analytics approved-to-saved conformance and media brief/official-schema mapping.
13. Recompute the object graph so an identical rerun is entirely `reuse` or `untouched`.
14. Distinguish pre-existing workspace changes from current-run writes and final workspace totals.
15. Record external dependencies and confirm that no runtime recette, publication, Submit, or GTM
    version action occurred.

Static configuration verification is not observed browser, network, CMP, or vendor-platform
behavior. Runtime recette and publication remain separate workflows.

## Operational statuses

Use one status per independent requirement or tag family:

| Status | Meaning |
| --- | --- |
| `Configured` | Authoritative saved-workspace readback satisfies the complete configuration and all applicable invariants. No write is required when it already matched. |
| `Partial` | The current run saved some in-scope objects but stopped before completing their dependent graph; exact saved state and safe recovery boundary are recorded. |
| `Blocked` | A critical business, source, destination, template, consent, conflict, access, or mutation fact prevents configuration. No planning/specification status substitutes for the operational result. |
| `Deferred` | The requirement belongs to the intentionally future server-side GTM, CAPI, event-ID, or browser/server deduplication capability. |

Apply mixed statuses at requirement/tag-family grain so one blocked family does not mislabel an
independent configured family.

## Configuration judgement matrix

Use every applicable row; load the detailed playbook for the selected requirement.

| Requirement or trap | Required saved-configuration judgement |
| --- | --- |
| Approved analytics event | Exact event, source event, timing, filter, outgoing fields, sources, literals, and item scope match the plan. |
| Valid custom analytics event with a recommended alternative | Preserve the approved event, report the advisory, and do not substitute or enrich it. |
| Invalid/reserved event or missing required analytics field | Block only the affected requirement; never invent or substitute a value/event. |
| Recommended/optional field absent from plan | Keep it absent; documentation is not payload authorization. |
| Multi-part tracking plan | Resolve only relevant included/reference/excluded/ambiguous parts; hidden and visible status alone decides nothing. |
| GA4 configuration | Measurement ID reference, connected destinations, settings variables, consent, and explicit page-view behavior are correct. |
| Manual page view or SPA | Reconcile Google tag, Enhanced Measurement, initial/history/application events, retained values, consent timing, and duplicate paths. |
| GA4 external administration | Keep custom definitions, key events, data-stream, cross-domain, and other property settings outside the GTM completion claim. |
| Media brief | Platform, business action/use, destination identity, official browser event/schema, installed template, and source mapping are explicit. |
| Media event absent from analytics plan | Configure from the media brief and official schema; use the plan only for compatible source evidence. |
| Informal media label | Block until the official event/conversion and destination identity are established. |
| Existing initialization | Reuse one compatible GTM/site/plugin/partner path or create one required base tag; do not add a speculative duplicate. |
| Google Ads conversion | Conversion ID/label, direct-versus-imported architecture, value/currency, transaction ID, action dependency, trigger, and consent are explicit. |
| Google Ads remarketing | Current business vertical/feed contract and every required item replace any unmodified GA4-array assumption. |
| Conversion Linker | Create/reuse only after current Google tag architecture, consumers, cross-domain need, and existing helpers are checked. |
| Microsoft UET | Base/page-load behavior, custom-event fields, goal dependency, SPA option, and UET consent route remain distinct. |
| Meta ecommerce | Current `content_ids`/`contents` contracts, catalog ID, value/currency, every item, installed template, and eligibility are explicit. |
| TikTok event | Current standard/custom event, objective fields, catalog, Event Builder/automatic overlap, template, and consent are explicit. |
| Snap event | Current browser Pixel/template documentation—not CAPI or another vendor—establishes fields, items, matching, and consent. |
| Unlisted media vendor | Current official browser event, field, template, consent, and matching documentation establishes every critical decision. |
| Required media value missing | The tag is ineligible; no empty, zero, guessed, or partial payload is sent unless explicitly and officially allowed. |
| Multi-item transformation | Missing/empty/one/many/zero/invalid cases preserve exact shape and all required items; invalid required items fail closed. |
| Catalog/feed ID | The actual catalog convention is approved; analytics item IDs are not assumed equivalent. |
| Direct source mapping | Use a DLV/direct field rather than an unnecessary transformation. |
| LUT/RLT | Multiple real deterministic inputs, clear mapping, and safe no-match behavior justify it. |
| Custom JavaScript | Built-ins cannot express the required output; the function is narrow, deterministic, null-safe, type-explicit, and side-effect free. |
| Transformation eligibility | Empty/undefined output is paired with the smallest explicit validity condition when the tag could otherwise execute. |
| DLV version | Version 1 literal-dot or Version 2 nested-path semantics match the source and all consumers. |
| Trigger Boolean logic | Firing-trigger OR, row-level AND, exception precedence, regex intent, repeatability, and event scope are correct. |
| Tag advanced settings | Priority, schedule, live-only, pause state, firing option, sequencing, and failure behavior remain default unless required. |
| Tag sequencing | The initiating tag carries the full consent predicate because sequenced tags ignore their own firing/exception triggers. |
| Default basic consent | Every in-scope base/event path is ineligible while the exact CMP state is unknown, uninitialized, or denied. |
| CMP block scope | Each exception can match every GTM event used by its consumers; a CMP-only event matcher does not block unrelated business events. |
| Compound CMP predicate | Independent category/purpose/vendor/product grants use the smallest OR-denial block set; no mutually exclusive AND or speculative consent helper. |
| Advanced consent | Exact product, explicit request, official denied-state behavior, defaults/updates, CMP/template support, user-data limits, and absence of a defeating block are proven. |
| Shared Google execution unit | Every destination has a compatible route or an approved officially supported separation; incompatible policies are blocked. |
| First-party user data | Explicit request, controlled source, accepted fields, normalization/hash ownership, consent, destination isolation, and no PII leakage are proven. |
| Template | Identity/version, publisher, permissions, fields/defaults, consumers, automatic behavior, and any approved update are verified before and after mutation. |
| Naming and folder | Default or approved convention is clear; related objects are grouped shallowly where useful and unrelated objects remain untouched. |
| Existing-object reuse | Output, ownership, source, shape, timing, consent, consumers, template, environment, and future change path are compatible. |
| Known conflicting implementation | Reconcile within in-scope authority or block; never add a parallel duplicate or silently disable unrelated collection. |
| Workspace and adapter | Dedicated workspace, pagination, stable IDs, fingerprints, pre-change state, conflicts, exact actions, and saved readback are complete. |
| Uncertain write or partial failure | Read back before retrying; stop dependent writes and preserve the exact current-operation recovery boundary. |
| Idempotent rerun | Every completed row resolves to `reuse` or `untouched`, never another create or repeat update. |
| Mutation unavailable | Status is `Blocked`, no live-change claim is made, and the exact access/capability needed is stated. |
| Server-side/deduplication request | Keep independent client-side work judgeable and mark the future capability `Deferred`; do not invent browser event IDs. |

## Analytics conformance proof

Before the first analytics write and again after saved readback, record the concise result for:

- expected and actual requirement IDs;
- included/reference-only/excluded scope differences;
- event, source event, timing, filters, outgoing fields, source paths, literals, and type/shape;
- unauthorized additions, removals, substitutions, and hidden-scope inclusions;
- blocking errors, advisories, implementation notes, and explicit amendments.

Use `scripts/validate_contract_conformance.py` when normalized JSON is available. It proves equality,
not workbook interpretation or official semantics. Keep technical GTM infrastructure outside the
analytics payload comparison and verify it through saved-object readback.

## Consent configuration proof

For basic gating, derive configured eligibility for CMP uninitialized/undefined, denied, another
vendor granted, complete grant, later grant, repeatable readiness/change, and revocation. Record the
normal trigger, block(s), predicate, event scope, and firing option responsible. Remember that a GTM
block cannot unload a script already loaded after grant.

For an explicitly approved advanced route, record the exact product/feature, defaults, updates,
returning choice, revocation, denied-state load/request/storage/data behavior, template/CMP support,
user-data restrictions, and absence of a conflicting block. Label it accurately as
`advanced consent-aware`, `native stop/hold`, `native cookie-control`, or
`adaptive/anonymous analytics`; do not collapse all behavior into “consent gated.”

These are saved-configuration expectations, never runtime observations.

## Concise handoff

Return only what the analyst needs to operate the workspace:

- target account, container, environment, and dedicated workspace;
- status by requirement/tag family;
- created, updated, reused, untouched, partial, blocked, and deferred in-scope objects;
- pre-existing workspace changes, current-run writes, and final totals;
- exact analytics conformance result or media brief/official-schema mapping result;
- material documentation advisories and blocking errors;
- selected consent route and any important configured limitation;
- exact partial recovery boundary or access blocker;
- external site, CMP, GA4-property, advertising-platform, catalog/feed, and publication dependencies;
- confirmation that an identical rerun is a no-op for configured work;
- confirmation that runtime recette and publication were not performed.

Do not duplicate a large technical annex by default. Preserve detailed object IDs, fingerprints,
pre-change representations, official sources, and static vectors in the current-operation evidence
when they are needed for safe recovery or review.
