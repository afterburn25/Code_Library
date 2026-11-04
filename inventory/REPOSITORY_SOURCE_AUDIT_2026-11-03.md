# Repository Source Preservation Audit — 2026-11-03

Source check: GitHub account `afterburn25`; 27 repositories accessible. Recorded as a point-in-time audit, not proof that deployed software or local folders match. No force pushes, deletion, deploys or unreviewed merges are authorized by this record.

| Repository | Current audit status | Recovery/action |
|---|---|---|
| [Smartthings](https://github.com/afterburn25/Smartthings) | Empty | No source or commit history found in this audit; do not invent source |
| [a](https://github.com/afterburn25/a) | Empty | No recoverable source found; likely placeholder/test, intent not verified |
| [b](https://github.com/afterburn25/b) | Empty | No recoverable source found; likely placeholder/test, intent not verified |
| [lock-manager](https://github.com/afterburn25/lock-manager) | Source present | Historical SmartThings source and docs on master |
| [nest-manager](https://github.com/afterburn25/nest-manager) | Source present | Historical SmartThings manager source and docs on master |
| [privora-os](https://github.com/afterburn25/privora-os) | Release archives present | Main retains versioned Privora OS ZIP releases; review archives individually; no replacement of live FPanel |
| [frames](https://github.com/afterburn25/frames) | Archive-heavy | Runtime certification ZIP archives and continuity docs; latest installable source not independently validated |
| [private-gather](https://github.com/afterburn25/private-gather) | Historical source recoverable | main deleted Aug 24; 340-file pre-removal commit restored in draft PR #63; not yet latest |
| [FPanel](https://github.com/afterburn25/FPanel) | Full source on main | Privora 5.0.0-dev.7.0 Rev5 Rev9, 337 files, Git tree exactly matches saved JSONL source snapshot; older PR #2 closed as superseded |
| [Privoralabs.com](https://github.com/afterburn25/Privoralabs.com) | Empty | No code, branches, or source records located |
| [Privoralabs.org](https://github.com/afterburn25/Privoralabs.org) | Empty | No code, branches, or source records located |
| [Model-Hub](https://github.com/afterburn25/Model-Hub) | Recovery README only | Pro 1.0.79 & Lite 1.1.60 source archives named with hashes but bytes not found; README added |
| [private-gather-APP](https://github.com/afterburn25/private-gather-APP) | Source present | React Native/Android app, scripts, docs and branches; recovery snapshot branch created |
| [stellar-continuum](https://github.com/afterburn25/stellar-continuum) | Source present | Godot/C# game source and tests |
| [Sentinel](https://github.com/afterburn25/Sentinel) | Source present | CMake/C++ application, include/src/tests/docs |
| [Docket_Unseen](https://github.com/afterburn25/Docket_Unseen) | Content present | Production/story research templates and documentation |
| [Coding_Agent](https://github.com/afterburn25/Coding_Agent) | Source present | Nexus 0.42.0 code at main 40423960; 1,393 files; recovery snapshot pinned |
| [Nexus_Core](https://github.com/afterburn25/Nexus_Core) | Recovery linked in PR | Standalone main had only DEVIN_ACCESS; draft PR #1 adds pinned Git submodule to Coding_Agent full source, not a full migration |
| [nexus-dogfood](https://github.com/afterburn25/nexus-dogfood) | Empty private repository | No contents verified; do not publish private test assets |
| [david](https://github.com/afterburn25/david) | Source present | Music-site scripts, docs, tests and assets |
| [Cajun_Web](https://github.com/afterburn25/Cajun_Web) | Source present | Business platform, tests, docs, CI and tools; active integration owner rules unchanged |
| [Spirit](https://github.com/afterburn25/Spirit) | Source present | PHP band website frontend, app, backend, docs, assets |
| [Website_Core](https://github.com/afterburn25/Website_Core) | Source present | Universal Core, SDK, module examples, PHP tests, packaging |
| [velvet_vixxen](https://github.com/afterburn25/velvet_vixxen) | Source present | PHP creator website, scripts, docs, tests |
| [Core_Mods](https://github.com/afterburn25/Core_Mods) | Module source on separate branches | main holds rules/templates/tools; actual Catering on module/catering and Landscaping on module/landscaping |
| [Pictures](https://github.com/afterburn25/Pictures) | Organization scripts present | Private photos tooling/reports; do not copy photo data |
| [Code_Library](https://github.com/afterburn25/Code_Library) | Toolkit review branch populated | main initialized README; review branch carries catalog, source references, Model Hub notes and recovery ledger |

## Confirmed recovery destinations

- **Private Gather backend:** [draft PR #63](https://github.com/afterburn25/private-gather/pull/63), 340 files proposed onto deleted main. Independent earlier source branch: `recovery/pre-removal-20261103`.
- **Privora/FPanel:** [main commit 442841d](https://github.com/afterburn25/FPanel/commit/442841d351f8bbe86c9c7b0a1f03d2e30ab5fc0e), 337 source files identical to saved `Privora-Rev5R9-GitHub-Tree.jsonl`, root tree `ef1d8c733f99692a90a85ebf7e346f464791434c`. Previous older PR #2 deliberately closed as superseded.
- **Nexus Core:** [draft PR #1](https://github.com/afterburn25/Nexus_Core/pull/1) pins the existing `Coding_Agent` source as a Git submodule. This is a pointer to the full external source, **not a standalone code migration**.
- **Private Gather mobile:** complete source remains in `private-gather-APP`; `recovery/mobile-source-snapshot-20261103` preserves a known exact commit.
- **Model Hub:** recovery README on [Model-Hub/main](https://github.com/afterburn25/Model-Hub), source missing pending original ZIP discovery.
- **Reusable toolkit:** `Code_Library` branch `library/starter-and-model-catalog-20261103` contains provenance-linked code references and recovery records for review.

## Recovery constraints

Historical archives can be newer than the last Git commit; a source-bearing branch alone does not prove the latest release. Never equate validation metadata with actual source bytes. Do not upload private credentials, deployed secrets, customer data, private user media or unreconciled binary packages. Verify exact source SHAs and test before naming a release deployable.
