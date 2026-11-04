# Model Hub source recovery and reuse audit

**Status:** Located project lineage and release metadata; actual source ZIP not yet accessible for extraction in this working session. **Do not claim extracted or verified code.**
**Checked:** 2026-11-03 (America/Chicago)
**Target toolkit:** `afterburn25/Code_Library`, review branch `library/starter-and-model-catalog-20261103`.

## GitHub status

- `afterburn25/Model-Hub`: repository exists and is public but GitHub currently reports no commits/branches/source files.
- Historical Model Hub implementations were delivered in ChatGPT conversations as Core and upgrade ZIP archives rather than committed to this GitHub repository.

## Recovered lineage

1. **Model Hub Pro**: versions progressed through the 1.0.x series; recorded release `1.0.79` on 2026-08-03, with **Model-Hub-Pro-1.0.79-Core.zip** and 1.0.78→1.0.79 upgrade.
2. **Model Hub Lite**: extracted from Pro's shared core, with separate plugin architecture and the Visual Design Lab. Historical releases progressed through **1.1.60** (2026-08-21), described as a host-migration-oriented Core archive preserving 2,830 files.
3. Historical Pro 0.27.60 archival validation metadata also exists, but it is an older lineage and should not supersede later source.

## Concrete recorded archive metadata

- `Model-Hub-Pro-1.0.79-Core.zip` — size 33,389,877 bytes; SHA-256 `b896436dea58593f7c5d635619914f9a711f3c853eb8c17077fb6db1e7ee401f`.
- `Model-Hub-Lite-1.1.60-Core.zip` — SHA-256 `1be33acba03b26c7532c3fd600630ae9a8d2f247937a2ce929f0a2fa1941e5a6`.
- `Model-Hub-Lite-1.1.59-to-1.1.60-Upgrade.zip` — SHA-256 `e148091aadf23117c8a7963c06531d97926086b74bd5a3a1901f24b64a8aeef9`.

Release metadata and hashes are in the user's file library; archive paths recorded in manifests are historical references, **not present accessible working files**.

## Potentially reusable components (unverified candidates)

- Plugin registration, dependency and packaging system.
- Visual page designer/Design Lab and reusable page layout controls.
- Theme switching, branding, responsive blocks and page publishing.
- Installer, upgrade and rollback safety logic.
- Content, media, authentication and administrative UI patterns.
- Licensing/updater adapters (never transfer live credentials, application secrets or business-specific license checks).

## Safe import procedure

1. Recover latest complete Core ZIP from prior download or prior conversation artifact. Prefer Lite 1.1.60 and Pro 1.0.79 as separate source lineages; compare rather than blindly combine.
2. Verify SHA-256 against preserved manifest and inspect ZIP for path traversal, symlinks, nested ZIPs, secrets, production customer data, binaries and licenses.
3. Create a read-only source inventory; identify original classes/scripts and dependencies.
4. Compare with Website Core `CORE_BOUNDARIES.md` and `docs/MODULE_API.md`; catalog Core-owned functionality as references, not duplicate implementations.
5. Extract one small, independently testable reusable unit at a time, document provenance, add tests and independent review. Place approved entries under function-specific toolkit folders.
6. Do not overwrite `afterburn25/Model-Hub` or merge source to `Code_Library/main` without verified source and review.

## Recovery blocker

Actual Model Hub Core ZIP bytes are not currently available in this session's working files or identified Library search results. The recorded SHA/metadata alone cannot reconstruct application source.
