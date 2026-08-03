#!/usr/bin/env python3
"""Build the whole vc-lab site from markdown.

    python3 script/build.py

Everything in docs/ is generated. Never hand-edit it — edit the markdown and
rebuild. Sources:

    glossary.md              -> glossary.html
    thesis.md, background.md -> thesis.html
    sprints/*.md             -> notes.html
    assignments/*.md         -> assignments.html
    deals/*.md               -> pipeline.html, proof.html
    impact.md                -> impact.html
"""

import json
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib_md import inline, render, slug, strip_md          # noqa: E402
from lib_shell import hero, page                            # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SITE = "https://vc-lab.vercel.app"
FAVICON = "🧭"   # tab icon — a companion is a thing you navigate by

SHORT_LABELS = {
    "the-rounds-how-money-arrives": "Rounds",
    "the-paperwork-how-the-money-is-structured": "Paperwork",
    "ownership-who-owns-what-and-how-it-shrinks": "Ownership",
    "the-protective-terms-what-investors-ask-for": "Deal terms",
    "the-payout-stack-who-actually-gets-paid-first": "Payout stack",
    "how-a-fund-is-built": "Fund structure",
    "how-a-fund-makes-money": "Fund economics",
    "keeping-score": "Metrics",
    "doing-the-work": "The work",
    "how-companies-are-judged": "Judging companies",
    "getting-out": "Exits",
}

STATUS_ORDER = ["invested", "diligence", "screening", "tracking", "passed"]
STATUS_LABEL = {
    "invested": "Invested",
    "diligence": "In diligence",
    "screening": "Screening",
    "tracking": "Tracking",
    "passed": "Passed",
}


# ---------------------------------------------------------------- helpers

def read(p: Path) -> str:
    return p.read_text() if p.exists() else ""


def frontmatter(text: str) -> tuple[dict, str]:
    """Parse a leading --- key: value --- block."""
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).split("\n"):
        if ":" in line:
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip()
    return meta, m.group(2)


def load_deals() -> list[dict]:
    out = []
    for p in sorted((ROOT / "deals").glob("*.md")):
        if p.name.startswith("_"):
            continue
        meta, body = frontmatter(read(p))
        meta["slug"] = p.stem
        meta["body"] = body.strip()
        meta.setdefault("status", "screening")
        meta.setdefault("name", p.stem.replace("-", " ").title())
        out.append(meta)
    return out


def load_glossary() -> list[tuple[str, list[tuple[str, str]], str]]:
    md = read(ROOT / "glossary.md")
    sections = []
    for part in re.split(r"^## ", md, flags=re.M)[1:]:
        title, _, rest = part.partition("\n")
        label = re.sub(r"^\d+\.\s*", "", title).strip()
        rest = rest.replace("\n---\n", "\n")
        chunks = re.split(r"^### ", rest, flags=re.M)
        prose = chunks[0].strip()
        terms = []
        for chunk in chunks[1:]:
            name, _, body = chunk.partition("\n")
            terms.append((name.strip(), body.strip()))
        sections.append((label, terms, prose))
    return sections


def render_term_body(body: str) -> str:
    """Term body with the 'Picture this' line lifted into a callout."""
    body = re.sub(r"\n(?=\*\*(?:Picture this|The tension))", "\n\n", body)
    out = []
    for block in re.split(r"\n\s*\n", body.strip()):
        if not block.strip():
            continue
        html_block = render(block, skip_h1=False)
        if block.lstrip().startswith(("**Picture this", "**The tension")):
            out.append(f'<div class="example">{html_block}</div>')
        else:
            out.append(html_block)
    return "".join(out)


# ---------------------------------------------------------------- pages

def build_glossary(sections) -> int:
    chunks, count, secs = [], 0, []
    for label, terms, prose in sections:
        if not terms:
            chunks.append(f'    <div class="group-label">{inline(label)}</div>')
            chunks.append(f'    <div class="sources">{render(prose, skip_h1=False)}</div>')
            continue
        s = slug(label)
        secs.append((s, label, len(terms)))
        chunks.append(f'    <div class="group-label" data-section="{s}">{inline(label)}</div>')
        if prose:
            chunks.append(f'    <p class="section-intro" data-section="{s}">{inline(prose)}</p>')
        for name, body in terms:
            count += 1
            a = slug(name)
            chunks.append(
                f'    <div class="term" id="{a}" data-section="{s}" data-order="{count}">\n'
                f'      <div class="term-section">{inline(label)}</div>\n'
                f'      <h3>{inline(name)}<a class="anchor" href="#{a}">#</a></h3>\n'
                f'      {render_term_body(body)}\n'
                f'    </div>'
            )

    filters = "\n".join(
        f'      <button class="chip" data-section="{s}" aria-pressed="false">'
        f'{SHORT_LABELS.get(s, lbl)}<span class="n">{n}</span></button>'
        for s, lbl, n in secs
    )

    body = f"""
  <div class="search-wrap">
    <div class="search-row">
      <input type="text" id="search" placeholder="Search {count} terms…" autocomplete="off">
      <span class="hint"><span class="kbd">/</span> search &nbsp;
      <span class="kbd">↑↓</span> move &nbsp;
      <span class="kbd">enter</span> open &nbsp;
      <span class="kbd">esc</span> clear</span>
    </div>
    <div class="controls">
      <span class="controls-label">Filter</span>
      <button class="chip" data-section="" aria-pressed="true">All<span class="n">{count}</span></button>
{filters}
    </div>
    <div class="controls">
      <span class="controls-label">Sort</span>
      <button class="chip" data-sort="curriculum" aria-pressed="true">Curriculum order</button>
      <button class="chip" data-sort="az" aria-pressed="false">A–Z</button>
      <button class="chip" data-sort="za" aria-pressed="false">Z–A</button>
      <span class="controls-divider"></span>
      <button class="chip" id="shuffle" aria-pressed="false">Shuffle</button>
    </div>
  </div>

  <p class="result-count" id="result-count"></p>

  <div id="terms">
{chr(10).join(chunks)}
  </div>

  <p class="no-results" id="no-results" style="display:none">No terms match that search.</p>
"""

    (DOCS / "glossary.html").write_text(page(
        title="glossary — vc companion",
        description=f"Venture capital in plain English — {count} terms, each with a concrete example.",
        section="learn", current="glossary.html",
        hero=hero("vc", "glossary",
                  f"Venture capital in plain English — <strong>{count} terms</strong>, each with a "
                  "concrete example. No jargon defined using more jargon.",
                  eyebrow="Learn"),
        body=body, extra_css=GLOSSARY_CSS, extra_js=GLOSSARY_JS,
    ))
    return count


