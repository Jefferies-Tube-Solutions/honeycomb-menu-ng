# v1.10.0-beta.9 — Beam of Origin implementation and validation

Branch: feature/v1.10-beta9-beam-of-origin. Exact cumulative baseline is the
published, owner-real-HA-accepted beta.8 source
3ff151adff815d933ddf786169a795ee704f5790. No master merge, stable release, live HA
commands or architecture review #154 are authorized by this feature task.

Optional collapsible.beam_of_origin (true or {color}, default OFF) adds a live,
inert source reference through the existing CubeElement renderer and owner-fed
HA state. Internal visualOnly avoids independent module/device subscriptions;
interactive:false plus inert/aria-hidden/pointer-events:none prevent actions and
focus. Source retains measured collapsed geometry; active physical hex boundaries
supply the softly feathered tapered SVG fan. The measured cluster silhouette
sets its wide end; each attachment is projected to a real hex boundary. Unique per-Hub gradients share the
existing popover, above its shield/backdrop and below controls and Info overlays.
Near/overlap/offscreen/unsupported sources suppress the reference. Existing
placement solver, original parent size ceilings, Bee and navigation are unchanged.
Bounded rAF updates follow existing layout/resize/scroll/visualViewport/navigation
notifications and animation completion; no new long-lived observers or polling.
Collapse/close/dispose/removal/reconfigure tear down the optional scene.

Current local evidence in /workspace/build-output/beta9 (outside Git):
- Node20 core contracts and 464 Node tests pass; 3 existing stable-only skips.
- Beam suite covers mobile/desktop live state, inert source, measured geometry in
  every direction, all module entry/Back, Radio/White, Info priority, multiple
  Hubs, crop/zoom/resize, size60/82/100/auto and Bee debug, timeout/outside/Escape.
- Six default-off screenshots are pixel-identical to immutable beta.8 (collapsed,
  expanded, restored; 390x844 and 1440x900).
- Approved mobile placement regression and complete docs/YAML validation pass.
- All 45 policies in the beta.8 five-viewport size/module matrix pass. The old
  process reported its hard-coded beta8 Bee aria-label failure; that assertion
  now checks the installed version and passes in an independent five-viewport
  diagnostic rerun. Final exact-SHA CI runs the complete corrected suite.
- Local HACS payload/beta metadata and checksum-verified actionlint pass.
- New beam suite is mandatory in build.yml. Release workflow/guards unchanged.

Outstanding before publication: exact-final-SHA push/PR CI and official HACS,
final reproducible bundle/checksum/source integrity, complete release evidence.
Both #156 reference images were supplied directly in the task and reviewed: the
annotation requires a cluster-wide facing fan, and the concept is intentionally
much brighter than the requested implementation. The fan follows that measured
silhouette with .34 source opacity fading to .025 at destination, 1.5px feather,
no stroke/glow/continuous animation and no copied decorative labels/dashboard.
The temporary environment-domain draft addition was removed; no network setting
change is required now. Do NOT publish if any mandatory release gate fails.

Owner authorizes guarded beta.9 publication only after all mandatory gates pass.
After publication, stop for owner testing on PAHA02-DEV. Synthetic QA does not
establish beta.9 real-device acceptance. Existing releases/tags and PR #161 remain
unchanged; there is no stable/master merge in this task.
