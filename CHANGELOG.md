# Changelog

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