def build_thesis() -> None:
    t = read(ROOT / "thesis.md")
    b = read(ROOT / "background.md")
    body = f"""
<div class="grid grid-2" style="margin-bottom:3rem">
  <div class="card">
    <div class="card-label">Sector</div>
    <div class="card-value">AI rebuilding trust</div>
    <p>Bridges, community bonds, belonging — technology that strengthens human connection instead
    of corroding it.</p>
  </div>
  <div class="card">
    <div class="card-label">Stage &amp; geography</div>
    <div class="card-value">Pre-seed &middot; US</div>
    <p>The earliest priceable moment, in the United States.</p>
  </div>
  <div class="card">
    <div class="card-label">Vehicle</div>
    <div class="card-value">Angel &rarr; Fund</div>
    <p>Personal checks now to build a real track record. A fund once there's evidence rather than
    assertion.</p>
  </div>
  <div class="card">
    <div class="card-label">Edge</div>
    <div class="card-value">Three ecosystems</div>
    <p>Plug and Play, Grid110, Material Change — founders building trust tech already know me.</p>
  </div>
</div>

<section>
  <h2 class="section-title"><span>The thesis</span></h2>
  <div class="prose">{render(t)}</div>
</section>

<section>
  <h2 class="section-title"><span>Background</span><span class="dim">who I am, how I work</span></h2>
  <div class="prose">{render(b)}</div>
</section>
"""
    (DOCS / "thesis.html").write_text(page(
        title="thesis — vc companion",
        description="AI that rebuilds human trust. Pre-seed, US, angel now and a fund later.",
        section="thesis", current="thesis.html",
        hero=hero("my", "thesis",
                  "AI that rebuilds human trust &middot; pre-seed &middot; United States &middot; "
                  "angel now, fund later.", eyebrow="Thesis"),
        body=body,
    ))


def build_notes() -> None:
    files = sorted((ROOT / "sprints").glob("sprint-*.md"))
    cards, bodies = [], []
    for p in files:
        md = read(p)
        first = md.split("\n", 1)[0].lstrip("# ").strip()
        num = re.search(r"sprint-(\d+)", p.stem)
        n = num.group(1) if num else "?"
        title = re.sub(r"^Sprint\s*\d+\s*[—-]\s*", "", first)
        done = "prep only" not in md.lower() and "not yet covered" not in md.lower()
        a = slug(p.stem)
        cards.append(
            f'<a class="card" href="#{a}">'
            f'<div class="card-label">Sprint {n}</div>'
            f'<h3>{inline(title)}</h3>'
            f'<span class="tag {"on" if done else ""}">{"Covered" if done else "Prep only"}</span>'
            f'</a>'
        )
        bodies.append(
            f'<section id="{a}">'
            f'<h2 class="section-title"><span>{inline(first)}</span>'
            f'<span class="dim">{"covered" if done else "prep only"}</span></h2>'
            f'<div class="prose">{render(md)}</div></section>'
        )

    body = (
        '<div class="grid grid-3" style="margin-bottom:3rem">' + "".join(cards) + "</div>"
        + "".join(bodies)
    )
    (DOCS / "notes.html").write_text(page(
        title="curriculum — vc companion",
        description="Session-by-session notes from every sprint of VC Lab's Venture Institute.",
        section="learn", current="notes.html",
        hero=hero("curriculum", "notes",
                  "Every VC Lab session, in my own words. Sources are public articles on "
                  '<a href="https://govclab.com">govclab.com</a>, reachable via '
                  "<code>vcl.to/VI&lt;sprint&gt;-&lt;session&gt;</code>.",
                  eyebrow="Learn"),
        body=body,
    ))


def build_assignments() -> None:
    files = [p for p in sorted((ROOT / "assignments").glob("*.md"))
             if p.name != "INBOX.md"]
    cards, bodies = [], []
    for p in files:
        md = read(p)
        meta, _ = frontmatter(md)
        first = md.split("\n", 1)[0].lstrip("# ").strip()
        title = re.sub(r"^Assignment\s*[—-]\s*", "", first)
        sub = re.search(r"\*\*Submitted:\*\*\s*([^\n·|*]+)", md)
        when = sub.group(1).strip() if sub else ""
        status = "Submitted" if sub else "Draft"
        a = slug(p.stem)
        cards.append(
            f'<a class="card" href="#{a}">'
            f'<div class="card-label">{inline(when) or "Filed"}</div>'
            f'<h3>{inline(title)}</h3>'
            f'<span class="tag {"on" if status == "Submitted" else "warn"}">{status}</span>'
            f'</a>'
        )
        bodies.append(
            f'<section id="{a}">'
            f'<h2 class="section-title"><span>{inline(title)}</span>'
            f'<span class="dim">{inline(when)}</span></h2>'
            f'<div class="prose">{render(md)}</div></section>'
        )

    inbox = read(ROOT / "assignments" / "INBOX.md")
    pending = len(re.findall(r"^### Set ", inbox, flags=re.M))
    banner = ""
    if pending:
        m = re.search(r"^## (.+)$", inbox, flags=re.M)
        name = m.group(1) if m else "Current sprint"
        banner = (f'<div class="callout"><strong>{inline(name)}</strong> — '
                  f'{pending} sets queued and not yet answered. '
                  f'They are in <code>assignments/INBOX.md</code>, which is what the weekly '
                  f'agents read.</div>')

    body = (banner + '<div class="grid grid-3" style="margin:2rem 0 3rem">'
            + "".join(cards) + "</div>" + "".join(bodies))
    (DOCS / "assignments.html").write_text(page(
        title="vc lab record — vc companion",
        description="Every assignment submitted to VC Lab's Venture Institute, kept verbatim.",
        section="proof", current="assignments.html",
        hero=hero("vc lab", "record",
                  "Every assignment I've submitted, kept verbatim. The public record of how my "
                  "thinking developed rather than a claim about where it landed.",
                  eyebrow="Proof"),
        body=body,
    ))


