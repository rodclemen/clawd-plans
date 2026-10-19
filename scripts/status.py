#!/usr/bin/env python3
"""Refresh the Status column in README.md from what's actually pushed to GitHub.

Each plan carries one hidden line saying where its build lives:

    <!-- track: repo=rodclemen/clawd-clash branch=star_trek folder=ClawdTrek title="Clawd Trek" source="Star Trek" cast=100 places=21 -->

Engine plans (no universe folder) say `kind=engine` instead of folder, title, cast and places.

The script looks at the build repo over GitHub's API and works out how far each universe is:
released in a tag, built on main, or somewhere along its branch. Only pushed branches can be seen.
It then rewrites the block between <!-- status:start --> and <!-- status:end --> in the README: a summary
line, then tables for the universes being built (with a progress bar), ready to pick up, and released. A
universe with no plan here (Clawd of the Rings) gets its track line in the README itself, and `url=` links it.

The detail overhaul (`kind=overhaul`) is worked out from the code and commit messages on main and its branch since
the `since` tag; see overhaul_status.

Run it locally with `python3 scripts/status.py` (it uses `gh auth token` if GITHUB_TOKEN isn't set),
or let .github/workflows/status.yml run it. `--check` prints the block without touching the README.
"""

import json
import os
import re
import shlex
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
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
    """Every file path at `ref`, mapped to its blob sha, or None if the ref isn't on GitHub."""
    t = get(f"/repos/{repo}/git/trees/{q(ref)}?recursive=1")
    return None if t is None else {e["path"]: e["sha"] for e in t["tree"] if e["type"] == "blob"}


_texts = {}


def text(repo, ref, path, blob=None):
    """A file's contents, from raw.githubusercontent.com: it doesn't count against the API's hourly limit. Fetched by
    commit, since raw caches a branch name for a few minutes and would miss what was just pushed. With the blob sha, a
    file that's the same on two refs is only fetched once."""
    if blob and blob in _texts:
        return _texts[blob]
    c = get(f"/repos/{repo}/commits/{q(ref)}")
    url = f"https://raw.githubusercontent.com/{repo}/{c['sha'] if c else q(ref)}/{urllib.parse.quote(path)}"
    req = urllib.request.Request(url, headers={"User-Agent": "clawd-plans-status"})
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    try:
        with urllib.request.urlopen(req) as r:
            body = r.read().decode()
    except urllib.error.HTTPError:
        body = ""
    if blob:
        _texts[blob] = body
    return body


def texts(repo, ref, files, paths):
    """Several files at once, as {path: contents}."""
    paths = sorted(paths)
    with ThreadPoolExecutor(8) as pool:
        return dict(zip(paths, pool.map(lambda p: text(repo, ref, p, files.get(p)), paths)))


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
    main = tree(repo, "main") or {}
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


# The detail overhaul. Every character and place gets a key (its enum case, or its name), and a key is done if:
#   - its drawing code changed since the `since` tag, on main or on the overhaul's branch. Its code is the function its
#     `draw:` / `still:` / `moving:` names, plus every function in the universe that those call; or
#   - a commit message since then covers it: "An audit of all thirty-five Clawd Slayer heroes" (the audit kept the ones
#     already at the bar as they were), or a `Detail: heroes, Area 51` footer naming groups (heroes, villains,
#     places) or names. The universe comes from the commit's scope: `feat(slayer): …` is Slayer.
# The keys from both refs go in one set per universe, so a commit on both, or a place redone twice, counts once.


def funcs(src):
    """Every `func name(…) { … }` in `src`, as {name: body}."""
    out = {}
    for m in re.finditer(r"\bfunc (\w+)\s*(?:<[^>]*>)?\(", src):
        i = src.find("{", m.end())
        depth, j = 0, i
        while 0 <= j < len(src):
            depth += {"{": 1, "}": -1}.get(src[j], 0)
            if depth == 0:
                break
            j += 1
        out.setdefault(m.group(1), src[i:j + 1])
    return out


