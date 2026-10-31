# beta.6 mobile free-canvas follow-up — implementation complete, not released

Branch: fix/beta6-mobile-free-space. Implementation commit:
3d60a4d7b9f97d438ca3f99daa29e7c7973f7b7f (subsequent handoff is documentation only).
Published beta.6 baseline: 6db9e046da496c5d6d437d8d0da08346136ec11f;
its immutable tag/release and fix/v1.10-beta6-placement branch remain unchanged.
Parent PR #157 remains open. The follow-up PR is stacked on that release branch.
Use `gh pr view fix/beta6-mobile-free-space` for the latest review/head/CI evidence;
verify actual runs rather than treating this checkpoint as proof of later CI.

Authorized scope: issue #148 mobile expanded-Hub placement only. Latest owner
comment and user follow-up read. No Beam of Origin #156, architecture review #154,
main/master merge, stable, production HA or environment configuration change.
No new beta label or publication is authorized; do not overwrite beta.6 assets/tag.
Owner mobile acceptance failed on published beta.6; full-size physical PC acceptance
remains unverified. Synthetic desktop tests never establish owner real-HA acceptance.

Root cause measured on 390x844: safe viewport [16,16..374,828], image bottom295.39,
original cube0 (195,147.88). Actual four-cube footprint fits below at100px, but the
19-slot planning envelope fits only71.6px, so beta.6 rejected it and overlaid image.
Follow-up keeps100px and places cube0 at(195,567.70), fully below the image.

Implementation: placeRoot first keeps beta.6's existing size/planning decision.
Small-screen behavior is determined by whether the standard working envelope can
fit the entire safe viewport at desired expanded size (not a new CSS breakpoint).
If constrained and existing small_screen behavior is enabled, examine every free
region using ALL actual visible controls at the already chosen size. Prefer below
if it fits; otherwise usable area and logical cube0 centering. Overlay the image
only when no external region fits. Desktop planning/85-84% hysteresis/origin fallback
remain byte-for-byte equivalent in tested desktop outcomes. Child geometry remains
actual-footprint based; original anchor and exact Back/collapse behavior retained.
Existing compact-phone opt-out (including legacy mobile alias) is untouched.

No YAML keys/names/defaults or package/release versions changed. Minimal
collapsible:true and all existing configurations remain compatible. Only shared
geometry/root lifecycle calls, tests/CI coverage, guide and rebuilt bundle changed.

Implementation-checkpoint validation:
- Node20 core contracts +459 Node tests pass, 3 existing stable-only skips.
- Chromium follow-up: four phone/landscape/tablet cases plus desktop matrix/panel
  cases pass; exact nested Back/collapse and no console/page errors verified.
- 8 desktop before/after PNGs are pixel-identical: 1440x900,1920x1080,2560x1440,
  3440x1440, each full19-slot full-size free region and cramped-strip origin fallback.
- Two-sided narrow panel/safe insets, translated/cropped image, orientation pass.
- Existing beta.6 five-case threshold/extended-slot suite passes. Full 49-case
  geometry/navigation matrix is running at this checkpoint; consult final PR/CI.
- HACS/local packaging/integrity, pinned actionlint and byte-identical rebuild pass.
- Browser plugin not available; existing Playwright/system Chromium used. No live HA.

Evidence outside Git: /workspace/build-output/beta6-mobile/; before/, after/,
matrix/, desktop-regression/, node.log. JSON records actual/planning footprints,
image/safe viewport, external candidates/rejection reasons, size, original/selected
anchors and actual bounds. Before bundle is exact published beta.6 payload.
Fixture corrections: restored a test-local bounding-box variable accidentally
shadowed by a boolean; panel anchors must be visibly clickable. Existing chrome
classification treats a full-height panel wider than half the viewport as a
horizontal band too; chrome detection was not changed by this placement-only fix.
The constrained-panel regression uses ordinary side panels leaving narrow canvas.

Next: finish/check complete geometry matrix and exact-head push/PR CI, report
actual results on the follow-up PR. Keep follow-up unreleased for owner review.
Do not auto-publish, overwrite beta.6, merge master, or begin #154/#156. Owner must
verify Android/mobile and PC in real HA; next corrective beta label needs agreement.