def build_pipeline(deals) -> None:
    by_status = {s: [d for d in deals if d.get("status") == s] for s in STATUS_ORDER}
    total = len(deals)
    passed = len(by_status["passed"])
    active = total - passed

    stats = f"""
<div class="grid grid-4" style="margin-bottom:2.5rem">
  <div class="card stat"><div class="n">{total}</div><div class="l">Companies seen</div></div>
  <div class="card stat"><div class="n">{active}</div><div class="l">Active</div></div>
  <div class="card stat"><div class="n">{passed}</div><div class="l">Passed, with reasons</div></div>
  <div class="card stat"><div class="n">{len(by_status['invested'])}</div><div class="l">Invested</div></div>
</div>"""

    if not deals:
        body = stats + """
<div class="empty">
  <p>No companies yet.</p>
  <p style="margin-top:0.75rem">Add one with <code>vc deal add "Company Name"</code>, then fill in
  the file it creates in <code>deals/</code>.</p>
</div>

<div class="callout accent" style="margin-top:2.5rem">
  <strong>Why the passes matter more than the advances.</strong> Anyone can list companies they
  liked. A written reason for every pass is what shows a partner how you actually filter — and it
  is the only way to find out your filter is miscalibrated.
</div>"""
    else:
        blocks = []
        for s in STATUS_ORDER:
            group = by_status[s]
            if not group:
                continue
            rows = []
            for d in group:
                url = d.get("url", "")
                name = (f'<a href="{url}" target="_blank" rel="noopener">{inline(d["name"])}</a>'
                        if url else inline(d["name"]))
                rows.append(
                    "<tr>"
                    f"<td><strong>{name}</strong></td>"
                    f'<td>{inline(d.get("one_liner", d.get("one-liner", "")))}</td>'
                    f'<td>{inline(d.get("source", ""))}</td>'
                    f'<td>{inline(d.get("stage", ""))}</td>'
                    f'<td>{inline(d.get("fit", ""))}</td>'
                    f'<td>{inline(d.get("reason", ""))}</td>'
                    "</tr>"
                )
            blocks.append(
                f'<section><h2 class="section-title"><span>{STATUS_LABEL[s]}</span>'
                f'<span class="dim">{len(group)}</span></h2>'
                '<div class="table-wrap"><table><thead><tr>'
                "<th>Company</th><th>What they do</th><th>Source</th>"
                "<th>Stage</th><th>Fit</th><th>Note</th>"
                "</tr></thead><tbody>" + "".join(rows) + "</tbody></table></div></section>"
            )
        body = stats + "".join(blocks)

    (DOCS / "pipeline.html").write_text(page(
        title="pipeline — vc companion",
        description="Companies seen, screened, and passed on — with a written reason for every decision.",
        section="practice", current="pipeline.html",
        hero=hero("deal", "pipeline",
                  "Every company I've looked at, with a written reason for every decision. "
                  "The passes are the point.", eyebrow="Practice"),
        body=body,
    ))


def build_impact() -> None:
    md = read(ROOT / "impact.md")
    entries = len(re.findall(r"^### ", md, flags=re.M))
    body = f"""
<div class="grid grid-4" style="margin-bottom:2.5rem">
  <div class="card stat"><div class="n">{entries}</div><div class="l">Founders helped</div></div>
</div>
<div class="prose">{render(md)}</div>"""
    (DOCS / "impact.html").write_text(page(
        title="founder impact — vc companion",
        description="What I actually did for founders, and what came of it.",
        section="practice", current="impact.html",
        hero=hero("founder", "impact",
                  "What I actually did for founders, and what came of it. Not a claim that I'm "
                  "helpful — a record.", eyebrow="Practice"),
        body=body,
    ))


def build_memo() -> None:
    md = read(ROOT / "deals" / "_template.md")
    _, tmpl = frontmatter(md)
    body = f"""
<div class="callout accent">
  <strong>How to use this.</strong> Run <code>vc memo "Company Name"</code> to scaffold a memo in
  <code>deals/</code>. Write it in under 90 minutes. If it takes longer, the thinking isn't clear
  yet — that's information too.
</div>

<section>
  <h2 class="section-title"><span>The eight sections</span></h2>
  <div class="prose">{render(tmpl)}</div>
</section>

<section>
  <h2 class="section-title"><span>The anti-memo</span><span class="dim">the section people skip</span></h2>
  <div class="prose">
    <p>Write the strongest possible case <em>against</em> the investment, honestly, as if you were
    being paid to kill it. Three reasons it matters:</p>
    <ul>
      <li>Investors read pitches by <strong>elimination by aspects</strong> — hunting for the fatal
      flaw. If you haven't found it, someone else will, and later.</li>
      <li>It's the difference between conviction and enthusiasm. If you can't articulate the bear
      case, you don't understand the company yet.</li>
      <li>When a deal goes wrong, the anti-memo tells you whether you were unlucky or wrong. Only
      one of those is fixable.</li>
    </ul>
  </div>
</section>"""
    (DOCS / "memo.html").write_text(page(
        title="deal memo — vc companion",
        description="The deal memo template: eight sections including an honest anti-memo.",
        section="practice", current="memo.html",
        hero=hero("deal", "memo",
                  "Eight sections, writable in ninety minutes, including the case against.",
                  eyebrow="Practice"),
        body=body,
    ))


def build_proof(deals, term_count) -> None:
    passed = [d for d in deals if d.get("status") == "passed"]
    impact = len(re.findall(r"^### ", read(ROOT / "impact.md"), flags=re.M))
    memos = len([d for d in deals if len(d.get("body", "")) > 400])
    assignments = len([p for p in (ROOT / "assignments").glob("*.md")
                       if p.name != "INBOX.md"])

    items = [
        ("Market map", len(deals), 40, "pipeline.html",
         "Companies in my niche, categorized and dated. Shows sourcing reach."),
        ("Screen with reasons", len(passed), 10, "pipeline.html",
         "Every pass with a written reason. Shows what I actually filter on."),
        ("Investment memos", memos, 1, "memo.html",
         "Full memos with the anti-memo attached. Shows I can write something a partner acts on."),
        ("Founder impact", impact, 3, "impact.html",
         "Named founders, what I did, what came of it. Shows the support edge is real."),
        ("VC Lab record", assignments, 5, "assignments.html",
         "Public, dated assignments. Shows how the thinking developed."),
        ("Glossary", term_count, 100, "glossary.html",
         "Vocabulary built from the work, each term with a worked example."),
    ]

    cards = []
    for label, have, target, href, why in items:
        pct = min(100, round(100 * have / target)) if target else 0
        done = have >= target
        cards.append(f"""
  <a class="card" href="{href}">
    <div class="card-label">{label}</div>
    <div class="card-value">{have}<span class="dim" style="font-size:0.55em"> / {target}</span></div>
    <div class="progress-track" style="margin:0.6rem 0 0.9rem">
      <div class="progress-fill" style="width:{pct}%"></div>
    </div>
    <p>{why}</p>
    <div style="margin-top:0.9rem"><span class="tag {'on' if done else ''}">
      {'Ready' if done else 'Building'}</span></div>
  </a>""")

    ready = sum(1 for _, h, t, *_ in items if h >= t)

    body = f"""
<div class="callout">
  <strong>The gap this closes.</strong> I have operating experience and a network. What I don't yet
  have is visible evidence of investment judgment — nobody can currently look at anything and see
  how I evaluate a company. Everything below is that evidence, built in public and dated.
</div>

<section>
  <h2 class="section-title"><span>The package</span><span class="dim">{ready} of {len(items)} ready</span></h2>
  <div class="grid grid-3">{''.join(cards)}</div>
</section>

<section>
  <h2 class="section-title"><span>The rubric</span><span class="dim">how a partner would score this</span></h2>
  <div class="prose">
    <ol>
      <li><strong>Judgment quality.</strong> Do the passes show a real filter, or does this person
      like everything? The reasons for saying no are the signal.</li>
      <li><strong>Sourcing edge.</strong> Did these companies come from somewhere the fund couldn't
      reach on its own, or are they on the same lists everyone reads?</li>
      <li><strong>Written clarity.</strong> Could a partner act on the memo in ten minutes? Is the
      anti-memo genuinely adversarial or decorative?</li>
      <li><strong>Thesis discipline.</strong> Is a coherent filter being applied, or is "AI for
      trust" stretched to fit whatever was interesting that week?</li>
      <li><strong>Founder value, evidenced.</strong> Is there proof a founder is better off, with a
      named outcome — not a claim of helpfulness?</li>
    </ol>
  </div>
</section>"""
    (DOCS / "proof.html").write_text(page(
        title="proof package — vc companion",
        description="Evidence of investment judgment: pipeline, screens, memos, and founder impact.",
        section="proof", current="proof.html",
        hero=hero("proof", "package",
                  "The evidence a fund can read. Built in public, dated, and updated as the work "
                  "happens.", eyebrow="Proof"),
        body=body,
    ))


