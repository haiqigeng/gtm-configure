# CMP platform patterns

## Contents

- [Purpose](#purpose)
- [Common state contract](#common-state-contract)
- [OneTrust](#onetrust)
- [Cookiebot](#cookiebot)
- [Didomi](#didomi)
- [Other CMPs](#other-cmps)
- [Saved-state acceptance](#saved-state-acceptance)

## Purpose

Use this reference after identifying the actual CMP product, deployment path, template/version, and
client-approved category/vendor/purpose policy. These patterns reduce repeated discovery but never
replace current official CMP documentation or legal decisions.

## Common state contract

For every CMP, establish from current documentation and container evidence:

- earliest initialization/default point;
- documented readiness and change events;
- exact category, vendor, purpose, or product state variable;
- unknown/uninitialized/undefined representation;
- initial grant, denial, later grant, repeated readiness/change, and revocation;
- page-to-page and SPA lifetime;
- template fields, permissions, defaults, and Google consent mapping when used.

For strict/basic gating, use the documented state variable directly and make every non-granted
state block. Independent required grants use OR-denial across the smallest reusable set of blocks.
Do not create a generic consent Custom JavaScript helper.

## OneTrust

Open the current OneTrust GTM and Google Consent Mode documentation. Inspect the deployed OneTrust
script/template version and the site's actual category IDs. Confirm current documented dataLayer
events and state variables rather than copying example category values from another client.

Official entry points:

- https://my.onetrust.com/articles/en_US/Knowledge/UUID-301b21c8-a73a-05e8-175a-36c9036728dc
- https://my.onetrust.com/articles/en_US/Knowledge/UUID-d81787f6-685c-2262-36c3-5f1f3369e2a7

Reconcile auto-blocking, site-deployed scripts, the CMP template, GTM additional-consent checks, and
manual blocking. Do not create parallel default/update paths. Treat region mappings and category
ownership as approved CMP inputs.

## Cookiebot

Inspect the current Cookiebot CMP gallery template, Domain Group ID, Consent Initialization setup,
default regions, consent-type mapping, and documented update event. Determine whether the CMP is
site-deployed or GTM-deployed and prevent duplicate initialization.

Official entry points:

- https://support.cookiebot.com/hc/en-us/articles/360003793854-Google-Tag-Manager-deployment
- https://support.cookiebot.com/hc/en-us/articles/360016047000-Cookiebot-and-Google-Consent-Mode

Do not infer that built-in consent checks satisfy the client's strict/basic policy. Attach additional
blocking when required, or implement an explicitly approved advanced route without a defeating
block.

## Didomi

Inspect the current Didomi web SDK, direct-site versus GTM deployment, documented readiness/change
events, vendor/purpose variables, and exact vendor identifiers. Prefer documented Didomi state
variables and events; do not parse a consent string with custom code when a direct variable exists.

Official entry points:

- https://developers.didomi.io/cmp/web-sdk/third-parties/tags-management/events-and-variables
- https://developers.didomi.io/cmp/web-sdk/third-parties/tags-management/tag-managers/google-tag-manager/configure-the-didomi-gtm-integration

Prove that a vendor grant includes every required purpose when the client's policy requires both.
Keep readiness and change triggers repeatable only where the consumer must become eligible after a
later grant.

## Other CMPs

For Axeptio, Commanders Act/TrustCommander, Usercentrics, Quantcast, or another CMP, follow the same
state contract. Locate current official GTM and consent documentation, inspect the installed
template, and record exact events and variables. If current primary evidence cannot establish a
critical grant or lifecycle rule, block the affected tag rather than borrowing a OneTrust,
Cookiebot, or Didomi pattern.

## Saved-state acceptance

Complete the consent truth table in the handoff reference. Read back every CMP tag, default/update
setting, normal trigger, exception/additional-consent check, predicate, event scope, firing option,
and consumer. Confirm that unknown and denial fail closed for basic routes, explicit advanced routes
remain unblocked as designed, repeated events cannot duplicate initialization, and revocation does
not receive an unsupported static guarantee.
