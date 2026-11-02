# Audit #154 complete; beta.10 published; owner acceptance required

This docs-only audit branch retains the reviewed beta.9 runtime. The installable
fix is on `fix/v1.10-beta10-xy-lifecycle`, not this review branch.

## Immutable source and release

- Reviewed/owner-accepted beta.9: `0f2101d9b1b4377168ae7fd5643bf01672a1683b`.
- Audit: [PR #164](https://github.com/NicolaiTandrup/honeycomb-menu-ng/pull/164),
  [report](ARCHITECTURE_AUDIT_154.md); report and FIX decision published before runtime edits.
- Focused beta.10: [PR #168](https://github.com/NicolaiTandrup/honeycomb-menu-ng/pull/168),
  source `a54cd007fff030d14d89872c4026b92cf0184405`.
- Public prerelease: [v1.10.0-beta.10](https://github.com/NicolaiTandrup/honeycomb-menu-ng/releases/tag/v1.10.0-beta.10).
- Bundle: `honeycomb-menu-ng.js`, 331735 bytes, SHA-256
  `b9a89296839e9bab77de41673547053264617985c2adeec325174367502e15b5`.

## Audit and fix

Audit covered the tracked repository, production graph/public YAML/registries,
all runtime subsystems, lifecycle/performance, build/dependencies, release gates,
tests and documentation. One confirmed release blocker: a detached XY Pad kept
issuing repeat HA service commands and retained global listeners. Eleven
nonblocking findings are deferred in #165–#167; no cleanup is required for stable.

Only XY Pad/menu lifecycle runtime changed from beta.9: stop and silently cancel
repeats on close/disposal/removal, Info, preview, background/blur, input cancel
and config replacement; remove/rebind listeners; guard late callbacks. Normal
mouse/touch service data and YAML remain compatible. No Beam, placement, parent
size ceiling, Bee, renderer, module or dependency refactor is included.

## Verified gates

All runs completed successfully for the exact beta.10 source above:

- [Push CI](https://github.com/NicolaiTandrup/honeycomb-menu-ng/actions/runs/41533813896): Build and workflow-lint.
- [PR CI](https://github.com/NicolaiTandrup/honeycomb-menu-ng/actions/runs/41533858869): Build and workflow-lint.
- [Official HACS](https://github.com/NicolaiTandrup/honeycomb-menu-ng/actions/runs/41533860259).
- [Guarded beta publisher](https://github.com/NicolaiTandrup/honeycomb-menu-ng/actions/runs/41540124243): verification/reproduction and publication.

Node core plus 464 tests passed, with 3 existing stable-only skips. Full Chromium
module/presentation/Info/Climate/Charger/Sonos and responsive placement/size/Beam
suites, new mobile/desktop XY cancellation/payload/20-cycle cleanup/reconnect
suite, docs/YAML/links/examples, performance/package and actionlint gates passed.
Two local builds were identical; publisher compared committed/rebuilt/CI/staged
bytes. Independent public download checks verified all three asset digests,
checksum, source tag and exact push/PR attempt provenance. Anonymous release/
bundle downloads and HACS published-beta discovery succeeded.

Preserved all 65 historical releases, 120 assets and 118 tags, including frozen
drafts, against the pre-audit inventory. No old metadata/assets/tags were changed.
Master remains `ba95dade58fa64c5183a312e0d1d00044feeb096`; latest stable remains
v1.9.0. v1.10.0 stable is unpublished. No retention setting change or deletion,
master merge, production HA access or unrelated development was performed.

Raw local evidence is outside Git in `/workspace/build-output/audit154` and
`/workspace/build-output/beta10`; CI preserves synthetic screenshot evidence.

## Next action — owner real Home Assistant acceptance, then #163

Stop here as required by the latest #154/#163 owner instructions. In HACS enable
beta versions, redownload v1.10.0-beta.10 and refresh frontend/resource caches.
YAML needs no changes. On PAHA02-DEV test repeat/on_release XY operation and
close, Back, Info, timeout, background/return; verify accepted Beam/navigation,
placement, size ceilings and modules. Tests use mocked services only and do not
establish physical HA/HVAC/charger/browser acceptance.

Keep #163 open. Do not merge PR #168 or publish stable until explicit owner
real-HA beta.10 acceptance. After that, follow the unchanged exact-source stable
promotion gates using the accepted immutable beta.10 evidence; never substitute
beta.9 silently or re-merge the historical cumulative beta PRs.
