from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


class SkillContractTest(unittest.TestCase):
    def test_openai_interface_metadata_matches_north_star(self) -> None:
        metadata = read("agents/openai.yaml")
        self.assertIn('display_name: "Configure Google Tag Manager"', metadata)
        self.assertIn('default_prompt: "Use $configure-gtm', metadata)
        short_line = next(line for line in metadata.splitlines() if "short_description:" in line)
        short_description = short_line.split('"', 2)[1]
        self.assertGreaterEqual(len(short_description), 25)
        self.assertLessEqual(len(short_description), 64)

    def test_entrypoint_routes_the_configuration_contract(self) -> None:
        skill = read("SKILL.md")
        self.assertIn("smallest authorized, statically verifiable", skill)
        self.assertIn("configuration-contract.md", skill)
        self.assertIn("for every request", skill)
        self.assertIn("Do not require or claim runtime execution", skill)

    def test_analytics_and_media_keep_distinct_business_authorities(self) -> None:
        utility = read("references/01-orientation/utility-contract.md")
        workflow = read("references/02-execution/implementation-workflow.md")
        self.assertIn("Approved tracking plan or direct analytics requirement", utility)
        self.assertIn("Human media-team brief", utility)
        self.assertIn("supporting evidence for reusable business events", utility)
        self.assertIn("Do not copy a GA4 destination name", workflow)

    def test_critical_facts_have_static_evidence_grades(self) -> None:
        contract = read("references/02-execution/configuration-contract.md")
        required_grades = (
            "approved-input",
            "official-current",
            "container-confirmed",
            "contract-sample",
            "assumption",
        )
        for grade in required_grades:
            self.assertIn(f"`{grade}`", contract)
        self.assertIn("Never use for a critical mutation decision", contract)
        self.assertIn("without requesting runtime access", contract)

    def test_result_statuses_match_static_configuration_scope(self) -> None:
        contract = read("references/02-execution/configuration-contract.md")
        acceptance = read("references/03-judgement/acceptance-and-handoff.md")
        for status in (
            "Configured",
            "Specification complete",
            "Partial",
            "Blocked",
            "Deferred",
        ):
            self.assertIn(f"`{status}`", contract)
            self.assertIn(f"`{status}`", acceptance)
        combined = contract + acceptance
        self.assertNotIn("Needs runtime QA", combined)
        self.assertIn("Runtime execution is outside this skill", combined)
        self.assertIn("saved state already matched the approved contract", combined)

    def test_configuration_contract_covers_field_and_object_graphs(self) -> None:
        contract = read("references/02-execution/configuration-contract.md")
        for term in (
            "Requirement record",
            "Field mapping",
            "Object change manifest",
            "Consent and external dependencies",
            "Static completion invariants",
            "pre-change state",
            "idempotency",
        ):
            self.assertIn(term, contract)

    def test_official_documentation_remains_current_authority_for_schema(self) -> None:
        sources = read("references/01-orientation/official-source-policy.md")
        media = read("references/02-execution/media-tags.md")
        self.assertIn("Never rely on memory", sources)
        self.assertIn("Do not copy an event catalogue into the skill", sources)
        self.assertIn(
            "Lack of a dedicated skill file never permits memory-based configuration", media
        )
        self.assertIn("source evidence grade", sources)

    def test_compound_consent_predicates_use_native_or_denial_graph(self) -> None:
        skill = read("SKILL.md")
        consent = read("references/02-execution/cmp-consent.md")
        triggers = read("references/02-execution/triggers-and-variables.md")
        acceptance = read("references/03-judgement/acceptance-and-handoff.md")
        self.assertIn("smallest reusable set of blocking triggers", skill)
        self.assertIn("category/purpose", consent)
        self.assertIn("independent required grants each need OR-denial behavior", consent)
        self.assertIn("any matching blocking/exception trigger prevents", triggers)
        self.assertIn("Compound consent predicate", acceptance)
        self.assertIn("Do not create a Custom JavaScript", consent)

    def test_strict_consent_lifecycle_remains_complete(self) -> None:
        consent = read("references/02-execution/cmp-consent.md")
        for term in (
            "Default to strict/basic gating",
            "unknown, undefined, uninitialized, and denied state block",
            "does not retry automatically",
            "every GTM event used by each consumer tag",
            "ignore their own firing and blocking triggers",
            "does not unload a vendor script",
            "logical AND",
            "documented CMP state variable directly",
            "does not contain <exact documented vendor token>",
        ):
            self.assertIn(term, consent)

    def test_advanced_consent_is_product_specific_and_explicit(self) -> None:
        registry = read("references/02-execution/vendor-consent-modes.md")
        google = read("references/02-execution/google-consent-mode.md")
        self.assertIn("per browser product, not only per vendor", registry)
        self.assertIn("strict/basic blocked", registry)
        self.assertIn("native stop/hold", registry)
        self.assertIn("native cookie-control", registry)
        self.assertIn("advanced consent-aware", registry)
        self.assertIn("adaptive/anonymous analytics", registry)
        self.assertIn("Use advanced behavior only when the analyst explicitly requests", google)
        self.assertIn("does not execute runtime recette", google)
        self.assertIn("static configuration expectation", google)

    def test_google_shared_execution_units_cannot_mix_routes(self) -> None:
        google = read("references/02-execution/google-consent-mode.md")
        analytics = read("references/02-execution/analytics-tags.md")
        google_ads = read("references/02-execution/media-google-ads.md")
        self.assertIn("blocks that tag for every connected destination", google)
        self.assertIn("officially supported destination-specific separation", google)
        self.assertIn("shared Google tag destinations", analytics)
        self.assertIn("shared with GA4", google_ads)

    def test_google_blocks_reuse_semantically_compatible_objects(self) -> None:
        google = read("references/02-execution/google-consent-mode.md")
        self.assertIn("semantically compatible", google)
        self.assertIn("do not duplicate an otherwise compatible block", google)

    def test_consent_registry_does_not_expand_analytics_scope(self) -> None:
        utility = read("references/01-orientation/utility-contract.md")
        registry = read("references/02-execution/vendor-consent-modes.md")
        self.assertIn("does not add an analytics tag-configuration route", utility)
        self.assertIn("classify consent capability only", registry)

    def test_trigger_and_tag_execution_settings_are_explicit(self) -> None:
        triggers = read("references/02-execution/triggers-and-variables.md")
        for term in (
            "firing triggers on one tag are alternatives",
            "filter rows within one trigger are cumulative",
            "Version 1 literal-dot",
            "Version 2 nested-path",
            "priority",
            "custom schedule",
            "live-only behavior",
            "firing option",
        ):
            self.assertIn(term, triggers)

    def test_page_view_remains_separate_from_initialization(self) -> None:
        analytics = read("references/02-execution/analytics-tags.md")
        media = read("references/02-execution/media-tags.md")
        self.assertIn("Keep page view separate by default", analytics)
        self.assertIn("revalidate every page parameter", analytics)
        self.assertIn("Do not make a base/configuration tag send a page view by default", media)

    def test_every_new_object_requires_a_current_justification(self) -> None:
        skill = read("SKILL.md")
        workflow = read("references/02-execution/implementation-workflow.md")
        contract = read("references/02-execution/configuration-contract.md")
        self.assertIn("Create an object only for a current requirement", skill)
        self.assertIn("Justify every new object by a current requirement", workflow)
        self.assertIn("requirement or documented constraint that justifies", contract)

    def test_adapter_contract_is_manifest_driven_and_idempotent(self) -> None:
        adapters = read("references/02-execution/tool-adapters.md")
        self.assertIn("Translate the change manifest deterministically", adapters)
        self.assertIn("current fingerprint", adapters)
        self.assertIn("complete pre-change representation", adapters)
        self.assertIn("Prove idempotency", adapters)
        self.assertIn("second run that proposes another create", adapters)
        self.assertIn("workspace", adapters)

    def test_external_administration_is_not_silently_claimed(self) -> None:
        analytics = read("references/02-execution/analytics-tags.md")
        media = read("references/02-execution/media-tags.md")
        self.assertIn("Record external Google and GA4 administration", analytics)
        self.assertIn("custom dimensions or metrics", analytics)
        self.assertIn("key-event designation", analytics)
        self.assertIn("Record external platform dependencies", media)
        self.assertIn("conversion actions", media)
        self.assertIn("Sending a browser event never proves", media)

    def test_priority_media_playbooks_exist_and_route_from_skill(self) -> None:
        skill = read("SKILL.md")
        platforms = (
            "media-google-ads.md",
            "media-microsoft-ads.md",
            "media-meta.md",
            "media-tiktok.md",
            "media-snapchat.md",
        )
        for platform in platforms:
            self.assertIn(platform, skill)
            self.assertTrue((ROOT / "references" / "02-execution" / platform).exists())

    def test_arrays_user_data_and_server_boundary_remain_guarded(self) -> None:
        meta = read("references/02-execution/media-meta.md")
        data = read("references/02-execution/data-contract-and-transformations.md")
        user_data = read("references/02-execution/first-party-data.md")
        utility = read("references/01-orientation/utility-contract.md")
        self.assertIn("content_ids", meta)
        self.assertIn("contents", meta)
        self.assertIn("zero-item, one-item, and multi-item", data)
        self.assertIn("Do not enable automatic or manual collection by default", user_data)
        self.assertIn("Do not create a browser/server event ID", data)
        self.assertIn("deferred in the current client-side version", utility)


if __name__ == "__main__":
    unittest.main()
