#!/usr/bin/env python3
"""Refresh the Status column in README.md from what's actually pushed to GitHub.

Each plan carries one hidden line saying where its build lives:

    <!-- track: repo=rodclemen/clawd-clash branch=star_trek folder=ClawdTrek title="Clawd Trek" source="Star Trek" cast=100 places=21 -->

Engine plans (no universe folder) say `kind=engine` instead of folder, title, cast and places.

The script looks at the build repo over GitHub's API and works out how far each universe is:
released in a tag, built on main, or somewhere along its branch. Only pushed branches can be seen.
It then rewrites the block between <!-- status:start --> and <!-- status:end --> in the README: a summary
line, then tables for the universes being built (with a progress bar), ready to pick up, and released. A
universe with no plan here (Clawd of the Rings) gets its track line in the README itself.

Run it locally with `python3 scripts/status.py` (it uses `gh auth token` if GITHUB_TOKEN isn't set),
or let .github/workflows/status.yml run it. `--check` prints the block without touching the README.
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


PHASES = {1: "the skeleton", 2: "the core ensemble", 3: "the rest of the cast", 4: "mechanics",
          5: "transitions", 6: "docs and trailer"}


def progress(repo, ref, files, plan):
    """How far the universe in `plan["folder"]` has got at `ref`: phase, counts and a rough percentage."""
    folder = f"{UNIVERSES}/{plan['folder']}/"
    mine = sorted(p for p in files if p.startswith(folder))
    if not mine:
        return None
    # The enums live in the roster (older universes) or the facts file (modules). A skeleton may commit every enum
    # case up front as stand-ins, so progress counts what's actually drawn: `Persona(` entries in the art files
    # and `Place(name:` entries in the places files.
    src = "".join(text(repo, ref, p) for p in mine if re.search(r"(Roster|Facts)\.swift$", p))
    art = "".join(text(repo, ref, p) for p in mine if "/Art/" in p)
    scenes = "".join(text(repo, ref, p) for p in mine if "/Places/" in p)
    cast = count_cast(src)
    drawn = len(re.findall(r"\bPersona\(", art)) + (1 if cast else 0)   # + HEM, drawn in Hem.swift
    places = len(re.findall(r"\bPlace\(name:", scenes))
    has_trips = any(re.search(r"(Wipes|Trips)\.swift$", p) for p in mine)
    slug = re.sub(r"[^a-z0-9]+", "-", plan.get("title", "").lower()).strip("-")
    has_docs = f"docs/roster-{slug}.png" in files

    want = int(plan.get("cast", 0)) or cast or 1
    want_places = int(plan.get("places", 0)) or places or 1
    # The cast and places are most of the work, so phases 1–3 carry 60% between them, split by what's drawn.
    share = 0.75 * min(drawn / want, 1) + 0.25 * min(places / want_places, 1)
    if has_docs:
        phase, pct = 6, 92
    elif has_trips:
        phase, pct = 5, 80
    elif drawn >= want:
        phase, pct = 4, 65
    else:
        phase = 1 if drawn <= 4 else 2 if drawn < 0.5 * want else 3   # the skeleton: 3 characters and HEM
        pct = 5 + round(55 * share)
    return dict(phase=phase, pct=pct, drawn=drawn, want=want, places=places, want_places=want_places)


def released_in(repo, plan):
    folder = f"{UNIVERSES}/{plan['folder']}/"
    for t in tags(repo):
        files = tree(repo, t)
        if files and any(p.startswith(folder) for p in files):
            return t.lstrip("v")
    return None


def universe_status(plan, claimed):
    """Where a universe is, as a dict: `state` is built, main, released, claimed or ready.
    `claimed`: the plan sits in in-progress/, so someone's building it even if nothing is pushed yet."""
    repo, branch = plan["repo"], plan.get("branch")
    main = tree(repo, "main") or set()
    version = released_in(repo, plan)
    if version:
        return dict(state="released", version=version, **(progress(repo, "main", main, plan) or {}))
    # Built on main behind `Universe.isReleased`, the way Clawd of the Rings was.
    p = progress(repo, "main", main, plan)
    if p:
        return dict(state="main", where="on `main`, not released yet", **p)
    if branch:
        files = tree(repo, branch)
        if files is not None:
            p = progress(repo, branch, files, plan) or dict(phase=1, pct=2, drawn=0, want=int(plan.get("cast", 0)),
                                                             places=0, want_places=int(plan.get("places", 0)))
            return dict(state="built", where=f"`{branch}`{fork(repo)}", date=last_commit(repo, branch), **p)
    if claimed:
        return dict(state="claimed", pct=0, where=f"`{branch}`{fork(repo)}, nothing pushed yet" if branch else "nothing pushed yet")
    return dict(state="ready")


def engine_status(plan):
    repo, branch = plan["repo"], plan["branch"]
    if get(f"/repos/{repo}/branches/{q(branch)}") is None:
        return dict(state="ready")
    cmp = get(f"/repos/{repo}/compare/main...{q(branch)}")
    if cmp and cmp["ahead_by"] == 0:
        return dict(state="merged", where=f"`{branch}`")
    ahead = f", {cmp['ahead_by']} commits ahead of `main`" if cmp else ""
    return dict(state="built", where=f"`{branch}`{fork(repo)}{ahead}", date=last_commit(repo, branch))


def fork(repo):
    return "" if repo == "rodclemen/clawd-clash" else f" in {repo}"


# The plans and the README


