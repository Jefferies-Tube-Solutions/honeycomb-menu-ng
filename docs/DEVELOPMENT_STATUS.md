# v1.10.0-beta.6 published — STOP for owner testing

Published: https://github.com/NicolaiTandrup/honeycomb-menu-ng/releases/tag/v1.10.0-beta.6
Development PR: https://github.com/NicolaiTandrup/honeycomb-menu-ng/pull/157
Exact tested/released source: 6db9e046da496c5d6d437d8d0da08346136ec11f
Release branch: fix/v1.10-beta6-placement (kept at the exact released source).
Baseline: published beta.5 83cbdd486a924f88f2ad399886dff4fb31d913db.
This handoff-only branch is separate from the released source; no runtime changes.

Issue #148 beta.6 only. Root image-free placement measures shared physical slots
0–18 plus all actual controls, prefers full size, accepts new regions at >=85%,
retains existing valid regions to 84%, and falls back near original physical cube
0 when cramped. Fallback reserves first ring plus every actual control; submenus
retain actual-footprint selected-cube promotion and exact parent Back. No extra
YAML or phantom controls. Normal collapsed max82/expanded_size stay independent.

Validation COMPLETE for the released source:
- Node20 core contract runner OK; 454 Node tests pass, 3 existing stable-only skips.
- All 30 mandatory local CI groups pass. Initial core browser missing-reference
  failure was repaired by fetching historical tags; complete rerun: 68 desktop +
  68 phone cases pass. No unresolved failure or suppressed assertion.
- Full module/browser/docs regressions, 49-case seven-viewport geometry matrix,
  five new beta.6 browser cases, 100/85/84% hysteresis, extended actual slots,
  nested exact Back, resize/rotation, safe areas, keyboard/editing/lifecycle pass.
- Custom expanded_size 50/82/120/150/200 and visible-edge clamping pass.
- HACS package, metadata/integrity, pinned checksum-verified actionlint, second
  byte-identical Node20 rebuild and unchanged guarded release verification pass.
- Owner A before/after: full 100px below image, pixel-identical screenshots.
  Owner B: beta.5 85.16px in cramped strip -> beta.6 100px at original cube-0 anchor.
  Four configured controls remain four. Screenshots use a pinned public HA floorplan.
- Downloaded actual public bundle independently passes the five-case Chromium
  placement/threshold/responsive/nested smoke suite; console/page-error checks pass.

Green exact-source runs:
Push: https://github.com/NicolaiTandrup/honeycomb-menu-ng/actions/runs/41241999624
PR: https://github.com/NicolaiTandrup/honeycomb-menu-ng/actions/runs/41242032668
Official HACS: https://github.com/NicolaiTandrup/honeycomb-menu-ng/actions/runs/41242075650
Guarded publication: https://github.com/NicolaiTandrup/honeycomb-menu-ng/actions/runs/41244207046
Both build/lint jobs and both publication jobs completed successfully.

Public payload: 317009 bytes; SHA256
f9ed6e5cc1ba171543f958798ee9848d979ca84988b48560309d1f2e661616d8.
Public tag/source, bundle/checksum/provenance and all three API asset digests
independently verified. All 114 pre-existing tags and 61 releases/assets retained;
master ba95dade58fa64c5183a312e0d1d00044feeb096 and latest stable v1.9.0 unchanged.
No source modules/Bee/image-sizing/release/retention workflow changes from beta.5.

Evidence outside Git: /workspace/build-output/beta6/; before/, full/, public-smoke/,
public-assets/, validation-resolved.json, geometry-summary.json, public-verification.json.
Browser plugin not available; repository Playwright/system Chromium. Direct local
CI artifact download was network-denied; the unchanged GitHub release workflow
successfully performed the required CI/committed/staged byte comparisons.

Owner next: in HACS enable beta versions, select/redownload v1.10.0-beta.6, refresh
frontend/resource cache, test both actual floorplans on Android/PC and report #148
acceptance. Existing minimal collapsible:true YAML needs no additions. Browser
fixtures use synthetic entities/services; no real HA, physical device or hardware
acceptance is claimed. No production Home Assistant changes were made.

STOP: do not merge main/master, publish stable, begin Beam of Origin #156 or the
architecture/dead-code review #154. Await owner beta.6 acceptance/new instructions.
No environment configuration was reapplied or published during this coding task.
