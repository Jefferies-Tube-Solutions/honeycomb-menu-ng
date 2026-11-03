# Repository-wide architecture and dead-code audit — issue #154

Reviewed baseline: published `v1.10.0-beta.9`, commit
`0f2101d9b1b4377168ae7fd5643bf01672a1683b`. Owner authorization and the conditional
release decision are in [#154](https://github.com/NicolaiTandrup/honeycomb-menu-ng/issues/154)
and [#163](https://github.com/NicolaiTandrup/honeycomb-menu-ng/issues/163), latest
owner comments dated 2026-11-02. This report is Stage A: **no runtime,
dependency, test, asset or release configuration edits were made for the audit**.
Temporary reproduction scripts and raw evidence are outside Git in
`/workspace/build-output/audit154`.

## Decision: FIX path, not direct stable promotion

**One confirmed release-blocking defect: B1, XY Pad teardown can continue issuing
HA service commands after the menu has closed and detached.** This is an action
lifecycle/safety defect, not a proposed architecture cleanup. It was reproduced
against the exact public beta.9 bundle using mocked HA services.

Do not promote this runtime unchanged to stable. The owner-approved next step is
one targeted `v1.10.0-beta.10` fix PR from the exact beta.9 ancestry, full regression
and exact-source CI/HACS gates, then the unchanged guarded beta publisher.
**Stop after beta.10 publication for owner real-HA acceptance.** Issue #163's
stable path remains pending; beta.9's visual acceptance does not automatically
accept a changed beta.10 runtime.

All N findings below are **nonblocking**. They are follow-up proposals, not
permission to refactor this release or a reason to delay it further.

## Scope and method

The inventory covers all 280 tracked files: 71 source JavaScript files, all core
and module directories, public Hub/Control/menu/Info/XY adapters, build and
installation scripts, every workflow, package/lock/HACS/license metadata, assets,
75 test/fixture files and 37 documentation Markdown files, plus examples and
historical references. The audit combined production import/bundle graphs,
registry and custom-element registration, YAML/public-interface references,
function/caller and DOM/CSS tracing, lifecycle ownership review, existing contract
tests, targeted real-Chromium reproductions and actual artifact measurements.
This is not a claim that every PNG was visually reviewed or every hardware/browser
combination was tested.

The production graph was generated with the repository's locked webpack build:
70 of 71 tracked source modules are reachable, plus generated
`src/brand/bee.generated.js`. The sole unbundled tracked source file is
`src/event-manager.js`. CommonJS exports, dynamic module/presentation registry
lookups, custom elements, YAML actions/templates, CSS/DOM selectors and generated
assets were considered before labeling anything unused. The retained production
bundle is the HACS payload and is **not** a disposable build artifact.

Architecture reviewed by subsystem:

| Surface | Ownership and review result |
|---|---|
| `src/runtime.js`, `helpers.js`, entry menu | NG namespace/API, YAML templates, HA provisioning, custom-card creation and mounting; legacy error-path findings N1/N2 |
| `cube-element.js`, public adapters, renderer/CSS | One native renderer and pointer/keyboard/hold/double-tap engine; module presentation/config and explicit user overrides remain distinct from physical layout |
| `core/{module-registry,action-registry,cube-config,module-menu,hub-launcher}` | Six modules registered explicitly; dynamic `mode`/aliases and action handlers are reachable and must not be deleted based on import-name searches |
| `core/{layout,hub-allocation,visibility,navigation-context}` | Physical allocation, scalar dependency snapshots, nested/sibling Back and size bounds; compatibility helpers noted in N5 |
| Hub, `image-sizing`, `expanded-layout`, Collapsible/Beam | Separate owner anchor and expanded geometry; measured viewport/image frames, bounded updates, inert origin and shared top-layer teardown |
| Light | Capability-aware palettes, numeric presets, Kelvin/HS bounds, connection-scoped palette memory; duplicated Kelvin calculation N6 |
| Media/Sonos | Individual room volume vs coordinator transport, trusted metadata/artwork, native Favorites request budgets/epochs, Join stale-request guards, device-bound Sleep estimates |
| Climate | Explicit capabilities/units/choices, exact semantic defrost mapping, bounded pending commands, no optimistic physical-device success |
| Charger | Verified role/device mapping, units/freshness/connection/fault checks, bounded command state, deduplicated aggregate power; transport duplication N7 |
| Info | Shared shell, immutable source-paint snapshot, text/containment bounds, suspended caller, fixed lifetime and explicit cleanup; bounded recomputation opportunity N8 |
| XY Pad | Public classic input path, separate legacy mouse/touch engine; missing cancellation and teardown is B1 |
| Build/dev/install/release/retention | Deterministic artifact, immutable dev filenames/atomic manifest, source approval and staged-asset checks; no safety-gate changes recommended |
| Tests/docs/assets | Current and immutable historical fixtures mapped to CI/imports/documented consumers; documentation drift and test gaps N9–N11 |

## B1 — RELEASE-BLOCKING: detached XY Pad continues actions

**Locations:** `src/xy-pad.js::_bindListeners` (lines 106–115),
`_handleOnDragStart` (130–140), `_handleOnDragEnd` (172–176), and the absence of a
`disconnectedCallback`; `src/honeycomb-menu.js::_handleXYPad` (around 1757),
`close`, `dispose` and the Info suspension boundary. Public configuration is
documented in `docs/CLASSIC_MENU.md` under `xy_pad`.

**Proof:** In real Chromium with the unchanged beta.9 bundle, open a normal menu
with `xy_pad.repeat: 50` and a mocked `light.turn_on` x-axis service. Start a drag
at a nonzero x offset, then close it through `ng.close()` with `animate:false`.
The pad reports `isConnected === false`, but its interval is still active.
Mock service calls increased from **2 at close to 6 after another 180ms**.
Tracked document/window/viewport listener count increased from **20 to 22**
after removal. The two anonymous bound document end listeners have no stored
identity for removal. `menu._handleXYPad` has no closing/disconnected guard.
The pad's own Lit drag listener can still call the detached menu's handler.

This is not a speculative garbage-collection observation: it produces actual
mocked service dispatches after closure. The same ownership gap matters during
dashboard replacement/removal, cancellation and suspension. A close animation
also leaves a connected pad for a while, so disconnect cleanup alone is not
sufficient. The separate legacy path lacks the preview/Info checks present in
the native cube action pipeline and needs the same cancellation boundary.

**Impact:** unexpected repeated commands and retained controls/listeners in
long-running tablet/kiosk sessions. Inherited legacy code is still reachable via
supported YAML; age does not make this safe to ship knowingly.

**Necessary proposed fix:** store/remove the pad's bound listeners; cancel its
repeat interval and gesture without emitting a release action on cancellation,
detachment, menu close/dispose or Info suspension; make terminal events idle-safe;
reject callbacks in inactive/disconnected/closing/preview/suspended scenes. Cover
touch cancellation/background interruption as part of that same gesture lifetime.
Keep the existing mouse/touch geometry, XY values, repeat/on-release YAML and
service payload semantics. Do not replace it with a new gesture framework.

**Risk / cost / decision:** medium interaction-regression risk, small isolated
runtime change plus meaningful Chromium lifecycle tests. **Fix now** in the
single beta.10 remedial PR; verify normal drag/repeat/on-release/reconnect and
zero post-close calls, orphan timers or listener growth. No automatic stable.

## Ranked nonblocking findings

### N1 — NONBLOCKING, P2: late custom-card recovery has reversed event arguments

**Location:** `src/helpers.js::createCard`, lines 194–196; compare
`fireEvent(_node, _event, _detail, _options)` at line 4. The late-registration
callback calls `fireEvent("ll-rebuild", {}, el)` with a string as the node.

**Evidence / impact:** a synthetic `custom:audit-late-card` registered after the
error placeholder produces `dispatchEvent is not a function` and no real custom
card. The already-defined custom-element path works and is the documented setup
order. This optional compatibility recovery failure is a real defect, but it
does not issue unintended commands or invalidate accepted native module flows.

**Proposal / risk / cost / decision:** correct the event target/order and test
late registration, detach-before-registration and placeholder replacement in a
separate compatibility PR. Small cost; low-to-medium lifecycle risk. **Defer to
1.10.1**, rather than silently expanding the safety fix.

### N2 — NONBLOCKING, P2: XY service rejection leaves an axis busy

**Location:** `honeycomb-menu.js::_handleXYPad`: `_service[axis]` resets only in
the fulfilled `.then`, not a rejection/finally path.

**Evidence / impact:** a rejected mock request followed by another x drag leaves
`x_busy === true` and only one request. Reopening the menu restores input. This
fails closed (no continuing commands), unlike B1. It is not necessary to alter
that error-recovery policy to stop post-close actions.

**Proposal / risk / cost / decision:** a separate error-handling PR can reset the
axis, report failure and ensure no automatic retry or stale completion revives a
closed scene. Small cost; medium command-race risk. **Defer**, and keep it distinct
from B1's mandatory cancellation scope.

### N3 — NONBLOCKING, P2: old dependency/toolchain surface and unused direct Lit 2 adapter

**Locations:** `package.json`, root lockfile, webpack configuration; bundled
lodash calls in `helpers.js`/`honeycomb-menu.js` and config preparation.

**Evidence:** installed direct declarations are lodash, lit and lit-element, plus
webpack/webpack-cli development declarations. The locked tree uses
`lodash@4.17.19`, `lit@2.7.2`, direct `lit-element@2.5.1` and lit's nested
`lit-element@3.3.1`; webpack is 4.43.0. Bundle stats include only the nested Lit 3
adapter. No production import or public resource points to direct Lit 2.
The current npm advisory response reports **37 vulnerable package entries**
(7 critical, 24 high, 5 moderate, 1 low); these are package-level advisory counts,
not 37 demonstrated application exploits. Most are build/watch dependencies.
Runtime lodash is included and must not be waved away as dev-only: current
`omit` property paths/options are fixed and templating is already an explicit
trusted-YAML code boundary. No new untrusted-to-privileged exploit was established
by this audit. This is not a universal security certification.

**Proposal / risk / cost / decision:** separately remove the unused direct Lit 2
dependency, then update the locked toolchain/lodash with runtime, template,
generated-bundle and browser tests. Medium-to-substantial cost and medium/high
build/output risk. **Plan for a later tested development train**; never run
`npm audit fix` during metadata promotion or weaken checks to silence advisories.

### N4 — NONBLOCKING, P3: one orphan source helper and ambiguous legacy artifacts

**Locations:** `src/event-manager.js`, root `honeycomb-menu.js` (68,549 bytes),
historical GIFs/examples and versioned documentation.

**Evidence:** the production graph includes every tracked source module except
`event-manager.js`. There is no import, registry/custom-element registration,
YAML public action or current documentation consumer for its `EventManager` API.
Its line 1 also imports `lodash/isEmpty` under the `isArray` name, so its array
removal branch would be wrong if reused. Do not mistake that unbundled defect
for an active service-dispatch bug. The root legacy bundle is not the webpack
entry or HACS filename; the coexistence test downloads an exact original version
separately. Historical repository/raw URLs can still have external consumers.

**Proposal / risk / cost / decision:** delete the orphan helper only after owner
review, in a tiny cleanup PR. **Leave historical/public artifacts alone** unless
an explicit deprecation/archive decision is made. Low cost for the helper;
unknown external-API risk for old assets. No measured production bundle saving
should be claimed for deleting a file already excluded from that bundle.

### N5 — NONBLOCKING, P3: vestigial private fields and compatibility adapters

**Locations:** Hub `_anchorWatchRaf` and `_hubBaseFaceMode`; menu
`_stateRefreshTimer`, `_startStateRefresh`/`_stopStateRefresh`;
`core/collapsible-hub.js::mobileGeometry`, `layout.js::centerPosition`,
`navigation-context.js::canEstablishAnchor`.

**Evidence:** `_anchorWatchRaf` is initialized/checked but never scheduled; anchor
watching actually uses a local frame in `_watchAnchor`. `_hubBaseFaceMode` is
assigned but not read. State-refresh hooks are intentionally no-ops, so there is
no hidden polling timer to remove. `mobileGeometry` and `centerPosition` have
tests but no active renderer caller; `canEstablishAnchor` is called and currently
always true. These cases are not all equivalent to unreachable code.

**Proposal / risk / cost / decision:** remove private unused fields/no-op calls
in one low-risk PR; retain or explicitly deprecate exported/tested adapters and
the active promotion policy seam separately. Small cost, low private-field risk,
medium compatibility risk. **Defer**; no deletion based solely on grep.

### N6 — NONBLOCKING, P3: repeated math and default visual literals

**Locations:** Light `presentation.js::kelvinToRgb` and
`controls.js::kelvinToCssRgb`; renderer `_parseColor`/`_foregroundForBackground`,
menu `_lightenColorString`, core `cube-presentation.js::channels`;
`core/submenu-theme.js`, module presentation/menu descriptors.

**Evidence:** Kelvin conversion repeats the same clamping/constants/logarithms.
RGB/hex handling serves different purposes (contrast, brightness, gradient
policy); it is near-duplication, not proof those functions are interchangeable.
`#34383d` borders and `#202224` inactive fills repeat, but active Light/Sonos
colors, gray availability, neutral submenu fill, user colors and gradients are
deliberate distinct policies. The Bee asset/version already has one shared owner.

**Proposal / risk / cost / decision:** first consolidate only identical Kelvin
math with exact swatch tests; separately review base visual tokens while keeping
domain/user overrides explicit. Small/medium cost and medium visual risk.
**Defer**; do not impose one generic style on every module.

### N7 — NONBLOCKING, P3: registry transport and command-state near-duplication

**Locations:** `core/ha-capability-registry.js`, Charger `registry.js`, Climate
and Charger `actions.js`, Sonos `native-favorites.js`/`sleep.js`/`grouping.js`.

**Evidence:** Climate and Charger separately own WeakMap connection sessions,
full registry requests, reconnect listeners, epoch/version state and unsubscribe
cleanup. Climate needs generic exact semantic metadata; Charger deliberately
filters/verifies Easee identities. Their command records also have different
acknowledgement and failure policies. Native Favorites already shares/bounds
requests and has explicit abort/epoch handling. Sleep's two connection-lifetime
listeners are installed once per session, not once per cube; they must not be
misclassified as per-render listener leakage.

**Proposal / risk / cost / decision:** measure mixed-module discovery first,
then consider a shared read-only transport, preserving module verification and
bounded command ownership. Medium/substantial cost, high async/capability risk.
**Leave current behavior for this release**; no generic command framework rewrite.

### N8 — NONBLOCKING, P3: large controllers and repeated presentation work

**Locations:** menu (2,169 lines), CubeElement (1,268), Hub (801): together
4,238 of 9,947 tracked source lines; `InfoCube.hass/_relayout`,
Sonos Join `resolve` and station recognition; native `_dispatchAction` and the
legacy menu `_handleItemAction` bridge.

**Evidence:** each controller combines several lifecycle responsibilities;
Info recomputes geometry on HA updates before layout-signature reuse, and Join
can resolve room/source station presentation more than once. There is no
measured critical-frame slowdown from those paths in this audit. One native
renderer/gesture pipeline is shared by menu items and persistent Controls; the
legacy event bridge and classic popup/XY compatibility are distinct reachable
interfaces, not a second proven independent renderer to delete.

**Proposal / risk / cost / decision:** benchmark representative HA updates,
memoize only proven repeated pure work, then extract one ownership concern per
PR while preserving public APIs and action counts. Medium/substantial cost and
high navigation/visual risk. **Defer**; controller line counts alone are not a
release blocker or a target for arbitrary code removal.

### N9 — NONBLOCKING, P2/P3: current documentation contains historical drift

**Locations:** `ARCHITECTURE.md` module list/anchor invariant;
`docs/AI_SETUP.md` version contract; README and `docs/CHARGER_MODULE.md` older
stable/prerelease statements; historical candidate/release checklists.

**Evidence:** architecture prose predates Climate/Charger and selected-child
promotion; some README/Charger passages still call v1.8.1 latest stable while
the current badge/intro says v1.9.0. Historical v1.8/v1.9 checklists include
version-specific prohibitions that are records of those releases, not current
authorization. Current owner instructions and executable guards take precedence.

**Proposal / risk / cost / decision:** mark historical documents clearly, update
current overview/AI contracts and link to module-specific schemas in a docs-only
PR. Small/medium cost, low runtime risk but examples still need validation.
**Defer broad consolidation**; update only beta.10 release/status facts in the
remedial candidate. Do not rewrite historical release records.

### N10 — NONBLOCKING, P2: test coverage omitted the legacy XY lifecycle

**Locations:** `test/browser/run.py`, fixture/harness modules and
`.github/workflows/build.yml`; current Node/browser module suites.

**Evidence:** accepted beta.9 has 464 Node passes plus three explicit stable-only
skips and full green CI, yet the direct documented XY teardown reproduction
still sends post-close commands. Existing shared-Cube gesture, Beam and Info
tests do not establish XY cancellation safety. The browser harness HA stub keeps
its `clients` Set; it is not a faithful production heap-retention model.

**Proposal / risk / cost / decision:** add mandatory focused XY normal/action,
cancel/close/remove/reconnect, preview/Info and resource-count tests for B1 now.
Improve the fixture's heap instrumentation separately; **do not infer a
production memory leak from the fixture's retained Set alone**. Small cost for
the required tests; medium cost for a shared lifecycle harness. No broad test
rewrite or disabled assertions.

### N11 — NONBLOCKING, P3: historical regression harness/CI maintenance cost

**Locations:** the version-named Python suites, immutable before/reference
captures and CI's sequential browser steps.

**Evidence:** version names do not mean obsolete tests: current CI imports those
fixtures and protects native Favorites, original/NG coexistence, pixel bounds,
mobile placement, size ceilings and nested Back. Full exact-source push and PR
runs are deliberately expensive. Some helper/setup code and viewport loops repeat.

**Proposal / risk / cost / decision:** in a future test-only PR, consolidate setup
or partition independent suites while preserving target discovery, counts,
screenshots, checksums, underlying exit statuses and every mandatory gate.
Medium cost/risk. **Leave all current gates enabled** for beta.10.

## Positive results, metrics and limitations

Baseline normal HACS bundle: **329,534 bytes**, SHA-256
`0f0ed9a988bea5ea60da3e597b9b19a81a88986d2d67cc0ea6519d0cc4bf6141`;
gzip measurement with `mtime=0`: **104,250 bytes**. Rebuilding for the graph left
the tracked bundle unchanged. Stage A before/after runtime, dependencies and
bundle are therefore identical; no size/CPU improvement is claimed.

Node 20.20.2 benchmark, 1,000 relevant updates per row: p95 allocator/visibility
latencies were approximately 0.030ms (5 configured cells), 0.049ms (20), and 0.085ms (50). All 1,000 unrelated updates
per row produced **zero visibility reevaluations and zero reallocations**.
These are current-instance pure-core measurements, not browser rendering or a
historical speedup. Heap deltas include allocation/GC noise and are not retained
memory results.

Thirty real-Chromium Collapsible/Beam expansion/collapse cycles, including six
Info opens/returns, showed no growth in tracked active observers or global
listeners. Removing the owner restored the initial counts: 0 active resize
observers, 1 existing fixture mutation observer and 20 tracked global listeners.
No HA actions escaped those synthetic flows. This positive result does not
erase the separate reproducible B1 failure (two extra XY document listeners and
four additional mocked post-close actions).

The audit baseline reran core/Node tests and the targeted probes. Exact-source
beta.9 push/PR CI, HACS and guarded publication are independently linked in
[#162](https://github.com/NicolaiTandrup/honeycomb-menu-ng/pull/162). Their green
result is supporting regression evidence, not proof of every failure path.
New beta.10 changes require fresh full gates; old beta.9 greens cannot authorize
publishing modified runtime.

The stable approval code was reviewed as executable policy: canonical version
validation accepts `1.10.0`, approved beta identity is version-relative, and
`version-metadata-v2` narrowly permits the known banner/two build-info literals.
It rejects other source/build/dependency changes. That mechanism must remain
unchanged, but it must **not** be used to skip beta.10 owner acceptance after B1.
Retention remains required `false`; its inaccessible Variables API is not a
reason to invent credentials or bypass the workflow's direct `vars` check.

Real-HA beta.8/beta.9 visual acceptance is the owner's reported evidence. These
probes used synthetic HA, Chromium and controlled service failures. They are not
exhaustive device, Firefox/WebKit, native pinch/Android WebView, production load,
or formal memory/security proofs. No production HA action was performed.

## Minimal follow-up grouping

1. **Now:** B1 cancellation/teardown and its mandatory tests only, beta.10 PR;
   normal release metadata/docs and deterministic bundle are necessary packaging.
2. **Later compatibility PR:** N1 late custom-card recovery and N2 explicit
   rejected-service recovery, with separate regression cases and no automatic retry.
3. **Later dependencies PR(s):** N3 unused direct Lit dependency first, then a
   separately tested build/runtime dependency upgrade. Never mix with promotion.
4. **Owner-reviewed cleanup PRs:** N4/N5 private dead-code cleanup; N6 identical
   math/tokens only; N7/N8 measured ownership/presentation improvements, separately.
5. **Docs/tests PRs:** N9 current-contract documentation and N10/N11 harness/CI
   maintenance. Preserve historical source, releases, fixtures and public APIs.

No Car/v1.11 feature, HACS catalog submission, stable/master merge, destructive
retention or architecture rewrite is part of the selected remedial path.

## Remediation handoff — 2026-11-02, after guarded beta.10 publication

B1 received only the targeted XY/menu lifecycle fix in separate [PR #168](https://github.com/NicolaiTandrup/honeycomb-menu-ng/pull/168),
source `a54cd007fff030d14d89872c4026b92cf0184405`, based on exact reviewed beta.9.
[Public v1.10.0-beta.10](https://github.com/NicolaiTandrup/honeycomb-menu-ng/releases/tag/v1.10.0-beta.10)
was published by [guarded run 41540124243](https://github.com/NicolaiTandrup/honeycomb-menu-ng/actions/runs/41540124243)
after exact-source push/PR/HACS success. New mobile/desktop browser regressions
prove repeat cancellation, silent on_release interruption, normal payloads,
Info/preview/background safety and listener cleanup/reconnect; the close test
fails against immutable beta.9. No N finding was refactored into this candidate.

Independent anonymous downloads and GitHub asset digests match the committed
331735-byte bundle, SHA-256
`b9a89296839e9bab77de41673547053264617985c2adeec325174367502e15b5`.
All three assets, exact tag and CI-attempt provenance were verified. All 65 prior
releases, 120 assets and 118 tags remain unchanged. Master/latest stable remain
unchanged, and v1.10.0 stable is unpublished. No retention setting was changed.

The report and initial FIX decision were published before runtime edits; this
follow-up records Stage B's result on the same docs-only review branch. See
[permanent handoff and exact CI links](DEVELOPMENT_STATUS.md). **Stop for owner
real-Home-Assistant beta.10 acceptance on PAHA02-DEV before stable under #163.**

## Stable authorization after beta.10 acceptance

The owner accepted installed beta.10 in real Home Assistant and authorized stable
promotion in [#163](https://github.com/NicolaiTandrup/honeycomb-menu-ng/issues/163#issuecomment-6598062637).
The earlier beta.10 stop was honored; stable now pins its exact public source and
bundle through the existing manifest/guard. This carries the completed report
into release documentation without repeating the audit or optional cleanup.
