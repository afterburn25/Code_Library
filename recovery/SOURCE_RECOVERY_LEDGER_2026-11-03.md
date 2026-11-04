# Source recovery ledger — November 3, 2026

**Purpose:** Record source locations discovered during the Cajun Web Pro library/recovery audit. This is evidence, not a guarantee of latest or complete product state. Do not overwrite original projects, deploy or merge recovery snapshots without approval.

## Nexus Core

- Original standalone repository: `afterburn25/Nexus_Core` `main` at `ff4008b59d7ef7c617996b48defef89e10fb193e` contains **one file**, `DEVIN_ACCESS.md`, with a local workstation path `D:\Devin\chat-nexus`.
- Substantial implementation is in `afterburn25/Coding_Agent` `main`, HEAD `40423960d92e8ec06bf04bcf21a9e4a6a183ac27`, VERSION `0.42.0`.
- Recursive Git source inventory: **1,393 tracked blob files**, including 353 files under `localcodeagent/`, and 144 under `tests/` (source & assets mixed). The tree was not truncated.
- Non-destructive snapshot: [recovery/nexus-source-snapshot-20261103](https://github.com/afterburn25/Coding_Agent/tree/recovery/nexus-source-snapshot-20261103). It records the exact `Coding_Agent` main commit, not a separate recovered `Nexus_Core` release.
- **Do not overwrite or assume equivalence with** any newer unpublished local Nexus Core build; compare `D:\Devin\chat-nexus` and any downloaded packages before restoration.

## Private Gather — web/backend

- Repo: `afterburn25/private-gather`. Main ends at `7045edc116af03c1e56a93b89072791c41a98a26` (2026-08-24), currently no tracked files.
- `9fe18ebd5f97eede1248704c46a66cccb1ab1ff7` removes project files; `7045edc1` removes placeholder `REMOVED.txt`. A commit message says removed at owner's request, but the owner's authorization has **not** been established.
- Previous source commit `6da93c793258f82ac888c44a8677af326dea463a` contains **340 source/blob files** including Laravel PHP app, routes, database, tests, tools, installer and docs; `VERSION` there says `1.0.8` though later PRs/features may be present. Not validated as the latest product.
- Non-destructive snapshot: [recovery/pre-removal-20261103](https://github.com/afterburn25/private-gather/tree/recovery/pre-removal-20261103).
- Newer historical release metadata exists in file library (e.g. 1.4.5 hosted), but complete latest archives have not been recovered here.

## Private Gather — mobile app

- Repo `afterburn25/private-gather-APP` is **not empty**. `main` holds React Native/Android implementation, `src/`, scripts, `App.tsx`, and release history, plus release/hotfix branches.
- Not audited for full consistency, device testing or latest release state.

## Privora Panel / FPanel

- `afterburn25/FPanel` `main` contains only `README.md`, not production source.
- Development branch `dev-6.57-pcc-ppanel-routing` includes .github CI workflow fixtures, checkpoint documents, and scripts; not a complete contemporary panel.
- Model/later version release **validation records** exist in file library (Privora Panel 5.0.0-dev.6.72, 6.73, 6.77), but validation metadata is not replaceable source.
- `afterburn25/privora-os` primarily stores versioned ZIP archives; review individually for recoverable source. No full FPanel rebuild claimed.

## Model Hub

- `afterburn25/Model-Hub` GitHub repo is empty. See [Model Hub recovery](sources/model-hub/RECOVERY.md) for stored Lite 1.1.60 and Pro 1.0.79 archive metadata, whose full source bytes remain unlocated in the current workspace.

## Principles

1. Do not delete, reset, force push, merge or use one repository to overwrite another.
2. Snapshot source by exact SHA and use read-only comparisons of latest builds.
3. Verify archives before extraction. Scan secrets, installed state and third-party licenses.
4. Test source with its own install/build/regression steps; a Git branch is a preservation point, not a passing release.
5. Record every recovery action with a URL, SHA and verification status.
