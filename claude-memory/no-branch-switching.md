---
name: no-branch-switching
description: Never git checkout another branch in the clawd-clash folder just to read code; other sessions work in it
metadata:
  node_type: memory
  type: feedback
  originSessionId: 0cb5d9d2-8731-4fff-92c1-e3b26663eafb
  modified: 2026-10-16T09:12:10.123Z
---

Don't switch the clawd-clash working folder to another branch to read code. Use `git show <branch>:<path>` or `git grep <branch>` instead. Stay on whatever branch the user is on.

**Why:** on 2026-10-16 I switched x-files → main so plan-writing agents could read main. Another session was working in the same folder at the time, and the user was confused about which branch we were on. They then said to stay on main and not change back.

**How to apply:** read other branches without checking them out. Only change branches when the user asks.
