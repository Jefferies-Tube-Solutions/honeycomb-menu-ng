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
