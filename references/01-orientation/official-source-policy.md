# Official source policy

## Contents

- [Principle](#principle)
- [Evidence hierarchy by decision](#evidence-hierarchy-by-decision)
- [Research procedure](#research-procedure)
- [Research record](#research-record)
- [Official entry points](#official-entry-points)
- [Conflict and failure handling](#conflict-and-failure-handling)

## Principle

Use current primary documentation at execution time. Never rely on memory, analogy, an old implementation, or an informal media event label for a vendor event, parameter, type, array shape, accepted value, template field, consent capability, CMP event, CMP variable, or vendor identity.

Use the requirement to establish business intent. Use official documentation to establish the destination contract. Use the installed template, target-container state, approved source contract, and representative payloads to establish the static implementation. Runtime evidence is outside this skill and is not an input requirement.

## Evidence hierarchy by decision

| Decision | Primary authority |
| --- | --- |
| Analytics business meaning | Approved tracking plan or direct analytics requirement |
| Media business objective | Current media-team brief |
| Destination event and field schema | Current official platform documentation |
| GTM field implementation | Native/installed template documentation, version, and visible field definitions |
| Source values and timing | Approved dataLayer/source contract and representative payloads |
| Client consent policy | Analyst-provided approved policy |
| Product consent capability and denied-state behavior | Current official product documentation, installed template, approved policy, and target-container configuration |
| CMP signal, event lifecycle, and vendor identity | Current official CMP documentation plus the approved site/CMP signal contract and target-container state |
| Existing local architecture and reuse | Target container and workspace |

Treat unofficial articles and community examples as discovery aids only. Do not use them as the sole support for a required value or behavior. Do not let an existing tag override current official documentation.

## Research procedure

For each platform, product, and CMP involved:

1. Open the current official page that directly covers the selected browser implementation.
2. Confirm that the page applies to client-side web and the installed product/template version.
3. Extract the official event name, standard/custom/deprecated status, fields, requirement status, types, formats, enumerations, cardinality, and conditional rules.
4. For consent work, establish whether denied state blocks, holds, suppresses cookies, or transmits a documented limited payload; record storage, identifiers, data use, modeling, defaults, updates, and revocation.
5. Inspect the installed GTM template and map documentation concepts to its visible fields.
6. Establish source values, timing, state lifetime, and CMP signals from an approved contract and representative payload.
7. Assign the applicable evidence grade from the configuration contract and record the source URL, page title, access date, decisions, and unresolved contradictions.

Do not copy an event catalogue into the skill and treat it as permanent. Re-open the live catalogue for every implementation because vendors change standard events, parameters, requirements, templates, and consent features.

## Research record

Record for each configured tag:

- official URL, page title, and access date;
- browser/client-side product and installed template/version;
- official event name and classification;
- exact field names and required, recommended, optional, or conditional status;
- accepted type, format, enum, and cardinality;
- source dataLayer key or configuration value;
- source evidence grade and representative non-sensitive input;
- GTM variable and template field;
- transformation and representative resolved output;
- consent support, per-product classification, denied-state request/storage behavior, selected mode, and CMP mechanism;
- unresolved contradiction or unavailable evidence.

Keep these four layers distinct even when their labels look similar:

1. source dataLayer key;
2. GTM variable;
3. template UI field;
4. vendor request/payload parameter.

## Official entry points

Use these as search entry points, then follow the current page for the exact requested feature:

| Need | Official entry point |
| --- | --- |
| GTM tags, triggers, variables, workspaces, and consent | https://support.google.com/tagmanager/ |
| GTM dataLayer | https://developers.google.com/tag-platform/tag-manager/datalayer |
| GTM Data Layer Variable versions | https://support.google.com/tagmanager/answer/7683362 |
| GTM firing triggers, exceptions, and sequencing | https://support.google.com/tagmanager/answer/7679318 and https://support.google.com/tagmanager/answer/6238868 |
| GTM priority, schedule, live-only behavior, and tag firing options | https://support.google.com/tagmanager/answer/2772421 and https://developers.google.com/tag-platform/tag-manager/api/reference/rest/v2/accounts.containers.workspaces.tags |
| GTM API workspaces, synchronization, fingerprints, and mutations | https://developers.google.com/tag-platform/tag-manager/api/v2 and https://developers.google.com/tag-platform/tag-manager/api/reference/rest/v2/accounts.containers.workspaces/sync |
| GTM container export/import | https://support.google.com/tagmanager/answer/6106997 |
| GTM Community Template Gallery | https://support.google.com/tagmanager/answer/9454109 |
| GA4 events and ecommerce | https://developers.google.com/analytics/devguides/collection/ga4/reference/events and https://developers.google.com/analytics/devguides/collection/ga4/ecommerce |
| GA4 configuration fields and page views | https://developers.google.com/analytics/devguides/collection/ga4/reference/config and https://developers.google.com/analytics/devguides/collection/ga4/views |
| GA4 custom dimensions and metrics | https://support.google.com/analytics/answer/14240153 |
| Google tag settings variables | https://support.google.com/tagmanager/answer/13438166 and https://support.google.com/tagmanager/answer/13438771 |
| Google Consent Mode | https://developers.google.com/tag-platform/security/concepts/consent-mode and https://developers.google.com/tag-platform/security/guides/consent |
| Google Ads conversion and remarketing | https://support.google.com/google-ads/answer/7521212 and https://support.google.com/tagmanager/answer/6106009 |
| Google Ads dynamic remarketing schema | https://support.google.com/google-ads/answer/7305793 |
| Google Ads enhanced conversions | https://support.google.com/google-ads/answer/13262500 |
| Microsoft Advertising UET | https://learn.microsoft.com/en-us/advertising/msa-help/hlp_ba_conc_uetv2customevent and https://learn.microsoft.com/en-us/advertising/msa-help/hlp_ba_conc_uet_parameters_table |
| Microsoft UET Consent Mode and GTM template | https://learn.microsoft.com/en-us/advertising/msa-help/hlp_ba_conc_uet_consent and https://learn.microsoft.com/en-us/advertising/msa-help/hlp_ba_conc_uet_dynamicconsentgtm |
| Microsoft Clarity Consent Mode | https://learn.microsoft.com/en-us/clarity/setup-and-installation/consent-mode and https://learn.microsoft.com/en-us/clarity/setup-and-installation/cmp-integration-guide |
| Meta Pixel browser events | https://developers.facebook.com/docs/meta-pixel/reference/ |
| TikTok Pixel standard events, parameters, and GTM | https://ads.tiktok.com/help/article/standard-events-parameters and https://ads.tiktok.com/help/article/how-to-create-tiktok-event-tags-with-google-tag-manager |
| TikTok Pixel cookie-consent behavior | https://ads.tiktok.com/help/article/how-to-use-cookies-with-tiktok-pixel |
| Snap Pixel and GTM | https://developers.snap.com/marketing-api/Ads-API/snap-pixel and https://businesshelp.snapchat.com/articles/en_US/Knowledge/formatting-pixel |
| Matomo tracking versus cookie consent | https://developer.matomo.org/guides/tracking-consent |
| Piwik PRO anonymous consent mode | https://help.piwik.pro/support/privacy/setting-consent-manager/ |
| Didomi GTM events, variables, and integration | https://developers.didomi.io/cmp/web-sdk/third-parties/tags-management/events-and-variables and https://developers.didomi.io/cmp/web-sdk/third-parties/tags-management/tag-managers/google-tag-manager/configure-the-didomi-gtm-integration |

For any unlisted media platform, CMP, template, or supported feature, locate and cite its current official documentation before configuring it. Lack of a dedicated playbook never permits inference.

## Conflict and failure handling

When sources disagree:

1. Prefer the current official page that directly covers the selected browser feature.
2. Confirm template version and visible field behavior.
3. Confirm the approved source contract, installed template, and saved container fields.
4. Record the contradiction and its impact.
5. Stop the affected object as blocked if no authoritative source resolves a critical decision.

If an official site is temporarily unavailable, retry or use another official page for the same product. Do not replace unavailable critical documentation with memory or an unofficial tutorial.
