# v1.10.0-beta.6 — Collapsible Hub placement correction

Authorized scope: issue #148 only, cumulative from published beta.5
83cbdd486a924f88f2ad399886dff4fb31d913db. User authorizes beta.6 prerelease only
AFTER all mandatory tests and unchanged guarded release-integrity gates pass.
No main/master merge, stable promotion, production HA, Beam of Origin #156 or
architecture/dead-code review #154. Stop for owner real-HA beta.6 testing.

Branch: fix/v1.10-beta6-placement. Published beta.5 tag/release/source verified;
latest owner geometry requirements on #148 read. Existing releases/PRs untouched.

Changes: shared expanded-layout helper unions the physical 0–18 planning envelope
with all actual root controls, checks all four outside-image regions, prefers
100% size and accepts new placement at >=85%. A previous valid free region stays
through the 84–85% neutral band; no-prior fallback chooses original cube 0.
Below 84%, reject it. Safe viewport fallback reserves center/first ring plus ALL
actual controls, fits largest size up to expanded_size, clamps near the original
physical floorplan anchor. Submenus continue to use actual footprints and exact
parent restoration. Original-anchor movement is included in fitting invalidation.
No extra YAML, phantom cubes, rendering/module changes or unrelated refactoring.
Version metadata, deterministic HACS bundle, docs and CI geometry test updated.

Current validation: Node20 core contracts OK; 454 Node tests pass, 3 existing
stable-only skips. HACS/local package, release/beta metadata, production build,
pinned actionlint pass. Focused Chromium owner A/B, 100/85/84% hysteresis, extended
slots, responsive phone/tablet/desktop, nested exact Back and timeout pass.
Scenario A: before/after full 100px below image. B: before 85.16px cramped strip,
after 100px at original floorplan anchor. Only 4 configured cubes render.
Mandatory full local browser/module suite and exact-head push/PR CI are pending.
The initial local core browser run lacked v1.7.0 reference tag; all historical tags
fetched and complete core run restarted. Do not treat that initial failure as pass.

Evidence (outside Git): /workspace/build-output/beta6/, before/, after/, full/.
Browser plugin not available; repository Playwright/system Chromium, pinned public
HA floorplan and button-card. All HA services/state synthetic. No actual HA,
physical Android/PC, owner-floorplan or hardware acceptance claimed.

Next: finish mandatory regressions/reproducibility, resolve any failures, create
PR and freeze tested branch head. Require all exact-head push+PR build/lint jobs
and official HACS success, then use unchanged release.yml expected_commit/tag,
publish=true for NEW v1.10.0-beta.6. Independently verify tag, public bundle,
checksums/provenance and preservation of existing tags/releases/master/stable.
Do not move released branch during verification; final handoff on separate docs
branch after publication if needed. No environment configuration/publication work.
