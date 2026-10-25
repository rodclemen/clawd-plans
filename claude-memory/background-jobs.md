---
name: background-jobs
description: "Waiting on a background job" state (teal hourglass), branch background-jobs 01f06c8, rebased on 4.1.0, ask before pushing; issue #7
metadata:
  type: project
  modified: 2026-10-25T08:56:20.399Z
---

Built 2026-10-25 on branch `background-jobs` (worktree ../Clawd-Clash-bg), commit 01f06c8, rebased onto the released main (85375a8) with a fresh Unreleased section. Builds; next-version says 4.1.1. Not pushed.

- **What it is:** a new `background` state. The session stands guard with a teal hourglass and its card reads WAITING ON A JOB.
- **Which AIs:** Claude Code, Qwen Code, Copilot CLI, and Gemini CLI (only when its wake-up settings are on).
- **Open work:** Codex and pi are left to issue #7 (rodclemen/clawd-clash), along with checking Copilot's rule against a real session.
- **Release:** it's a feature, so it raises the last number (4.1.1), after Superclawdtural's 4.1.0.

**Why:** the owner asked for it to be committed and pushed only after Superclawdtural is done.

**How to apply:** once 4.1.0 is out, rebase the branch onto main. Its CHANGELOG line sits under Unreleased, Added, so move it if the release has renamed that section. Then ask before pushing. Related: [[superclawdtural]], [[version-rule]].
