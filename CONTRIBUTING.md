# Contributing

Keep the runtime skill agent-neutral and focused on GTM configuration for expert
web analysts. Do not commit client containers, tracking plans, screenshots,
domains, credentials, personal data, browser traces, or generated reports.

Before opening a pull request, run:

~~~powershell
python -m pip install -e ".[dev]"
python -m ruff format --no-cache --check scripts tests
python -m ruff check --no-cache scripts tests
python scripts/check_release.py --tag v2026.7.18 --release-notes CHANGELOG.md
python -m unittest discover -s tests -v
python -m compileall -q scripts
python scripts/build_skill_package.py --output dist/configure-gtm-test.zip
~~~

Changes to consent, schema mapping, platform playbooks, template governance,
reuse, or acceptance rules should include a focused regression test or an
explicit validation scenario. Keep live event catalogues in official vendor
documentation rather than copying them into the skill. Keep server-side GTM
and deduplication changes marked as deferred until that capability is formally
added to the skill.
