# Acceptance and handoff

## Contents

- [Completion definition](#completion-definition)
- [Judgement statuses](#judgement-statuses)
- [Static validation matrix](#static-validation-matrix)
- [Consent proof](#consent-proof)
- [Handoff output](#handoff-output)

## Completion definition

Mark a configuration complete only when all applicable conditions pass:

1. Confirm the target account, web container, environment, authorization, and workspace.
2. Create or reuse a dedicated workspace when possible; document and obtain approval for any Default Workspace fallback.
3. Identify the correct analytics or media requirement authority.
4. For media, capture the media-team objective independently of any analytics tracking plan.
5. Map every requirement to exact GTM objects and every destination field to its source, type, shape, transformation, and template field.
6. Consult current official documentation for every destination event, parameter, template setting, per-product consent capability, CMP signal, and vendor identity.
7. Validate the source dataLayer event, timing, types, null behavior, and zero/one/multi-item payloads where applicable.
8. Inspect the installed template identity/version/permissions and reconcile its fields with official documentation.
9. Reuse semantically compatible objects, avoid unintended duplicates, and justify every new object by a current requirement or documented constraint. A direct field or DLV must not be replaced by an unnecessary helper.
10. Verify a normal firing path and the selected strict/basic or explicitly approved advanced consent behavior for every tag.
11. Under the default strict/basic route, prove unknown, uninitialized, and denied state prevent firing. Treat a CMP value outside its documented contract as a blocking integration defect rather than a helper-variable requirement.
12. Keep base/configuration tags from sending automatic page views by default and resolve every documented vendor exception or automatic/manual duplicate.
13. Enable first-party user-data features only with explicit authorization, approved sources, current vendor requirements, and consent controls.
14. Re-read every saved object and inspect references after mutation.
15. Record configuration evidence separately from runtime Preview/network/vendor evidence. If any required runtime assertion remains, use `Needs runtime QA`; do not also label that requirement `Complete`.
16. Confirm that no publish, Submit, or GTM version action occurred.

If any applicable condition is unverified, do not mark the affected work complete.

## Judgement statuses

| Status | Meaning |
| --- | --- |
| Complete | All applicable configuration criteria pass and every runtime assertion required by the acceptance contract is already evidenced; no required validation remains. |
| Blocked | Critical authorization, destination, official requirement, source data, template behavior, consent fact, or runtime timing cannot be established safely. |
| Deferred | The requirement depends on server-side GTM, Conversions API, browser/server deduplication, event-ID architecture, or another planned future capability. |
| Needs runtime QA | Static object state passes, but one or more explicitly listed GTM Preview, browser network, CMP journey, or vendor-diagnostic assertions remain. Do not also label the same requirement `Complete`. |

Apply a status per requirement/tag family when a mixed implementation has different outcomes.

## Static validation matrix

Use every applicable scenario:

| Scenario | Required assertion |
| --- | --- |
| Analytics tracking-plan event | The plan's business action maps to the current official analytics event/parameters and a vendor-neutral Custom Event. |
| Direct analytics request | Missing plan does not block when business meaning and source contract are otherwise established. |
| Media brief absent from tracking plan | The media brief drives the destination; the plan is used only for reusable source evidence. |
| Informal media event label | No tag is created until the official standard/custom event and field schema are established. |
| Standard versus custom media event | A standard event is preferred when semantics fit; custom use and platform limitations are documented. |
| GA4 config | `GA4 - Config` uses a relative measurement-ID reference where appropriate and does not send an automatic page view by default. |
| GA4 Event Settings | `GA4 - Event Setting` exists only when genuinely shared fields simplify the design. |
| Manual GA4 page view | Automatic and Enhanced Measurement behavior is inspected, every parameter is current on the actual firing event, and no duplicate page view remains. |
| Google Ads conversion | Conversion ID/label, value, currency, transaction ID, trigger, and consent match current official requirements. |
| Google Ads dynamic remarketing | Business vertical/feed IDs and every item match the current Google Ads schema rather than an unmodified GA4 array. |
| Conversion Linker | It is created/reused only after checking the current Google tag architecture and existing linkers. |
| Microsoft UET | UET base/page-load behavior and custom-event fields match current Microsoft documentation and platform-goal conditions remain distinct. |
| Meta ecommerce | `content_ids`, `contents`, value/currency, and all items use the current documented shapes; item zero is not selected. |
| TikTok event | Current standard/custom name, reserved-name rules, objective-specific parameters, and Event Builder duplicates are checked. |
| Snap event | Current browser Pixel event/template documentation, rather than Conversions API analogy, establishes the schema. |
| Other media vendor | Current official browser, event, parameter, consent, and template documentation is recorded before configuration. |
| Base/configuration tag | When initialization is in scope, one compatible path supplies only documented behavior, has a valid once-per-page opportunity after initial or later consent grant where required, and does not duplicate an existing base implementation or inherent page-load event. |
| Default strict/basic consent | One shared CMP block per vendor/platform prevents tag loading/firing for unknown and denied consent. |
| Blocking-trigger event scope | The exception matcher activates on every normal GTM event used by its consumer tags; a CMP-only event matcher does not claim to block unrelated business events. |
| Direct CMP blocking condition | The blocking trigger tests the documented CMP state variable directly with one native negative condition that covers every non-granted state. No consent CJS, JavaScript, table, or Boolean helper is created; an unsupported source contract is `Blocked`. |
| Advanced Google product-family Consent Mode | The exact Google tag, GA4, Google Ads, Floodlight, or Conversion Linker products are listed; explicit approval exists; defaults precede affected tags, updates are timely, and blocking logic does not defeat intended behavior. |
| Shared Google execution unit | Every destination or consumer of a shared Google tag/linker has a compatible consent route, or a current officially supported separation is approved; incompatible basic and advanced policies are not attached to one execution unit. Compatible blocking triggers are reused by semantic equivalence rather than duplicated by product label. |
| Advanced Microsoft Advertising UET | Explicit approval exists; `ad_storage`, immediate loading, anonymized denied-state collection, updates, and GTM template behavior match current Microsoft documentation. |
| Microsoft Clarity advanced mode | Clarity is decided separately from UET; its current Consent API/types, cookieless denied behavior, storage, updates, and UET coupling are verified. |
| Adaptive/anonymous analytics | The exact Matomo, Piwik PRO, or other official reduced-data mode and its limits are documented, and an approved client policy exists; the agent does not supply the legal basis. Capability classification does not authorize tag configuration outside this skill's current Google tag/GA4 analytics route. |
| Native cookie or stop/hold control | Cookie suppression or event holding is not mislabeled as advanced denied-state measurement; unresolved transmission remains strictly blocked. |
| First-party user data | Explicit authorization, vendor field/normalization/hash rules, controlled sources, consent, and no PII leakage are proven. |
| Source missing | The required dataLayer change is a blocker; no DOM/click/URL fallback or invented value is added silently. |
| Multi-item transformation | Empty, one-item, and multi-item outputs preserve exact arrays, objects, types, and all eligible items. |
| Lookup/RLT | Multiple deterministic scenarios and tested no-match behavior justify the table. |
| Custom JavaScript | Built-ins cannot express a required destination transformation cleanly; the function is narrow, null-safe, and tested. Routine CMP vendor consent is not transformed in CJS. |
| SPA page view | Application event, History Change, Enhanced Measurement, and vendor auto-SPA behavior cannot duplicate one another. |
| Tag sequencing | The initiating tag carries the vendor block and denied/unknown consent cannot invoke setup or cleanup tags that would ignore their own triggers. |
| Community template | Publisher, version, permissions, fields, update diff, and approval are recorded. |
| Existing-object reuse | Output, ownership, timing, consent, consumers, environment, and future change path are compatible. |
| Tool unavailable | The complete object specification is returned and no live-change claim is made. |
| Deferred server-side dependency | No event-ID or browser/server configuration is added; future work is recorded as deferred. |

## Consent proof

For strict/basic gating, evaluate each vendor's base/configuration and event tags under:

- CMP not initialized;
- consent value undefined;
- CMP value outside its documented contract, which fails integration validation and leaves the affected design blocked;
- vendor denied;
- another vendor granted while this vendor remains denied;
- vendor granted before the normal event;
- grant after initial denial;
- revocation after grant, including any already-loaded script and automatic vendor behavior;
- repeatable consent-change and page-view events.

Record `fires` or `does not fire`, the normal trigger, the blocking trigger, and the actual condition responsible. A visible consent value or built-in-check label without final non-fire proof fails strict/basic acceptance.

For advanced behavior, record instead:

- explicit approval and vendor feature;
- exact browser product and consent classification;
- default and updated consent states;
- whether the tag loads under denied state;
- exact documented request/storage behavior under denied state;
- absence of disallowed cookies or user-provided data;
- the mechanism that changes behavior after grant/revocation.

Label the result `advanced consent-aware`, not `strictly blocked`.

## Handoff output

Return a concise traceable handoff containing:

- target account, container, environment, and workspace;
- primary requirement source for analytics and/or media;
- requirement-to-object map;
- field-level source-to-DLV-to-template-to-destination map;
- official sources, page titles, access dates, and key decisions;
- consent-capability matrix per browser product, including denied-state loading, requests, storage, API/types, CMP/template, approval, and status;
- template identity/version and permissions;
- created, modified, reused, and intentionally untouched objects;
- current requirement or documented constraint justifying each created object;
- normal firing trigger and final consent mechanism per tag/browser product;
- configuration validation results and judgement status;
- blockers, missing dataLayer requirements, deferred capabilities, and required runtime tests;
- explicit confirmation that no publication or GTM version occurred.

Do not present static inspection as runtime evidence. Route full interactive journey validation to the separate GTM Preview recette workflow.
