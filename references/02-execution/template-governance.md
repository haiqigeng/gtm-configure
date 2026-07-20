# Template governance

## Choose the safest supported implementation

Use this preference order when it satisfies current official vendor requirements:

1. GTM native/built-in tag template;
2. current official vendor-published template;
3. reviewed Community Template Gallery template;
4. approved organization-owned custom template;
5. Custom HTML or Custom Image only when no suitable template exists and the vendor officially documents that route.

Do not assume that a Community Template Gallery entry is endorsed by Google. Verify publisher and repository independently.

## Inspect before adding or updating

Record:

- template name, type, publisher, repository, and documentation;
- installed version/commit or available version evidence;
- requested permissions and allowed domains/global variables/cookies/storage;
- field names, defaults, required fields, and hidden automatic behavior;
- consent APIs/checks and automatic matching/event behavior;
- existing tags that consume the template;
- container/zone type restrictions, boundaries, and linked-container ownership when Zones are present;
- update diff and changed permissions when an update is available.

Do not add or update a template as an incidental side effect. Obtain approval when installation, update, or new permissions materially expand execution or data access.

## Map documentation to the installed fields

Keep the official destination parameter separate from the template UI label. Confirm that the installed template actually supports every required field and current schema.

If official vendor documentation and the installed template disagree:

1. check the template version and official repository/release notes;
2. inspect field code/permissions when accessible;
3. check whether a native/newer template supersedes it;
4. block the affected implementation if no authoritative mapping exists.

Do not force an official parameter into an unrelated custom-field slot.

## Avoid Custom HTML for consent and native products

Do not use Custom HTML to set GTM consent state when a verified CMP/consent template can use the GTM consent APIs. Do not reimplement Google Analytics, Google Ads, Floodlight, or another natively supported tag in Custom HTML without a documented requirement and approval.

When Custom HTML/Image is unavoidable, document script/pixel source, execution timing, selected consent mechanism and denied-state behavior, CSP impact, failure behavior, and the reason no supported template fits.

Do not modify Zones, linked containers, allow/block restrictions, or container security policy as an incidental configuration step. Record a restriction that prevents the requested tag as an external dependency or blocker unless that exact control is separately authorized.

## Verify after mutation

Re-read the saved tag and template. Confirm:

- template identity/version did not change unexpectedly;
- every field is stored in the intended type/shape;
- permissions remain within the approved scope;
- automatic events or matching features remain disabled unless explicitly selected;
- consent settings and triggers reference the intended objects.

Record the template in the handoff even when no template change occurred.

## Official entry points

- https://support.google.com/tagmanager/answer/9454109
- https://developers.google.com/tag-platform/tag-manager/templates
- https://developers.google.com/tag-platform/tag-manager/templates/permissions
- https://support.google.com/tagmanager/answer/7647043
