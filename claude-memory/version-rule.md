---
name: version-rule
description: Only a new universe bumps the minor version (3.6 -> 3.7); every other release is a patch (3.6.1, 3.6.2...)
metadata:
  type: feedback
---

From 3.6.0 on (rule set 2026-10-17): a release that adds a universe is the next `3.N.0`; fixes, tweaks and features without a new universe are patch releases (3.6.1, 3.6.2, ...).

**Why:** the user wants the minor number to mean "a new universe".

**How to apply:** pick the version for `./release.sh` this way, and write the CHANGELOG heading to match. It's also in clawdify_guide.md's Step 8. Related: [[audit-plan-2026-10]].
