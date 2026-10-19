#!/usr/bin/env python3
"""Refresh the Status column in README.md from what's actually pushed to GitHub.

Each plan carries one hidden line saying where its build lives:

    <!-- track: repo=rodclemen/clawd-clash branch=star_trek folder=ClawdTrek title="Clawd Trek" cast=100 places=21 -->

Engine plans (no universe folder) say `kind=engine` instead of folder, title, cast and places.

The script looks at the build repo over GitHub's API and works out how far each universe is:
released in a tag, built on main, or somewhere along its branch. Only pushed branches can be seen.
It then rewrites the Status cell of every README row that links to a tracked plan. Rows without a
tracked plan (Clawd of the Rings) are left as they are.

Run it locally with `python3 scripts/status.py` (it uses `gh auth token` if GITHUB_TOKEN isn't set),
or let .github/workflows/status.yml run it. `--check` prints the statuses without touching the README.
"""

import base64
import json
import os
import re
import shlex
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
API = "https://api.github.com"
UNIVERSES = "Sources/App/Universes"


def token():
    t = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if t:
        return t
    try:
        return subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None   # unauthenticated: 60 requests an hour, still enough for one run


TOKEN = token()
_cache = {}


def get(path):
    """GET from the API; None for a 404 (a branch that isn't pushed, a file that isn't there)."""
    if path in _cache:
        return _cache[path]
    req = urllib.request.Request(API + path, headers={"Accept": "application/vnd.github+json", "User-Agent": "clawd-plans-status"})
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    try:
        with urllib.request.urlopen(req) as r:
            data = json.load(r)
    except urllib.error.HTTPError as e:
        if e.code in (404, 409, 422):   # 409: an empty repo; 422: a ref that doesn't resolve
            data = None
        else:
            raise
    _cache[path] = data
    return data


def q(s):
    return urllib.parse.quote(s, safe="")


def tree(repo, ref):
    """Every file path at `ref`, or None if the ref isn't on GitHub."""
    t = get(f"/repos/{repo}/git/trees/{q(ref)}?recursive=1")
    return None if t is None else {e["path"] for e in t["tree"] if e["type"] == "blob"}


def text(repo, ref, path):
    """A file's contents, from raw.githubusercontent.com: it doesn't count against the API's hourly limit."""
    url = f"https://raw.githubusercontent.com/{repo}/{q(ref)}/{urllib.parse.quote(path)}"
    req = urllib.request.Request(url, headers={"User-Agent": "clawd-plans-status"})
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    try:
        with urllib.request.urlopen(req) as r:
            return r.read().decode()
    except urllib.error.HTTPError:
        return ""


def last_commit(repo, ref):
    c = get(f"/repos/{repo}/commits/{q(ref)}")
    return c["commit"]["committer"]["date"][:10] if c else None


def tags(repo):
    """Release tags, oldest first (v3.0.0 … v3.7.0)."""
    names = [t["name"] for t in get(f"/repos/{repo}/tags?per_page=100") or []]
    def key(n):
        return [int(x) for x in re.findall(r"\d+", n)]
    return sorted((n for n in names if re.match(r"v?\d+\.\d+", n)), key=key)


# What a universe's folder tells us


def count_cast(src):
    """Cases in every `enum …Hero` / `enum …Villain`, the same way the app's own counts come from allCases."""
    n = 0
    for m in re.finditer(r"enum \w*(?:Hero|Villain)\b[^{]*\{(.*?)\n\}", src, re.S):
        body = re.sub(r"//.*", "", m.group(1))
        for line in re.findall(r"^\s*case\s+([^\n=(:]+)", body, re.M):
            n += len([x for x in line.split(",") if x.strip()])
    return n


def progress(repo, ref, files, plan):
    """How far the universe in `plan["folder"]` has got at `ref`, as a short phrase."""
    folder = f"{UNIVERSES}/{plan['folder']}/"
    mine = sorted(p for p in files if p.startswith(folder))
    if not mine:
        return None
    # The enums and place keys live in the roster (older universes) or the facts file (modules). A skeleton may
    # commit every enum case up front as stand-ins, so progress counts the characters actually drawn: the
    # `Persona(` entries in the art files.
    src = "".join(text(repo, ref, p) for p in mine if re.search(r"(Roster|Facts)\.swift$", p))
    art = "".join(text(repo, ref, p) for p in mine if "/Art/" in p)
    cast = count_cast(src)
    drawn = len(re.findall(r"\bPersona\(", art)) + (1 if cast else 0)   # + HEM, drawn in Hem.swift
    # Place keys are declared up front too, so count the places actually drawn in Places/.
    scenes = "".join(text(repo, ref, p) for p in mine if "/Places/" in p)
    places = len(re.findall(r"\bPlace\(name:", scenes))
    has_trips = any(re.search(r"(Wipes|Trips)\.swift$", p) for p in mine)
    slug = re.sub(r"[^a-z0-9]+", "-", plan.get("title", "").lower()).strip("-")
    has_docs = f"docs/roster-{slug}.png" in files

    want = int(plan.get("cast", 0)) or None
    want_places = int(plan.get("places", 0)) or None
    if has_docs:
        phase = "phase 6, docs and trailer"
    elif has_trips:
        phase = "phase 5, transitions"
    elif want and drawn >= want:
        phase = "phase 4, mechanics"
    elif drawn > 4:   # the skeleton: the lead hero, the lead villain, one more, and HEM
        phase = "phase 2–3, the cast"
    else:
        phase = "phase 1, skeleton"
    bits = [f"**{phase}**", f"{drawn}/{want or cast} drawn"]
    if places:
        bits.append(f"{places}/{want_places} places" if want_places else f"{places} places")
    return " · ".join(bits)


