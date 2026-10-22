---
name: renders-outside-build
description: "Put renders the owner should review outside build/ (e.g. ~/Desktop/<name>), since ./build.sh wipes build/"
metadata:
  node_type: memory
  type: feedback
  originSessionId: a61c6245-2afc-419d-8fa2-a66b84712007
  modified: 2026-10-22T08:19:44.770Z
---

Renders for the owner to review (transition clips, sheets, frames) go outside `build/`, e.g. `~/Desktop/hawkins-trips/`, and their full absolute path is given when reporting them.

**Why:** on 2026-10-22 the Stranger Clawds trip renders were written to `build/hawkins-trips/`, then a later `./build.sh` wiped `build/`; the owner went looking and found nothing, and was rightly angry about the wasted time and tokens.

**How to apply:** render review material straight to a folder outside the repo's `build/`, or copy it out before any `./build.sh`. Related: [[short-bang-commands]] (build.sh wipes build/).
