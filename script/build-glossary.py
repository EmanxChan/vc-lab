#!/usr/bin/env python3
"""Build docs/glossary.html from glossary.md.

Keeps the markdown as the single source of truth so the repo and the published
site can't drift apart. Run after editing glossary.md:

    python3 script/build-glossary.py
"""

import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "glossary.md"
OUT = ROOT / "docs" / "glossary.html"

EXAMPLE_PREFIXES = ("**Picture this", "**The tension", "**Picture this —")


def slug(name: str) -> str:
    """URL anchor for a term. Must match script/vc's slug()."""
    s = re.sub(r"[^\w\s-]", "", name.lower())
    return re.sub(r"[\s_]+", "-", s).strip("-")


def inline(text: str) -> str:
    """Convert inline markdown to HTML, escaping everything else."""
    text = html.escape(text, quote=False)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)",
                  r'<a href="\2" target="_blank" rel="noopener">\1</a>', text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)
    return text


def render_block(block: str) -> str:
    """Render one blank-line-delimited block as a paragraph or list."""
    lines = [ln.rstrip() for ln in block.strip().split("\n") if ln.strip()]
    if not lines:
        return ""

    # A block may open with a lead-in sentence and then become a list.
    first_item = next(
        (i for i, ln in enumerate(lines)
         if re.match(r"^\d+\.\s", ln) or ln.startswith("- ")),
        None,
    )
    if first_item:  # not None and not 0
        lead = "\n".join(lines[:first_item])
        rest = "\n".join(lines[first_item:])
        return render_block(lead) + render_block(rest)

    if all(re.match(r"^\d+\.\s", ln) or ln.startswith("   ") for ln in lines):
        items, current = [], ""
        for ln in lines:
            if re.match(r"^\d+\.\s", ln):
                if current:
                    items.append(current)
                current = re.sub(r"^\d+\.\s", "", ln)
            else:
                current += " " + ln.strip()
        if current:
            items.append(current)
        return "<ol>" + "".join(f"<li>{inline(i)}</li>" for i in items) + "</ol>"

    if all(ln.startswith("- ") or ln.startswith("  ") for ln in lines):
        items, current = [], ""
        for ln in lines:
            if ln.startswith("- "):
                if current:
                    items.append(current)
                current = ln[2:]
            else:
                current += " " + ln.strip()
        if current:
            items.append(current)
        return "<ul>" + "".join(f"<li>{inline(i)}</li>" for i in items) + "</ul>"

    return f"<p>{inline(' '.join(lines))}</p>"


def render_body(body: str) -> str:
    """Render a term body, wrapping example blocks in a callout."""
    # Examples usually sit on the line straight after the definition with no
    # blank line between, so force a break before each marker.
    body = re.sub(r"\n(?=\*\*(?:Picture this|The tension))", "\n\n", body)

    out = []
    for block in re.split(r"\n\s*\n", body.strip()):
        if not block.strip():
            continue
        rendered = render_block(block)
        if block.lstrip().startswith(EXAMPLE_PREFIXES):
            out.append(f'<div class="example">{rendered}</div>')
        else:
            out.append(rendered)
    return "".join(out)


def parse(md: str):
    """Yield (section_title, [(term, body)], prose) tuples."""
    # drop everything before the first section heading
    parts = re.split(r"^## ", md, flags=re.M)[1:]
    for part in parts:
        title, _, rest = part.partition("\n")
        rest = rest.replace("\n---\n", "\n")
        chunks = re.split(r"^### ", rest, flags=re.M)
        prose = chunks[0].strip()
        terms = []
        for chunk in chunks[1:]:
            name, _, body = chunk.partition("\n")
            terms.append((name.strip(), body.strip()))
        yield title.strip(), terms, prose


TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>vc glossary — e-man chan</title>
<meta name="description" content="Venture capital in plain English — {count} terms, each with a concrete example. Deal terms, the payout stack, fund economics, and performance metrics.">
<meta name="author" content="Emmanuel Chan">
<meta property="og:title" content="VC Glossary | E-man Chan">
<meta property="og:description" content="Venture capital in plain English, with a concrete example for every term.">
<link rel="stylesheet" href="style.css">
<style>
.example {{
    border-left: 3px solid var(--gold);
    background: rgba(127,127,127,0.06);
    padding: 0.8rem 1rem;
    margin-top: 0.75rem;
    border-radius: 0 4px 4px 0;
}}
.example p, .example li {{ font-size: 0.9rem; color: var(--text); }}
.example ol, .example ul {{ margin: 0.4rem 0 0 1.1rem; }}
.example li {{ margin-bottom: 0.3rem; }}
.term ol, .term ul {{ margin: 0.5rem 0 0 1.2rem; }}
.term li {{ font-size: 0.93rem; color: var(--muted); margin-bottom: 0.3rem; }}
.section-intro {{ font-size: 0.93rem; color: var(--muted); margin-bottom: 1.25rem; max-width: 720px; }}
.count {{ font-variant-numeric: tabular-nums; }}
.sources p, .sources li {{ font-size: 0.9rem; color: var(--muted); }}
.sources ul {{ margin: 0.5rem 0 0 1.2rem; }}
.sources li {{ margin-bottom: 0.5rem; }}

/* deep links */
.term {{ scroll-margin-top: 5rem; }}
.anchor {{
    text-decoration: none;
    color: var(--muted);
    opacity: 0;
    margin-left: 0.5rem;
    font-weight: 400;
    transition: opacity 0.15s ease;
}}
.term:hover .anchor {{ opacity: 0.5; }}
.anchor:hover {{ opacity: 1 !important; color: var(--accent); }}
.term:target {{
    border-left-color: var(--gold);
    box-shadow: 0 0 0 1px var(--gold);
}}

/* keyboard-first search */
.search-wrap {{
    position: sticky;
    top: 0;
    z-index: 900;
    background: var(--bg);
    padding: 1rem 0;
    margin-bottom: 1rem;
}}
.search-row {{ display: flex; align-items: center; gap: 0.75rem; flex-wrap: wrap; }}
.kbd {{
    font-family: 'Courier New', monospace;
    font-size: 0.7rem;
    border: 1px solid var(--line);
    border-bottom-width: 2px;
    border-radius: 4px;
    padding: 0.15em 0.4em;
    color: var(--muted);
}}
.hint {{ font-size: 0.8rem; color: var(--muted); }}
.term.active {{ border-left-color: var(--gold); box-shadow: 0 0 0 1px var(--gold); }}
@media (max-width: 768px) {{ .hint {{ display: none; }} }}

/* filters + sort */
.controls {{
    display: flex;
    align-items: center;
    gap: 0.5rem;
    flex-wrap: wrap;
    margin-top: 0.75rem;
}}
.chip {{
    font-size: 0.75rem;
    font-family: inherit;
    border: 1px solid var(--line);
    background: transparent;
    color: var(--muted);
    padding: 0.35em 0.8em;
    border-radius: 50px;
    cursor: pointer;
    white-space: nowrap;
    transition: all 0.15s ease;
}}
.chip:hover {{ border-color: var(--accent); color: var(--text); }}
.chip[aria-pressed="true"] {{
    background: var(--accent);
    border-color: var(--accent);
    color: #fff;
    font-weight: 600;
}}
.chip .n {{ opacity: 0.6; margin-left: 0.35em; font-variant-numeric: tabular-nums; }}
.controls-divider {{
    width: 1px;
    height: 1.4em;
    background: var(--line);
    margin: 0 0.35rem;
}}
.controls-label {{
    font-size: 0.68rem;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: var(--muted);
    margin-right: 0.1rem;
}}
.result-count {{
    font-size: 0.8rem;
    color: var(--muted);
    margin: 1rem 0 0.5rem;
    font-variant-numeric: tabular-nums;
}}
.term .term-section {{
    font-size: 0.65rem;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: var(--accent);
    margin-bottom: 0.3rem;
    display: none;
}}
body.flat .term .term-section {{ display: block; }}
body.flat .group-label, body.flat .section-intro {{ display: none !important; }}
@media (max-width: 768px) {{
    .controls {{ gap: 0.35rem; }}
    .chip {{ font-size: 0.7rem; padding: 0.3em 0.65em; }}
}}
</style>
</head>
<body>

