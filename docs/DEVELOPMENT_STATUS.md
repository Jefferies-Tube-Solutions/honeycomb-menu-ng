# v1.10.0 stable promotion from owner-accepted beta.10

Branch: release/v1.10.0-stable, directly from public beta.10
`a54cd007fff030d14d89872c4026b92cf0184405`. Owner installed/tested that beta in
real HA and explicitly authorized stable merge/publication in #163, comment
6598062637. No additional general approval is needed. Do not repeat audit #154.

## Scope and source contract

Single cumulative promotion PR to master. Only version/release metadata, approval
manifest, necessary promotion tests and documentation may change. Source, assets,
HACS filename, dependencies and build semantics remain approved beta.10. Bundle
may differ only in banner and two canonical build-info version literals. Manifest
pins beta.10 source/src tree, public SHA-256 and size. Preserve XY safety, Beam,
Climate, Sonos, Charger, Info, shared Bee, approved placement/sizing and YAML.

Audit is complete; [report](ARCHITECTURE_AUDIT_154.md) is retained here from docs-only
#164. Its blocker was fixed/published in beta.10 (#168); optional #165–#167 stay
deferred. Do not merge historical beta PRs individually or begin v1.11/Car.

## Execution checkpoint — publication not yet complete

Read [stable checklist](V1_10_STABLE_RELEASE.md) and [guarded procedure](RELEASING.md).
Next: finish local source/artifact/docs checks, commit/push this branch, create the
single PR, require exact-head push/PR full CI and official HACS success. Then
merge normally, verify actual master/source/normalized bundle and await full
exact-master CI. Dispatch stable-release.yml first publish=false then publish=true
using the same full green master SHA. Independently verify public latest stable,
assets/checksums/provenance/HACS and preserved history before reporting completion.

RELEASE_RETENTION_ENABLED must remain explicitly false. The existing stable
publisher checks it and forces retention dry-run only. Never query/change the
inaccessible Variables API, bypass a failed gate, force refs or delete old tags,
assets, releases, drafts or branches. No production HA commands/access.

Local/remote gate results and final source/CI/release details will be recorded in
#163 and the final permanent handoff after publication. Evidence outside Git:
/workspace/build-output/stable110. Do not infer completion from a prepared PR,
master merge, dispatch or this checkpoint. Keep exact candidate/master fixed
through validation/publication. Put later handoff-only updates on a separate
branch so the released master SHA stays pinned.
