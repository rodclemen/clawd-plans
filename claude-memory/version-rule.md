---
name: version-rule
description: "Universe bumps the major (4.0.0), feature the minor, else patch; scripts/next-version.sh computes it, release.sh uses it"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 61a2c692-d7b8-43ec-b62f-7c0d60bec48c
  modified: 2026-10-23T11:27:55.819Z
---

From Stranger Clawds on (decided 2026-10-23, replacing the 3.N.0 rule): a new universe raises the first number (3.7.1 -> 4.0.0 -> 5.0.0), a feature the middle one (4.1.0), fixes/polish/docs the last one (4.1.1). The biggest kind in a release decides; the last number counts up past 9 (4.0.10) and moves once per release, not per fix. Stranger Clawds ships as 4.0.0, not 3.8.0.

**Why:** the user wants each kind of release visible in the number, with no spill between kinds. They first proposed universe = +0.5 steps (3.7.5); that collides with patches in a three-number version, so they chose this.

**How to apply:** don't pick versions by hand. `scripts/next-version.sh` reads commits since the last tag (a universe newly `shipped` in NUMBERS, then any `feat:` commit) and `./release.sh` with no version uses it. So commit prefixes matter: `feat:` only for real features. Rule is in clawdify_guide.md's "Version numbers". Related: [[audit-plan-2026-10]].