<nav class="main-nav">
  <div class="nav-bar">
    <div class="nav-links-wrapper">
      <div class="nav-links">
        <a href="index.html">home</a>
        <a href="structure.html">structure</a>
        <a href="notes.html">notes</a>
        <a href="https://emanchan.com">emanchan.com</a>
      </div>
    </div>
    <div class="nav-theme-container">
      <button id="theme-toggle" class="theme-btn" aria-label="Toggle dark mode">◐</button>
    </div>
  </div>
</nav>

<header class="hero">
  <h1 class="fluid">vc <span class="hl">glossary</span></h1>
  <p class="hero-sub">Venture capital in plain English — <span class="count">{count}</span> terms,
  each with a concrete example. No jargon defined using more jargon.</p>
</header>

<main class="container">

  <div class="search-wrap">
    <div class="search-row">
      <input type="text" id="search" placeholder="Search {count} terms…" autocomplete="off">
      <span class="hint"><span class="kbd">/</span> search &nbsp;
      <span class="kbd">↑↓</span> move &nbsp;
      <span class="kbd">enter</span> open &nbsp;
      <span class="kbd">esc</span> clear</span>
    </div>
    <div class="controls" id="filters">
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
{body}
  </div>

  <p class="no-results" id="no-results" style="display:none">No terms match that search.</p>

</main>

<footer>
  <p>Emmanuel Chan &middot; <a href="https://emanchan.com">emanchan.com</a> &middot;
  <a href="https://github.com/EmanxChan/vc-lab">source</a></p>
</footer>

