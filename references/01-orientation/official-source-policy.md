# Official source policy

## Principle

Use current, primary documentation to determine configuration requirements. Never rely on memory or inference for a vendor event name, parameter name, supported value, item schema, tag-template field, consent requirement, CMP event, CMP variable, or vendor identifier.

Use the requirement/tracking plan to understand what the business wants to measure. Use official documentation to determine how the destination platform accepts it.

## Evidence hierarchy

Use the following sources for their appropriate purpose:

1. The approved requirement or tracking plan: business intent, event timing, required reporting outcome.
2. Current official Google, vendor, and CMP documentation: protocol and product configuration semantics.
3. The existing target container: current local configuration and reusable objects.
4. Live GTM Preview, dataLayer, cookies, or site source: actual event order, field values, and CMP runtime state.
5. Unofficial articles or community examples: background only; never the sole basis for a required configuration value.

Do not let an existing tag override current official documentation. It may be incomplete, obsolete, or misconfigured.

## Research record

For every platform-specific configuration, capture in work notes:

- official URL and page title;
- access date;
- exact event and parameter/field names used;
- allowed type, format, and cardinality;
- required versus optional status;
- source field and any transformation;
- tag template/version constraints, if applicable;
- unresolved contradiction between documentation and runtime data.

Stop and report a blocker if official documentation is unavailable or does not establish a critical field's behavior. Do not fill the gap with a plausible-looking value.

## Source entry points

Use the current page that directly documents the feature being configured, starting from these official sources:

| Need | Official source |
| --- | --- |
| GTM tag, trigger, variable, consent, and Google tag behavior | https://support.google.com/tagmanager/ |
| GA4 web collection, events, parameters, and configuration | https://developers.google.com/analytics/devguides/collection/ga4 |
| Google tag settings variables | https://support.google.com/tagmanager/answer/13438166 |
| Meta Pixel/browser event requirements and parameters | https://developers.facebook.com/docs/meta-pixel/reference/ |
| Didomi GTM integration, dataLayer events, and variables | https://developers.didomi.io/cmp/web-sdk/third-parties/tags-management/ |

These links are entry points, not frozen implementation rules. Follow the current official documentation for the exact vendor, tag type, event, and version in the request.

## Resolve conflicts explicitly

When sources disagree:

1. Prefer the current official page that directly covers the feature.
2. Inspect the installed GTM template and live runtime shape.
3. Document the contradiction and its impact.
4. Ask for direction if no official source resolves it.

For CMP configuration, never assume that a dataLayer event and a similarly named dataLayer variable have the same role. Verify each independently in the CMP's official documentation and in the site's runtime data.
