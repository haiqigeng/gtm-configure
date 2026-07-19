# Changelog

## 2026.7.18

### Why This Release Matters

- Separates analytics tracking-plan intake from media-team implementation briefs.
- Expands the skill from a GA4/Meta foundation into a scalable client-side
  analytics and media configuration system.
- Makes strict/basic consent blocking the default and advanced consent an
  explicit, evidence-backed exception.

### What Changed

- Add dedicated browser playbooks for Google Ads, Microsoft Advertising, Meta,
  TikTok, and Snapchat, plus a mandatory official-documentation fallback for
  every other media platform.
- Require field-level media mappings from business action through dataLayer,
  GTM variable, installed template field, and official destination parameter.
- Add Google basic/advanced Consent Mode architecture and vendor-native consent
  routing without conflating built-in checks with strict firing prevention.
- Expand advanced consent beyond GA4 with a per-product capability map covering
  the Google tag family, Microsoft Advertising UET, Microsoft Clarity,
  Matomo/Piwik PRO adaptive analytics, TikTok native cookie control, and strict
  fallbacks for products without proven denied-state behavior.
- Prefer one reusable CMP blocking trigger per vendor/platform and block
  unknown, uninitialized, and denied states by default.
- Require a valid once-per-page base/config initialization path after both an
  initial consent grant and a later grant; a blocked page-load trigger is not
  treated as if it retries automatically.
- Require blocking-trigger event scope to cover every consumer event, protect
  sequenced tags at the initiating tag, and distinguish revocation from
  unloading a script that already ran.
- Require direct native filtering of the CMP's documented vendor-state variable
  and prohibit speculative consent CJS, JavaScript, table, or Boolean helpers.
- Treat a CMP value outside its documented contract as a blocking integration
  defect rather than a runtime transformation requirement.
- Require every new GTM object to serve a current requirement or documented
  platform/template constraint, including base tags and manual page views.
- Reuse semantically equivalent Google product blocks; split them only when
  vendor identity, event scope, consent policy, ownership, or route differs.
- Reconcile destination-level consent choices with shared Google tag/linker
  execution units so incompatible basic and advanced routes are not claimed.
- Clarify that cross-vendor consent research does not add unsupported analytics
  tag-configuration routes.
- Keep configuration/base tags from sending page views by default while
  documenting vendor-specific inherent page-load exceptions.
- Add first-party user-data governance for enhanced conversions and advanced
  matching, with explicit approval, source, consent, normalization, and hashing
  requirements.
- Add data-contract, ecommerce-array, Custom JavaScript, Custom Event-first
  trigger, SPA, template-governance, and MCP/API/UI adapter references.
- Expand acceptance scenarios and release checks to protect the new contracts.
- Cross-check release versions and current-section notes, lint in CI, and prove
  exact deterministic runtime-archive contents.
- Include the MIT license in the distributable skill archive.

### What Users Should Do

- Provide a tracking plan or direct requirement for analytics work.
- Provide the media platform, requested business action, destination use, and
  available account/pixel/conversion details for media work.
- Expect the agent to reopen current official vendor and CMP documentation for
  every implementation.
- State explicitly when advanced consent or first-party user-data collection is
  approved; otherwise the skill uses strict/basic vendor blocking.
- Review the object and field-level change map before any separate publication.

### Validation

- Skill structure and direct reference routing are checked automatically.
- Critical analytics/media intake, consent, page-view, official-source,
  template, array, and deferred-scope contracts have regression checks.
- Forward tests cover a GA4/Didomi pre-CMP page view with event-scoped fields,
  mixed GA4 basic and Google Ads advanced consent on a shared Google tag,
  multi-item Meta/TikTok media mapping, an unlisted media vendor, and
  partial-failure handling in a dedicated workspace.
- Unit tests, Python compilation, deterministic package build, and whitespace
  checks are run before release.

### Known Limits

- The skill configures client-side web GTM only.
- Vendor event catalogues and parameter schemas are intentionally not frozen in
  the package; current official documentation is required at execution time.
- Server-side GTM, Conversions API, event-ID architecture, and browser/server
  deduplication remain deferred.
- Full GTM Preview, network, CMP journey, and vendor-diagnostics recette remains
  a separate workflow.

## 2026.7.13

### Why This Release Matters

- Establishes the first repository release for the GTM configuration skill.
- Makes the utility contract explicit for expert web analysts using AI agents.

### What Changed

- Structure the skill into orientation, execution, and judgement layers.
- Add explicit audience, objective, use cases, flexible-input, output, workspace,
  authority, and boundary contracts.
- Add dedicated-workspace preference and approved Default Workspace fallback.
- Keep server-side GTM and deduplication as deferred future capabilities rather
  than permanent exclusions.
- Add repository README, release metadata, release checks, package building,
  CI, contribution guidance, and security guidance.

### What Users Should Do

- Load "SKILL.md" as the runtime entrypoint.
- Provide a tracking-plan row or direct human requirement.
- Allow the agent to discover missing container, template, CMP, and runtime
  evidence when the selected route needs it.
- Review the object-level change map before publication.

### Validation

- Skill frontmatter validator passed.
- Orientation, execution, and judgement structure check passed.
- Required references, direct routes, and repository metadata check passed.
- Runtime package build and unit checks are run before the release is published.

### Known Limits

- V1 configures client-side GTM only.
- Server-side GTM, Conversions API, browser/server deduplication, and related
  routing are deferred to a later version of this same skill.
- Full interactive GTM Preview recette remains a separate workflow.
