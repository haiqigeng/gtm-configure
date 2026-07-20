#!/usr/bin/env python3
"""Run dependency-free repository and skill release checks."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEMVER = re.compile(r"^v(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)$")
CURRENT_RELEASE = "2.0.0"
REQUIRED_FILES = (
    "SKILL.md",
    "agents/openai.yaml",
    "references/01-orientation/utility-contract.md",
    "references/01-orientation/official-source-policy.md",
    "references/02-execution/configuration-contract.md",
    "references/02-execution/implementation-workflow.md",
    "references/02-execution/analytics-tags.md",
    "references/02-execution/media-tags.md",
    "references/02-execution/media-google-ads.md",
    "references/02-execution/media-microsoft-ads.md",
    "references/02-execution/media-meta.md",
    "references/02-execution/media-tiktok.md",
    "references/02-execution/media-snapchat.md",
    "references/02-execution/cmp-consent.md",
    "references/02-execution/vendor-consent-modes.md",
    "references/02-execution/google-consent-mode.md",
    "references/02-execution/first-party-data.md",
    "references/02-execution/data-contract-and-transformations.md",
    "references/02-execution/triggers-and-variables.md",
    "references/02-execution/template-governance.md",
    "references/02-execution/tool-adapters.md",
    "references/02-execution/naming-and-reuse.md",
    "references/03-judgement/acceptance-and-handoff.md",
    "README.md",
    "CHANGELOG.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "pyproject.toml",
    ".gitattributes",
    ".gitignore",
    ".github/workflows/ci.yml",
    ".github/workflows/release.yml",
    "scripts/check_release.py",
    "scripts/build_skill_package.py",
    "tests/test_release.py",
    "tests/test_skill_contract.py",
    "tests/test_configuration_scenarios.py",
    "tests/fixtures/configuration_scenarios.json",
)
STALE_FILES = (
    "references/execution-contract.md",
    "references/official-source-policy.md",
    "references/analytics-tags.md",
    "references/media-tags.md",
    "references/cmp-consent.md",
    "references/naming-and-reuse.md",
    "references/validation-scenarios.md",
    "tests/test_semantic_scenarios.py",
    "tests/fixtures/semantic_scenarios.json",
)
FORBIDDEN_ARTIFACT_NAMES = {
    ".coverage",
    ".pytest_cache",
    ".ruff_cache",
    "__pycache__",
    "release",
}
SCAN_EXCLUDED_ROOTS = {".git", ".venv", "dist", "venv"}


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def parse_frontmatter() -> tuple[str, str]:
    text = read("SKILL.md")
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md frontmatter is missing")
    _, raw, _ = text.split("---", 2)
    values: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip():
            continue
        key, separator, value = line.partition(":")
        if not separator:
            raise ValueError(f"invalid frontmatter line: {line}")
        values[key.strip()] = value.strip().strip('"')
    if list(values) != ["name", "description"]:
        raise ValueError("frontmatter must contain only name and description")
    if values.get("name") != "configure-gtm":
        raise ValueError("frontmatter name must be configure-gtm")
    if not values.get("description"):
        raise ValueError("frontmatter description is empty")
    return values["name"], values["description"]


def check_links() -> list[str]:
    errors: list[str] = []
    skill = read("SKILL.md")
    links = re.findall(r"\]\(([^)]+)\)", skill)
    for link in links:
        if link.startswith(("http://", "https://")):
            continue
        if not (ROOT / link).exists():
            errors.append(f"SKILL.md references missing resource: {link}")

    reference_files = {
        path.relative_to(ROOT).as_posix()
        for path in (ROOT / "references").rglob("*")
        if path.is_file()
    }
    linked_references = {link for link in links if link.startswith("references/")}
    for reference in sorted(reference_files - linked_references):
        errors.append(f"reference is not directly routed from SKILL.md: {reference}")
    for reference in sorted(reference_files):
        text = read(reference)
        if len(text.splitlines()) > 100 and "## Contents" not in text:
            errors.append(f"long reference is missing a Contents section: {reference}")
    return errors


def check_required_files() -> list[str]:
    errors = [
        f"missing required file: {path}" for path in REQUIRED_FILES if not (ROOT / path).exists()
    ]
    errors.extend(f"stale file remains: {path}" for path in STALE_FILES if (ROOT / path).exists())
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)
        if relative.parts[0] in SCAN_EXCLUDED_ROOTS:
            continue
        if path.name in FORBIDDEN_ARTIFACT_NAMES:
            errors.append(f"generated artifact must be removed: {relative}")
        if path.suffix in {".pyc", ".pyo"}:
            errors.append(f"generated bytecode must be removed: {relative}")
    return errors


def check_content() -> list[str]:
    errors: list[str] = []
    skill = read("SKILL.md")
    utility = read("references/01-orientation/utility-contract.md")
    sources = read("references/01-orientation/official-source-policy.md")
    configuration_contract = read("references/02-execution/configuration-contract.md")
    workflow = read("references/02-execution/implementation-workflow.md")
    analytics = read("references/02-execution/analytics-tags.md")
    media = read("references/02-execution/media-tags.md")
    consent = read("references/02-execution/cmp-consent.md")
    google_consent = read("references/02-execution/google-consent-mode.md")
    vendor_consent = read("references/02-execution/vendor-consent-modes.md")
    triggers = read("references/02-execution/triggers-and-variables.md")
    adapters = read("references/02-execution/tool-adapters.md")
    judgement = read("references/03-judgement/acceptance-and-handoff.md")
    readme = read("README.md")
    changelog = read("CHANGELOG.md")
    contributing = read("CONTRIBUTING.md")
    agent_metadata = read("agents/openai.yaml")
    pyproject = read("pyproject.toml")
    ci_workflow = read(".github/workflows/ci.yml")
    release_workflow = read(".github/workflows/release.yml")
    required_terms = (
        "01 - Orientation",
        "02 - Execution",
        "03 - Judgement",
        "dedicated GTM workspace",
        "Server-side GTM",
        "browser/server deduplication",
        "media-team brief",
        "strict/basic CMP gating",
        "Classify consent behavior per browser product",
        "Create an object only for a current requirement",
        "smallest authorized, statically verifiable",
        "configuration-contract.md",
        "Do not require or claim runtime execution",
    )
    errors.extend(
        f"SKILL.md missing required term: {term}" for term in required_terms if term not in skill
    )
    utility_terms = (
        "## Audience",
        "## Objective",
        "## Current use cases",
        "## Inputs",
        "## Outputs",
        "## Boundaries",
    )
    errors.extend(
        f"utility contract missing section: {term}" for term in utility_terms if term not in utility
    )
    contract_terms = (
        "Use different primary inputs for analytics and media",
        "Human media-team brief",
        "Current official media-vendor documentation",
    )
    errors.extend(
        f"utility contract missing requirement authority: {term}"
        for term in contract_terms
        if term not in utility
    )
    configuration_contract_terms = (
        "## Evidence grades",
        "`approved-input`",
        "`official-current`",
        "`container-confirmed`",
        "`contract-sample`",
        "## Requirement record",
        "## Field mapping",
        "## Object change manifest",
        "## Consent and external dependencies",
        "## Result statuses",
        "`Configured`",
        "`Specification complete`",
        "`Partial`",
        "`Blocked`",
        "`Deferred`",
        "## Static completion invariants",
        "authoritative current-workspace readback",
        "idempotency",
    )
    errors.extend(
        f"configuration contract missing requirement: {term}"
        for term in configuration_contract_terms
        if term not in configuration_contract
    )
    source_terms = (
        "Never rely on memory",
        "Do not copy an event catalogue into the skill",
        "Microsoft Advertising UET",
        "Microsoft Clarity Consent Mode",
        "TikTok Pixel standard events",
        "Snap Pixel and GTM",
    )
    errors.extend(
        f"official source policy missing contract: {term}"
        for term in source_terms
        if term not in sources
    )
    workflow_terms = (
        "For media, treat the media-team brief as the primary business input",
        "Default to strict/basic behavior",
        "Keep configuration/base tags from sending an automatic page view by default",
        "Justify every new object by a current requirement",
    )
    errors.extend(
        f"workflow missing contract: {term}" for term in workflow_terms if term not in workflow
    )
    analytics_terms = (
        "GA4 - Config",
        "GA4 - Event Setting",
        "send_page_view",
        "Block - <CMP> - GA4 denied",
    )
    errors.extend(
        f"analytics reference missing contract: {term}"
        for term in analytics_terms
        if term not in analytics
    )
    media_terms = (
        "Treat the media brief as the primary business input",
        "dataLayer key",
        "template UI field",
        "current official standard event",
        "multi-item payloads",
    )
    errors.extend(
        f"media reference missing contract: {term}" for term in media_terms if term not in media
    )
    consent_terms = (
        "Default to strict/basic gating",
        "unknown, undefined, uninitialized, and denied state block",
        "every GTM event used by each consumer tag",
        "ignore their own firing and blocking triggers",
        "does not unload a vendor script",
        "Select advanced/native consent only explicitly",
        "documented CMP state variable directly",
    )
    errors.extend(
        f"consent reference missing contract: {term}"
        for term in consent_terms
        if term not in consent
    )
    google_consent_terms = (
        "Basic consent mode",
        "Advanced consent mode",
        "advanced consent-aware",
        "Do not attach a blocking trigger",
        "Google Ads Conversion Tracking and Remarketing",
        "Floodlight",
        "Conversion Linker",
    )
    errors.extend(
        f"Google consent reference missing contract: {term}"
        for term in google_consent_terms
        if term.lower() not in google_consent.lower()
    )
    vendor_consent_terms = (
        "strict/basic blocked",
        "native stop/hold",
        "native cookie-control",
        "advanced consent-aware",
        "adaptive/anonymous analytics",
        "Google Analytics 4",
        "Google Ads Conversion Tracking and Remarketing",
        "Floodlight",
        "Conversion Linker",
        "Microsoft Advertising UET",
        "Microsoft Clarity",
        "Matomo",
        "Piwik PRO Analytics",
        "TikTok Pixel",
        "classify consent capability only",
        "Discovery baseline last reviewed",
    )
    errors.extend(
        f"vendor consent reference missing contract: {term}"
        for term in vendor_consent_terms
        if term not in vendor_consent
    )
    consent_logic_terms = (
        "logical AND",
        "does not contain <exact documented vendor token>",
        "Do not create a Custom JavaScript",
        "Shared Google execution unit",
        "any matching blocking trigger prevents",
        "smallest reusable set of blocks",
    )
    combined_logic = "\n".join((consent, google_consent, triggers, judgement))
    errors.extend(
        f"consent logic contract missing: {term}"
        for term in consent_logic_terms
        if term not in combined_logic
    )
    forbidden_consent_logic = (
        "one narrow Boolean variable",
        "one tested Boolean result",
        "separate GA4, Google Ads, and Floodlight blocks even when",
    )
    errors.extend(
        f"obsolete consent implementation remains: {term}"
        for term in forbidden_consent_logic
        if term in combined_logic or term in readme
    )
    judgement_terms = (
        "## Static completion definition",
        "## Judgement statuses",
        "## Static validation matrix",
        "## Consent configuration proof",
        "## Handoff output",
    )
    errors.extend(
        f"judgement reference missing section: {term}"
        for term in judgement_terms
        if term not in judgement
    )
    trigger_terms = (
        "firing triggers on one tag are alternatives",
        "filter rows within one trigger are cumulative",
        "any matching blocking/exception trigger prevents",
        "Version 1 literal-dot",
        "Version 2 nested-path",
        "priority",
        "custom schedule",
        "live-only behavior",
        "firing option",
        "setup/cleanup references",
    )
    errors.extend(
        f"trigger reference missing semantic: {term}"
        for term in trigger_terms
        if term not in triggers
    )
    adapter_terms = (
        "configuration contract as the adapter input",
        "current fingerprint",
        "Do not mutate from an informal prose summary",
        "Prove idempotency",
        "synchronize workspace state",
    )
    errors.extend(
        f"tool-adapter reference missing contract: {term}"
        for term in adapter_terms
        if term not in adapters
    )
    readme_terms = (
        "## Who It Serves",
        "## Utility Objective",
        "## Inputs",
        "## Outputs",
        "## Workflow Architecture",
        "## Boundaries",
        "## Related Skills",
        "## Release Checks",
    )
    errors.extend(f"README missing section: {term}" for term in readme_terms if term not in readme)
    metadata_terms = (
        'display_name: "Configure Google Tag Manager"',
        'default_prompt: "Use $configure-gtm',
    )
    errors.extend(
        f"agents/openai.yaml missing contract: {term}"
        for term in metadata_terms
        if term not in agent_metadata
    )
    short_description = re.search(
        r'^\s+short_description: "(?P<value>[^"]+)"\s*$', agent_metadata, re.M
    )
    if not short_description:
        errors.append("agents/openai.yaml has no quoted short_description")
    elif not 25 <= len(short_description.group("value")) <= 64:
        errors.append("agents/openai.yaml short_description must contain 25-64 characters")
    if not re.search(rf"^## {re.escape(CURRENT_RELEASE)}\s*$", changelog, re.M):
        errors.append("CHANGELOG is missing the current release section")
    expected_tag = f"v{CURRENT_RELEASE}"
    if not re.search(rf'^version = "{re.escape(CURRENT_RELEASE)}"$', pyproject, re.M):
        errors.append("pyproject version does not match CURRENT_RELEASE")
    version_contracts = (
        ("README release check", f"--tag {expected_tag} --release-notes", readme),
        ("README package command", f"configure-gtm-{expected_tag}.zip", readme),
        ("CONTRIBUTING release check", f"--tag {expected_tag} --release-notes", contributing),
        ("CI release check", f"--tag {expected_tag} --release-notes", ci_workflow),
        ("README version policy", "Semantic Versioning: `vMAJOR.MINOR.PATCH`", readme),
        ("release workflow tag filter", '      - "v*.*.*"', release_workflow),
    )
    for label, expected, text in version_contracts:
        if expected not in text:
            errors.append(f"{label} does not match the current release")
    if re.search(r"Scope excludes[^.]*\b(server-side|deduplication)\b", skill, re.I):
        errors.append("server-side/deduplication appears in the permanent exclusion sentence")
    if "future extensions of this skill" not in skill.lower():
        errors.append("future capability boundary is not explicit")
    if len(skill.splitlines()) >= 500:
        errors.append("SKILL.md exceeds the 500-line guidance limit")
    release_text = "\n".join(read(path) for path in ("SKILL.md", "README.md", "CHANGELOG.md"))
    if re.search(r"TODO|\[TODO\]", release_text, re.I):
        errors.append("release-facing files contain placeholders")
    return errors


def check_git_release_state(
    tag: str | None, *, require_git_tag: bool, require_clean_tree: bool
) -> list[str]:
    errors: list[str] = []
    if require_clean_tree:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            errors.append(f"cannot inspect git worktree: {result.stderr.strip()}")
        elif result.stdout.strip():
            errors.append("release worktree is not clean")

    if require_git_tag:
        if not tag:
            errors.append("--require-git-tag requires --tag")
        else:
            result = subprocess.run(
                ["git", "tag", "--points-at", "HEAD"],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            if result.returncode != 0:
                errors.append(f"cannot inspect tags at HEAD: {result.stderr.strip()}")
            elif tag not in result.stdout.splitlines():
                errors.append(f"release tag {tag} does not point at HEAD")
    return errors


def check_release_notes(path: Path) -> list[str]:
    if not path.exists():
        return [f"release notes file does not exist: {path}"]
    text = path.read_text(encoding="utf-8")
    section = re.search(
        rf"^## {re.escape(CURRENT_RELEASE)}\s*$\n(?P<body>.*?)(?=^## |\Z)",
        text,
        re.M | re.S,
    )
    if not section:
        return [f"release notes are missing the {CURRENT_RELEASE} section"]
    text = section.group("body")
    headings = (
        "Why This Release Matters",
        "What Changed",
        "What Users Should Do",
        "Validation",
        "Known Limits",
    )
    return [
        f"release notes missing heading: {heading}"
        for heading in headings
        if f"### {heading}" not in text
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tag")
    parser.add_argument("--release-notes", type=Path)
    parser.add_argument("--require-git-tag", action="store_true")
    parser.add_argument("--require-clean-tree", action="store_true")
    args = parser.parse_args()
    errors: list[str] = []
    try:
        _, description = parse_frontmatter()
        if "expert web analyst" not in description.lower():
            errors.append("frontmatter does not identify the expert web analyst audience")
        if len(description) > 1024:
            errors.append("frontmatter description exceeds 1024 characters")
        if "<" in description or ">" in description:
            errors.append("frontmatter description contains a forbidden angle bracket")
    except ValueError as exc:
        errors.append(str(exc))
    errors.extend(check_required_files())
    errors.extend(check_links())
    errors.extend(check_content())
    if args.tag:
        if not SEMVER.fullmatch(args.tag):
            errors.append(f"invalid Semantic Version release tag: {args.tag}")
        elif args.tag != f"v{CURRENT_RELEASE}":
            errors.append(
                f"release tag {args.tag} does not match current release v{CURRENT_RELEASE}"
            )
    if args.release_notes:
        errors.extend(check_release_notes(args.release_notes))
    errors.extend(
        check_git_release_state(
            args.tag,
            require_git_tag=args.require_git_tag,
            require_clean_tree=args.require_clean_tree,
        )
    )
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Release check: FAIL ({len(errors)} error(s))")
        return 1
    print(
        f"Release check: PASS ({len(REQUIRED_FILES)} required files, {len(read('SKILL.md').splitlines())} SKILL.md lines)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
