from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "semantic_scenarios.json"


class SemanticScenarioFixtureTest(unittest.TestCase):
    def test_regression_scenarios_are_complete_and_non_leaking(self) -> None:
        payload = json.loads(FIXTURE.read_text(encoding="utf-8"))
        self.assertEqual(payload["version"], 1)
        scenarios = payload["scenarios"]
        expected_ids = {
            "didomi-direct-vendor-block",
            "undocumented-cmp-shape-blocks",
            "media-payload-cjs-remains-valid",
            "compatible-google-block-reuse",
            "existing-initialization-prevents-duplicate",
        }
        self.assertEqual({scenario["id"] for scenario in scenarios}, expected_ids)

        for scenario in scenarios:
            with self.subTest(scenario=scenario["id"]):
                self.assertTrue(scenario["request"].startswith("Using the configure-gtm skill"))
                self.assertIn("Do not modify a container.", scenario["request"])
                self.assertGreaterEqual(len(scenario["must_include"]), 2)
                self.assertGreaterEqual(len(scenario["must_not_include"]), 1)
                self.assertFalse(
                    set(scenario["must_include"]) & set(scenario["must_not_include"])
                )

    def test_consent_scenarios_never_expect_a_consent_helper(self) -> None:
        scenarios = json.loads(FIXTURE.read_text(encoding="utf-8"))["scenarios"]
        for scenario in scenarios:
            forbidden = " ".join(scenario["must_not_include"]).lower()
            if "cmp" in scenario["request"].lower() or "didomi" in scenario["request"].lower():
                self.assertIn("consent cjs", forbidden)


if __name__ == "__main__":
    unittest.main()
