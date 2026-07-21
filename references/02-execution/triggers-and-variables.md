# Triggers and variables

## Contents

- [Prefer dataLayer Custom Events](#prefer-datalayer-custom-events)
- [Configure Custom Event triggers precisely](#configure-custom-event-triggers-precisely)
- [Model trigger Boolean logic](#model-trigger-boolean-logic)
- [Handle initial page views and SPA navigation separately](#handle-initial-page-views-and-spa-navigation-separately)
- [Use blocking triggers as vendor policy objects](#use-blocking-triggers-as-vendor-policy-objects)
- [Select variables by purpose](#select-variables-by-purpose)
- [Use lookup tables selectively](#use-lookup-tables-selectively)
- [Inspect advanced tag execution settings](#inspect-advanced-tag-execution-settings)
- [Use tag sequencing only when required](#use-tag-sequencing-only-when-required)
- [Account for environments and hostnames](#account-for-environments-and-hostnames)
- [Official entry points](#official-entry-points)

## Prefer dataLayer Custom Events

Use the exact approved dataLayer event and timing. When an approved input authorizes a new source
contract, default to one exact vendor-neutral Custom Event per business action whenever the dataLayer
can provide the success signal. Reuse the same normal trigger across analytics and media tags only
when event timing and semantics are identical and the selected reference architectures remain
compatible.

Create a different trigger type only when:

- no reliable business event exists;
- the analyst approves the fallback;
- an approved site contract, supplied implementation artifact, or authoritative human decision establishes that the chosen signal represents the action;
- the selector, URL, history state, visibility rule, or timing is stable;
- the handoff records the resulting fragility and external site dependency.

Do not create click, form, timer, scroll, visibility, DOM, or URL triggers merely because GTM supports them. A click is not automatically a successful form submission, purchase, or lead.

## Configure Custom Event triggers precisely

- Match the exact dataLayer event name by default.
- Use a regex event name only for a real, documented family of equivalent events.
- Keep consent out of the normal business trigger when a shared vendor block can express it cleanly.
- Add business filters only when the same event name legitimately represents distinct scenarios.
- Check whether the event can repeat and whether one tag execution per push is correct.

Name normal triggers `CE - <event_name>`.

## Model trigger Boolean logic

Record the complete Boolean expression before creating triggers:

- firing triggers on one tag are alternatives: any matching firing trigger can make the tag eligible;
- filter rows within one trigger are cumulative and must all match;
- any matching blocking/exception trigger prevents the tag from firing;
- trigger groups, setup/cleanup sequencing, and tag firing options add separate lifecycle rules;
- regex event names and filters must be deliberately anchored or unanchored, escaped, and tested against supplied positive and negative examples.

Use the smallest trigger graph that expresses the approved logic. Do not compress independent OR-denial conditions into one trigger whose AND filters can never match together.

## Handle initial page views and SPA navigation separately

For an initial page view under strict/basic gating, use the CMP's verified one-time readiness event when the page-view dataLayer push precedes usable consent state.

Revalidate every page parameter on the CMP event that actually fires the tag. Use browser built-ins or retained dataLayer state only when the approved source contract establishes that the value remains current; do not assume a value scoped to an earlier `page_view` push remains available. If the required source is unavailable or stale under the contract, record a blocker and require a CMP-safe application event or source contract.

For an SPA:

1. Prefer an application-owned virtual-page-view Custom Event with the final URL/title/referrer values.
2. Inspect Enhanced Measurement and every vendor's automatic SPA behavior.
3. Use History Change only as an approved fallback when no reliable application event exists.
4. Update configuration fields before the separate page-view event when the destination requires it.
5. Prevent initial-load, browser-history, router, and manual duplicate page views.

## Use blocking triggers as vendor policy objects

Create the smallest reusable set of blocks that expresses the approved CMP predicate. One vendor/platform block is preferred when one native condition represents the complete grant. When category/purpose, vendor, product consent type, or initialization are independent required grants, use semantically named reusable blocks so any missing grant blocks; do not force mutually exclusive denial conditions into one AND trigger. Name vendor blocks `Block - <CMP> - <Vendor> denied` and qualify shared category/purpose blocks clearly.

Make the blocking trigger's event matcher cover every normal event used by its consumer tags. For Custom Event consumers, use a tested regex scope when one shared block must cover several event names. Do not use a CMP readiness/change event as the exception's event name for unrelated business-event tags: the exception must activate on the same GTM event that could fire the tag.

Do not label a normal Custom Event trigger as a blocking trigger. Do not append `CE` to a block name. Inspect all consumers before changing a shared block.

## Select variables by purpose

| Need | Preferred variable |
| --- | --- |
| Direct event value | DLV |
| Stable ID or semantic constant | Constant |
| Shared Google configuration/event fields | Google tag settings variable when it genuinely simplifies the design |
| Exact multi-scenario mapping | Lookup table |
| Pattern-based deterministic mapping | Regex lookup table |
| Required array/object or multi-step conversion | Narrow Custom JavaScript |
| Stable URL component | Built-in or user-defined URL variable when no dataLayer source is available |
| Stable click/element property | Auto-event variable only for an approved non-dataLayer fallback |

Prefer dataLayer values over DOM extraction. Do not use a JavaScript Variable to access a value already exposed cleanly through a DLV.

For every DLV, record whether Version 1 literal-dot or Version 2 nested-path semantics match the actual source key. Do not change a reused DLV version without inspecting every consumer.

## Use lookup tables selectively

Create a lookup or regex table only when:

- at least two real input scenarios need a mapping;
- the mapping is deterministic and easier to understand than repeated conditions or code;
- every input/output and default/no-match behavior is defined;
- the table reduces real duplication;
- representative inputs can be tested.

Apply this judgement to analytics and media alike. Do not force a table into a direct one-to-one mapping.

## Inspect advanced tag execution settings

For every created or updated tag, inspect priority, custom schedule, live-only behavior, pause state, firing option, setup/cleanup references, and consent settings. Preserve defaults unless a current requirement or documented template/vendor constraint justifies a non-default value.

Record the selected firing option, normally once per event unless the approved lifecycle requires once per page or unlimited execution. A higher priority changes asynchronous start order but does not create a completion dependency; use sequencing when a documented dependency must finish first.

## Use tag sequencing only when required

Prefer independent tags triggered by the same business event when the vendor template handles initialization correctly. Use setup/cleanup sequencing only when current official documentation or installed template behavior requires a strict dependency.

GTM setup and cleanup tags invoked through sequencing ignore their own firing and blocking triggers. Put the applicable vendor block on the initiating tag, verify that a denied/unknown event never starts the sequence, and do not treat an exception attached only to the sequenced tag as protection.

Document failure behavior: decide whether the event tag should run if the setup tag fails. Do not use sequencing to hide a missing base-tag or consent design.

## Account for environments and hostnames

Reuse or create environment/hostname mappings only when the implementation genuinely differs by environment or region. Prefer one tested LUT/RLT over duplicated tags when the destinations and consent policy remain semantically aligned.

Never send staging/test traffic to a production destination unless explicitly intended. Do not infer an environment mapping from hostname alone without confirming the target architecture.

## Official entry points

- https://support.google.com/tagmanager/answer/7679316
- https://support.google.com/tagmanager/answer/7679219
- https://support.google.com/tagmanager/answer/7679318
- https://support.google.com/tagmanager/answer/6238868
- https://support.google.com/tagmanager/answer/2772421
- https://developers.google.com/tag-platform/tag-manager/datalayer
- https://support.google.com/tagmanager/answer/7683362
- https://developers.google.com/tag-platform/tag-manager/api/reference/rest/v2/accounts.containers.workspaces.tags
