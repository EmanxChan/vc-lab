# VC Lab — Venture Institute Notes

My working notebook for **VC Lab's Venture Institute (Cohort 7)**, run by Decile Group through
the Founder Institute portal.

| Page | URL |
|---|---|
| Home | https://vc-lab.vercel.app |
| Glossary | https://vc-lab.vercel.app/glossary.html |
| Structure & capital flow | https://vc-lab.vercel.app/structure.html |
| Curriculum notes | https://vc-lab.vercel.app/notes.html |

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
| [`docs/`](docs/) | The published site |
| [`script/`](script/) | Build tooling |

**The glossary is generated.** `glossary.md` is the single source of truth; `docs/glossary.html`
is built from it. Never hand-edit the HTML — edit the markdown and run:

```bash
python3 script/build-glossary.py
```

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
3. Sunday: copy the final answers out of the submission-prep PR and paste them into the portal.
   Neither agent submits anything on my behalf.
4. File the submitted text in `assignments/` and clear the block from `INBOX.md`.

The answers I give on Tuesday are the whole point — they're what makes Sunday's output mine rather
than generic. A detail I supply should visibly change the text.

**Portal formatting:** FI uses a Trix rich-text editor. Markdown does not render. Paste plain
paragraphs with simple lists — no tables, no code fences, no `#` headings.

## Commitment

I'm keeping this glossary and these notes current for the full program. Every term I don't know
goes in. By the end I want a reference I actually built rather than a list I skimmed.
