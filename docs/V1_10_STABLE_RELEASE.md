# v1.10.0 stable promotion

Owner [real-HA beta.10 acceptance and stable authorization](https://github.com/NicolaiTandrup/honeycomb-menu-ng/issues/163#issuecomment-6598062637)
satisfies the remaining #154/#163 gate. Audit [report](ARCHITECTURE_AUDIT_154.md)
is complete; the XY lifecycle blocker is fixed and nonblocking #165–#167 deferred.
This is a single cumulative metadata-only promotion, not another feature beta.

## Approved immutable source

- Public beta: v1.10.0-beta.10, source a54cd007fff030d14d89872c4026b92cf0184405.
- src Git tree: da8678487d3360cc1136c88ca2f7a4780144e0b4.
- Public JS: 331735 bytes, SHA-256
  b9a89296839e9bab77de41673547053264617985c2adeec325174367502e15b5.
- release-approval.json pins those facts and issue #163. Existing version-metadata-v2
  guard requires identical src/assets/dependencies/build inputs and normalized
  bundle, allowing only the banner and two canonical build-info version literals.

## Local candidate evidence

Stable bundle: 331711 bytes, SHA-256
0b1b9736ef9b5b22d1d4896c5709c4524c408ead5d56258b39fff6587e27b17c.
Two builds were byte-identical; all 467 Node tests passed with zero skips,
including actual-manifest approved-source/bundle gates. Local HACS/GPL packaging
passed. Security audit reports exactly the same 37 advisories as completed #154;
that report classifies the unchanged findings as nonblocking and #166 tracks
follow-up. No dependency upgrades or new exposure enter this promotion.
Exact-head full push/PR/master CI, official HACS and publisher results remain
mandatory remote gates; local evidence is not a substitute.

## Required execution

1. Release branch release/v1.10.0-stable starts directly at the approved beta.10
   commit. One cumulative PR targets master; historical beta PRs stay unmerged.
2. Run Node, complete Chromium module/XY/Beam/size/placement regressions, native
   Sleep boundary, performance, docs/YAML/links, HACS/GPL/package, workflow lint,
   deterministic builds, checksum and public-beta/source approval validation.
3. Require exact candidate push AND PR CI and official HACS success. Stable CI
   reads vars.RELEASE_RETENTION_ENABLED directly and requires exact false.
4. Merge only the matching green cumulative PR normally with a merge commit.
   Verify actual master SHA/ancestry/src tree and reproducible normalized bytes.
5. Wait for full exact-master Build and workflow-lint CI. Dispatch unchanged
   stable-release.yml on master with that SHA and publish=false; require success
   with publication/retention skipped and no new tag/release. Then dispatch the
   same exact SHA with publish=true and require guarded publication success.
6. Independently verify public/latest/non-prerelease v1.10.0, exact master/tag,
   three downloaded asset digests, checksum, public beta and CI provenance, HACS
   root filename and all old release/asset/tag/branch inventory. Post-publication
   retention must be dry-run only with cleanup skipped. No deletions/settings changes.
7. Update permanent handoff and #163 with actual evidence, close only after all
   independent checks pass, then stop. No v1.11/Car or production HA changes.

## Acceptance boundaries

Owner installed/tested beta.10 in real HA and approved stable. Automated tests use
synthetic HA with Chromium desktop/tablet/mobile; they do not prove every physical
HA/HVAC/charger model, browser or native pinch scenario. Existing Beam suppression
and inherited layout/capability limitations remain. No accepted runtime changed.

Exact current PR/CI/publication evidence is in [development status](DEVELOPMENT_STATUS.md)
and issue #163; pending checks must not be inferred as passed from this checklist.
