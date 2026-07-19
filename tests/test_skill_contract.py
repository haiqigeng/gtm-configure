from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


class SkillContractTest(unittest.TestCase):
    def test_openai_interface_metadata_matches_skill(self) -> None:
        metadata = read("agents/openai.yaml")
        self.assertIn('display_name: "Configure Google Tag Manager"', metadata)
        self.assertIn('default_prompt: "Use $configure-gtm', metadata)
        short_line = next(line for line in metadata.splitlines() if "short_description:" in line)
        short_description = short_line.split('"', 2)[1]
        self.assertGreaterEqual(len(short_description), 25)
        self.assertLessEqual(len(short_description), 64)

    def test_analytics_and_media_have_distinct_primary_inputs(self) -> None:
        utility = read("references/01-orientation/utility-contract.md")
        self.assertIn("Google tag/GA4 analytics", utility)
        self.assertIn("Approved tracking plan or direct analytics requirement", utility)
        self.assertIn("Human media-team brief", utility)
        self.assertIn("supporting evidence for reusable business events", utility)

    def test_official_documentation_is_runtime_authority(self) -> None:
        sources = read("references/01-orientation/official-source-policy.md")
        media = read("references/02-execution/media-tags.md")
        self.assertIn("Never rely on memory", sources)
        self.assertIn("Do not copy an event catalogue into the skill", sources)
        self.assertIn(
            "Lack of a dedicated skill file never permits memory-based configuration", media
        )

    def test_consent_defaults_and_advanced_exception_are_explicit(self) -> None:
        skill = read("SKILL.md")
        consent = read("references/02-execution/cmp-consent.md")
        google = read("references/02-execution/google-consent-mode.md")
        vendor_consent = read("references/02-execution/vendor-consent-modes.md")
        acceptance = read("references/03-judgement/acceptance-and-handoff.md")
        self.assertIn("consent-controlled", skill)
        self.assertNotIn("consent-gated", skill)
        self.assertIn("Default to strict/basic gating", consent)
        self.assertIn(
            "unknown, undefined, uninitialized, and denied state block", consent
        )
        self.assertIn("does not retry automatically", consent)
        self.assertIn("every GTM event used by each consumer tag", consent)
        self.assertIn("ignore their own firing and blocking triggers", consent)
        self.assertIn("does not unload a vendor script", consent)
        self.assertIn("logical AND", consent)
        self.assertIn("documented CMP state variable directly", consent)
        self.assertIn("does not contain <exact documented vendor token>", consent)
        self.assertIn("Do not create a Custom JavaScript", consent)
        self.assertNotIn("one narrow Boolean variable", consent)
        self.assertNotIn("one tested Boolean result", consent)
        self.assertIn("Use advanced behavior only when the analyst explicitly requests", google)
        self.assertIn("advanced consent-aware", google)
        self.assertIn("Google Ads Conversion Tracking and Remarketing", google)
        self.assertIn("Floodlight", google)
        self.assertIn("Conversion Linker", google)
        self.assertIn("Classify behavior before naming it", vendor_consent)
        self.assertIn("Microsoft Advertising UET", vendor_consent)
        self.assertIn("Microsoft Clarity", vendor_consent)
        self.assertIn("adaptive/anonymous analytics", vendor_consent)
        self.assertIn("native cookie-control", vendor_consent)
        self.assertIn("does not execute the full interactive runtime recette", google)
        self.assertIn("Do not also label the same requirement `Complete`", acceptance)

    def test_advanced_consent_is_selected_per_product(self) -> None:
        skill = read("SKILL.md")
        registry = read("references/02-execution/vendor-consent-modes.md")
        microsoft = read("references/02-execution/media-microsoft-ads.md")
        tiktok = read("references/02-execution/media-tiktok.md")
        self.assertIn("vendor-consent-modes.md", skill)
        self.assertIn("per browser product, not only per vendor", registry)
        self.assertIn("Google Analytics 4", registry)
        self.assertIn("Google Ads Conversion Tracking and Remarketing", registry)
        self.assertIn("Floodlight", registry)
        self.assertIn("Conversion Linker", registry)
        self.assertIn("Microsoft Advertising UET", registry)
        self.assertIn("Microsoft Clarity", registry)
        self.assertIn("Matomo", registry)
        self.assertIn("Piwik PRO Analytics", registry)
        self.assertIn("TikTok Pixel", registry)
        self.assertIn("Treat Clarity separately from UET", registry)
        self.assertIn("Clarity's decision separate", microsoft)
        self.assertIn("native cookie-control", tiktok)
        self.assertIn("Otherwise retain the strict/basic block", tiktok)

    def test_shared_google_execution_units_cannot_mix_consent_routes(self) -> None:
        skill = read("SKILL.md")
        google = read("references/02-execution/google-consent-mode.md")
        analytics = read("references/02-execution/analytics-tags.md")
        google_ads = read("references/02-execution/media-google-ads.md")
        acceptance = read("references/03-judgement/acceptance-and-handoff.md")
        self.assertIn("one shared execution unit", skill)
        self.assertIn("blocks that tag for every connected destination", google)
        self.assertIn("officially supported destination-specific separation", google)
        self.assertIn("shared Google tag destinations", analytics)
        self.assertIn("shared with GA4", google_ads)
        self.assertIn("Shared Google execution unit", acceptance)

    def test_google_blocks_reuse_semantically_compatible_objects(self) -> None:
        google = read("references/02-execution/google-consent-mode.md")
        self.assertIn("semantically compatible", google)
        self.assertIn("do not duplicate an otherwise compatible block", google)
        self.assertNotIn(
            "separate GA4, Google Ads, and Floodlight blocks even when", google
        )

    def test_consent_registry_does_not_expand_analytics_scope(self) -> None:
        utility = read("references/01-orientation/utility-contract.md")
        registry = read("references/02-execution/vendor-consent-modes.md")
        self.assertIn("does not add an analytics tag-configuration route", utility)
        self.assertIn("classify consent capability only", registry)

    def test_config_tags_do_not_implicitly_own_page_view(self) -> None:
        analytics = read("references/02-execution/analytics-tags.md")
        media = read("references/02-execution/media-tags.md")
        self.assertIn("Keep page view separate by default", analytics)
        self.assertIn("revalidate every page parameter", analytics)
        self.assertIn("Do not make a base/configuration tag send a page view by default", media)
        self.assertIn("When the approved requirement includes a manually managed page view", analytics)
        self.assertIn("Create a GTM base/configuration tag only when initialization is in scope", media)

    def test_every_new_object_requires_a_current_justification(self) -> None:
        skill = read("SKILL.md")
        workflow = read("references/02-execution/implementation-workflow.md")
        acceptance = read("references/03-judgement/acceptance-and-handoff.md")
        data = read("references/02-execution/data-contract-and-transformations.md")
        self.assertIn("Create an object only for a current requirement", skill)
        self.assertIn("Justify every new object by a current requirement", workflow)
        self.assertIn("justify every new object by a current requirement", acceptance)
        self.assertIn("routine CMP vendor consent", data)

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

    def test_media_arrays_and_user_data_are_guarded(self) -> None:
        meta = read("references/02-execution/media-meta.md")
        data = read("references/02-execution/data-contract-and-transformations.md")
        user_data = read("references/02-execution/first-party-data.md")
        self.assertIn("content_ids", meta)
        self.assertIn("contents", meta)
        self.assertIn("multi-item", data)
        self.assertIn("Do not enable automatic or manual collection by default", user_data)

    def test_server_side_and_event_id_remain_deferred(self) -> None:
        data = read("references/02-execution/data-contract-and-transformations.md")
        utility = read("references/01-orientation/utility-contract.md")
        self.assertIn("Do not create a browser/server event ID", data)
        self.assertIn("deferred in the current client-side version", utility)


if __name__ == "__main__":
    unittest.main()