DIAGRAM = """          HOW CAPITAL FLOWS THROUGH A VENTURE FUND
          ========================================

        +--------------------------------------+
        |           LIMITED PARTNERS           |
        |                (LPs)                 |
        |   family offices, funds of funds,    |
        |  exited founders, tech execs, HNWIs  |
        +--------------------------------------+
              |                          ^
   (1) commit |                          | (6) distributions
       capital|                          |     1. LP capital returned
       + calls|                          |     2. preferred return ~8%
              v                          |     3. remainder split 80/20
        +--------------------------------------+       +------------------------+
        |               THE FUND               |--2%-->|   MANAGEMENT COMPANY   |
        |       (a Limited Partnership)        |  fee  |        (ManCo)         |
        |   holds the capital and the shares   |       | brand, IP, staff, ops  |
        +--------------------------------------+       +------------------------+
              |                          ^
   (3) invest |                          | (5) exit proceeds
              |                          |     IPO / M&A / secondary
              v                          |
        +--------------------------------------+       +------------------------+
        |         PORTFOLIO COMPANIES          |<--(4)-|    GENERAL PARTNER     |
        |      (the startups in the fund)      | picks |          (GP)          |
        +--------------------------------------+       |  decides every deal,   |
                                                       |  earns 20% carry after |
                                                       |  LPs are made whole    |
                                                       +------------------------+"""

ENTITIES = [
    ("Limited Partner (LP)",
     "The investor in the fund — family offices, funds of funds, exited founders, tech executives, "
     "and high-net-worth individuals. LPs commit capital and have it called over time, but they "
     "don't pick companies and don't run anything. Their liability is limited to what they "
     "committed, which is what makes them “limited.”"),
    ("Management Company (ManCo)",
     "The operating business. It owns the firm's brand and intellectual property, employs the "
     "staff, signs the vendor contracts, and pays the bills. Funded by the management fee — "
     "roughly 2% of committed capital per year. Think of it as the firm you'd actually go to "
     "work at."),
    ("The Fund",
     "A limited partnership that exists to hold money and shares. LPs commit to it, it calls their "
     "capital, it buys equity in startups, and it holds those securities on everyone's behalf. It "
     "has no employees. Most firms run several funds at once, each a separate vehicle with its own "
     "vintage and LPs."),
    ("General Partner (GP)",
     "The decision-making entity. Composed of managing partners, general partners, and venture "
     "partners, the GP chooses every investment the fund makes and carries unlimited liability for "
     "it. In exchange it earns carried interest — typically 20% of profits, and only after LPs "
     "have received their capital back plus a preferred return."),
]


def build_structure() -> None:
    cards = "".join(
        f'<div class="card"><h3>{inline(n)}</h3><p>{inline(d)}</p></div>'
        for n, d in ENTITIES
    )
    body = f"""
<section>
  <h2 class="section-title"><span>The diagram</span><span class="dim">ManCo · GP · LP</span></h2>
  <div class="diagram"><pre>{DIAGRAM.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')}</pre></div>
</section>

<section>
  <h2 class="section-title"><span>The four entities</span></h2>
  <div class="grid grid-2">{cards}</div>
</section>

<section>
  <h2 class="section-title"><span>What "ManCo, GP, LP" means</span></h2>
  <div class="prose" style="max-width:780px">
    <p>The phrase describes the three-entity structure that nearly every venture firm uses. What
    looks from the outside like one company is actually three legal entities with deliberately
    separated jobs: the <strong>ManCo</strong> runs the business and is paid fees, the
    <strong>GP</strong> makes investment decisions and is paid carry, and the <strong>Fund</strong>
    holds the LPs' capital and the securities it buys.</p>
    <p>The separation is the point. It keeps operating expenses, performance compensation, and
    investor capital in three different pockets, so a firm can't quietly fund payroll out of
    investor money or let one fund's problems reach another's assets. It also isolates liability —
    the GP carries unlimited liability for investment decisions, while LPs risk only what they
    committed.</p>
    <p>All three are typically structured as pass-through entities, so profits aren't taxed at the
    entity level and instead flow to individual returns — avoiding double taxation on the same
    gains. Practically, it means a fund manager wears three hats at once: operator of the ManCo,
    decision-maker at the GP, and fiduciary to the Fund.</p>
  </div>
  <div class="callout accent">
    Want to see what this means at exit? The
    <a href="drills.html">waterfall calculator</a> shows who actually gets paid, and in what order.
  </div>
</section>"""
    (DOCS / "structure.html").write_text(page(
        title="how a fund works — vc companion",
        description="The ManCo, GP, LP structure and how capital flows from commitment to distribution.",
        section="learn", current="structure.html",
        hero=hero("capital", "flow",
                  "How a venture fund is actually organized — and how money travels from an LP's "
                  "commitment, through startups, and back out again.", eyebrow="Learn"),
        body=body,
        extra_css=".diagram{background:var(--card);border:1px solid var(--line);border-radius:6px;"
                  "padding:1.5rem;overflow-x:auto;margin:1rem 0 2rem}"
                  ".diagram pre{background:none;border:none;padding:0;font-size:0.7rem;"
                  "line-height:1.35;white-space:pre;color:var(--text)}",
    ))


