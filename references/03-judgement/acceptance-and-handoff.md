# Acceptance and handoff

## Completion definition

Mark an implementation complete only when all applicable conditions are satisfied:

1. The target container, environment, authorization, and workspace are confirmed.
2. A dedicated workspace was created or reused when possible; any fallback to Default Workspace is documented and approved.
3. The business requirement is mapped to exact GTM objects, or an explicit blocker is recorded.
4. Official documentation was consulted for every vendor-specific event, field, data shape, template setting, CMP signal, and vendor identity.
5. Existing compatible objects were reused and unintended duplicates were avoided.
6. Each tag has a verified normal firing path and the correct built-in or trigger-based consent gate.
7. Unknown and denied consent produce the required non-fire decision for strictly gated tags.
8. Resolved values, types, transformations, and all required ecommerce items are correct.
9. Automatic/manual page-view duplication and CMP timing are checked when applicable.
10. Every saved object was re-read or otherwise verified after mutation.
11. The handoff records changes, reuse decisions, sources, blockers, deferred capabilities, and runtime tests still required.
12. No publish or GTM version action occurred.

If a condition cannot be verified, do not silently mark the work complete.

## Judgement statuses

Use one of these statuses:

| Status | Meaning |
| --- | --- |
| Complete | Configuration-level acceptance criteria are satisfied; only separately identified runtime recette may remain. |
| Blocked | A critical input, official requirement, authorization, or runtime fact cannot be established safely. |
| Deferred | The request depends on a future capability, such as server-side GTM or deduplication, not implemented by V1. |
| Needs runtime QA | Static configuration is complete, but interactive preview/journey evidence is still required. |

## Static validation matrix

Use the scenarios that apply:

| Scenario | Required assertion |
| --- | --- |
| GA4 business custom event | A vendor-neutral Custom Event feeds the documented GA4 event and official parameters. |
| Manual GA4 page view | Automatic/enhanced page-view behavior is inspected and no duplicate page view is created. |
| Page view before CMP readiness | The selected CMP event has verified one-time behavior and the tag stays blocked without the required vendor consent. |
| Media purchase with many items | Every item is present in vendor-required arrays with the documented shape and types. |
| Existing-object modification | Reused trigger/variable consumers are inspected and retain compatible behavior. |
| Lookup table justified | Multiple deterministic scenarios, default behavior, and representative outputs are documented. |
| Lookup table not justified | A direct mapping is retained; no artificial abstraction is added. |
| Event Settings variable not justified | GA4 event-specific fields remain on the event tag and no settings variable is created. |
| Semantic reuse | A matching existing variable/trigger is reused only after checking purpose, output, and consumers. |
| Official documentation unavailable | The unresolved field is recorded as a blocker; no inferred configuration is created. |
| CMP event versus CMP variable | Event timing and state-value semantics are verified separately. |
| Deferred server-side dependency | The dependency is recorded as deferred; no server-specific configuration is added in V1. |

## Consent proof

For each vendor, evaluate the final tag logic under:

- unknown or uninitialized;
- vendor denied;
- vendor enabled;
- another vendor enabled but this vendor denied;
- consent changed after page load, when relevant.

Record the final expected decision as "fires" or "does not fire," with the specific trigger, blocking, or built-in mechanism responsible. A consent value that is merely visible in Data Layer or a tag parameter fails this validation.

## Handoff output

Return a concise, traceable change map containing:

- target container, environment, and workspace;
- requirement-to-object mapping;
- official documentation consulted and access date;
- created, modified, reused, and intentionally untouched objects;
- final consent-gating mechanism per vendor;
- validation results and judgement status;
- blockers, deferred capabilities, and runtime tests still required;
- confirmation that no publish action occurred.

Full interactive journey testing belongs to the separate GTM Preview recette workflow. Do not present static configuration validation as completed runtime evidence.