def drawings(sources):
    """A universe's characters and places, from {path: contents} of its Swift files:
    ({key: (name, group, code)}, {name: code}), where code is everything that draws it."""
    fs = funcs("".join(sources.values()))

    def code(expr):
        seen, todo = set(), re.findall(r"\b(\w+)\b", expr)
        while todo:
            n = todo.pop()
            if n in fs and n not in seen:
                seen.add(n)
                todo += re.findall(r"\b(\w+)\s*\(", fs[n])
        return "".join(fs[n] for n in sorted(seen))

    def call(src, i):
        """The text of the call whose `(` is at src[i], up to its matching `)`."""
        depth = 0
        for j in range(i, len(src)):
            depth += {"(": 1, ")": -1}.get(src[j], 0)
            if depth == 0:
                return src[i:j + 1]
        return src[i:]

    chars, places = {}, {}
    for path, src in sources.items():
        group = "villains" if "Villain" in path else "heroes"
        for m in re.finditer(r"\.(\w+): Persona\(name: \"([^\"]+)\"", src):
            body = call(src, src.index("(", m.start()))
            chars[m.group(1)] = (m.group(2), group, code(body.split("draw:", 1)[-1]))
        for m in re.finditer(r"Place\(name: \"([^\"]+)\"", src):
            body = call(src, src.index("(", m.start()))
            places[m.group(1)] = code(body.split("panel:", 1)[-1])   # still: and moving:, named or as closures
    return chars, places


def universe_drawings(repo, ref, files, folder):
    mine = [p for p in files if p.startswith(f"{UNIVERSES}/{folder}/") and p.endswith(".swift")]
    return drawings(texts(repo, ref, files, mine))


def commits_since(repo, ref, date):
    """{sha: message} for every commit on `ref` after `date`."""
    out, page = {}, 1
    while True:
        batch = get(f"/repos/{repo}/commits?sha={q(ref)}&since={q(date)}&per_page=100&page={page}") or []
        out.update((c["sha"], c["commit"]["message"]) for c in batch)
        if len(batch) < 100:
            return out
        page += 1


def covered(messages, folders):
    """What the commit messages say is done: {folder: set of groups and names}."""
    out = {f: set() for f in folders}
    for msg in messages:
        m = re.match(r"\w+\(([\w-]+)\)!?:", msg)
        hits = [f for f in folders if m and m.group(1).replace("-", "") in f.lower()]
        if len(hits) != 1:
            continue
        said = out[hits[0]]
        said.update(g.lower() for g in re.findall(r"\bAn audit of [^.:]*?\b(heroes|villains)\b", msg, re.I))
        for line in re.findall(r"^Detail:\s*(.+)$", msg, re.M):
            said.update(x.strip() for x in re.split(r",\s*|\s+and\s+", line) if x.strip())
    return out


def overhaul_status(plan):
    """How far the detail overhaul has got in each universe that was out at the `since` tag."""
    repo, branch, since = plan["repo"], plan.get("branch"), plan.get("since", "v3.7.0")
    base = tree(repo, since) or {}
    refs = {"main": tree(repo, "main") or {}}
    if branch and tree(repo, branch) is not None:
        refs[branch] = tree(repo, branch)
    folders = sorted({p.split("/")[3] for p in base if re.match(UNIVERSES + r"/[^/]+/Art/", p)})
    date = get(f"/repos/{repo}/commits/{q(since)}")["commit"]["committer"]["date"]
    messages = {}
    for ref in refs:
        messages.update(commits_since(repo, ref, date))
    said = covered(messages.values(), folders)
    titles = {pl["folder"]: pl.get("title") for pl in tracked_plans().values() if pl.get("folder")}
    rows = []
    for folder in folders:
        old_chars, old_places = universe_drawings(repo, since, base, folder)
        chars, places, done_chars, done_places = {}, {}, set(), set()
        for ref, files in refs.items():
            now_chars, now_places = universe_drawings(repo, ref, files, folder)
            chars.update(now_chars)
            places.update(now_places)
            done_chars |= {k for k, v in now_chars.items() if k not in old_chars or v[2] != old_chars[k][2]}
            done_places |= {k for k, v in now_places.items() if k not in old_places or v != old_places[k]}
        done_chars |= {k for k, (name, group, _) in chars.items() if group in said[folder] or name in said[folder]}
        done_places |= set(places) if "places" in said[folder] else set(places) & said[folder]
        conf, path = {}, f"{UNIVERSES}/{folder}/universe.conf"
        for ref, files in refs.items():   # the title and number, from the module manifest once the refactor has one
            for line in text(repo, ref, path, files[path]).split("\n") if path in files else []:
                k, _, v = line.partition("=")
                if v and not k.strip().startswith("#"):
                    conf.setdefault(k.strip(), v.split("#")[0].strip())
        rows.append(dict(title=conf.get("title") or titles.get(folder) or folder, number=int(conf.get("number", 99)),
                         chars=len(done_chars), places=len(done_places), want_chars=len(chars), want_places=len(places)))
    dates = [d for d in (last_commit(repo, r) for r in refs) if d]
    return dict(state="overhaul", refs=list(refs), since=since.lstrip("v"), date=max(dates) if dates else None, rows=rows)


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
            plans[rel if rel != "README.md" else f"README.md#{fields.get('folder') or fields.get('kind')}"] = fields
    return plans