def build_drills(sections) -> None:
    terms = [(t, b) for _, ts, _ in sections for t, b in ts]
    payload = json.dumps([
        {"t": t, "d": strip_md(b.split("**Picture this")[0])[:400]}
        for t, b in terms
    ], ensure_ascii=False)

    body = f"""
<section>
  <h2 class="section-title"><span>Waterfall calculator</span>
  <span class="dim">who gets what at exit</span></h2>
  <p style="color:var(--muted);font-size:0.92rem;margin-bottom:1.5rem">
    Change the numbers and watch the split move. This is the fastest way to internalize why
    a "$40M exit" can mean everything or nothing depending on the stack above you.</p>

  <div class="calc">
    <div class="calc-inputs">
      <label>Exit price <span class="unit">$M</span>
        <input type="number" id="exit" value="40" min="0" step="1"></label>
      <label>Series A invested <span class="unit">$M</span>
        <input type="number" id="a-inv" value="10" min="0" step="0.5"></label>
      <label>Series A preference <span class="unit">×</span>
        <input type="number" id="a-mult" value="1" min="0" step="0.5"></label>
      <label>Series A ownership <span class="unit">%</span>
        <input type="number" id="a-own" value="25" min="0" max="100" step="1"></label>
      <label>Series B invested <span class="unit">$M</span>
        <input type="number" id="b-inv" value="15" min="0" step="0.5"></label>
      <label>Series B preference <span class="unit">×</span>
        <input type="number" id="b-mult" value="1" min="0" step="0.5"></label>
      <label>Series B ownership <span class="unit">%</span>
        <input type="number" id="b-own" value="19" min="0" max="100" step="1"></label>
      <label>Waterfall
        <select id="mode">
          <option value="senior">Seniority (B paid first)</option>
          <option value="pari">Pari passu (shared pro rata)</option>
        </select></label>
    </div>
    <div class="calc-out" id="calc-out"></div>
  </div>
</section>

<section>
  <h2 class="section-title"><span>Scenarios</span><span class="dim">answer, then reveal</span></h2>
  <div id="scenarios"></div>
</section>

<section>
  <h2 class="section-title"><span>Explain it to me</span>
  <span class="dim">the reverse test</span></h2>
  <p style="color:var(--muted);font-size:0.92rem;margin-bottom:1.25rem">
    A term appears. Say the definition out loud, in plain language, as if to a founder. Then
    reveal. Getting this right matters more than recognizing the term on a page.</p>
  <div class="flash card" id="flash">
    <div class="flash-term" id="flash-term">—</div>
    <div class="flash-def" id="flash-def"></div>
    <div class="controls" style="margin-top:1.25rem">
      <button class="chip" id="flash-reveal">Reveal</button>
      <button class="chip" id="flash-next">Next term</button>
      <span class="controls-divider"></span>
      <span class="controls-label" id="flash-count"></span>
    </div>
  </div>
</section>"""

    (DOCS / "drills.html").write_text(page(
        title="drills — vc companion",
        description="Waterfall calculator, exit scenarios, and reverse flashcards.",
        section="learn", current="drills.html",
        hero=hero("practice", "drills",
                  "Definitions don't stick. Worked situations do. Change the numbers until the "
                  "mechanics feel obvious.", eyebrow="Learn"),
        body=body, extra_css=DRILLS_CSS,
        extra_js="window.TERMS = " + payload + ";\n" + DRILLS_JS,
    ))


def build_index(deals, term_count) -> None:
    sprints = list((ROOT / "sprints").glob("sprint-*.md"))
    covered = sum(1 for p in sprints
                  if "prep only" not in read(p).lower()
                  and "not yet covered" not in read(p).lower())
    assignments = len([p for p in (ROOT / "assignments").glob("*.md")
                       if p.name != "INBOX.md"])
    impact = len(re.findall(r"^### ", read(ROOT / "impact.md"), flags=re.M))

    body = f"""
<div class="grid grid-4" style="margin-bottom:3.5rem">
  <div class="card stat"><div class="n">{term_count}</div><div class="l">Glossary terms</div></div>
  <div class="card stat"><div class="n">{covered}/{len(sprints)}</div><div class="l">Sprints covered</div></div>
  <div class="card stat"><div class="n">{len(deals)}</div><div class="l">Companies seen</div></div>
  <div class="card stat"><div class="n">{assignments}</div><div class="l">Assignments filed</div></div>
</div>

<section>
  <h2 class="section-title"><span>Start here</span></h2>
  <div class="grid grid-2">
    <a class="card" href="thesis.html">
      <div class="card-label">Thesis</div>
      <h3>What I invest in, and why me</h3>
      <p>AI rebuilding human trust, pre-seed, US. Angel now, fund later. Plus the edge that makes
      the dealflow real rather than aspirational.</p>
    </a>
    <a class="card" href="glossary.html">
      <div class="card-label">Learn</div>
      <h3>{term_count} terms, {covered} sprints, drills</h3>
      <p>Venture capital in plain English, each term with a worked example. Plus a waterfall
      calculator and scenario drills that make the mechanics stick.</p>
    </a>
    <a class="card" href="pipeline.html">
      <div class="card-label">Practice</div>
      <h3>Pipeline, memos, founder impact</h3>
      <p>The actual work: companies screened with written reasons, deal memos with the case
      against, and a record of founders helped.</p>
    </a>
    <a class="card" href="proof.html">
      <div class="card-label">Proof</div>
      <h3>What a fund can read</h3>
      <p>Evidence of judgment, assembled from the work above and scored against the rubric a
      partner would actually use.</p>
    </a>
  </div>
</section>

<section>
  <h2 class="section-title"><span>How this works</span></h2>
  <div class="prose">
    <p>Four sections, and they do different jobs on purpose.
    <strong>Thesis</strong> is the spine — everything else is judged against it.
    <strong>Learn</strong> is knowledge coming in.
    <strong>Practice</strong> is the work itself.
    <strong>Proof</strong> is what comes out the other side, for someone else to read.</p>
    <p>Nothing here is written for an audience first. It's a working notebook that happens to be
    public, which is the only reason it stays honest.</p>
  </div>
  <div class="callout">
    In the terminal: <code>vc pari passu</code> to look something up,
    <code>vc note "..."</code> to catch a thought,
    <code>vc deal add</code> to log a company,
    <code>vc quiz</code> to drill.
    On this site, press <code>/</code> anywhere in the glossary to search.
  </div>
</section>"""
    (DOCS / "index.html").write_text(page(
        title="vc companion — e-man chan",
        description="A working venture capital notebook: thesis, glossary, deal pipeline, and the "
                    "proof of judgment behind them.",
        section="", current="index.html",
        hero=hero("vc", "companion",
                  "A working notebook for becoming an investor — thesis, vocabulary, live deal "
                  "pipeline, and the evidence behind them. Built in public while going through "
                  '<a href="https://govclab.com/venture-institute/">VC Lab\'s Venture Institute</a>.'),
        body=body,
    ))


# ---------------------------------------------------------------- assets