def tracked_plans():
    """Every `<!-- track: … -->` line, by the file it's in. The README's own lines are universes with no plan here."""
    plans = {}
    for path in sorted(ROOT.glob("**/*.md")):
        if ".github" in path.parts:
            continue
        for m in re.finditer(r"^<!--\s*track:(.*?)-->", path.read_text(), re.M):   # at a line's start, not in prose
            fields = dict(kv.split("=", 1) for kv in shlex.split(m.group(1)))
            rel = path.relative_to(ROOT).as_posix()
            plans[rel if rel != "README.md" else f"README.md#{fields['folder']}"] = fields
    return plans


def bar(pct):
    full = round(pct / 10)
    return f"`{'█' * full}{'░' * (10 - full)}` {pct}%"


def short_date(iso):
    y, m, d = (int(x) for x in iso.split("-"))
    return f"{d} {['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][m - 1]}"


def name(path, plan):
    title = plan.get("title", path)
    link = title if path.startswith("README.md") else f"[{title}]({path})"
    source = f"<br><sub>{plan['source']}</sub>" if plan.get("source") else ""
    return f"**{link}**{source}"


def who(plan):
    return f"{plan['who']} · " if plan.get("who") else ""


def counts(st, planned=False):
    if planned:
        return f"{st['want']} characters · {st['want_places']} places"
    return f"{st['drawn']}/{st['want']} characters · {st['places']}/{st['want_places']} places"


def render(plans, statuses):
    building = [p for p in plans if plans[p].get("kind") != "engine" and statuses[p]["state"] in ("built", "main", "claimed")]
    ready = [p for p in plans if plans[p].get("kind") != "engine" and statuses[p]["state"] == "ready"]
    released = [p for p in plans if plans[p].get("kind") != "engine" and statuses[p]["state"] == "released"]
    engine = [p for p in plans if plans[p].get("kind") == "engine"]
    building.sort(key=lambda p: -statuses[p]["pct"])
    released.sort(key=lambda p: [int(x) for x in statuses[p]["version"].split(".")], reverse=True)

    out = [f"🚧 **{len(building)}** being built · ✅ **{len(released)}** released · 📝 **{len(ready)}** ready to pick up", ""]
    if building:
        out += ["### 🚧 Being built", "", "| Universe | Progress | Where it's at |", "|---|---|---|"]
        for p in building:
            st = statuses[p]
            if st["state"] == "claimed":
                out.append(f"| {name(p, plans[p])} | {bar(0)} | **In progress**<br><sub>{who(plans[p])}{st['where']}</sub> |")
                continue
            when = f", last commit {short_date(st['date'])}" if st.get("date") else ""
            out.append(f"| {name(p, plans[p])} | {bar(st['pct'])} | **Phase {st['phase']} of 6**, {PHASES[st['phase']]}"
                       f"<br><sub>{counts(st)} · {who(plans[p])}{st['where']}{when}</sub> |")
        out.append("")
    if ready:
        out += ["### 📝 Ready to pick up", "", "| Universe | Size |", "|---|---|"]
        for p in ready:
            pl = plans[p]
            out.append(f"| {name(p, pl)} | {pl.get('cast', '?')} characters · {pl.get('places', '?')} places |")
        out.append("")
    if released:
        out += ["### ✅ Released", "", "| Universe | Released in | Size |", "|---|---|---|"]
        for p in released:
            st = statuses[p]
            size = f"{st['drawn']} characters · {st['places']} places" if "drawn" in st else ""
            by = f"<br><sub>by {plans[p]['who']}</sub>" if plans[p].get("who") else ""
            out.append(f"| {name(p, plans[p])} | **{st['version']}**{by} | {size} |")
        out.append("")
    if engine:
        out += ["### ⚙️ Engine plans", "", "| Plan | Status |", "|---|---|"]
        for p in engine:
            st = statuses[p]
            label = {"ready": "📝 planned, no branch pushed yet", "merged": f"✅ merged into `main` ({st.get('where')})",
                     "built": f"🚧 **in progress**<br><sub>{st.get('where')}, last commit {short_date(st['date']) if st.get('date') else '?'}</sub>"}[st["state"]]
            out.append(f"| {name(p, plans[p])} | {label} |")
        out.append("")
    return "\n".join(out).rstrip("\n")


def main():
    check = "--check" in sys.argv
    plans = tracked_plans()
    statuses = {}
    for path, plan in plans.items():
        claimed = path.startswith("in-progress/")
        st = statuses[path] = engine_status(plan) if plan.get("kind") == "engine" else universe_status(plan, claimed)
        # A plan at the top level with something pushed should move to in-progress/ (and to done/ once released).
        if "/" not in path and not path.startswith("README") and plan.get("kind") != "engine" and st["state"] != "ready":
            print(f"note: {path} has a build under way; move it to in-progress/", file=sys.stderr)
        if path.startswith("in-progress/") and st["state"] == "released":
            print(f"note: {path} is released; move it to done/", file=sys.stderr)
        print(f"{path}: {st}")

    old = README.read_text()
    m = re.search(r"(<!-- status:start -->\n).*?(<!-- status:end -->)", old, re.S)
    if not m:
        sys.exit("README.md has no <!-- status:start --> … <!-- status:end --> block")
    new = old[:m.end(1)] + render(plans, statuses) + "\n" + old[m.start(2):]
    if check:
        print(render(plans, statuses))
    elif new != old:
        README.write_text(new)
        print("README.md updated")
    else:
        print("README.md already up to date")


if __name__ == "__main__":
    main()
