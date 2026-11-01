# v1.10.0-beta.8 — configured size ceiling and optional Bee diagnostics

Owner authorizes beta.8 publication only after all mandatory validation and fresh
exact-head CI pass. Branch: feature/v1.10-beta8-size-ceiling. Exact published
baseline: v1.10.0-beta.7 / 87c192a0a5f16bd880cf93692d5275d1d6130ed2 (PR #159).
Read primary issue #160 and shared Bee issue #153, including current owner comments.
Owner has accepted beta.7 mobile/PC placement; preserve that solver and navigation.
Beam of Origin #156 is deferred to beta.9. Architecture review #154 remains separate.
No main/master merge, stable publication, production HA commands or prior-release edits.

Implemented one original-config Hub ceiling (auto/omitted 82px; numeric N including
N > 82). Omitted expanded_size defaults to that ceiling; explicit expanded_size
only lowers the effective target. Root uses that effective target through the
existing placement engine; shared context clamps nested setup/resize/fitting before
rendering, with hover bounded too. Root solver, planning envelope, thresholds,
hysteresis, selected-cube promotion and exact Back mechanisms remain unchanged.
The legacy small_screen:false compact path also uses the effective lower target
for stored root geometry, so its engine dimensions agree with physical cubes.

Shared CubeElement Bee optionally reveals actual measured SVG CSS-pixel width with
the installed version when top-level size_debug:true. Strict boolean validation,
default false, same ordinary version-only/resting presentation. Resize/style/viewport
observers refresh while visible, without polling, and clean up on hide/detach.
Unavailable geometry uses compact N/A so even small debug cubes keep text contained.
Normal tap and expanded hold/Shift+Enter version gestures remain shared and safe.
README, Collapsible Hub and shared Bee guides document policy and optional YAML.

Prepared package/lock version 1.10.0-beta.8 and prerelease metadata; shared build
formatter produces v1.10.0 beta 8. Current deterministic 320690-byte bundle SHA256:
59fff63d433c8a0ff123292c79ec1b5ae478c4804af2ddbaf7380fb65e0bbc05.

Validation checkpoint before release commit:
- Node20 core runner and 461 Node tests pass; 3 existing stable-only skips.
- Focused 390x844 nine-policy size matrix passes across root/ring/Bee, Light,
  White/Color/Kelvin, Sonos/Radio/Join/Sleep, Climate, Charger, recursive and Back.
- Focused diagnostics pass DOM-vs-display measurement, actual fractional transforms,
  live resize, unavailable geometry, containment/accessibility and detach cleanup.
  Omitted/false screenshots are pixel-identical; no service calls escape the mocks.
- Existing beta.7 mobile placement suite passes on the beta.8 bundle.
- HACS local payload, beta metadata, actionlint and diff whitespace checks pass.
- Existing 100px placement fixtures now explicitly set parent size:100, preserving
  their original accepted geometry assertions. Independent beta.8 tests cover the
  full default/auto82 and explicit numeric matrix at all five required viewports.

Full mandatory local suite and fresh push/PR CI must still finish on final code;
DO NOT treat this preparation checkpoint as release completion. New beta8_size.py
is mandatory in build.yml. Release workflow and integrity scripts are unchanged.
Evidence outside Git: /workspace/build-output/beta8/. Browser plugin unavailable;
use repository Playwright/system Chromium and synthetic HA fixtures only.

Next: create/push development PR against beta.7 release branch, obtain all green
Node/Chromium/modules/docs/HACS and workflow checks at exact final SHA, reproduce
the committed bundle, then freeze head and dispatch existing release.yml with
expected_tag=v1.10.0-beta.8, exact expected_commit and publish=true. Independently
verify public tag/assets/provenance/checksums/HACS beta discovery, all previous
releases/tags and unchanged master/latest stable v1.9.0. Record publication handoff
on a separate docs branch, keeping the published source branch immutable.

Stop after verified release for owner physical Home Assistant acceptance. Synthetic
Chromium evidence does not establish real Android/iOS/desktop HA or hardware tests.
HACS owner step: enable beta versions, select/redownload v1.10.0-beta.8 and refresh
frontend/resource cache. Existing YAML remains compatible; debug is optional.
