# Configure GTM

An agent-neutral skill for expert web analysts who use Codex, Claude, or
another AI agent to create and modify clean, reusable, officially documented,
and consent-gated Google Tag Manager configurations.

## Who It Serves

- Expert web analysts and analytics consultants.
- GTM specialists configuring analytics and media platforms.
- Analysts translating an approved tracking plan or direct human requirement
  into GTM objects.
- AI agents that can follow Markdown skills and use a GTM MCP, API, export, or
  UI.

## Utility Objective

Convert an approved tracking plan or direct human measurement requirement into
a traceable client-side GTM configuration. The skill preserves business
intent, validates platform schemas against current official documentation,
reuses compatible objects, applies explicit consent gates, and reports what was
created or changed.

The objective is implementation quality and traceability. The skill does not
claim to make legal decisions.

## V1 Use Cases

- Create tags, triggers, variables, settings variables, and transformations.
- Modify existing GTM objects for a new or changed requirement.
- Configure analytics tags, including Google tag and GA4 events.
- Configure client-side media tags and vendor-specific payload transformations.
- Implement or adjust CMP consent gates.

## Inputs

Inputs may be supplied by the analyst, discovered by the agent, or conditional
to the selected route. They do not all need to be available at intake.

- Human requirement or tracking-plan row.
- Target container, account, environment, and requested scope.
- Existing tags, triggers, variables, templates, folders, and workspace state.
- Current official platform and CMP documentation.
- Runtime dataLayer, CMP, preview, or site evidence when timing or data shape
  matters.
- Sample payloads, vendor IDs, template versions, or mappings when required.

The agent should discover safely derivable information and block only when a
critical authorization, business, schema, or consent decision cannot be
established.

## Outputs

For an authorized request, the output is:

- configuration in a dedicated workspace whenever possible;
- the container, environment, and workspace used;
- a requirement-to-object map;
- created, modified, reused, and intentionally untouched objects;
- official sources and platform decisions;
- final firing and consent-gating behavior;
- validation results, blockers, deferred capabilities, and remaining runtime QA;
- confirmation that no publication occurred.

For planning, read-only, or blocked work, return the same object-level
specification without claiming that live changes were made.

## Workflow Architecture

The package follows three explicit layers:

1. Orientation defines audience, objective, inputs, outputs, authority, workspace
   policy, and boundaries.
2. Execution defines workspace handling, inspection, documentation research,
   object design, mutation, and handoff.
3. Judgement defines completion, blocked/deferred statuses, acceptance
   criteria, consent proof, and runtime-QA boundaries.

Start at "SKILL.md", then load only the relevant reference files.

## Workspace And Mutation Policy

For authorized changes, reuse a dedicated workspace with the same scope or
create one when possible. Avoid the Default Workspace. If a dedicated
workspace cannot be created or reused, explain why and obtain approval before
using the Default Workspace.

Never publish or create a GTM version as part of this skill.

## Boundaries

This skill does not create or redesign tracking plans, develop the website or
dataLayer, audit or clean containers, run full interactive GTM Preview recette,
make legal consent decisions, or publish GTM.

Server-side GTM, Conversions API, browser/server deduplication, and related
routing are future extensions of this same skill. They are deferred in V1, not
permanent exclusions.

## Repository Map

- "SKILL.md": runtime entrypoint and routing.
- "agents/openai.yaml": optional OpenAI interface metadata.
- "references/01-orientation/": utility and source authority.
- "references/02-execution/": workflow and conditional domain rules.
- "references/03-judgement/": acceptance and handoff.
- "scripts/check_release.py": dependency-free package/release checks.
- "scripts/build_skill_package.py": deterministic runtime skill archive.
- "tests/": regression checks for repository tooling.

## Related Skills

- GA4 tracking-plan skill: create or review the measurement plan.
- GTM container audit/cleanup skill: inspect hygiene, logic, and cleanup.
- GTM Preview recette skill: execute interactive runtime validation.

## Install The Skill

Copy the runtime files "SKILL.md", "agents/", and "references/" into the
target agent's supported skill directory. The repository-level README,
release tooling, tests, and metadata are not required at runtime.

## Release Checks

Run:

~~~powershell
python scripts/check_release.py --tag v2026.7.13 --release-notes CHANGELOG.md
python -m unittest discover -s tests -v
python -m compileall -q scripts
python scripts/build_skill_package.py --output dist/configure-gtm-v2026.7.13.zip
git diff --check
~~~

Releases use calendar versioning: "vYYYY.MM.DD" with an optional ".N"
suffix for same-day follow-ups.
