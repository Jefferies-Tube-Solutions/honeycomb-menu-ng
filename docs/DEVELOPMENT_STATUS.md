# v1.10.0-beta.7 published — STOP for owner testing

Release: https://github.com/NicolaiTandrup/honeycomb-menu-ng/releases/tag/v1.10.0-beta.7
Release PR: https://github.com/NicolaiTandrup/honeycomb-menu-ng/pull/159
Exact tested/released source: 87c192a0a5f16bd880cf93692d5275d1d6130ed2
Frozen release branch: release/v1.10.0-beta7-mobile.
Approved implementation: PR #158, 7dcf7f252aac1930d65ae71cab8477bf4cedf269.
This handoff branch is documentation only and does not move the released branch.

Beta.7 publishes the approved mobile placement fix with standard beta.N metadata.
Runtime source/tests/scripts/workflows remain EXACTLY PR #158. The generated bundle
differs solely in version strings. No redesign, HACS/AwesomeVersion patch, parser
extension, YAML keys or unrelated styling/features. Normal and expanded Bee show
v1.10.0 beta 7. Collapsed/expanded sizes, desktop thresholds/fallback, actual mobile
footprint/free lower canvas, safe bounds, submenu promotion and exact Back retained.

All mandatory checks PASSED at the exact release SHA:
- Node20 core contract runner +459 passing Node tests, 3 existing stable-only skips.
- All31 local pipeline groups: full136-case core Chromium, all module/navigation/
  sizing/Info/Light/Sonos/Climate/Charger regressions,49-case geometry matrix,
  beta.6 threshold suite,6-case mobile follow-up/large desktop cases, docs/YAML,
  HACS packaging, integrity, pinned checksum-verified actionlint and reproducibility.
- Fresh push build/lint: https://github.com/NicolaiTandrup/honeycomb-menu-ng/actions/runs/41297031395
- Fresh PR build/lint: https://github.com/NicolaiTandrup/honeycomb-menu-ng/actions/runs/41297038432
- Official HACS: https://github.com/NicolaiTandrup/honeycomb-menu-ng/actions/runs/41297036554
- Guarded verification + publication: https://github.com/NicolaiTandrup/honeycomb-menu-ng/actions/runs/41299106987
No mandatory jobs were skipped. The existing guarded workflow reproduced and
compared committed, CI-built and staged bundle/checksum bytes before publication.

Public bundle:317609 bytes; SHA256
0f514fdf0a33e020ccc3e36dba31d9db8e1bc190b3a7bc11b3f84959f38f3681.
Tag, release title/flags, exact source, all3 asset digests, checksum and source/CI
provenance independently verified. Downloaded public bundle matches committed and
second local Node20 build bytes. Public download smoke tests:7 normal/expanded Bee
cases and6 mobile/desktop geometry/navigation cases pass with no console/page errors.

HACS2.0.5/AwesomeVersion25.8.0 recognize beta.7 as a newer beta than beta.6;
HACS pending_update=true. Observed actual GitHub prerelease discovery selects beta.7.
All115 prior tags and62 prior releases/assets retained, including original beta.6
6db9e046da496c5d6d437d8d0da08346136ec11f. Master remains
ba95dade58fa64c5183a312e0d1d00044feeb096; latest stable v1.9.0 unchanged.

Evidence outside Git: /workspace/build-output/beta7/ (full/, public-assets/,
public-mobile/, public-bee/, public-verification.json, public-smoke.json and CI logs).
Browser plugin unavailable; repository Playwright/system Chromium, synthetic HA only.

Owner next on PAHA02-DEV: enable beta versions in HACS, select/redownload
v1.10.0-beta.7, hard-refresh frontend/resource cache and confirm Bee label. Existing
resource URL/YAML remain valid. Actual Android/mobile and full-size physical PC/
real Home Assistant acceptance remain pending; synthetic tests do not certify them.
No production Home Assistant was modified.

STOP after verified release. No main/master merge or stable promotion. Beam of
Origin #156 is for beta.8 and remains unimplemented; architecture review #154 stays
separate after layout acceptance. Await owner real-device testing/new instructions.
No environment configuration was changed or published during this release task.
