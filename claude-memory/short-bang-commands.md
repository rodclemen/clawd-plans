---
name: short-bang-commands
description: "Commands for the user to run with `!` must be short single lines (pastes wrap and break); never test file-touching code by redirecting HOME"
metadata:
  node_type: memory
  type: feedback
  originSessionId: be19b5c9-e9f0-4576-b0b5-ea68d1892e1a
  modified: 2026-10-16T22:01:13.645Z
---

Long commands the user pastes after `!` get wrapped by the terminal: newlines land inside quoted JSON and arguments, and the command fails. That happened 3 times on 2026-10-16/17, and heredocs broke too because indented `EOF` doesn't end them.

**Why:** the user runs what Claude gives them verbatim and doesn't debug shell quoting.
**How to apply:**
- Keep every `!` command short enough to fit on one line.
- When a command needs a payload, write the payload or a tiny script to a file first (`build/` is git-ignored), then give a short `! sh build/x.sh` or `--input build/x.json`.
- Never use heredocs in commands for the user.

Also: the app finds home through `FileManager.homeDirectoryForCurrentUser`, which ignores `HOME`. A test that redirected HOME once overwrote the real `~/.claude/settings.json`. Test file-touching code only with explicit paths, or under `sandbox-exec` denying writes. Before `./build.sh` (which wipes `build/`), check whether a copy is running from `build/` and whether hooks point at it.
