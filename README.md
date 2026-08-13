# VC Lab — Venture Institute Notes

My working notebook for **VC Lab's Venture Institute (Cohort 7)**, run by Decile Group through
the Founder Institute portal.

| Section | Page | What it's for |
|---|---|---|
| — | [Home](https://vc-lab.vercel.app) | Where everything is, and how far along it is |
| **Thesis** | [Thesis](https://vc-lab.vercel.app/thesis.html) | What I invest in, the path, the edge |
| **Learn** | [Glossary](https://vc-lab.vercel.app/glossary.html) | 249 terms, each with a worked example and a deep dive |
| | [Curriculum](https://vc-lab.vercel.app/notes.html) | Every VC Lab session, in my words |
| | [How a fund works](https://vc-lab.vercel.app/structure.html) | ManCo/GP/LP and the capital flow |
| | [Drills](https://vc-lab.vercel.app/drills.html) | Waterfall calculator, scenarios, flashcards |
| **Practice** | [Pipeline](https://vc-lab.vercel.app/pipeline.html) | Companies seen, with a reason for every decision |
| | [Deal memo](https://vc-lab.vercel.app/memo.html) | The eight-section template |
| | [Founder impact](https://vc-lab.vercel.app/impact.html) | What I did, and what came of it |
| **Proof** | [Proof package](https://vc-lab.vercel.app/proof.html) | The evidence, scored against a partner's rubric |
| | [VC Lab record](https://vc-lab.vercel.app/assignments.html) | Every assignment, verbatim |

### Why four sections

**Thesis** is the spine — everything else is judged against it. **Learn** is knowledge coming in.
**Practice** is the work itself. **Proof** is what comes out for someone else to read. Mutually
exclusive, collectively exhaustive: every page has exactly one home.

Mirror on GitHub Pages: https://emanxchan.github.io/vc-lab/ — same content, both auto-deploy on push.

---

## Thesis

**AI that rebuilds human trust · pre-seed · US · angel now, fund later.**
See [thesis.md](thesis.md) and [background.md](background.md).

---

## How this repo works

| Path | What's in it |
|---|---|
| [`thesis.md`](thesis.md) | The thesis, the path, and my dealflow edge |
| [`background.md`](background.md) | Who I am, brand values, working rhythm |
| [`sprints/`](sprints/) | One note per VC Lab sprint, in my own words |
| [`assignments/`](assignments/) | The exact text I submitted, dated |
| [`glossary.md`](glossary.md) | VC vocabulary, defined plainly as I encounter it |
| [`profiles/`](profiles/) | One deep dive per term — why it matters, what it looks like, where it goes wrong |
| [`docs/`](docs/) | The published site |
| [`nuggets.md`](nuggets.md) | Captured thoughts, append-only. Triaged weekly. |
| [`script/`](script/) | The `vc` CLI and the glossary build |

## The `/vclab` skill

In any Claude Code session, `/vclab` loads the whole workflow — voice rules, how to read and fill
the fi.co portal, the never-fabricate and never-submit rules, and the glossary build. Say things
like "pull the new sprint prompts", "fill the drafts", or "add these terms to the glossary".

Lives at `~/.claude/skills/vclab/SKILL.md`.

## The `vc` command

```bash
# Learn
vc pari passu          # look up a term — fuzzy, so "liq pref" works
vc quiz                # adaptive flashcards, weighted to what I miss
vc random              # one term, for a spare minute
vc list [section]      # everything, or one section

# Capture
vc note "..."          # catch a thought in 3 seconds
vc notes               # recent captures

# Practice
vc deal "Company"      # start tracking a company
vc pass "Co" reason    # log a pass with its reason
vc memo "Company"      # scaffold the full eight-section memo
vc deals               # show the pipeline
vc impact "Founder"    # log what I did for a founder

# Ship
vc build               # rebuild the site
vc fill                # copy Sunday's answers for the portal
```

Installed via a symlink: `ln -sf ~/Projects/active/vc-lab/script/vc ~/.local/bin/vc`

On the site, press **`/`** to search from anywhere, arrows to move, Enter to jump. Every term has
a deep link (`glossary.html#pari-passu`). The site works offline after one visit.

Each term reads at two depths. The card is the quick answer — the definition and a **Picture this**
example. **Go deeper** expands a drawer with why it matters, what it looks like in practice, where
it goes wrong, where the term comes from, and links to related terms. **Read the full entry** opens
the term's own page at `/g/<term>` for the version worth sitting with.

### Studying it

A **term of the day** sits at the top, the same one all day, cycling through all 249 before it
repeats. Mark anything **Learned** and the tracker fills — with a streak for consecutive days,
milestone marks at 10/25/50/100/249, and a nudge pointing at whichever section is thinnest.

The **🎲 dice** opens a random deep dive. It prefers terms marked learned a week ago and not opened
since — reading the entry resets that clock — then terms not yet learned, then anything. The badge
on the dice is how many are due for review.

Progress lives in `localStorage`, so it is per-browser. **Export progress** copies it as JSON and
**Import** merges it in — earliest learned date, latest seen date — so a phone and a laptop can be
reconciled without a backend.

**The entire site is generated.** Markdown is the source of truth; everything in `docs/` is
built from it. Never hand-edit HTML — edit the markdown and run:

```bash
vc build     # or: python3 script/build.py
```

| Source | Becomes |
|---|---|
| `glossary.md` | glossary.html |
| `profiles/*.md` | the deep-dive drawers, and `docs/g/<term>.html` |
| `thesis.md`, `background.md` | thesis.html |
| `sprints/*.md` | notes.html |
| `assignments/*.md` | assignments.html |
| `deals/*.md` | pipeline.html, proof.html |
| `impact.md` | impact.html |

Terms use a fixed shape: a plain-language definition, then a line starting with
`**Picture this:**` giving a concrete example with real numbers. The build script turns that
second line into the highlighted callout. Keep the shape and new terms format themselves.

---

## Two numbering systems — don't confuse them

This trips people up. The **FI portal sprints** and the **VC Lab curriculum sprints** are
different things.

| FI portal sprint | Covers VC Lab sprints |
|---|---|
| Sprint 1 — Orientation & Investment Thesis | Sprint 0 (orientation, thesis) |
| Sprint 2 — Venture Fundamentals | Sprints 1, 2, 3 (basics, structures, performance) |

Files in `sprints/` follow **VC Lab** numbering. Files in `assignments/` follow whatever the
portal called the set.

## Source-link decoder

Assignment links are shaped `https://vcl.to/VI<sprint>-<session>` and 301-redirect to public
articles on govclab.com. `VI3-2` = VC Lab Sprint 3, Session 2 = Venture Fund Economics.
No login needed.

**WebFetch returns the redirect rather than following it cross-host** — fetch the `vcl.to` URL
first, then fetch the govclab.com target it reports.

Currently live: **Sprints 1–3, plus 4.3.** Everything else (`VI2-4`, `VI3-4`, `VI4-1/2/4`, and
most of Sprints 5–8) returns a Rebrandly broken-link page. Sprints 5–8 run inside Decile Hub and
may never have public articles.

**Exception:** `vcl.to/VI7-2` does **not** point to a govclab article — it redirects to a Google
Doc *worksheet* (`docs.google.com/.../copy`) containing the Sprint 2 assignment sets. Not every
working short link is an article; check where it actually lands.

## VC Lab curriculum map

| Sprint | Title | Notes |
|---|---|---|
| 0 | Orientation | ☑ |
| 1 | Introduction to VC Basics | ☑ |
| 2 | Venture Capital Firm Structures | ☑ |
| 3 | Venture Capital Performance | ☑ |
| 4 | Finding and Closing Limited Partners | ☑ read-ahead |
| 5 | Venture Deals | ☐ prep only |
| 6 | Venture Operations | ☐ prep only |
| 7 | Venture Accounting | ☐ prep only |
| 8 | Venture Careers | ☐ prep only |

---

## Working agreement

Conventions for anyone (including future me, or Claude) picking this up cold.

**Voice**
- I'm an **angel first**, fund later. Don't write GP-fund-sizing arguments as if I run a fund.
- Plain language over jargon. Define the term the first time it appears.
- My thesis is **"AI rebuilding human trust"** — bridges, community bonds, belonging. Not the
  vaguer "AI and humanity." That framing was corrected once; don't drift back.
- No tables in wedge/positioning work — prose and simple lists read better there.

**Process**
- **List before you push.** For anything scraped or imported, show me the inventory with
  keep/skip recommendations first. This is how we kept vendor marketing copy out of the repo.
- Vendor/marketing copy pasted from Decile Base or Hub is **slop** — skip it. Keep only what I
  actually thought or wrote.
- Don't edit anything in the FI portal (fi.co) unless I explicitly ask. Drafting text for me to
  paste is fine; submitting on my behalf is not.
- Assignments get filed in `assignments/` verbatim as submitted, so the repo matches the record.

**Reading the portal**
- `https://fi.co/enrolled/assignments` lists sprints; each sprint page has 7 sets.
- Sets are collapsed by default and "Expand all" doesn't reliably work. Submitted answers live
  in `<trix-editor>` elements — read them with the javascript tool:
  `Array.from(document.querySelectorAll('trix-editor')).map(e => e.innerText)`
- Requires my live Chrome session. A scheduled/cloud agent **cannot** reach fi.co.

**What I have to supply**
Live session content — mentor feedback, Airmeet discussion, working group — is invisible to any
tool. If it matters, I have to write it down.

---

## The weekly loop

Two scheduled cloud agents run against this repo. Neither can reach fi.co, so prompts get to them
only through `assignments/INBOX.md`.

| When | Agent | What it does |
|---|---|---|
| **Tue 7pm PT** | Weekly check | Probes every `vcl.to` link, audits the repo, drafts answers to anything in the inbox, and ends with numbered questions for me. Opens a PR. |
| **Sun 10am PT** | Submission prep | Reads my answers from the week, writes the final copy-paste-ready versions, flags what's still missing. Opens a PR. |

**My job in the loop, in order:**

1. Paste new assignment prompts into [`assignments/INBOX.md`](assignments/INBOX.md).
2. Tuesday: answer the questions in the PR — either as **PR comments**, or by appending a section
   headed `## My answers` to that week's file in `weekly/`. The Sunday agent reads both.
3. Sunday: run `vc fill`, paste into the Chrome console on the assignment page, review, submit.
4. File the submitted text in `assignments/` and clear the block from `INBOX.md`.

### Getting Sunday's answers into the portal

The cloud agents have no browser and **cannot reach fi.co** — it needs an authenticated session.
So the Sunday agent writes `weekly/YYYY-MM-DD-fill.json` alongside its report, and:

```bash
vc fill          # pulls latest, copies a browser snippet to the clipboard
```

Then: open the assignment page in Chrome → `Option+Cmd+J` for the console → paste → Enter.
Every set is filled at once. **Nothing is ever submitted automatically** — review each answer,
then click Save Draft or Submit myself.

Or just open a Claude Code session and ask it to fill the drafts; it does the same thing
through the browser tools.

The answers I give on Tuesday are the whole point — they're what makes Sunday's output mine rather
than generic. A detail I supply should visibly change the text.

**Portal formatting:** FI uses a Trix rich-text editor. Markdown does not render. Paste plain
paragraphs with simple lists — no tables, no code fences, no `#` headings.

## Commitment

I'm keeping this glossary and these notes current for the full program. Every term I don't know
goes in. By the end I want a reference I actually built rather than a list I skimmed.
