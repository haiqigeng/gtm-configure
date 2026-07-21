from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "configuration_scenarios.json"


class ConfigurationScenarioFixtureTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(FIXTURE.read_text(encoding="utf-8"))
        cls.scenarios = cls.payload["scenarios"]

    def test_scenario_corpus_has_expected_north_star_coverage(self) -> None:
        self.assertEqual(self.payload["version"], 3)
        self.assertIn("not model-output or runtime tests", self.payload["description"])
        expected_ids = {
            "ga4-tracking-plan-static",
            "media-brief-meta-static",
            "compound-cmp-predicate",
            "shared-google-incompatible-routes",
            "missing-source-contract",
            "tool-unavailable-specification",
            "partial-mutation-journal",
            "idempotent-rerun",
            "ga4-external-administration",
            "unlisted-browser-vendor",
            "tracking-plan-valid-custom-advisory",
            "tracking-plan-blocking-schema-error",
            "tracking-plan-optional-field-omitted",
            "tracking-plan-source-scope-manifest",
            "legacy-container-pattern-rejected",
            "conflicting-existing-implementation-blocked",
            "adapter-pagination-capability-discovery",
            "workspace-change-attribution",
            "server-side-deduplication-deferred",
        }
        self.assertEqual({scenario["id"] for scenario in self.scenarios}, expected_ids)

    def test_every_scenario_is_a_well_formed_static_contract(self) -> None:
        allowed_routes = {"analytics", "media", "consent", "combined"}
        allowed_evidence = {
            "approved-input",
            "official-current",
            "container-confirmed",
            "contract-sample",
            "assumption",
        }
        allowed_actions = {"create", "update", "reuse", "untouched", "remove"}
        allowed_statuses = set(self.payload["allowed_statuses"])

        for scenario in self.scenarios:
            with self.subTest(scenario=scenario["id"]):
                self.assertIn(scenario["route"], allowed_routes)
                self.assertTrue(scenario["request"].startswith("Use configure-gtm"))
                self.assertIn("No runtime access is available.", scenario["request"])
                self.assertIn(scenario["expected_status"], allowed_statuses)
                self.assertTrue(set(scenario["evidence_grades"]) <= allowed_evidence)
                self.assertIsInstance(scenario["external_dependencies"], list)
                self.assertGreaterEqual(len(scenario["external_dependencies"]), 1)
                self.assertGreaterEqual(len(scenario["expected_invariants"]), 1)
                self.assertGreaterEqual(len(scenario["forbidden_invariants"]), 1)
                self.assertFalse(
                    set(scenario["expected_invariants"]) & set(scenario["forbidden_invariants"])
                )

                for action in scenario["expected_actions"]:
                    self.assertIn(action["action"], allowed_actions)
                    self.assertTrue(action["object_type"])
                    self.assertTrue(action["name"])
                    self.assertTrue(action["justification"])

                for discrepancy in scenario.get("discrepancies", []):
                    self.assertIn(
                        discrepancy["class"],
                        {"blocking-error", "advisory", "implementation-note"},
                    )
                    self.assertTrue(discrepancy["approved"])
                    self.assertTrue(discrepancy["documented"])
                    self.assertTrue(discrepancy["default_action"])

    def test_status_specific_evidence_prevents_false_completion(self) -> None:
        for scenario in self.scenarios:
            with self.subTest(scenario=scenario["id"]):
                status = scenario["expected_status"]
                if status == "Specification complete":
                    self.assertFalse(scenario["live_state_claim"])
                elif status == "Blocked":
                    self.assertFalse(scenario["live_state_claim"])
                    self.assertEqual(scenario["expected_actions"], [])
                elif status == "Partial":
                    self.assertTrue(scenario["live_state_claim"])
                    self.assertTrue(scenario["saved_partial_state"])
                    self.assertTrue(scenario["recovery_boundary"])
                elif status == "Configured":
                    self.assertTrue(scenario["live_state_claim"])
                    self.assertTrue(scenario["saved_object_readback"])
                    self.assertTrue(scenario["idempotent_second_execution"])
                elif status == "Deferred":
                    self.assertFalse(scenario["live_state_claim"])
                    self.assertEqual(scenario["expected_actions"], [])

    def test_compound_consent_uses_or_denial_without_helper_code(self) -> None:
        scenario = next(item for item in self.scenarios if item["id"] == "compound-cmp-predicate")
        blocks = [
            action
            for action in scenario["expected_actions"]
            if action["object_type"] == "blocking trigger"
        ]
        self.assertEqual(len(blocks), 2)
        forbidden = " ".join(scenario["forbidden_invariants"]).lower()
        self.assertIn("consent cjs", forbidden)
        self.assertIn("mutually exclusive and", forbidden)

    def test_scenario_corpus_covers_every_result_type(self) -> None:
        statuses = {scenario["expected_status"] for scenario in self.scenarios}
        self.assertEqual(
            statuses,
            {"Configured", "Specification complete", "Partial", "Blocked", "Deferred"},
        )

    def test_tracking_plan_scenarios_never_silently_redesign_collection(self) -> None:
        advisory = next(
            item for item in self.scenarios if item["id"] == "tracking-plan-valid-custom-advisory"
        )
        action_names = {action["name"] for action in advisory["expected_actions"]}
        self.assertIn("GA4 - Event - account_created", action_names)
        self.assertNotIn("GA4 - Event - sign_up", action_names)
        self.assertEqual(advisory["discrepancies"][0]["class"], "advisory")

        blocked = next(
            item for item in self.scenarios if item["id"] == "tracking-plan-blocking-schema-error"
        )
        self.assertEqual(blocked["expected_status"], "Blocked")
        self.assertEqual(blocked["expected_actions"], [])
        self.assertEqual(blocked["discrepancies"][0]["class"], "blocking-error")

    def test_container_state_is_integration_evidence_not_architecture_authority(self) -> None:
        legacy = next(
            item for item in self.scenarios if item["id"] == "legacy-container-pattern-rejected"
        )
        actions = {action["name"]: action["action"] for action in legacy["expected_actions"]}
        self.assertEqual(actions["DLV - event.plan_type"], "create")
        self.assertEqual(actions["Existing broad Custom JavaScript helper"], "untouched")

        conflict = next(
            item
            for item in self.scenarios
            if item["id"] == "conflicting-existing-implementation-blocked"
        )
        self.assertEqual(conflict["expected_status"], "Blocked")
        self.assertIn("parallel tag added", conflict["forbidden_invariants"])

    def test_workspace_change_attribution_is_explicit(self) -> None:
        scenario = next(
            item for item in self.scenarios if item["id"] == "workspace-change-attribution"
        )
        self.assertEqual(scenario["preexisting_workspace_changes"], 2)
        self.assertEqual(scenario["current_run_changes"], 1)
        self.assertEqual(scenario["final_workspace_changes"], 3)


if __name__ == "__main__":
    unittest.main()