def released_in(repo, plan):
    folder = f"{UNIVERSES}/{plan['folder']}/"
    for t in tags(repo):
        files = tree(repo, t)
        if files and any(p.startswith(folder) for p in files):
            return t.lstrip("v")
    return None


def universe_status(plan, claimed):
    """`claimed`: the plan sits in in-progress/, so someone's building it even if nothing is pushed yet."""
    repo, branch = plan["repo"], plan.get("branch")
    who = f" ({plan['who']})" if plan.get("who") else ""
    version = released_in(repo, plan)
    if version:
        return f"released in {version}{who}"
    # Built on main behind `Universe.isReleased`, the way Clawd of the Rings was.
    main = tree(repo, "main") or set()
    p = progress(repo, "main", main, plan)
    if p:
        return f"{p} · on `main`, not released yet{who}"
    if branch:
        files = tree(repo, branch)
        if files is not None:
            p = progress(repo, branch, files, plan) or "**branch made**, no universe folder yet"
            return f"{p} · branch `{branch}`{fork(repo)}, last commit {last_commit(repo, branch)}{who}"
    if claimed:
        where = ", ".join(x for x in [plan.get("who"), f"branch `{branch}`{fork(repo)}" if branch else None] if x)
        return f"**in progress**, nothing pushed yet{f' ({where})' if where else ''}"
    return f"plan ready, no branch pushed yet{who}"


def engine_status(plan):
    repo, branch = plan["repo"], plan["branch"]
    if get(f"/repos/{repo}/branches/{q(branch)}") is None:
        return "planned, no branch pushed yet"
    cmp = get(f"/repos/{repo}/compare/main...{q(branch)}")
    if cmp and cmp["ahead_by"] == 0:
        return f"merged into `main` (branch `{branch}`)"
    ahead = f", {cmp['ahead_by']} commits ahead of `main`" if cmp else ""
    return f"**in progress** · branch `{branch}`{fork(repo)}{ahead}, last commit {last_commit(repo, branch)}"


def fork(repo):
    return "" if repo == "rodclemen/clawd-clash" else f" in {repo}"


# The plans and the README


def tracked_plans():
    plans = {}
    for path in sorted(ROOT.glob("**/*.md")):
        if ".github" in path.parts:
            continue
        m = re.search(r"^<!--\s*track:(.*?)-->", path.read_text(), re.M)   # at a line's start, not quoted in prose
        if m:
            fields = dict(kv.split("=", 1) for kv in shlex.split(m.group(1)))
            plans[path.relative_to(ROOT).as_posix()] = fields
    return plans


def main():
    check = "--check" in sys.argv
    plans = tracked_plans()
    statuses = {}
    for path, plan in plans.items():
        claimed = path.startswith("in-progress/")
        statuses[path] = engine_status(plan) if plan.get("kind") == "engine" else universe_status(plan, claimed)
        # A plan at the top level with something pushed should move to in-progress/ (and to done/ once released).
        started = not statuses[path].startswith(("plan ready", "planned"))
        if "/" not in path and started:
            print(f"note: {path} has a build under way; move it to in-progress/", file=sys.stderr)
        if path.startswith("in-progress/") and statuses[path].startswith("released"):
            print(f"note: {path} is released; move it to done/", file=sys.stderr)

    lines = README.read_text().split("\n")
    seen = set()
    for i, line in enumerate(lines):
        m = re.match(r"\|\s*\[[^\]]*\]\(([^)]+)\)\s*\|", line)
        if m and m.group(1) in statuses:
            cells = line.split("|")
            # | plan | universe | status |  →  ['', plan, universe, status, '']
            cells[-2] = f" {statuses[m.group(1)]} "
            lines[i] = "|".join(cells)
            seen.add(m.group(1))
    for path in sorted(set(statuses) - seen):
        print(f"note: {path} is tracked but has no row in README.md", file=sys.stderr)

    for path, s in statuses.items():
        print(f"{path}: {s}")
    if not check:
        new = "\n".join(lines)
        if new != README.read_text():
            README.write_text(new)
            print("README.md updated")
        else:
            print("README.md already up to date")


if __name__ == "__main__":
    main()