GLOSSARY_CSS = """
.example { border-left: 3px solid var(--gold); background: var(--tint);
           padding: 0.8rem 1rem; margin-top: 0.75rem; border-radius: 0 4px 4px 0; }
.example p, .example li { font-size: 0.9rem; color: var(--text); }
.example ol, .example ul { margin: 0.4rem 0 0 1.1rem; }
.term ol, .term ul { margin: 0.5rem 0 0 1.2rem; }
.term li { font-size: 0.93rem; color: var(--muted); margin-bottom: 0.3rem; }
.term { background: var(--card); border: 1px solid var(--line);
        border-left: 3px solid var(--accent); border-radius: 0 5px 5px 0;
        padding: 1.4rem 1.6rem; margin-bottom: 1rem; scroll-margin-top: 5rem; }
.term h3 { font-size: 1.05rem; font-weight: 700; margin-bottom: 0.5rem; }
.term p { font-size: 0.93rem; color: var(--muted); }
.term p + p { margin-top: 0.6rem; }
.term.hidden { display: none; }
.group-label { font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.2em;
               color: var(--accent); font-weight: 700; margin: 2.5rem 0 1rem; }
.section-intro { font-size: 0.92rem; color: var(--muted); margin-bottom: 1.25rem; max-width: 720px; }
.sources p, .sources li { font-size: 0.9rem; color: var(--muted); }
.sources ul { margin: 0.5rem 0 0 1.2rem; }
.sources li { margin-bottom: 0.5rem; }
.no-results { color: var(--muted); font-style: italic; padding: 2rem 0; }
.anchor { text-decoration: none; color: var(--muted); opacity: 0; margin-left: 0.5rem;
          font-weight: 400; transition: opacity 0.15s ease; }
.term:hover .anchor { opacity: 0.5; }
.anchor:hover { opacity: 1 !important; color: var(--accent); }
.term:target, .term.active { border-left-color: var(--gold); box-shadow: 0 0 0 1px var(--gold); }
.search-wrap { position: sticky; top: 0; z-index: 900; background: var(--bg); padding: 1rem 0; }
.search-row { display: flex; align-items: center; gap: 0.75rem; flex-wrap: wrap; }
#search { width: 100%; max-width: 420px; padding: 0.8rem 1.1rem; font-family: inherit;
          font-size: 1rem; background: var(--card); color: var(--text);
          border: 1px solid var(--line); border-radius: 50px; outline: none; }
#search:focus { border-color: var(--accent); }
.kbd { font-family: var(--mono); font-size: 0.7rem; border: 1px solid var(--line);
       border-bottom-width: 2px; border-radius: 4px; padding: 0.15em 0.4em; color: var(--muted); }
.hint { font-size: 0.78rem; color: var(--muted); }
.result-count { font-size: 0.8rem; color: var(--muted); margin: 0.5rem 0;
                font-variant-numeric: tabular-nums; }
.term-section { font-size: 0.62rem; text-transform: uppercase; letter-spacing: 0.12em;
                color: var(--accent); margin-bottom: 0.3rem; display: none; }
body.flat .term-section { display: block; }
body.flat .group-label, body.flat .section-intro { display: none !important; }
@media (max-width: 768px) { .hint { display: none; } }
"""

GLOSSARY_JS = """
(function () {
  var search = document.getElementById('search');
  var container = document.getElementById('terms');
  var countEl = document.getElementById('result-count');
  var noResults = document.getElementById('no-results');
  var terms = [].slice.call(document.querySelectorAll('.term'));
  var labels = [].slice.call(document.querySelectorAll('.group-label'));
  var intros = [].slice.call(document.querySelectorAll('.section-intro'));
  var sourceBlocks = [].slice.call(
    container.querySelectorAll('.sources, .group-label:not([data-section])'));
  labels = labels.filter(function (l) { return l.hasAttribute('data-section'); });
  var section = '', sortMode = 'curriculum', cursor = -1;

  terms.forEach(function (t) {
    var h = t.querySelector('h3');
    t.dataset.title = h ? h.textContent.replace('#', '').toLowerCase().trim() : '';
    t.dataset.all = t.textContent.toLowerCase();
  });

  function matches(el, q) {
    if (!q) return true;
    if (el.dataset.all.indexOf(q) !== -1) return true;
    var words = q.split(/\\s+/).filter(Boolean);
    var tw = el.dataset.title.split(/\\s+/);
    return words.every(function (w) {
      return tw.some(function (x) { return x.indexOf(w) === 0; });
    });
  }
  function flat() { return sortMode !== 'curriculum' || section !== ''; }
  function visibleTerms() {
    return terms.filter(function (t) { return !t.classList.contains('hidden'); });
  }
  function highlight(i) {
    terms.forEach(function (t) { t.classList.remove('active'); });
    var vis = visibleTerms();
    if (!vis.length) return;
    cursor = Math.max(0, Math.min(i, vis.length - 1));
    vis[cursor].classList.add('active');
    vis[cursor].scrollIntoView({ block: 'center', behavior: 'smooth' });
  }
  function reorder() {
    var list = terms.slice();
    if (sortMode === 'az' || sortMode === 'za') {
      list.sort(function (a, b) { return a.dataset.title.localeCompare(b.dataset.title); });
      if (sortMode === 'za') list.reverse();
    } else if (sortMode === 'shuffle') {
      for (var i = list.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var t = list[i]; list[i] = list[j]; list[j] = t;
      }
    } else {
      list.sort(function (a, b) { return (+a.dataset.order) - (+b.dataset.order); });
    }
    document.body.classList.toggle('flat', flat());
    list.forEach(function (t) { container.appendChild(t); });
    if (!flat()) {
      labels.forEach(function (label) {
        var sec = label.dataset.section;
        var first = list.filter(function (t) { return t.dataset.section === sec; })[0];
        if (!first) return;
        container.insertBefore(label, first);
        var intro = intros.filter(function (i) { return i.dataset.section === sec; })[0];
        if (intro) container.insertBefore(intro, first);
      });
    }
    sourceBlocks.forEach(function (el) { container.appendChild(el); });
  }
  function filter() {
    var q = search.value.toLowerCase().trim();
    var visible = 0; cursor = -1;
    terms.forEach(function (t) {
      var ok = matches(t, q) && (!section || t.dataset.section === section);
      t.classList.toggle('hidden', !ok);
      t.classList.remove('active');
      if (ok) visible++;
    });
    labels.forEach(function (label) {
      if (flat()) { label.style.display = 'none'; return; }
      var any = terms.some(function (t) {
        return t.dataset.section === label.dataset.section && !t.classList.contains('hidden');
      });
      label.style.display = any ? '' : 'none';
    });
    intros.forEach(function (i) { i.style.display = (q || flat()) ? 'none' : ''; });
    var narrowed = !!(q || section);
    sourceBlocks.forEach(function (el) { el.style.display = narrowed ? 'none' : ''; });
    noResults.style.display = visible ? 'none' : 'block';
    var bits = [];
    if (q) bits.push('matching "' + search.value.trim() + '"');
    if (section) {
      var chip = document.querySelector('.chip[data-section="' + section + '"]');
      if (chip) bits.push('in ' + chip.childNodes[0].textContent.trim());
    }
    countEl.textContent = narrowed
      ? visible + (visible === 1 ? ' term ' : ' terms ') + bits.join(' ') : '';
  }

  search.addEventListener('input', filter);
  document.querySelectorAll('.chip[data-section]').forEach(function (chip) {
    chip.addEventListener('click', function () {
      section = chip.dataset.section;
      document.querySelectorAll('.chip[data-section]').forEach(function (c) {
        c.setAttribute('aria-pressed', String(c === chip));
      });
      reorder(); filter(); window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  });
  document.querySelectorAll('.chip[data-sort]').forEach(function (chip) {
    chip.addEventListener('click', function () {
      sortMode = chip.dataset.sort;
      document.querySelectorAll('.chip[data-sort]').forEach(function (c) {
        c.setAttribute('aria-pressed', String(c === chip));
      });
      document.getElementById('shuffle').setAttribute('aria-pressed', 'false');
      reorder(); filter();
    });
  });
  document.getElementById('shuffle').addEventListener('click', function () {
    sortMode = 'shuffle';
    document.querySelectorAll('.chip[data-sort]').forEach(function (c) {
      c.setAttribute('aria-pressed', 'false');
    });
    this.setAttribute('aria-pressed', 'true');
    reorder(); filter(); window.scrollTo({ top: 0, behavior: 'smooth' });
  });
  document.addEventListener('keydown', function (e) {
    var typing = document.activeElement === search;
    if (e.key === '/' && !typing) { e.preventDefault(); search.focus(); search.select(); return; }
    if (!typing) return;
    if (e.key === 'Escape') { search.value = ''; filter(); search.blur(); }
    else if (e.key === 'ArrowDown') { e.preventDefault(); highlight(cursor + 1); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); highlight(cursor - 1); }
    else if (e.key === 'Enter') {
      e.preventDefault();
      var vis = visibleTerms();
      if (!vis.length) return;
      var el = vis[cursor >= 0 ? cursor : 0];
      location.hash = '#' + el.id;
      el.scrollIntoView({ block: 'center' });
      search.blur();
    }
  });
})();
"""

