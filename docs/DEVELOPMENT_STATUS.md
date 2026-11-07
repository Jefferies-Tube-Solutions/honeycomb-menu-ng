# Jefferies Navigation v2.0.0 stable promotion

Promotion is prepared from exact beta source
`8814ee7481a95bf523b155889d1d4981b93dd445`. The owner tested v2 on PAHA02-DEV and
authorized stable in [the approval record](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/issues/171).
The manifest pins the expected public beta tag, source tree, size and checksum.
Verify the actual public beta asset and tag before promoting.

Keep the beta as an ancestor of the stable promotion commit. The version metadata
and public notice change, while the protected runtime and build inputs stay
pinned. Run the exact-commit checks in [the stable procedure](RELEASING.md).
Publication requires green push and PR checks, a normal master merge, green
exact-master CI, and the guarded verify-only and publish dispatches. Keep release
retention explicitly disabled.

## v2.0.0-beta.1 baseline

The rewrite is based on v1.10.0 stable, master commit
`25291186b07bfee81b8877fe731e00a417d56c12` (PR #169). The preceding promotion
and owner acceptance are recorded in [the v1.10.0 release checklist](V1_10_STABLE_RELEASE.md)
and issue #163. Previous release history remains available at the original tags.

Feature branch: `feature/jefferies-navigation-v2`. The public names, resource
and YAML changes are listed in [V2_MIGRATION.md](V2_MIGRATION.md). The compass
is a round dial rendered from the approved Draft 02 scene. The shared cell draws
the outer hexagon. The [branding gate](BRANDING.md) pins the runtime dial, public
publisher artwork and product identity. The shared renderer, positioning
engine, action registry, module boundaries and XY Pad teardown stay in place.

Run `npm ci`, `npm test`, `NODE_OPTIONS=--openssl-legacy-provider npm run build`,
`node scripts/check-beta.js` and `node scripts/check-hacs-package.js`. CI runs
the Chromium and documentation regression matrix. See the feature branch
checks for results tied to its commit.

Use the separate PAHA02-DEV dashboard for real Home Assistant verification.
Publication uses the existing guarded manual beta workflow on the exact green
feature-branch SHA, with a verification-only dispatch before publication. Keep
release retention disabled.
