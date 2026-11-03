# v1.10.0 stable published and independently verified

Release execution #163 is complete. This handoff-only branch retains the exact
published master runtime and records final evidence without moving released master.

## Source, approval and public release

- Promotion PR [#169](https://github.com/NicolaiTandrup/honeycomb-menu-ng/pull/169)
  merged normally from `5701937fc6b4eb143727d35565b5884962f957c8`.
- Actual merged/published master: `25291186b07bfee81b8877fe731e00a417d56c12`.
- [Public v1.10.0 Stable](https://github.com/NicolaiTandrup/honeycomb-menu-ng/releases/tag/v1.10.0):
  draft=false, prerelease=false, GitHub latest stable; tag matches that master SHA.
- Approved real-HA beta.10: `a54cd007fff030d14d89872c4026b92cf0184405`,
  src tree `da8678487d3360cc1136c88ca2f7a4780144e0b4`.
- Owner installed/tested beta.10 and authorized stable in #163, comment 6598062637.
  The completed #154 audit and focused beta.10 fix are retained; #165–#167 remain
  optional follow-ups. No historical beta PR was merged individually.

Runtime, dependencies, assets, HACS config and build semantics equal approved
beta.10. Existing version-metadata-v2 guard proves bundle differences are only
the banner and two canonical version literals. XY safety, Beam, Climate, Sonos,
Charger, Info, Bee, placement, size ceilings and YAML are preserved.

## Completed exact-source gates

| Gate | Verified result |
|---|---|
| [Candidate push CI 41598327727](https://github.com/NicolaiTandrup/honeycomb-menu-ng/actions/runs/41598327727) | Success, attempt 1, candidate 5701937 |
| [Candidate PR CI 41598358647](https://github.com/NicolaiTandrup/honeycomb-menu-ng/actions/runs/41598358647) | Success, attempt 1, same candidate |
| [Candidate official HACS 41598386305](https://github.com/NicolaiTandrup/honeycomb-menu-ng/actions/runs/41598386305) | Success |
| [Exact-master CI 41603602129](https://github.com/NicolaiTandrup/honeycomb-menu-ng/actions/runs/41603602129) | Build and workflow-lint success, attempt 1, master 2529118 |
| [Master official HACS 41603661185](https://github.com/NicolaiTandrup/honeycomb-menu-ng/actions/runs/41603661185) | Success, same master |
| [Stable verify-only 41609078871](https://github.com/NicolaiTandrup/honeycomb-menu-ng/actions/runs/41609078871) | Verification/reproduction success; publish/retention skipped; no tag/release created |
| [Stable publication 41609230370](https://github.com/NicolaiTandrup/honeycomb-menu-ng/actions/runs/41609230370) | Verify and publish success; retention inventory success, cleanup skipped |

All 467 Node tests passed with zero skips, including the actual stable approval,
source-equivalence and negative publication-integrity gates. Full Chromium
module/presentation, Light/Sonos/Favorites/Sleep/Charger/Info/Climate, editor and
coexistence tests, responsive Hub/placement/five-viewport size/Beam regressions,
XY mouse/touch/payload/cancellation/reconnect/20-cycle cleanup, native Sleep
boundary, performance, docs/YAML/links/rendered examples, package/GPL/HACS and
pinned actionlint passed in candidate push/PR and exact-master CI.

Two local builds were identical; both stable workflow dispatches reproduced and
compared committed/rebuilt/CI/staged bundle/checksum bytes. Security scan reports
exactly the same 37 dependency advisories as audit #154, deferred as nonblocking
to #166; no dependency upgrade or new exposure entered this metadata promotion.

## Independently verified public assets

| Asset | Bytes | SHA-256 |
|---|---:|---|
| honeycomb-menu-ng.js | 331711 | 0b1b9736ef9b5b22d1d4896c5709c4524c408ead5d56258b39fff6587e27b17c |
| SHA256SUMS.txt | 87 | d466b7b0d328589611b3a17a295b4eccf6e249e77e7db81a207fc793c0ff3a01 |
| release-provenance.json | 858 | 2dc578d5e02b65750ce8a95039b2aae0f962bba587cb4c0534e8f8702e188fad |

Anonymous release metadata plus tagged and latest bundle downloads match the
committed bytes. All server asset digests, checksum contents and exact-master
CI attempt/approved-beta provenance match. HACS root filename/content-in-root
and public stable discovery are valid. Catalog listing remains a separate task.

All 66 prior releases, 123 assets, 119 tags and 140 prior branches were preserved;
only the authorized master merge changed an old branch. Frozen drafts remain
unchanged. Retention stayed explicitly false at CI/publication gates; forced
read-only retention inventory succeeded and cleanup was skipped. No deletion,
overwrite, force push, retention setting change or production HA action occurred.

Evidence outside Git: /workspace/build-output/stable110, including inventories,
CI records, source checks, security comparison and independently downloaded assets.

## HACS and acceptance boundaries

In HACS select/update or redownload v1.10.0 Stable. Beta versions are unnecessary;
turn them off if desired, retain the existing NG module resource and refresh
frontend/resource caches on all clients. No YAML changes from beta.10 are needed.
Owner beta.10 real-HA acceptance is recorded; synthetic Chromium tests do not
establish every physical HA/HVAC/charger model or browser/native pinch scenario.

Stop here. Do not start v1.11/Car, new modules or optional architecture cleanup.
Future work requires its own owner scope. Keep master and v1.10.0 tag pinned to
the verified release SHA; this separate docs-only handoff does not republish it.