<script>
(function () {{
  var key = 'vclab-theme';
  var btn = document.getElementById('theme-toggle');
  var stored = localStorage.getItem(key);
  var prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  if (stored === 'dark' || (!stored && prefersDark)) document.body.classList.add('dark-mode');
  btn.addEventListener('click', function () {{
    document.body.classList.toggle('dark-mode');
    localStorage.setItem(key, document.body.classList.contains('dark-mode') ? 'dark' : 'light');
  }});

  var search = document.getElementById('search');
  var terms = Array.prototype.slice.call(document.querySelectorAll('.term'));
  var labels = Array.prototype.slice.call(document.querySelectorAll('.group-label'));
  var sourcesHidden = false;
  var intros = Array.prototype.slice.call(document.querySelectorAll('.section-intro'));
  var noResults = document.getElementById('no-results');
  var cursor = -1;

  terms.forEach(function (t) {{
    var h = t.querySelector('h3');
    t.dataset.title = h ? h.textContent.replace('#', '').toLowerCase().trim() : '';
    t.dataset.all = t.textContent.toLowerCase();
  }});

  // Matches whole words in any order, so "liq pref" finds "Liquidation preference".
  function matches(el, q) {{
    if (!q) return true;
    if (el.dataset.all.indexOf(q) !== -1) return true;
    var words = q.split(/\\s+/).filter(Boolean);
    var titleWords = el.dataset.title.split(/\\s+/);
    return words.every(function (w) {{
      return titleWords.some(function (tw) {{ return tw.indexOf(w) === 0; }});
    }});
  }}

  function visibleTerms() {{
    return terms.filter(function (t) {{ return !t.classList.contains('hidden'); }});
  }}

  function highlight(i) {{
    terms.forEach(function (t) {{ t.classList.remove('active'); }});
    var vis = visibleTerms();
    if (!vis.length) return;
    cursor = Math.max(0, Math.min(i, vis.length - 1));
    var el = vis[cursor];
    el.classList.add('active');
    el.scrollIntoView({{ block: 'center', behavior: 'smooth' }});
  }}

  var container = document.getElementById('terms');
  var countEl = document.getElementById('result-count');
  var section = '';
  var sortMode = 'curriculum';

  // The trailing "Where this came from" block: its heading has no data-section.
  var sourceBlocks = Array.prototype.slice
    .call(container.querySelectorAll('.sources, .group-label:not([data-section])'));
  labels = labels.filter(function (l) {{ return l.hasAttribute('data-section'); }});

  // Section headings only make sense in curriculum order with no section filter.
  function flat() {{
    return sortMode !== 'curriculum' || section !== '';
  }}

  function reorder() {{
    var list = terms.slice();
    if (sortMode === 'az' || sortMode === 'za') {{
      list.sort(function (a, b) {{
        return a.dataset.title.localeCompare(b.dataset.title);
      }});
      if (sortMode === 'za') list.reverse();
    }} else if (sortMode === 'shuffle') {{
      for (var i = list.length - 1; i > 0; i--) {{
        var j = Math.floor(Math.random() * (i + 1));
        var tmp = list[i]; list[i] = list[j]; list[j] = tmp;
      }}
    }} else {{
      list.sort(function (a, b) {{
        return (+a.dataset.order) - (+b.dataset.order);
      }});
    }}
    document.body.classList.toggle('flat', flat());
    list.forEach(function (t) {{ container.appendChild(t); }});
    // keep section headings (and their intros) with their terms in curriculum order
    if (!flat()) {{
      labels.forEach(function (label) {{
        var sec = label.dataset.section;
        var first = list.filter(function (t) {{ return t.dataset.section === sec; }})[0];
        if (!first) return;
        container.insertBefore(label, first);
        var intro = intros.filter(function (i) {{ return i.dataset.section === sec; }})[0];
        if (intro) container.insertBefore(intro, first);
      }});
    }}
    // the sources block always belongs at the very bottom
    sourceBlocks.forEach(function (el) {{ container.appendChild(el); }});
  }}

  function filter() {{
    var q = search.value.toLowerCase().trim();
    var visible = 0;
    cursor = -1;
    terms.forEach(function (t) {{
      var ok = matches(t, q) && (!section || t.dataset.section === section);
      t.classList.toggle('hidden', !ok);
      t.classList.remove('active');
      if (ok) visible++;
    }});
    labels.forEach(function (label) {{
      if (flat()) {{ label.style.display = 'none'; return; }}
      var any = terms.some(function (t) {{
        return t.dataset.section === label.dataset.section && !t.classList.contains('hidden');
      }});
      label.style.display = any ? '' : 'none';
    }});
    intros.forEach(function (i) {{
      i.style.display = (q || flat()) ? 'none' : '';
    }});
    noResults.style.display = visible ? 'none' : 'block';

    // hide the sources block whenever the list is narrowed
    sourcesHidden = !!(q || section);
    sourceBlocks.forEach(function (el) {{
      el.style.display = sourcesHidden ? 'none' : '';
    }});

    var bits = [];
    if (q) bits.push('matching "' + search.value.trim() + '"');
    if (section) {{
      var chip = document.querySelector('.chip[data-section="' + section + '"]');
      if (chip) bits.push('in ' + chip.childNodes[0].textContent.trim());
    }}
    countEl.textContent = (q || section)
      ? visible + (visible === 1 ? ' term ' : ' terms ') + bits.join(' ')
      : '';
  }}

  search.addEventListener('input', filter);

  document.querySelectorAll('.chip[data-section]').forEach(function (chip) {{
    chip.addEventListener('click', function () {{
      section = chip.dataset.section;
      document.querySelectorAll('.chip[data-section]').forEach(function (c) {{
        c.setAttribute('aria-pressed', String(c === chip));
      }});
      reorder();
      filter();
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }});
  }});

  document.querySelectorAll('.chip[data-sort]').forEach(function (chip) {{
    chip.addEventListener('click', function () {{
      sortMode = chip.dataset.sort;
      document.querySelectorAll('.chip[data-sort]').forEach(function (c) {{
        c.setAttribute('aria-pressed', String(c === chip));
      }});
      document.getElementById('shuffle').setAttribute('aria-pressed', 'false');
      reorder();
      filter();
    }});
  }});

  document.getElementById('shuffle').addEventListener('click', function () {{
    sortMode = 'shuffle';
    document.querySelectorAll('.chip[data-sort]').forEach(function (c) {{
      c.setAttribute('aria-pressed', 'false');
    }});
    this.setAttribute('aria-pressed', 'true');
    reorder();
    filter();
    window.scrollTo({{ top: 0, behavior: 'smooth' }});
  }});

  // "/" focuses search from anywhere on the page.
  document.addEventListener('keydown', function (e) {{
    var typing = document.activeElement === search;
    if (e.key === '/' && !typing) {{
      e.preventDefault();
      search.focus();
      search.select();
      return;
    }}
    if (!typing) return;

    if (e.key === 'Escape') {{
      search.value = '';
      filter();
      search.blur();
    }} else if (e.key === 'ArrowDown') {{
      e.preventDefault();
      highlight(cursor + 1);
    }} else if (e.key === 'ArrowUp') {{
      e.preventDefault();
      highlight(cursor - 1);
    }} else if (e.key === 'Enter') {{
      e.preventDefault();
      var vis = visibleTerms();
      if (!vis.length) return;
      var el = vis[cursor >= 0 ? cursor : 0];
      location.hash = '#' + el.id;
      el.scrollIntoView({{ block: 'center' }});
      search.blur();
    }}
  }});

  // Work offline — it's static text, it shouldn't need a network.
  if ('serviceWorker' in navigator) {{
    navigator.serviceWorker.register('sw.js').catch(function () {{}});
  }}
}})();
</script>

