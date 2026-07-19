# Configure GTM

An agent-neutral skill for expert web analysts using Codex, Claude, or another capable AI agent to create and modify clean, reusable, officially documented, and consent-controlled client-side Google Tag Manager configurations.

## Who It Serves

- Expert web analysts and analytics consultants.
- GTM specialists configuring the supported analytics and browser media platforms.
- Analysts translating an approved analytics tracking plan, direct requirement, or media-team brief into GTM objects.
- AI agents that can use a GTM MCP, API, export, or signed-in UI.

## Utility Objective

Convert an approved implementation requirement into a traceable client-side GTM configuration. Preserve business intent, validate every destination schema against current official documentation, reuse compatible objects, apply explicit consent behavior, and report exactly what changed.

Use different requirement authorities:

- For analytics, use the tracking plan or direct analytics requirement as the primary business input.
- For media, use the human media-team brief as the primary business input. Use a tracking plan only to discover reusable source events and values.

The objective is implementation quality and traceability, not legal advice or a claim of legal compliance.

## Current Client-Side Use Cases

- Create or modify tags, normal triggers, blocking triggers, variables, settings variables, and transformations.
- Configure Google tag and GA4 events.
- Configure Google Ads conversions, remarketing, dynamic remarketing, and explicitly approved enhanced conversions.
- Configure Microsoft Advertising UET, Meta Pixel, TikTok Pixel, and Snap Pixel browser tags.
- Configure another browser media vendor by researching its current official documentation.
- Implement strict/basic CMP blocking by default.
- Implement product-specific Google, Microsoft, or vendor-native advanced/cookieless/anonymous consent only when explicitly requested, approved, and officially documented.
- Validate the available dataLayer contract and produce missing-data requirements without developing the site.

## Inputs

Inputs can be supplied by the analyst, discovered by the agent, or required only for the chosen route. They do not all need to exist at intake.

- Analytics tracking-plan row or direct analytics requirement.
- Media-team brief: platform, business action, destination use, and available account/pixel/conversion identifiers.
- Target account, web container, environment, workspace, and mutation authority.
- Existing tags, triggers, variables, templates, folders, and workspace state.
- Current official platform, template, and CMP documentation.
- dataLayer event, fields, types, cardinality, timing, and representative payloads.
- CMP state and client-approved basic/strict or advanced consent policy.
- Conditional feed, catalog, conversion-label, user-data, or environment details.

The agent should derive safe values and block only when a critical authorization, business, destination, data, template, or consent decision cannot be established.

## Outputs

For authorized configuration, return:

- changes in a dedicated workspace whenever possible;
- target account, container, environment, and workspace;
- requirement-to-object and field-level source-to-destination maps;
- created, modified, reused, and intentionally untouched objects;
- template identity/version and relevant permissions;
- official source URLs, titles, access dates, and decisions;
- normal triggers and final consent behavior per browser product/vendor;
- static validation, blockers, deferred capabilities, and remaining runtime QA;
- confirmation that no publication or GTM version occurred.

For planning, read-only, unavailable-tool, or blocked work, return the same object-level specification without claiming live changes.

## Workflow Architecture

The runtime package has three layers:

1. Orientation defines utility, requirement authority, inputs/outputs, boundaries, and official-source policy.
2. Execution defines workspace handling, analytics/media branching, data contracts, consent architecture, platform playbooks, templates, tools, naming, and mutation.
3. Judgement defines acceptance, status, consent proof, handoff, and runtime-QA boundaries.

`SKILL.md` routes directly to every reference so an agent loads only the applicable platform and feature files.

## Key Defaults

- Use vendor-neutral dataLayer Custom Events for business actions.
- Use a dedicated workspace and avoid the Default Workspace.
- Use relative GTM references rather than repeated hard-coded IDs or values when they improve clarity.
- Create an object only for a current requirement or documented platform/template constraint; prefer a direct field or DLV over a helper variable.
- Keep config/base tags from sending an automatic page view by default; implement page view separately unless a vendor has a documented inherent exception.
- Use one reusable CMP blocking trigger per vendor/platform for strict/basic gating.
- Make unknown, uninitialized, and denied consent block.
- Make each block's event scope cover every consumer firing path, and gate any tag sequence at its initiating tag.
- Test the CMP's documented vendor-state variable directly through one native negative blocking condition. Do not create a consent CJS, JavaScript, table, or Boolean helper; block an unsupported CMP contract instead.
- Treat revocation as a separate vendor-behavior decision; a GTM block does not unload a script that already ran.
- Classify consent per browser product; use advanced/native consent and first-party user-data features only after explicit approval and official denied-state proof.
- Reconcile per-product consent choices with shared Google tags and helpers; one execution unit cannot carry incompatible basic and advanced policies.
- Preserve every ecommerce item and exact vendor array/object shape.
- Never publish or create a GTM version.

## Official Documentation Policy

The playbooks contain stable research and decision procedures, not frozen event catalogues. For every implementation, reopen the current official vendor pages and installed template. Record exact event/field requirements, types, shapes, consent behavior, source mapping, and access date.

If a platform has no dedicated playbook, research its official browser implementation, event, parameter, consent, matching, and template documentation before configuration. Never infer one vendor's schema from GA4 or another media platform.

## Workspace And Mutation Policy

For authorized changes, reuse a compatible dedicated workspace or create one when possible. Explain the constraint and obtain approval before using the Default Workspace.

Prefer a connected GTM MCP, then the GTM API. Use the UI for unsupported operations or visual verification. Re-read every saved object and preserve unrelated work.

## Boundaries

This skill does not create tracking plans, develop the website/dataLayer, audit or clean containers, run a full interactive GTM Preview recette, make legal consent decisions, configure advertising-platform settings without separate authorization, publish, or create GTM versions.

Server-side GTM, Conversions API, browser/server deduplication, and event-ID architecture remain future extensions of this skill. They are deferred current-scope capabilities, not permanent exclusions.

The vendor consent-capability map does not add analytics implementation support beyond Google tag/GA4. Its Matomo and Piwik PRO entries are classification references only in this release.

## Repository Map

- `SKILL.md`: runtime entrypoint and direct routing.
- `agents/openai.yaml`: OpenAI interface metadata.
- `references/01-orientation/`: utility and evidence authority.
- `references/02-execution/`: workflow, platform, consent, data, template, tool, and naming rules.
- `references/03-judgement/`: acceptance and handoff.
- `scripts/check_release.py`: dependency-free structure/content checks.
- `scripts/build_skill_package.py`: deterministic runtime archive.
- `tests/`: regression checks for release tooling and critical skill contracts.

## Related Skills

- GA4 tracking-plan skill: create or review the measurement plan.
- GTM container audit/cleanup skill: inspect hygiene, correctness, and cleanup.
- GTM Preview recette skill: execute interactive runtime validation.

## Install The Skill

Copy runtime files `SKILL.md`, `agents/`, and `references/` into the target agent's supported skill directory. Keep `LICENSE` with redistributed copies. Repository metadata, tests, and release tooling are not required at runtime.

## Release Checks

Run:

~~~powershell
python -m pip install -e ".[dev]"
python -m ruff format --no-cache --check scripts tests
python -m ruff check --no-cache scripts tests
python scripts/check_release.py --tag v2026.7.18 --release-notes CHANGELOG.md
python -m unittest discover -s tests -v
python -m compileall -q scripts
python scripts/build_skill_package.py --output dist/configure-gtm-v2026.7.18.zip
git diff --check
~~~

Releases use calendar versioning: `vYYYY.M.D` with an optional `.N` suffix for same-day follow-ups.
