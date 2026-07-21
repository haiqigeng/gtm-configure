# Tracking-plan fidelity and conformance

## Contents

- [Keep measurement design outside configuration](#keep-measurement-design-outside-configuration)
- [Separate the collection and implementation contracts](#separate-the-collection-and-implementation-contracts)
- [Normalize the approved scope](#normalize-the-approved-scope)
- [Classify documentation discrepancies](#classify-documentation-discrepancies)
- [Resolve discrepancies before mutation](#resolve-discrepancies-before-mutation)
- [Prove contract conformance](#prove-contract-conformance)
- [Use the deterministic comparator](#use-the-deterministic-comparator)

## Keep measurement design outside configuration

For the analytics tracking-plan route, implement the approved tracking plan faithfully. Do not
rename an event, substitute a recommended event, add or remove a parameter, add a literal, change
the business success moment, or broaden scope because another design appears more optimal.

The tracking-plan analyst or tracking-plan skill owns measurement design and optimization. This
skill owns technical validation, GTM design, authorized mutation, and static verification. A later
explicit analyst decision can amend the approved input; record that decision before using it.

Use current official documentation to validate the approved collection contract and guide its GTM
implementation. Documentation can establish that a requested event or field is invalid, reserved,
deprecated, required, optional, recommended, typed differently, or unsupported by the selected
template. Documentation does not authorize this skill to rewrite the approved analytics contract.

Apply the same fidelity rule to a direct analytics requirement once the analyst has explicitly
approved its event, fields, source event, and business timing. When a direct request supplies only
an informal business action, present the documented choices and obtain an exact analytics decision
instead of silently designing the measurement plan.

The media route remains separate. A media-team brief establishes the media objective, while current
official media documentation establishes the destination event and payload schema.

## Separate the collection and implementation contracts

Treat these as the authorized **collection contract**:

- included business requirements and explicitly excluded source items;
- destination event name and classification selected by the approved analytics input;
- outgoing event, item, user-property, and other payload fields;
- approved literals, source paths, transformations, and null behavior;
- source event, business success moment, repeatability, and business filters.

Treat these as the **implementation contract** when they do not change collection semantics:

- account, container, workspace, destination identity, tag type, and installed template;
- GTM variables, Data Layer Variable version, folders, and object references;
- firing and blocking triggers that reproduce the approved source event and business timing;
- consent settings, firing options, sequencing, priority, and documented template mechanics;
- fingerprints, adapter actions, pagination, mutation order, and saved-state verification.

Official documentation and confirmed container evidence may establish implementation facts. They
may not add a destination payload field or business condition absent from the approved collection
contract. When official documentation requires such a field, record a blocking discrepancy rather
than inventing it.

## Normalize the approved scope

Before designing GTM objects, create a source-scope manifest that records every relevant workbook
sheet, table, row group, or supplied requirement as:

- `included`, with its stable requirement ID and source reference;
- `reference-only`, such as a dictionary, guide, or example;
- `excluded`, with the approved reason;
- `ambiguous`, with the exact decision required.

Visibility is evidence, not authority. Do not automatically exclude a hidden sheet or implement a
visible sheet. Do not silently import stale, duplicate, foreign-client, or illustrative content.
Block only the ambiguous requirements when the remaining scope is independently safe to configure.

Normalize each included requirement into an adapter-neutral record before container mutation. Keep
client-specific workbook interpretation with the capable agent; do not use a universal spreadsheet
parser to guess semantics. Preserve source sheet/cell or row references so the normalized record can
be reviewed against the approved input.

## Classify documentation discrepancies

Record one of these outcomes for every apparent plan/documentation difference:

| Class | Meaning | Required behavior |
| --- | --- | --- |
| `blocking-error` | The requested collection is invalid, reserved, missing a required field, type/shape incompatible, unsupported, or impossible to map safely. | Do not mutate the affected requirement. Present the exact evidence and decision needed. |
| `advisory` | The approved collection remains technically valid, but current documentation indicates a recommended event, parameter, or more appropriate analytics convention. | Report before mutation and preserve the approved contract by default. Do not substitute or enrich it. |
| `implementation-note` | Documentation determines a GTM/template setting without changing the collection contract. | Apply it within the authorized implementation scope and record the evidence. |

Do not misclassify an optional or recommended destination field as required. Do not downgrade a
required-field or reserved-name conflict to an advisory merely to complete the configuration.

## Resolve discrepancies before mutation

Produce a concise preflight discrepancy report before the first write. Include the requirement ID,
approved value, documented finding, class, impact, official source, and default action.

- Continue unchanged for a documented advisory unless the analyst explicitly amends the approved
  input.
- Stop the affected requirement for a blocking error until the analyst supplies a corrected plan or
  explicit approved decision.
- Continue unaffected requirements only when they have independent dependencies and mutation cannot
  leave a misleading or conflicting partial implementation.
- Repeat unresolved discrepancies in the handoff. If a discrepancy appears only after a saved-state
  readback, stop dependent writes and apply the partial-failure contract.

## Prove contract conformance

Before mutation, compare the normalized approved collection contract with the intended tag contract.
After mutation, compare it again with authoritative current-workspace readback. Require:

- identical included requirement IDs;
- identical destination and source event names;
- identical business timing and filters;
- exact parameter/property/item-field set equality;
- exact approved source or literal for every outgoing field;
- zero unauthorized additions, removals, substitutions, or hidden-scope inclusions.

Keep implementation infrastructure in a separate manifest. Necessary IDs, consent settings, GTM
references, and template mechanics are not unauthorized payload enrichment, but each still needs a
current requirement or documented implementation constraint.

A zero-difference result may proceed without a separate approval table. Any non-zero semantic
difference must be corrected, classified as a blocking discrepancy, or supported by a new explicit
approved decision before the affected write.

## Use the deterministic comparator

Use `scripts/validate_contract_conformance.py` when the approved, intended, or saved contracts can be
represented as normalized JSON. The agent remains responsible for interpreting the source artifact;
the script only performs deterministic equality checks.

Each JSON document must contain:

- `scope`, normally with `included`, `reference_only`, and `excluded` collections;
- `requirements`, a list of unique objects containing a stable string `id`;
- collection-semantic fields inside each requirement, with `parameters` represented as a mapping
  when parameter order is irrelevant.

Requirement and scope-list order is non-semantic. Nested arrays inside a requirement remain
order-sensitive so the comparator cannot hide reordered transformation steps or other sequences.

Repository or adapter metadata may live outside `scope` and `requirements`; the comparator ignores
that implementation metadata deliberately.

Run it before and after mutation:

~~~powershell
python scripts/validate_contract_conformance.py --approved approved.json --candidate intended.json
python scripts/validate_contract_conformance.py --approved approved.json --candidate saved.json
~~~

Exit code `0` means exact conformance, `1` means a deterministic difference, and `2` means an invalid
input or invocation. Preserve the JSON report in the technical handoff.