def bar(pct):
    full = round(pct / 10)
    return f"`{'█' * full}{'░' * (10 - full)}` {pct}%"


def short_date(iso):
    y, m, d = (int(x) for x in iso.split("-"))
    return f"{d} {['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][m - 1]}"


def name(path, plan):
    title = plan.get("title", path)
    url = plan.get("url") or (None if path.startswith("README.md") else path)   # a README entry has no plan to link
    link = f"[{title}]({url})" if url else title
    source = f"<br><sub>{plan['source']}</sub>" if plan.get("source") else ""
    return f"**{link}**{source}"


def who(plan):
    return f"{plan['who']} · " if plan.get("who") else ""


def counts(st, planned=False):
    if planned:
        return f"{st['want']} characters · {st['want_places']} places"
    return f"{st['drawn']}/{st['want']} characters · {st['places']}/{st['want_places']} places"


def pct(done, total):
    return round(100 * done / total) if total else 0


def render_overhaul(plan, st):
    rows = sorted(st["rows"], key=lambda r: (-pct(r["chars"] + r["places"], r["want_chars"] + r["want_places"]), r["number"]))
    chars, places = sum(r["chars"] for r in rows), sum(r["places"] for r in rows)
    want_chars, want_places = sum(r["want_chars"] for r in rows), sum(r["want_places"] for r in rows)
    where = " and ".join(f"`{r}`" for r in st["refs"]) + f" since {st['since']}"
    out = [f"### 🎨 {plan.get('title', 'Detail overhaul')}", ""]
    if plan.get("source"):
        out += [plan["source"], ""]
    out += [f"**Overall** {bar(pct(chars + places, want_chars + want_places))} · {chars}/{want_chars} characters · "
            f"{places}/{want_places} places<br><sub>{where}, last commit {short_date(st['date']) if st.get('date') else '?'}</sub>", "",
            "| Universe | Characters | Places |", "|---|---|---|"]
    for r in rows:
        tick = " ✅" if r["chars"] >= r["want_chars"] and r["places"] >= r["want_places"] else ""
        out.append(f"| **{r['title']}**{tick} | {bar(pct(r['chars'], r['want_chars']))}<br><sub>{r['chars']}/{r['want_chars']}</sub> "
                   f"| {bar(pct(r['places'], r['want_places']))}<br><sub>{r['places']}/{r['want_places']}</sub> |")
    return out + [""]


def render(plans, statuses):
    universe = [p for p in plans if plans[p].get("kind") not in ("engine", "overhaul")]
    building = [p for p in universe if statuses[p]["state"] in ("built", "main", "claimed")]
    ready = [p for p in universe if statuses[p]["state"] == "ready"]
    released = [p for p in universe if statuses[p]["state"] == "released"]
    engine = [p for p in plans if plans[p].get("kind") == "engine"]
    overhaul = [p for p in plans if plans[p].get("kind") == "overhaul"]
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
    for p in overhaul:
        out += render_overhaul(plans[p], statuses[p])
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
        kind = plan.get("kind")
        st = statuses[path] = (engine_status(plan) if kind == "engine" else overhaul_status(plan) if kind == "overhaul"
                               else universe_status(plan, claimed))
        # A plan at the top level with something pushed should move to in-progress/ (and to done/ once released).
        if "/" not in path and not path.startswith("README") and not plan.get("kind") and st["state"] != "ready":
            print(f"note: {path} has a build under way; move it to in-progress/", file=sys.stderr)
        if path.startswith("in-progress/") and st["state"] == "released":
            print(f"note: {path} is released; move it to done/", file=sys.stderr)
        print(f"{path}: {st['state']}")

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
