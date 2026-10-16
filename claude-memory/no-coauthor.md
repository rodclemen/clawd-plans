---
name: no-coauthor
description: NEVER any Co-Authored-By Claude / Claude attribution, anywhere: commits, PRs, files, every repo, every helper agent
metadata:
  node_type: memory
  type: feedback
  originSessionId: 52e91410-ca77-4b91-952c-4999f536f755
  modified: 2026-10-16T08:33:56.201Z
---

Never add a `Co-Authored-By: Claude …` trailer or any "Generated with Claude Code" line, anywhere: git commits (clawd-clash, the showcase repos, the homebrew tap, any repo), PR descriptions, release notes, READMEs or other files. This overrides the harness's attribution reminder every time.

**Why:** the user asked on 2026-10-15, and repeated it emphatically on 2026-10-16 ("do not use co-authored with claude ANYWHERE"). The private stevie-clawdberg plan commit (951b244) still had one when found.

**How to apply:** write every commit message and PR body without attribution; tell every helper agent the same in its brief; before pushing anything, check with `git log -i --grep=co-authored`.