</body>
</html>
"""


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


def main() -> int:
    md = SRC.read_text()
    chunks, count = [], 0
    sections = []

    for title, terms, prose in parse(md):
        label = re.sub(r"^\d+\.\s*", "", title)
        if not terms:
            chunks.append(f'    <div class="group-label">{inline(label)}</div>')
            chunks.append(f'    <div class="sources">{render_body(prose)}</div>')
            continue
        sections.append((slug(label), label, len(terms)))
        chunks.append(
            f'    <div class="group-label" data-section="{slug(label)}">'
            f'{inline(label)}</div>'
        )
        if prose:
            chunks.append(
                f'    <p class="section-intro" data-section="{slug(label)}">'
                f'{inline(prose)}</p>'
            )
        for name, body in terms:
            count += 1
            anchor = slug(name)
            sec_slug = slug(label)
            chunks.append(
                f'    <div class="term" id="{anchor}" data-section="{sec_slug}" '
                f'data-order="{count}">\n'
                f'      <div class="term-section">{inline(label)}</div>\n'
                f'      <h3>{inline(name)}'
                f'<a class="anchor" href="#{anchor}" aria-label="Link to this term">#</a>'
                f'</h3>\n'
                f'      {render_body(body)}\n'
                f'    </div>'
            )

    filters = "\n".join(
        f'      <button class="chip" data-section="{s}" aria-pressed="false">'
        f'{SHORT_LABELS.get(s, lbl)}<span class="n">{n}</span></button>'
        for s, lbl, n in sections
    )

    OUT.write_text(TEMPLATE.format(
        count=count, body="\n".join(chunks), filters=filters
    ))
    print(f"wrote {OUT.relative_to(ROOT)} — {count} terms, {len(sections)} sections")
    return 0


if __name__ == "__main__":
    sys.exit(main())
