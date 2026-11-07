# Jefferies Navigation v2 rewrite decisions

## 2026-11-06

| Decision | Reason | Consequence |
| --- | --- | --- |
| Use Sol Medium for implementation and keep deployment and release verification separate. | This is a broad cross-file refactor with established behavior to preserve. | One implementation owner; deployment and publication use independent verification. |
| Start from the current master commit `25291186b07bfee81b8877fe731e00a417d56c12`. | The stable HC behavior is the comparison baseline. | Prior releases and unrelated historical work are preserved. |
| Rename product-owned namespaces, element names, modules, assets and configuration keys as required for JTS-N. Preserve the shared rendering and control behavior. | The owner explicitly waived backward compatibility while requiring feature parity. | Existing HC configurations will need new names when manually moved to JTS-N. Attribution and historical records remain. |
| Use the approved Draft 02 compass from the JTS Brand System. | The icon already has owner approval and a registered source. | Preserve compass provenance and the existing control's behavior and accessibility. |
| Use a separate test dashboard and resource on development HA. | This allows side-by-side checks and an independent rollback path. | Existing HC dashboard is retained as a comparison baseline. Tests that could actuate real devices use mocks. |
| Publish only from the guarded beta workflow after exact-candidate CI and development-HA acceptance. | This is the agreed publication gate. | No stable promotion or release until the exact tested candidate passes. |
| Keep this running log on its own GitHub branch. | The owner requested an independent, recoverable record. | Decisions are available independently of the rewrite worktree or feature branch. |

## Current checkpoint

Baseline located. Development host and file-share access verified. Rewrite and acceptance pending; no beta has been published.

### Namespace and packaging

- The dashboard card types are `custom:jts-n-hub` and `custom:jts-n-control`. The Info Cube is the `jts-n-info-cube` overlay, opened with the `jts-n-info` action. Product-owned popup configuration uses `jts_n_menu`; shared domain terms such as Light, Sonos and Climate remain recognizable.
- Use `jefferies-navigation.js` as the distribution bundle and `window.jefferiesNavigation` for build diagnostics. Keep the GitHub repository and its release history under the current slug for this beta. Changing the repository itself is a separate catalog and distribution decision.
- Use SemVer `v2.0.0-beta.1` for the requested v2.0 beta-1, as required by the guarded publisher.
- Register resources and create the separate dashboard through Home Assistant's supported interface. Do not edit live `.storage` files directly. File access to the dev host and an existing authenticated browser view were verified. Browser input later became unavailable, so dashboard creation is still pending.
- Development installs use `/local/jts-n-dev/jefferies-navigation.js` and an immutable, content-hashed runtime. The legacy dashboard resource is kept separate.

### Verification checkpoint

- The rebrand uses the existing shared renderer, action dispatch and control modules. The Compass replaces the Bee as the visible brand control and retains version inspection and collapse/back semantics.
- The initial v2 build passed local HACS, license, checksum and eight legacy coexistence checks. A Windows run passed 457 Node tests; seven local shell/platform checks require the Linux CI run. Historical browser fixture mismatches are being repaired separately from the runtime.
- The deployment check compares the running diagnostics with the installed manifest and exact commit. Device writes are exercised using mocks, with a read-only dashboard for real Home Assistant smoke testing.

### Candidate handoff

- [Draft PR #170](https://github.com/Jefferies-Tube-Solutions/honeycomb-menu-ng/pull/170) records the v2 feature branch. Candidate commit `e1747ddf0fa6645565c64d2815d53732a66517ec` has the same Git tree as the local candidate.
- The production bundle SHA-256 is `c368a81f5a154e6accf1494d4fb3f7bd0cb7c5b73879d990ef4ed46dcd8f3a0a`. Historical test-fixture fixes do not change the bundle.
- The repository remains under the old slug while the dashboard product and release asset use Jefferies Navigation. The draft PR starts CI while keeping the stable branch intact.

### Development deployment and release hold

- Installed exact candidate `e1747ddf0fa6645565c64d2815d53732a66517ec` on the development Home Assistant under its separate static resource folder. The server serves version `2.0.0-beta.1-dev+e1747ddf0fa6`. Runtime SHA-256 is `0691711888d7ed70104661a49b7c5536435062f61d974490a00a32aac6499126`.
- Downloaded the loader and runtime from the development host and verified both manifest hashes. Ran those exact bytes in a synthetic browser fixture at 1280×820 and 390×844. Both passed custom element registration, Compass version inspection and Info Cube open/return, with no browser errors or device service calls.
- Do not treat the fixture as a real Home Assistant dashboard acceptance. The authenticated browser view was readable, but browser input was denied. Dashboard resource registration and the dedicated Lovelace test page remain pending. The [read-only test dashboard YAML](fixtures/jts-n-dev-dashboard.yaml) is available on this branch. Keep the existing HC dashboard as a comparison and do not edit Home Assistant internal storage directly.
- To resume in the authenticated development UI, register the JavaScript module `/local/jts-n-dev/jefferies-navigation.js`, create the separate read-only test dashboard, reload, and verify the compass, installed version, Info return and collapse/back behavior. The production beta workflow remains on hold until the acceptance and exact-head CI gates pass.

### Exact-head CI result

- The [pull request build](https://github.com/Jefferies-Tube-Solutions/honeycomb-menu-ng/actions/runs/42300758884) and [push build](https://github.com/Jefferies-Tube-Solutions/honeycomb-menu-ng/actions/runs/42300731558) both finished green for `e1747ddf0fa6645565c64d2815d53732a66517ec`. Both passed the build and workflow-lint jobs, including Ubuntu tests, browser regressions, documentation and reproducibility.
- The beta has not been tagged or released. The remaining gate is acceptance in the authenticated Home Assistant dashboard on the development instance. After acceptance, use `release.yml` on `feature/jefferies-navigation-v2` with the same full SHA and tag `v2.0.0-beta.1`: verify first, then publish. Preserve the stable release and existing retention policy.

### 2026-11-07 dashboard and Compass correction

- Reuse the existing Honeycomb NG Test dashboard at its current URL. This supersedes the separate-dashboard decision. Preserve the layout, entities, actions and other cards. Keep a local backup before saving the converted dashboard. The live dashboard config and identifiers stay out of GitHub.
- Use the round compass dial from approved Draft 02 for the in-card graphic. Keep the approved full hexagonal brand artwork for standalone branding. The card renderer already supplies the hexagonal frame.
- The previous development installation copied and verified static assets. It did not register the resource or migrate the live dashboard. Those steps remain separate acceptance gates.

### Repository identity and future releases

- The desired repository slug is `Jefferies-Tube-Solutions/jefferies-navigation`. This supersedes the earlier choice to retain the old slug for beta. Keep the same repository history and existing release records.
- v2 is a clean cutover. Do not add HC aliases, resource shims, compatibility adapters or fallback bundle filenames. Historical documentation, license notices and existing release records keep their original identity.
- Future candidates must pass an automated branding check through the existing CI and release test entry points. Document the approved artwork source and separate the circular in-card image from the full hexagonal product logo. Record asset hashes and confirm naming/packaging rules.
