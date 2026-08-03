# PRD — Turning the notebook into a companion

**Status:** proposal, nothing built yet
**Owner:** E-man
**Date:** August 2026

---

## The problem

What exists today is a very good **notebook**. 111 glossary terms, curriculum notes, a diagram,
assignments filed. It's a place where finished thinking is stored.

A companion is different. A companion is something you reach for *during* the work — mid-call,
mid-pitch, mid-scroll — and something that catches a thought before it evaporates. Three gaps
stand between the two:

**1. Lookup is too slow when it matters.** Finding "pari passu" means opening a browser, loading
the page, typing in a box. In a live conversation that's already too many steps, so I won't do
it — I'll nod and look it up later, which is to say never.

**2. There's nowhere to put a nugget.** When Kelly says something sharp in a session, or I read a
thing that reframes something, there's no capture path shorter than "open an editor, pick a file,
decide where it goes, write markdown, commit." So insights die in the gap between having them and
filing them.

**3. Nothing comes back to me.** The repo only answers when asked. It never says "you wrote this
three weeks ago and it's relevant now," and it never tests whether I actually retained the 111
terms I collected.

## What "companion" means here

Three jobs, in priority order:

1. **Answer fast** — under five seconds from wondering to knowing, without leaving what I'm doing
2. **Catch cheaply** — capture a thought in one line, sort it out later
3. **Come back** — resurface what I've written and check what I've retained

## Non-goals

- Not a CRM. Deal tracking lives in Decile Hub; duplicating it is a trap.
- Not a public publication. This is a working tool that happens to be public.
- Not an app to install. Everything should work from a browser or a terminal I already have open.
- No login, no accounts, no database. The moment this needs infrastructure it stops being durable.

---

## Phase 1 — Make lookup instant

*The highest-value work. Ship this first.*

### 1.1 Keyboard-first search
Press `/` anywhere on the site to focus search. Arrow keys to move, Enter to jump, Escape to
clear. Fuzzy matching, so "liq pref" finds "Liquidation preference."

### 1.2 Deep links per term
Every term gets an anchor: `/glossary.html#pari-passu`. Makes any term linkable from notes,
messages, or an assignment.

### 1.3 A terminal command
```bash
vc pari passu
```
Prints the definition and its example in the terminal. No browser at all. A small script reading
`glossary.md` directly, symlinked into `~/Projects/active/bin/`.

### 1.4 Offline access
A service worker so the glossary works on a plane, in a basement, or on hotel wifi. It's static
text — there's no excuse for it to need a network.

**Done when:** I can go from wondering to knowing in under five seconds, from either a browser
tab or a terminal, without a network.

---

## Phase 2 — Make capture frictionless

*The gap most likely to cause real loss.*

### 2.1 One-line capture
```bash
vc note "Kelly: LPs re-up based on how you handled the bad news, not the good"
```
Appends to `nuggets.md` with a timestamp and an auto-tag. Under three seconds, no decisions
required. The whole point is that filing happens later, not now.

### 2.2 `nuggets.md`
A single append-only file. Insights, quotes, half-thoughts, things a mentor said, questions I
couldn't answer. Chronological, lightly tagged, deliberately unstructured. **This is the file
that makes the notebook mine rather than a summary of public articles.**

### 2.3 Weekly triage
The Tuesday agent already runs. Give it one more job: read new nuggets, propose where each
belongs — a glossary term, a thesis update, an assignment answer, a LinkedIn post — and open a PR.
I approve or reject. Nothing auto-files.

### 2.4 Voice capture
A shortcut that transcribes and appends. The lowest-friction path of all, and the only one that
works while walking or driving — which is when a lot of the actual thinking happens.

**Done when:** capturing a thought costs less effort than losing it.

---

## Phase 3 — Make it come back to me

*Learning, not storage.*

### 3.1 Flashcards
`/quiz` on the site, or `vc quiz` in the terminal. Term on the front, my definition on the back.
Spaced repetition, ordered by what I've missed. The glossary already has 111 cards written — this
just turns them around.

### 3.2 "Explain it to me" mode
The reverse test, which is the one that matters. The site shows a scenario:

> *A company sells for $5M. Series A put in $10M at 1x, Series B put in $15M at 1x, pari passu.
> Who gets what?*

I answer, then reveal. This is the format I actually learn from — I don't remember definitions,
I remember worked situations.

### 3.3 Connections
Cross-links between terms. From "liquidation preference," see seniority, pari passu, stacked
preferences, and the hold-up problem. Learning the neighborhood beats learning the word.

### 3.4 Weekly resurface
The Tuesday report opens with one thing I wrote weeks ago that's relevant to this week's sprint.
Small feature, disproportionate value — it's the difference between an archive and a memory.

---

## Phase 4 — Make it useful in the field

*Only after 1–3 are real.*

### 4.1 Deal memo template
A fill-in page producing a clean memo. Eight prompts including the anti-memo. Exports to markdown
for `deals/`.

### 4.2 Thesis-fit check
A short scored list against my thesis. Does this actually rebuild human trust, or am I stretching
because I like the founder? Written when calm, applied when excited — that's the whole value.

### 4.3 Question bank
The good questions, kept where I can grab them: for founders, for LPs, for references. Sorted by
situation. Grows from `nuggets.md`.

### 4.4 Founder-signal checklist
Built from the research already in the glossary — prior shared experience (68.6% of unicorn
teams), evidence over projections, talent-factory background. A structured read on the team when
there's no revenue to read.

---

## Sequencing

| Phase | Effort | Value | When |
|---|---|---|---|
| 1 — instant lookup | Low | High | Now |
| 2 — capture | Low | Highest | Now |
| 3 — retention | Medium | High | After 1–2 have been used a few weeks |
| 4 — field tools | Medium | Situational | When actually looking at deals |

Phases 1 and 2 are a few hours of work between them and are where nearly all the value is. Do
those, use them for two weeks, then decide whether 3 and 4 earn their keep.

## How we'll know it worked

Not page views. Three questions:

1. Did I look something up *during* a conversation instead of after it?
2. Is there anything in `nuggets.md` that would have otherwise been lost?
3. Could I explain the payout stack to a founder without opening the site?

If all three are yes by the end of the program, it's a companion. If not, it's still a very good
notebook — which is not nothing, but isn't what we set out to build.

## Open questions

- Voice capture: use macOS Shortcuts, or something simpler?
- Does `nuggets.md` stay public? A public commitment to think in the open, or a private file that
  makes me more honest? **Leaning private, synced but gitignored.**
- Should the terminal tool be its own repo so it's installable, or stay a script here?
