# CMP and consent gating

## Establish what actually gates a tag

Classify each relevant tag using its final GTM firing logic:

| Mechanism | Counts as a gate only when |
| --- | --- |
| Built-in consent requirement | The tag explicitly requires the relevant consent type and GTM demonstrably prevents firing when it is denied. |
| Firing-trigger condition | The condition is part of the firing trigger and evaluates false under denied/unknown consent. |
| Blocking or exception trigger | The exception evaluates true under denied/unknown consent and prevents the tag from firing. |
| Observation only | A variable, event parameter, log, or informational check reads consent but does not prevent firing. This is not a gate. |

Never call a tag consent-gated merely because it evaluates, reports, or transmits consent state.

## Choose the implementation mechanism

Do not make a legal/privacy decision. Identify the client-approved policy and implement it accurately:

- If the project uses strict vendor blocking, prefer one reusable blocking trigger per vendor/platform.
- If the project uses Google built-in Consent Mode, inspect the exact tag settings and policy before adding exception triggers; do not silently mix mechanisms that change intended behavior.
- If the project uses a consent condition in a firing trigger, confirm it blocks every relevant firing path.

When strict vendor blocking is the agreed approach, ordinary business-event tags should normally use:

1. a normal Custom Event trigger for the business action; and
2. a vendor-specific blocking/exception trigger that is true when the vendor is not enabled.

Name the latter clearly, for example "Block - Didomi - Meta denied". Do not add "CE" to a blocking trigger name just because the tag's normal trigger is a Custom Event.

## Verify CMP semantics first

Before creating a condition or exception:

1. Read the CMP's current official GTM/dataLayer documentation.
2. Identify the correct CMP dataLayer event(s), dataLayer variable(s), cookies, or API state for the installed CMP/version.
3. Inspect the live dataLayer to confirm event order, values, types, and state before/after consent.
4. Identify the exact vendor ID or consent key required for the platform.
5. Design the condition so unknown, undefined, and denied state behave according to the approved strictness.

Do not infer a vendor ID, delimiter, matching rule, or event frequency from a remembered example. In particular, distinguish a Didomi event such as readiness/consent change from a variable such as an enabled-vendors value: they serve different purposes. Use the documented and observed value format for the actual site. Do not append a delimiter to a sample vendor value by convention.

## Blocking-trigger design

For a vendor such as Meta, a strict blocking trigger may conceptually mean:

    Block when the CMP's verified enabled-vendors state does not contain the exact, verified Meta vendor identity.

Implement the actual GTM condition only after confirming the CMP's documented value format and the live value. Avoid substring collisions and undefined-state loopholes. Reuse that blocking trigger for the vendor's relevant tags unless the vendor's policy or identity differs.

Use a normal trigger condition only when it is more precise or is required by the selected consent model. Do not duplicate separate consent conditions on every event trigger when one shared vendor block expresses the policy safely.

## Page-view timing

Page-view dataLayer events commonly occur before CMP state is available. Handle this separately:

1. Inspect the CMP's official event lifecycle and identify an event with the needed one-time page semantics.
2. Verify its actual firing order in the target site.
3. Attach the page-view logic to that event only with a verified consent decision.
4. Define whether a later consent change should create a page view and how duplicate sends are prevented.

Do not assume a generic consent-changed event is safe for a page view; it may fire multiple times. Do not claim that a tag is gated because a CMP variable exists in the container.

## Consent validation matrix

Validate each vendor tag against at least:

| State | Expected result under strict blocking |
| --- | --- |
| Unknown or CMP not initialized | Vendor tag does not fire. |
| Vendor denied | Vendor tag does not fire. |
| Vendor enabled and business event occurs | Tag may fire once if all non-consent conditions pass. |
| Different vendor enabled only | This vendor's tag does not fire. |
| Consent changes after initial page load | Behavior matches the documented page-view policy without duplicates. |
