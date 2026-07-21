# Acceptance and handoff

## Contents

- [Static completion definition](#static-completion-definition)
- [Judgement statuses](#judgement-statuses)
- [Static validation matrix](#static-validation-matrix)
- [Collection-contract conformance proof](#collection-contract-conformance-proof)
- [Consent configuration proof](#consent-configuration-proof)
- [Handoff output](#handoff-output)

## Static completion definition

Assign `Configured` only when authoritative current-workspace readback proves that the target
already matches the approved contract or that authorized changes brought it into that state, and
every applicable condition passes:

1. Confirm the target account, web container, environment, authorization, and workspace by stable
   identity.
2. Create or reuse a dedicated workspace when possible; document and obtain approval for any
   Default Workspace fallback.
3. Identify the correct analytics or media business authority, classify every relevant source item
   as included, reference-only, excluded, or ambiguous, and create one configuration-contract record
   per independently judgeable requirement.
4. For media, capture the media-team objective independently of any analytics tracking plan.
5. Give every critical business, source, destination, template, consent, and container fact a
   non-assumption evidence grade.
6. For analytics, preserve the approved collection contract exactly and use current official
   documentation to classify conformant choices, advisories, and blocking errors without silently
   substituting or enriching the plan. For media, use the official destination schema independently.
7. Establish the source event, timing contract, type, scope, cardinality, null behavior, state
   lifetime, and representative zero/one/many payloads where applicable.
8. Map every destination field through business meaning, source contract, GTM resolution, installed
   template field, official destination contract, and representative result.
9. Inspect the installed template identity/version/permissions and reconcile visible fields and
   hidden behavior with current official documentation.
10. Select the target architecture from the applicable skill playbooks and current official/template
    documentation. Use container state only for integration evidence. Reuse an existing object only
    after it passes the same architecture and static checks as a new object; never reproduce a legacy
    pattern or add a parallel implementation around a known conflict.
11. Prove a static normal firing path and the selected strict/basic or explicitly approved advanced
    consent configuration for every tag without describing it as observed runtime behavior.
12. Resolve known base/configuration, automatic/manual event, environment, and shared-execution-unit
    conflicts from the available container and approved-input evidence.
13. Enable first-party user-data features only with explicit authorization, approved sources,
    current vendor requirements, and consent controls.
14. Record every external site, CMP, GA4-administration, advertising-platform, and publication
    dependency without claiming it was completed by GTM configuration.
15. Before mutation, prove exact approved-to-intended collection-contract conformance: identical
    scope, requirement IDs, events, business timing, fields, sources, and literals, with no
    unauthorized additions, removals, or substitutions.
16. Capture stable IDs/fingerprints, exact pre-change state, and pre-existing workspace changes.
    Whether or not a write is needed, re-read every relevant saved object and prove both
    approved-to-saved collection conformance and intended-to-saved implementation conformance.
17. Report pre-existing workspace changes, current-run changes, and final workspace totals
    separately. Confirm that a repeated execution would reuse or leave objects untouched and that no
    publish, Submit, or GTM version action occurred.

For `Specification complete`, apply the same conditions except live mutation and saved-object
readback. Provide exact planned fields, dependencies, action semantics, and verification assertions,
and state that no live GTM object changed.

Runtime execution is outside this skill and is never an input or completion condition. Static
configuration must not be presented as browser, network, CMP, or vendor-platform observation.

## Judgement statuses

Apply one status per requirement or tag family:

| Status | Meaning |
| --- | --- |
| `Configured` | Authoritative current-workspace readback proves the saved state already matched the approved contract or that authorized changes were applied; every relevant object passes the static invariants. |
| `Specification complete` | The complete object-level design passes static invariants, but mutation was not authorized or no mutation path was available. |
| `Partial` | The current authorized operation changed some objects but could not finish; exact saved state, dependencies, and safe recovery boundary are recorded. |
| `Blocked` | A critical authorization, business, source, destination, template, consent, or mutation fact cannot be established safely. |
| `Deferred` | The requirement depends on server-side GTM, CAPI, browser/server deduplication, event-ID architecture, or another intentionally future capability. |

Apply mixed statuses at requirement or tag-family grain. Do not label an unaffected family `Partial`
or `Blocked` merely because another family failed.

## Static validation matrix

Use every applicable scenario:

| Scenario | Required static assertion |
| --- | --- |
| Analytics tracking-plan event | The exact approved event, field set, source contract, and business timing are preserved when technically valid; official findings validate and classify rather than silently redesign the plan. |
| Direct analytics request | A missing plan does not block when the analyst has explicitly approved the exact event, field set, business timing, intended use, and complete source contract. An informal business action alone does not authorize the skill to design the measurement plan silently. |
| Media brief absent from tracking plan | The media brief drives the destination; the plan is used only for reusable source evidence. |
| Informal media label | No tag is configured until the official standard/custom event, destination identity, and field schema are established. |
| No runtime access | Approved inputs, representative payloads, current documentation, template, and container evidence are graded; runtime is not requested or used as a completion gate. |
| Critical assumption | The affected requirement is `Blocked`; an assumption never supplies an ID, source timing/type, consent predicate, or required destination field. |
| Valid custom event with documented recommended alternative | The approved custom event is preserved, the recommended alternative and consequences are reported as advisory before mutation, and no substitution occurs without a new explicit decision. |
| Invalid or reserved analytics event | The affected requirement is `Blocked`; the skill reports current official evidence and never substitutes another event automatically. |
| Missing required analytics field | The affected requirement is `Blocked`; no source, literal, empty value, or optional fallback is invented. |
| Recommended or optional field absent from plan | The field remains absent and is reported as advisory when useful; it is not added automatically. |
| Workbook/source scope | Every relevant source item is included, reference-only, excluded, or ambiguous with evidence; hidden does not mean excluded and visible does not mean in scope. |
| GA4 config | `GA4 - Config` uses a relative measurement-ID reference where appropriate and follows the approved page-view architecture. |
| GA4 Event Settings | `GA4 - Event Setting` exists only when genuinely shared fields simplify the selected events. |
| Manual GA4 page view | Known Google tag and Enhanced Measurement settings are reconciled, parameters are available under the source contract, and no known automatic/manual duplicate remains. |
| GA4 external administration | Required custom definitions, key-event designation, data-stream, Enhanced Measurement, cross-domain, or other Google/GA4 settings outside the GTM authorization are listed separately. |
| Google Ads conversion | Conversion ID/label, value, currency, transaction ID, trigger, direct/imported architecture, external conversion action, and consent are explicit. |
| Google Ads dynamic remarketing | Business vertical/feed IDs and every item match the current Google Ads schema rather than an unmodified GA4 array. |
| Conversion Linker | It is created/reused only after checking current Google tag architecture, consumers, cross-domain need, and existing linkers. |
| Microsoft UET | Base/page-load behavior, custom-event fields, external goal configuration, and selected consent route remain distinct. |
| Meta ecommerce | `content_ids`, `contents`, value/currency, catalog identifiers, and all items use current documented browser shapes. |
| TikTok event | Current standard/custom name, objective fields, Event Builder/automatic dependencies, and external settings are recorded. |
| Snap event | Current browser Pixel and installed-template documentation, rather than CAPI analogy, establishes the schema. |
| Other media vendor | Current official browser event, field, consent, matching, and template documentation is recorded before configuration. |
| Existing initialization | A compatible GTM tag, hard-coded/partner dependency supplied by the analyst, or template path is reused; no speculative duplicate base tag is added. |
| Base/configuration tag | One compatible initialization path contains only documented behavior and has a valid configured opportunity under the approved consent lifecycle. |
| Default strict/basic consent | The approved CMP predicate translates into blocks that are expected to prevent every in-scope loader/event path for unknown and denied states. |
| Blocking-trigger event scope | Each exception can activate on every GTM event used by its consumers; a CMP-only matcher does not claim to block unrelated events. |
| Compound consent predicate | Required category/purpose, vendor, product consent type, initialization, and region components from the approved policy are represented or the design is blocked. |
| Direct CMP condition | Native documented state is tested directly when safe; unsupported or undocumented state shape is blocked rather than hidden in a speculative helper. |
| Advanced Google family | Exact products, explicit approval, defaults/updates, shared execution units, and intended denied-state behavior are documented without a defeating block. |
| Shared Google execution unit | Every destination/consumer has a compatible route or an officially supported separation is approved; incompatible routes are not claimed to coexist. |
| Advanced Microsoft UET | Explicit approval, `ad_storage`, default/update order, installed template, and documented denied-state behavior are established. |
| Microsoft Clarity | Clarity is decided separately from UET and uses its current official Consent API/types and installed integration. |
| Native cookie or stop/hold control | Cookie suppression or holding is not mislabeled as advanced denied-state measurement. |
| First-party user data | Explicit authorization, accepted fields, normalization/hash ownership, controlled source, consent, and destination isolation are proven statically. |
| Missing source | The required site/dataLayer obligation is a blocker; no DOM/click/URL value or placeholder is silently invented. |
| Non-dataLayer fallback | The analyst explicitly approves the supplied stable selector/URL/history/visibility contract and its fragility is documented; otherwise it is blocked. |
| Multi-item transformation | Supplied empty, one-item, and multi-item cases preserve exact arrays, objects, types, and every eligible item. |
| Lookup/RLT | Multiple real deterministic scenarios and safe no-match behavior justify the table. |
| Custom JavaScript | Built-ins cannot express a required destination transformation cleanly; the function is narrow, deterministic, null-safe, and covered by static test vectors. |
| DLV version | Version 1 literal-dot versus Version 2 nested-path semantics are selected deliberately for the supplied source contract. |
| Trigger filters | OR behavior across firing triggers, AND behavior within filters, exception precedence, regex anchoring, and repeatability are explicit. |
| Tag advanced settings | Priority, schedule, live-only behavior, firing option, sequencing, and failure behavior remain default unless currently required and documented. |
| SPA page view | Application event, known History Change and Enhanced Measurement settings, and vendor automatic behavior do not create a known duplicate. |
| Tag sequencing | The initiating tag carries the vendor block and unknown/denied state is statically expected not to start setup or cleanup tags. |
| Community template | Publisher, version/commit, permissions, fields, update diff, consumers, and explicit approval are recorded. |
| Existing-object reuse | The skill reference architecture is selected first; output, ownership, timing, consent, consumers, environment, template, future change path, and all static criteria are compatible. Existing prevalence alone is irrelevant. |
| Legacy container pattern | A nonconformant local helper, trigger, consent route, page-view pattern, or tag architecture is not reused or copied merely because it exists. |
| Conflicting existing implementation | The skill updates/disables only within authority or blocks the affected requirement; it never adds a knowingly duplicate parallel implementation. |
| Workspace precondition | Dedicated workspace identity, pre-existing changes, synchronization state, conflicts, object IDs, fingerprints, and pre-change state are recorded. |
| Workspace change attribution | Pre-existing changes, current-run actions, and final workspace totals are reported separately. |
| Idempotent second execution | The saved state produces `reuse` or `untouched`, not duplicate objects or repeat updates. |
| Tool unavailable | The complete contract is `Specification complete` and no live-change claim is made. |
| Partial mutation | Dependent writes stop; saved created/updated objects, untouched work, exact blocker, and safe recovery boundary are recorded. |
| Deferred server-side dependency | No event-ID or browser/server configuration is added; future work is `Deferred`. |

## Collection-contract conformance proof

For every analytics tracking-plan implementation, record both pre-write and saved-state results:

- expected and actual requirement counts;
- missing and extra requirement IDs;
- included/reference-only/excluded scope differences;
- event-name, source-event, business-timing, filter, parameter, source-path, literal, and type/shape mismatches;
- unauthorized additions, removals, substitutions, or hidden-scope inclusions;
- blocking errors, advisories, implementation notes, and explicit analyst amendments.

The approved-to-intended comparison must pass before the first affected write. The
approved-to-saved comparison must pass before `Configured`. When normalized JSON is available, use
`scripts/validate_contract_conformance.py` and preserve its JSON result. The comparator proves
equality only; it does not interpret a client workbook or establish official semantics.

Keep the implementation manifest separate and verify required technical IDs, consent, GTM
references, template fields, firing options, and adapter state independently. Do not classify
necessary implementation infrastructure as an unauthorized payload field.

## Consent configuration proof

For strict/basic gating, derive an expected configuration decision for each vendor base/configuration
and event tag under:

- CMP not initialized or source undefined;
- source value outside its approved documented contract;
- required category/purpose or vendor denied;
- another vendor granted while this vendor remains denied;
- required grant present before the normal event;
- later grant after an initial denial;
- revocation after grant, including the limitation that a GTM block does not unload an already
  loaded script;
- repeatable readiness/change and business events.

Record `expected to fire` or `expected not to fire`, the normal trigger, blocking trigger, predicate,
event scope, tag firing option, and condition responsible. Mark this as static configuration logic.
Do not write `fires` or `does not fire` as an observed fact.

For explicitly approved advanced behavior, record instead:

- exact browser product, official feature, and approval;
- defaults, updates, returning-choice handling, and revocation command;
- documented denied-state loading, request, storage, identifier, and data-use behavior;
- installed template/CMP support and fields;
- absence of disallowed user-provided data in the configured denied route;
- any external account, CMP, site, or optional validation dependency.

Label the configuration `advanced consent-aware`, `native stop/hold`, `native cookie-control`, or
`adaptive/anonymous analytics` as applicable; do not collapse it into `consent gated`.

## Handoff output

Return two layers.

### Analyst summary

- target account, container, environment, and workspace;
- authorized scope and primary analytics/media inputs;
- source-scope result and tracking-plan/documentation blocking errors, advisories, and implementation notes;
- status by requirement/tag family;
- pre-existing workspace changes, current-run created/updated/reused/untouched/partial/blocked/deferred work, and final workspace totals;
- approved-to-intended and approved-to-saved collection-contract conformance result;
- external site, CMP, GA4, advertising-platform, publication, and optional validation dependencies;
- confirmation that runtime execution was not performed or claimed;
- confirmation that no publication or GTM version occurred.

### Technical annex

- complete configuration-contract records and evidence grades;
- normalized source-scope manifest, discrepancy report, explicit analyst amendments, and deterministic conformance output;
- requirement-to-object graph and ordered change manifest;
- field-level business-to-source-to-GTM-to-template-to-destination map;
- current official sources, page titles, access dates, and decisions;
- product-level consent predicate and capability matrix;
- template identity/version, permissions, fields, and consumers;
- object IDs/paths, fingerprints, pre-change state, intended/saved fields, and references;
- pre-existing workspace snapshot, current-operation mutation journal, and final workspace totals;
- static validation results and idempotency result;
- exact partial-state recovery boundary, blockers, external dependencies, and deferrals.

Keep the summary concise and the annex complete. Do not duplicate the entire annex in object notes,
and do not present static inspection as runtime evidence.
