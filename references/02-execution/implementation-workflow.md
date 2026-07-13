# Implementation workflow

## 1. Orient the request

Read the utility contract and classify:

- target container, account, workspace, and environment;
- direct human requirement versus tracking-plan input;
- read-only, planning, or authorized mutation;
- analytics, media, CMP, or combined scope;
- current V1 work versus deferred server-side/deduplication capability.

Do not mutate when the request is only for analysis or planning.

## 2. Resolve the workspace

For an authorized change:

1. Find a dedicated workspace already assigned to the same requirement.
2. If none exists, create a dedicated implementation workspace when permitted.
3. Record the workspace name/ID and scope.
4. Do not use the Default Workspace unless a dedicated workspace is unavailable and the analyst has approved that fallback.

Do not create a workspace merely for a read-only review.

## 3. Form the implementation contract

Extract:

- business action and expected outcome;
- vendor-neutral dataLayer event;
- source fields, types, cardinality, timing, and sample values;
- destination vendor, template, official event, and fields;
- consent policy, CMP, vendor identity, and denied behavior;
- acceptance criteria and runtime tests still needed.

Accept a direct human requirement as a valid source. If a tracking plan and human instruction conflict, expose the conflict and ask which intent governs.

Classify missing information as:

- discoverable from the container, docs, template, or runtime;
- conditional and not needed for the selected route;
- critical and blocking because it cannot be derived safely.

## 4. Inspect before designing

Inventory relevant tags, triggers, exception/blocking triggers, variables, settings variables, folders, templates, and CMP integrations.

Capture:

- object type, name, folder, and references;
- resolved value or transformation output;
- tag-template and event settings;
- firing triggers, exception triggers, and built-in consent settings;
- existing consumers and semantic purpose.

Compare semantics, not names alone. Detect duplicate automatic/manual measurement, competing consent mechanisms, and reusable constants or mappings.

## 5. Research official requirements

Read the current official documentation for every selected platform and CMP. Verify:

- official event and parameter names;
- required and optional fields;
- types, formats, enumerations, and cardinality;
- tag-template configuration fields;
- CMP event frequency, state variables, vendor identity, and value format.

Use runtime evidence to verify actual site timing and values. Do not replace a missing official requirement with memory, an unofficial example, or an existing imperfect tag.

## 6. Design the object graph

Default to:

- one vendor-neutral Custom Event trigger per business action;
- destination-specific tags consuming that event;
- reusable vendor blocking triggers when strict blocking is the approved policy;
- direct variables or constants where they are clearer;
- lookup tables only for real deterministic multi-scenario mappings;
- Custom JavaScript only for a necessary, documented transformation.

For page views, explicitly design CMP timing and automatic/manual duplicate prevention.

Read the relevant analytics, media, CMP, and naming references before finalizing the graph.

## 7. Mutate only the approved scope

Use a purpose-built GTM MCP or API when available. Use the UI only for unavailable API operations or visual verification.

Create or modify only the approved workspace objects. Verify each saved object, preserve unrelated changes, and record every created, modified, reused, and untouched object.

Do not publish or create a GTM version.

## 8. Handoff

Apply the acceptance and handoff reference. Separate:

- configuration verified from documentation and object state;
- runtime tests still required;
- unresolved blockers;
- deferred future server-side or deduplication capability.

If the GTM MCP/API is unavailable, provide the complete object specification and state that no live configuration was changed.
