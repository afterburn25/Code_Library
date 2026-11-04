# GitHub source recovery — action log (2026-11-03, America/Chicago)

This log distinguishes **new commits made in this recovery session**, **existing commits found**, and **pending work**. No production deployment, payment activation, force-push, deletion, or main-branch restore of formerly deleted application code is part of this log.

## Source preservation and import

| Project | Result | Evidence |
|---|---|---|
| Private Gather web/backend | Draft recovery PR reintroduces 340 files in a new commit; original main's removal history remains intact | [PR #63](https://github.com/afterburn25/private-gather/pull/63), head `f8592c47ac6a48ce15b01c0c00525cb4d768505a`; original pre-removal `6da93c793258f82ac888c44a8677af326dea463a` |
| Private Gather mobile | Existing React Native/Android source preserved in a pinned recovery branch | [snapshot](https://github.com/afterburn25/private-gather-APP/tree/recovery/mobile-source-snapshot-20261103), original `1d9d508162cfcd4f6a3ced5f7491fdf449410705` |
| Nexus Core | Draft PR adds pinned submodule pointing at full `Coding_Agent` code and docs; not a standalone source migration | [PR #1](https://github.com/afterburn25/Nexus_Core/pull/1), source commit `40423960d92e8ec06bf04bcf21a9e4a6a183ac27` (0.42.0, 1,393 files) |
| Privora Panel/FPanel | Full source recovered on main by a separate commit during audit; exact 337-file Git tree matches saved `Privora-Rev5R9-GitHub-Tree.jsonl` | [Commit 442841d](https://github.com/afterburn25/FPanel/commit/442841d351f8bbe86c9c7b0a1f03d2e30ab5fc0e), root tree `ef1d8c733f99692a90a85ebf7e346f464791434c`, model 5.0.0-dev.7.0 Rev5 Rev9 |
| FPanel older records | Historical branch remains. Draft PR #2 closed without merge because older files could downgrade new 7.0 main | [PR #2](https://github.com/afterburn25/FPanel/pull/2), preserved branch `recovery/fpanel-dev-record-20261103` |
| Model Hub | README committed with recoverable Pro 1.0.79 and Lite 1.1.60 archive filenames/hashes and next steps. Original Core ZIPs recovered and checksum-verified (Pro 719 files, Lite 2,830 files). A cleaned 3,548-file import kit is prepared but not committed to GitHub | [Model-Hub main](https://github.com/afterburn25/Model-Hub), commit `eff8b7de6e7ebd1bfe30d5762d6e0b96093d58cb` |
| Privoralabs.com | README now records recovered historical 1.3.49 Core and the missing newer 1.5.22 archive; not restored website source | [Commit](https://github.com/afterburn25/Privoralabs.com/commit/8769a9cdd50aa457a0c7e18240bdc8afcecfbede) |
| Privoralabs.org | README source-recovery starting point committed, **not restored site source** | [Commit](https://github.com/afterburn25/Privoralabs.org/commit/0ec9db856b41c65c60110311f05802d126219d0a) |
| Code_Library | New catalog contains 22 source/provenance candidates, with four unmodified code references copied on separate review branch | [Review branch](https://github.com/afterburn25/Code_Library/tree/library/starter-and-model-catalog-20261103) |

## Risks and incomplete work

- No independent tests or live VPS acceptance run in this recovery session. Git tree SHA equivalence is **source integrity**, not running software certification.
- Private Gather's recovered backend tree has `VERSION=1.0.8`, while later 1.3/1.4 release history exists; reconcile archives/PRs before treating this as the current build.
- Nexus Core is not copied directly into the standalone repository. The submodule preserves all recorded code and tests at an immutable commit until a separately planned migration.
- Model Hub Pro/Lite complete Core ZIPs are recovered and match release hashes; clean source kit SHA-256 `19b10bfb1d4ba374a78c49d4413572813e157df484028874e572d865e1fb331e`, still awaiting repository import. Private Gather Hosted 1.4.5 ZIP is also recovered: source-only 527-file kit SHA-256 `0d352e23f3470e0bce977acdeba0f3c857da80608fe0f6fdad17329f7015c5d5`. Privora Labs 1.3.49 historical source is recovered, while newer 1.5.22 raw bytes remain unavailable.
- Public repositories may expose proprietary code: examine access settings and prior deletion rationale before merging or publishing recovered source to main.
- Existing source in other repositories remains untouched. Read-only inventory: [Repository Source Audit](../inventory/REPOSITORY_SOURCE_AUDIT_2026-11-03.md).

## Required verification gates before release

Review commit provenance, check secret/PII exposure, run language-specific test suites and build/install acceptance, verify deployment compatibility, and require explicit approval for merge or production activation.