DRILLS_CSS = """
.calc { display: grid; grid-template-columns: minmax(260px, 1fr) 1.3fr; gap: 1.5rem; }
.calc-inputs { display: grid; gap: 0.85rem; align-content: start; }
.calc-inputs label { display: grid; gap: 0.3rem; font-size: 0.78rem;
  text-transform: uppercase; letter-spacing: 0.08em; color: var(--muted); }
.calc-inputs .unit { color: var(--accent); }
.calc-inputs input, .calc-inputs select {
  font-family: inherit; font-size: 0.95rem; padding: 0.55rem 0.7rem;
  background: var(--card); color: var(--text);
  border: 1px solid var(--line); border-radius: 5px; outline: none;
  text-transform: none; letter-spacing: normal;
}
.calc-inputs input:focus, .calc-inputs select:focus { border-color: var(--accent); }
.calc-out { background: var(--card); border: 1px solid var(--line);
  border-radius: 6px; padding: 1.5rem; }
.bar { display: flex; height: 34px; border-radius: 5px; overflow: hidden; margin-bottom: 1.25rem;
  border: 1px solid var(--line); }
.bar > div { display: flex; align-items: center; justify-content: center;
  font-size: 0.7rem; font-weight: 700; color: #fff; overflow: hidden; white-space: nowrap; }
.seg-a { background: var(--accent); }
.seg-b { background: var(--navy); }
.seg-c { background: var(--gold); color: #121212 !important; }
.payout { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
.payout td { padding: 0.5rem 0; border-bottom: 1px solid var(--line); color: var(--text); }
.payout td:last-child { text-align: right; font-variant-numeric: tabular-nums; font-weight: 700; }
.payout .who { color: var(--muted); font-size: 0.8rem; }
.verdict { margin-top: 1.25rem; font-size: 0.88rem; padding: 0.9rem 1.1rem;
  border-left: 3px solid var(--gold); background: var(--tint); border-radius: 0 4px 4px 0; }
.scn { background: var(--card); border: 1px solid var(--line); border-radius: 6px;
  padding: 1.4rem 1.6rem; margin-bottom: 1rem; }
.scn .q { font-size: 0.98rem; margin-bottom: 0.9rem; }
.scn .a { display: none; font-size: 0.92rem; color: var(--muted);
  border-left: 3px solid var(--accent); padding-left: 1rem; margin-top: 1rem; }
.scn.open .a { display: block; }
.flash { text-align: center; padding: 2.5rem 1.5rem; }
.flash-term { font-size: 1.8rem; font-weight: 700; letter-spacing: -0.02em; }
.flash-def { display: none; margin-top: 1.25rem; color: var(--muted); font-size: 0.95rem;
  max-width: 620px; margin-left: auto; margin-right: auto; }
.flash.open .flash-def { display: block; }
.flash .controls { justify-content: center; }
@media (max-width: 820px) { .calc { grid-template-columns: 1fr; } }
"""

