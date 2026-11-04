# Instructions for AI coding agents

This repository is a **reviewed-source candidate library**, not the canonical source for its referenced projects. Each catalog entry records the actual originating repository and branch.

## Agent workflow

1. Search `catalog.json` with `python tools/search_catalog.py <query>` (standard library only). Read only matching entries, not every source file.
2. Prefer directly using Website Core `ModuleContext`, existing SDK scaffolding and module packaging. Do not recreate Core-owned auth, settings, routing, content, media, queries, installation or commerce.
3. Read an entry's `source_repo`, `source_path`, `source_ref` and `status` before copying or adapting. Entries marked `reference_only` are unmodified snapshots with their original namespace and assumptions, not ready-made standalone libraries.
4. Preserve original source and use short-lived feature branches. Update linked references after checking the latest origin; never silently overwrite upstream project code.
5. Require security, proprietary-license and dependency reviews and deterministic tests for every extracted component. Never infer passing tests from PHP lint or a passing document validator.
6. Do not ingest live credentials, personal data, key material, runtime dumps, paid third-party source or content requiring unverified redistribution permission.
7. Preserve existing project ownership: do not modify active `Cajun_Web`, `Website_Core`, `Core_Mods`, or another agent's branch without explicit assignment.
8. Never run Git push, merge, production deploy, real payments or destructive actions as part of merely searching this library.
9. Never put ZIP archives inside ZIP archives.

No source is automatically approved for production solely by appearing here.
