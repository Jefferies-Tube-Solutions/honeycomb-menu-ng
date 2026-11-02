# v1.10.0-beta.10 — targeted release-blocker fix after audit #154

Branch: `fix/v1.10-beta10-xy-lifecycle`, based on exact public, owner-accepted
beta.9 `0f2101d9b1b4377168ae7fd5643bf01672a1683b`. Master and all historical
releases are preserved. Do not merge historical cumulative beta PRs.

## Published audit and conditional decision

The complete repository-wide audit is published separately, before runtime
changes, in docs-only [PR #164](https://github.com/NicolaiTandrup/honeycomb-menu-ng/pull/164)
and [issue #154](https://github.com/NicolaiTandrup/honeycomb-menu-ng/issues/154#issuecomment-6589394815).
It distinguishes one confirmed release blocker from eleven nonblocking findings,
with module graph, dependency, performance and Chromium lifecycle evidence.
Follow-up issues #165–#167 defer optional recovery/toolchain/cleanup work.

Selected **FIX** under the latest owner instructions in #154/#163: published
beta.9 XY Pad repeat calls continue after close, its interval remains active and
document listeners are retained. This is unsafe post-close action dispatch.
Keep v1.10.0 stable unpublished. Publish only focused beta.10 after all gates;
then stop for owner real-HA acceptance on PAHA02-DEV before stable promotion.

## Candidate scope and validation

Runtime changes only in `src/xy-pad.js` and `src/honeycomb-menu.js`: cancel repeats
at close/dispose/removal, suspend gestures on Info/background/blur/cancel/config
change, clean up named listeners and reject late closed/suspended XY callbacks.
Cancellation emits no release action. Normal mouse/touch payloads and YAML are
preserved. No rejected-service recovery refactor, dependency update, new feature,
renderer, Beam, placement or size-policy change is included.

`test/browser/beta10_xy.py` verifies both mobile and desktop, normal mouse/touch
and exact payloads, repeat and on_release, animated close, direct disposal/removal,
Info, preview, cancellation/background, reconnect and 20 repeated cleanup cycles.
It is mandatory in push/PR CI alongside all existing Node, module, responsive
geometry, Beam, documentation, package, reproducibility and workflow checks.

Local evidence lives outside Git in `/workspace/build-output/audit154` and
`/workspace/build-output/beta10`. Full final-source CI/HACS and guarded workflow
results must be verified from GitHub, not inferred from this checkpoint. The
publisher must match branch HEAD, exact-source green push AND PR CI, valid new
beta tag, deterministic bundle, SHA-256 and provenance. Do not bypass any gate.

## Authorized remaining sequence

1. Finish local verification, commit/push this focused candidate and open a PR.
2. Require exact-head push/PR Build and workflow-lint plus official HACS success.
3. Dispatch existing `release.yml` on this branch with final full expected SHA,
   `expected_tag: v1.10.0-beta.10`, approved notes and `publish: true`.
4. Independently verify public prerelease/tag/source, three assets, SHA-256,
   provenance and public HACS beta availability; preserve old release inventory.
5. Record final URLs/SHA/results in the PR and issues #154/#163. **Stop for owner
   real-HA beta.10 acceptance; do not automatically publish stable or merge master.**

Owner acceptance of beta.9 does not cover this changed runtime. All service tests
use synthetic Home Assistant. No production HA access, Car/new modules or broad
architecture cleanup is authorized. Retention remains disabled; no release/tag/
asset deletion or retention setting change is part of this task.
