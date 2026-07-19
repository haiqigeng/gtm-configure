# Google product-family Consent Mode

## Contents

- [Treat Consent Mode as broader than GA4](#treat-consent-mode-as-broader-than-ga4)
- [Choose the mode explicitly](#choose-the-mode-explicitly)
- [Verify consent types](#verify-consent-types)
- [Implement the default basic route](#implement-the-default-basic-route)
- [Implement advanced mode only when approved](#implement-advanced-mode-only-when-approved)
- [Keep tag behavior and page views separate](#keep-tag-behavior-and-page-views-separate)
- [Configure every Google product consistently](#configure-every-google-product-consistently)
- [Define the Tag Assistant handoff](#define-the-tag-assistant-handoff)
- [Official entry points](#official-entry-points)

## Treat Consent Mode as broader than GA4

Google Consent Mode is not a GA4-only feature. Current Google documentation lists built-in consent checks for:

- the Google tag;
- Google Analytics, including GA4;
- Google Ads Conversion Tracking and Remarketing, with Phone Call Conversions currently identified as pending support;
- Floodlight;
- Conversion Linker.

Verify this live list for every implementation. Decide basic or advanced behavior per destination/product, then reconcile those decisions with the actual Google tag and helper execution units.

A blocking trigger attached to one shared Google tag blocks that tag for every connected destination; leaving the tag unblocked can expose every connected destination to that tag's denied-state behavior. Do not claim that incompatible per-product policies coexist merely because the destinations are listed separately. If one executable Google tag or helper serves products that require different routes, use only a current, officially supported destination-specific separation that the analyst approves. Otherwise mark the affected configuration `Blocked` pending an architecture decision.

## Choose the mode explicitly

Use current Google documentation to distinguish basic and advanced Consent Mode.

Default this skill to basic behavior: prevent Google tags from loading until the required consent is granted. Use advanced behavior only when the analyst explicitly requests and approves Google tags loading under denied defaults and sending the documented cookieless or limited-data signals.

Basic Consent Mode blocks Google tags until the required grant. Advanced Consent Mode loads consent-aware Google tags under documented defaults and changes their behavior according to consent state.

Do not describe built-in consent checks as a strict firing gate. Google tags with built-in checks can still execute in advanced mode and alter storage/transmission according to consent state.

## Verify consent types

Map the client-approved policy to the current Google consent types required by each destination. Verify at least:

- `analytics_storage` for Analytics storage behavior;
- `ad_storage` for advertising storage behavior;
- `ad_user_data` for sending user data to Google for advertising;
- `ad_personalization` for personalized advertising.

Check any additional consent type or privacy setting against current official documentation. Do not assume that GA4 always needs only `analytics_storage`; advertising features can introduce additional requirements.

## Implement the default basic route

For basic behavior:

1. Verify how the CMP supplies the consent state.
2. Reuse a strict block when the CMP identity, native condition, event scope, denied-state policy, ownership, and expected change path are semantically compatible. Separate GA4, Google Ads, Floodlight, or linker blocks only when one of those dimensions or the selected consent route differs; do not duplicate an otherwise compatible block merely because the product label differs.
3. Make unknown, uninitialized, and denied state block.
4. Attach the applicable block to each Google config, event, conversion, remarketing, and linker execution unit only after verifying that every destination or consumer of that unit has a compatible basic policy.
5. Fire tags only after the required grant.
6. Confirm that no Google request is sent before consent under the approved basic policy.

Use names such as `Block - Didomi - GA4 denied` and `Block - Didomi - Google Ads denied`.

Built-in consent checks may remain visible, but the shared CMP block is the mechanism that enforces the default strict/basic non-fire policy.

## Implement advanced mode only when approved

For advanced behavior:

1. Use the CMP's supported GTM consent template when available and verified.
2. Fire consent-default logic on `Consent Initialization - All Pages` before affected Google tags.
3. Set the approved default states, normally denied where required by the client policy.
4. Send consent updates as soon as the user confirms or changes a choice and before a page transition.
5. Use the GTM consent template APIs rather than a Custom HTML `gtag('consent', ...)` workaround when implementing consent inside GTM.
6. Let Google tags use their documented built-in consent behavior.
7. Do not add additional consent requirements or exception triggers that block the denied-state pings the approved advanced design intends to send.
8. Configure region defaults, `wait_for_update`, ads data redaction, URL passthrough, or service-specific settings only when explicitly required and documented.

Do not silently convert an existing basic implementation to advanced mode merely because Google recommends or supports modeling.

Do not attach a blocking trigger that would suppress the denied-state behavior explicitly approved for Advanced Consent Mode.

## Keep tag behavior and page views separate

Consent defaults and updates do not justify an automatic page view. Keep `GA4 - Config` from sending a page view by default and use a separate `GA4 - Event - page_view` design.

Inspect Enhanced Measurement and browser-history page views independently. Consent Mode does not prevent duplicate automatic/manual events by itself.

## Configure every Google product consistently

Apply the selected product decision to each in-scope Google tag, GA4 tag, Google Ads conversion/remarketing tag, Floodlight tag, and Conversion Linker. Verify each tag's built-in checks, installed template settings, and denied-state behavior.

Different products may use different approved routes, but never mix a basic blocked product with an advanced product accidentally. Inventory shared destinations and helpers, require an explicit destination-by-destination decision and validation matrix, and split or block the design when one execution unit cannot satisfy every selected route.

## Define the Tag Assistant handoff

This configuration skill does not execute the full interactive runtime recette. Specify the following assertions for the GTM Preview recette workflow. If equivalent runtime evidence was not already supplied and verified, classify the affected configuration as `Needs runtime QA`, not `Complete`.

Verify:

- default consent is set before affected tags;
- every required consent type has the expected initial value;
- updates occur on the interaction page;
- revocation updates the state;
- basic mode sends no pre-consent Google request;
- advanced mode sends only the documented denied-state requests and no cookies/storage prohibited by the selected state;
- tags list the expected built-in and additional consent checks;
- page views and conversions are not duplicated after consent updates.

Record whether the result is `strict/basic blocked` or `advanced consent-aware`; do not collapse both into the label `consent gated`.

## Official entry points

- https://developers.google.com/tag-platform/security/concepts/consent-mode
- https://developers.google.com/tag-platform/security/guides/consent
- https://developers.google.com/tag-platform/security/guides/privacy
- https://support.google.com/tagmanager/answer/10718549
- https://developers.google.com/tag-platform/security/guides/consent-debugging
