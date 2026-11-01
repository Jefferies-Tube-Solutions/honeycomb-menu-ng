# v1.10.0-beta.7 — release preparation from approved PR #158

Owner authorizes standard beta.7 publication after ALL mandatory fresh exact-head
CI and existing guarded release checks. No main/master merge, stable, production
HA, HACS/AwesomeVersion changes or new version format. Beam of Origin #156 is
planned for beta.8 and is OUT of beta.7. Architecture review #154 stays deferred.

Release branch: release/v1.10.0-beta7-mobile.
Exact approved implementation: 7dcf7f252aac1930d65ae71cab8477bf4cedf269 (PR #158),
verified green push41246504454 and PR41246507979. Those runs DO NOT validate the
new release commit. Published beta.6 baseline6db9e046da496c5d6d437d8d0da08346136ec11f
and its tag/release remain immutable. No source/test/workflow/script changes from
PR #158: only version/lock/release metadata, generated bundle and release docs.

Prepared package/lock1.10.0-beta.7, prerelease title
Honeycomb NG v1.10.0-beta.7 — Mobile Placement Fix. Existing shared formatter emits
v1.10.0 beta 7. Generated317609-byte bundle differs from PR #158 only in exact
version literals; SHA2560f514fdf0a33e020ccc3e36dba31d9db8e1bc190b3a7bc11b3f84959f38f3681.
Node20 core runner +459 Node tests pass, 3 existing stable-only skips. Local HACS
packaging, beta metadata and pinned checksum-verified actionlint pass.

Next gate: run the entire existing mandatory pipeline against this release commit,
including core/browser/modules, both normal/expanded Bee, mobile/landscape/tablet,
desktop matrix, safe bounds, selected-cube promotion, exact Back and docs/YAML.
Require fresh complete green push+PR build/lint jobs at exact FINAL branch SHA,
o skipped mandatory jobs, official HACS, reproducibility and SHA256. Use only the
unchanged guarded release.yml with expected_commit, expected_tag=v1.10.0-beta.7
and publish=true after every gate passes. Freeze the branch during verification.
Do not change its head for unrelated handoff while publishing.

After publication independently verify public tag/source/assets/provenance/digests,
HACS beta update detection, correct Bee label and downloadable bundle smoke tests.
Preserve every existing tag/release and master/latest stable. Record final handoff
on a separate docs branch if needed, preserving the exact published source head.

Evidence outside Git: /workspace/build-output/beta7/, full/ and public-assets/.
Browser plugin unavailable; repository Playwright/system Chromium with synthetic
HA fixtures. No real physical Android/PC or production HA commands are authorized.
Owner actual Android/mobile and full-size desktop acceptance remain pending.

HACS owner action after verified release: enable beta versions, select/redownload
v1.10.0-beta.7 and refresh frontend/resource cache. No YAML changes. Stop for owner
real Home Assistant testing after release verification, without beginning #154/#156.