DRILLS_JS = """
(function () {
  // ---- waterfall calculator
  var ids = ['exit','a-inv','a-mult','a-own','b-inv','b-mult','b-own'];
  var out = document.getElementById('calc-out');
  var mode = document.getElementById('mode');
  function v(id) { return parseFloat(document.getElementById(id).value) || 0; }
  function money(x) { return '$' + (Math.round(x * 100) / 100).toFixed(2) + 'M'; }

  function calc() {
    var exit = v('exit');
    var aPref = v('a-inv') * v('a-mult'), bPref = v('b-inv') * v('b-mult');
    var aOwn = v('a-own') / 100, bOwn = v('b-own') / 100;
    var a = 0, b = 0, rest = 0, note = '';

    if (mode.value === 'senior') {
      b = Math.min(bPref, exit);
      a = Math.min(aPref, exit - b);
      rest = Math.max(0, exit - a - b);
    } else {
      var total = aPref + bPref;
      if (exit < total) {
        a = total ? exit * (aPref / total) : 0;
        b = total ? exit * (bPref / total) : 0;
      } else { a = aPref; b = bPref; rest = exit - total; }
    }
    // each series converts instead if that pays more
    var aConv = exit * aOwn, bConv = exit * bOwn;
    var aConverted = aConv > a, bConverted = bConv > b;
    if (aConverted) { rest = Math.max(0, rest - (aConv - a)); a = aConv; }
    if (bConverted) { rest = Math.max(0, rest - (bConv - b)); b = bConv; }

    if (exit < aPref + bPref) {
      note = 'The exit is below the ' + money(aPref + bPref) + ' of stacked preferences. ' +
             'Founders and employees get nothing.';
    } else if (aConverted || bConverted) {
      note = (aConverted && bConverted ? 'Both series convert' :
              aConverted ? 'Series A converts' : 'Series B converts') +
             ' — the exit is high enough that taking equity beats taking the preference.';
    } else {
      note = 'Everyone takes their preference. Common holders split what is left.';
    }

    var tot = Math.max(exit, 0.0001);
    function pct(x) { return (100 * x / tot).toFixed(1); }
    out.innerHTML =
      '<div class="bar">' +
        '<div class="seg-a" style="width:' + pct(a) + '%">' + (a / tot > 0.09 ? 'A ' + pct(a) + '%' : '') + '</div>' +
        '<div class="seg-b" style="width:' + pct(b) + '%">' + (b / tot > 0.09 ? 'B ' + pct(b) + '%' : '') + '</div>' +
        '<div class="seg-c" style="width:' + pct(rest) + '%">' + (rest / tot > 0.09 ? 'Common ' + pct(rest) + '%' : '') + '</div>' +
      '</div>' +
      '<table class="payout">' +
        '<tr><td>Series A<div class="who">' + (aConverted ? 'converted to common' : 'took preference') + '</div></td><td>' + money(a) + '</td></tr>' +
        '<tr><td>Series B<div class="who">' + (bConverted ? 'converted to common' : 'took preference') + '</div></td><td>' + money(b) + '</td></tr>' +
        '<tr><td>Founders &amp; employees<div class="who">common stock</div></td><td>' + money(rest) + '</td></tr>' +
      '</table>' +
      '<div class="verdict">' + note + '</div>';
  }
  ids.forEach(function (id) { document.getElementById(id).addEventListener('input', calc); });
  mode.addEventListener('change', calc);
  calc();

  // ---- scenarios
  var SCENARIOS = [
    ['A company sells for $5M. Series A put in $10M at 1x, Series B put in $15M at 1x, pari passu. Who gets what?',
     'Preferences total $25M against a $5M exit, so it splits pro rata: Series A gets (10/25) x $5M = <strong>$2M</strong>, Series B gets (15/25) x $5M = <strong>$3M</strong>. Founders and employees get <strong>nothing</strong>. Being first in did not help Series A here.'],
    ['You own 10% of a company worth $10M. It raises at $50M and you are diluted to 8%. Did you lose?',
     'No. Your stake went from $1M to <strong>$4M</strong>. Dilution reduced your percentage and quadrupled your value — it is the price of the company being worth more, not a theft.'],
    ['A fund reports 2.0x TVPI and 0.2x DPI. What is it telling you, and what is it not?',
     'It is telling you the portfolio is <em>marked</em> at twice the money in. It is not telling you the money came back — only <strong>0.2x</strong> is realized cash. The other 1.8x is paper. A fund that leads with TVPI and goes quiet about DPI is showing you the flattering number.'],
    ['A founder says they are raising $2M on a post-money SAFE at a $10M cap. What do you own?',
     '<strong>20%</strong> ($2M / $10M), and on a post-money SAFE that percentage is locked — later SAFEs dilute the founders, not you. On a pre-money SAFE it would not be locked, which is the mistake that costs founders 5–10% more dilution than they modelled.'],
    ['Series B invested $15M for 18.75%. The company can sell for $65M or IPO at $70M. Which does Series B prefer?',
     'The <strong>$65M sale</strong>. It pays their full $15M preference. The $70M IPO triggers mandatory conversion, paying 18.75% x $70M = <strong>$13.1M</strong> — $1.9M less. They are rationally incentivised to block the better outcome. That is the hold-up problem, and why mandatory conversion clauses exist.'],
    ['You have $600K in the bank burning $50K a month. When should you start raising?',
     'You have <strong>12 months</strong> of runway and fundraising takes about six. You should already be raising. Investors read a founder who starts at four months of runway as either inattentive or desperate, and both hurt the price.'],
    ['A fund is $200M and owns 10% of your company. You sell for $40M. How does that land for them?',
     'They get <strong>$4M</strong> — two percent of the fund. It rounds to nothing, not because you failed but because of the denominator. This is why fund size, not enthusiasm, decides which exits count, and why matching investor math to your ambition matters before you take the check.'],
    ['Investor A has 12x odds ratio pre-2016 and 1.7x after. What does that tell you?',
     'That the edge decayed. Their alumni were once wildly overrepresented among unicorn founders and are now near baseline — the PayPal pattern. Talent factories move. Backing a background because it was predictive a decade ago is backing a stale signal.']
  ];
  var wrap = document.getElementById('scenarios');
  wrap.innerHTML = SCENARIOS.map(function (s, i) {
    return '<div class="scn" data-i="' + i + '">' +
      '<div class="q"><strong>' + (i + 1) + '.</strong> ' + s[0] + '</div>' +
      '<button class="chip">Show answer</button>' +
      '<div class="a">' + s[1] + '</div></div>';
  }).join('');
  wrap.addEventListener('click', function (e) {
    if (e.target.tagName !== 'BUTTON') return;
    var card = e.target.closest('.scn');
    card.classList.toggle('open');
    e.target.textContent = card.classList.contains('open') ? 'Hide answer' : 'Show answer';
  });

  // ---- reverse flashcards
  var flash = document.getElementById('flash');
  var fTerm = document.getElementById('flash-term');
  var fDef = document.getElementById('flash-def');
  var fCount = document.getElementById('flash-count');
  var order = window.TERMS.map(function (_, i) { return i; });
  var at = -1;
  function shuffle(a) {
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
  }
  function next() {
    at++;
    if (at >= order.length) { shuffle(order); at = 0; }
    var t = window.TERMS[order[at]];
    fTerm.textContent = t.t;
    fDef.innerHTML = t.d;
    flash.classList.remove('open');
    fCount.textContent = (at + 1) + ' of ' + order.length;
  }
  document.getElementById('flash-reveal').addEventListener('click', function () {
    flash.classList.add('open');
  });
  document.getElementById('flash-next').addEventListener('click', next);
  shuffle(order); next();
})();
"""


def build_favicon() -> None:
    """Emoji tab icon, as an SVG so it stays sharp at every size."""
    (DOCS / "favicon.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
        f'<text x="32" y="32" font-size="56" text-anchor="middle" '
        f'dominant-baseline="central">{FAVICON}</text></svg>\n',
        encoding="utf-8",
    )


def main() -> int:
    DOCS.mkdir(exist_ok=True)
    sections = load_glossary()
    deals = load_deals()
    build_favicon()

    n = build_glossary(sections)
    build_thesis()
    build_notes()
    build_assignments()
    build_structure()
    build_pipeline(deals)
    build_memo()
    build_impact()
    build_drills(sections)
    build_proof(deals, n)
    build_index(deals, n)

    pages = sorted(p.name for p in DOCS.glob("*.html"))
    print(f"built {len(pages)} pages · {n} glossary terms · {len(deals)} deals")
    print("  " + "  ".join(pages))
    return 0


if __name__ == "__main__":
    sys.exit(main())
