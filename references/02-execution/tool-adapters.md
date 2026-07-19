# Tool adapters

## Use a capability-first execution order

Prefer:

1. a purpose-built GTM MCP connected to the correct Google account;
2. the GTM API with appropriate container/workspace access;
3. a complete container export for read-only design or import-ready specification;
4. the signed-in GTM UI for unavailable operations or visual verification;
5. an object-level implementation specification when no mutation path is available.

Do not open a browser merely because one exists when a connected semantic GTM tool can perform and verify the operation. Do not claim a mutation from an export-only or read-only source.

## Establish tool capabilities before mutation

Confirm whether the selected adapter can:

- list accounts, containers, workspaces, versions, and permissions;
- create/reuse a dedicated workspace;
- read, create, and modify tags, triggers, variables, folders, and templates;
- expose built-in/additional consent settings and blocking triggers;
- inspect references/consumers and workspace conflicts;
- re-read saved objects;
- avoid version creation and publication.

Use the UI only for missing semantic fields, unsupported template operations, or visual confirmation. Keep the same target account/container/workspace across adapters.

## Apply read-before-write discipline

For every adapter:

1. Resolve the target by stable account/container/workspace ID, not display name alone.
2. Read current object state and conflicts.
3. Design the complete dependency graph.
4. Create dependencies before consumers.
5. Re-read every mutation and compare intended versus stored fields.
6. Record returned IDs and fingerprints/version identifiers where available.
7. Stop on a conflict or unexpected consumer rather than overwriting silently.

Never use a guessed template type code or API parameter. Derive it from the existing object, API schema, official template, or tool response.

## Handle partial failure

If a mutation fails:

- stop dependent writes;
- inventory which objects were created or changed;
- do not delete or roll back unrelated user work;
- repair only the objects created or changed by the current authorized operation when safe;
- restore a modified pre-existing object only when its exact pre-change state was captured and restoration remains within the authorized operation; otherwise preserve the partial state and report it;
- remove an object only when the current authorization explicitly includes rollback or deletion and its ownership is confirmed;
- report the partial state and exact blocker.

Do not publish to make an API/MCP change visible.

## Use export/import safely

Treat an export as complete evidence only when it includes all relevant tags, triggers, variables, templates, folders, consent settings, and references from the intended workspace/version.

For an import-ready specification, preserve container/object schema and clearly distinguish create, merge, overwrite, and delete behavior. Do not import automatically when the analyst authorized only configuration design.

## Use the UI as a controlled fallback

When UI work is required:

- verify the signed-in Google account and container ID before each mutation batch;
- select the dedicated workspace explicitly;
- inspect visible template and consent fields;
- save one logical object at a time and re-open it;
- never click Submit, Publish, or Create Version;
- record any UI-only field that the semantic adapter could not verify.

## Return a specification when blocked

If authentication, permissions, tool availability, or workspace limits prevent mutation, provide:

- exact object type and name;
- complete configuration fields;
- normal and blocking trigger references;
- dependencies and creation order;
- official source evidence;
- validation and acceptance matrix;
- explicit statement that no live GTM object changed.
