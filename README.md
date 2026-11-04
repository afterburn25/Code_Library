# Cajun Web Pro Code Library

Reusable, provenance-tracked code patterns, developer tools, generator recipes and tests for Cajun Web Pro projects.

**Status:** Initial catalog and extraction are under review. A catalog entry is not a claim that source is production-ready.

## Principles

- **Reuse Website Core, do not rebuild it.** Use its supported `ModuleContext` API, SDK and module packaging tools.
- Reference existing tested implementations instead of copying or forking entire applications.
- Extract small, purpose-specific code with an origin repository/path/commit and an explicit license/security review.
- Keep `main` for reviewed, validated additions; use short-lived feature branches and draft PRs for imports.
- Do not copy secrets, credentials, customer records, media uploads, payment data or production databases.
- Do not automatically edit source repositories, merge a PR, activate live payments or deploy a website.
- Never place ZIP archives inside ZIP archives.

## Source projects

- [Website_Core](https://github.com/afterburn25/Website_Core): universal PHP website foundation and module SDK.
- [Core_Mods](https://github.com/afterburn25/Core_Mods): industry modules and standards.
- [Cajun_Web](https://github.com/afterburn25/Cajun_Web): business platform, testing and release tooling.
- [Coding_Agent](https://github.com/afterburn25/Coding_Agent): model routing, tool registry and runtime patterns.
- [Spirit](https://github.com/afterburn25/Spirit): small PHP utilities and website patterns.
- [Model-Hub](https://github.com/afterburn25/Model-Hub): reserved as a source candidate; GitHub reported an empty repository on 2026-11-03.

## Next

See the library import draft pull request for the starter catalog and working tools. Full repository-wide extraction and functional acceptance remain in progress.
