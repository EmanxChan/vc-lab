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
  </div>

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

  function filter() {{
    var q = search.value.toLowerCase().trim();
    var visible = 0;
    cursor = -1;
    terms.forEach(function (t) {{
      var ok = matches(t, q);
      t.classList.toggle('hidden', !ok);
      t.classList.remove('active');
      if (ok) visible++;
    }});
    labels.forEach(function (label) {{
      var any = false, node = label.nextElementSibling;
      while (node && !node.classList.contains('group-label')) {{
        if (node.classList.contains('term') && !node.classList.contains('hidden')) any = true;
        node = node.nextElementSibling;
      }}
      label.style.display = any ? '' : 'none';
    }});
    intros.forEach(function (i) {{ i.style.display = q ? 'none' : ''; }});
    noResults.style.display = visible ? 'none' : 'block';
  }}

  search.addEventListener('input', filter);

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


def main() -> int:
    md = SRC.read_text()
    chunks, count = [], 0

    for title, terms, prose in parse(md):
        label = re.sub(r"^\d+\.\s*", "", title)
        if not terms:
            chunks.append(f'    <div class="group-label">{inline(label)}</div>')
            chunks.append(f'    <div class="sources">{render_body(prose)}</div>')
            continue
        chunks.append(f'    <div class="group-label">{inline(label)}</div>')
        if prose:
            chunks.append(f'    <p class="section-intro">{inline(prose)}</p>')
        for name, body in terms:
            count += 1
            anchor = slug(name)
            chunks.append(
                f'    <div class="term" id="{anchor}">\n'
                f'      <h3>{inline(name)}'
                f'<a class="anchor" href="#{anchor}" aria-label="Link to this term">#</a>'
                f'</h3>\n'
                f'      {render_body(body)}\n'
                f'    </div>'
            )

    OUT.write_text(TEMPLATE.format(count=count, body="\n".join(chunks)))
    print(f"wrote {OUT.relative_to(ROOT)} — {count} terms")
    return 0


if __name__ == "__main__":
    sys.exit(main())
