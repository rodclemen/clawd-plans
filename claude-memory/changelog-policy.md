---
name: changelog-policy
description: "Which Clawd Clash changelogs get updated: only CHANGELOG.md routinely; universe repos' changelogs only for showcase-worthy changes"
metadata:
  node_type: memory
  type: project
  originSessionId: d926bf6a-6c29-4d4f-969c-daebd2276adf
  modified: 2026-10-14T10:03:48.923Z
---

Only `CHANGELOG.md` in clawd-clash is kept up with every change (release.sh requires a `## <version> ` entry and uses it as release notes). `history/*.md` (the old apps' changelogs, moved 2026-10-14) are frozen. The universe showcase repos (rodclemen/star-clawds, marvelous-clawds, detective-clawds) each have a plain-language CHANGELOG.md that gets an entry only now and then, for something worth showing off in that universe; they point to clawd-clash's changelog for the rest.

**Why:** the user chose this on 2026-10-14 over keeping four changelogs in step each release ("option 1 is fine").

**How to apply:** add entries to CHANGELOG.md as part of each change; don't update the universe repos' changelogs unless the user asks or a change is a notable per-universe feature (then suggest it). See [[release-setup]].
