"""Minimal markdown → HTML for the vc-lab site.

Deliberately small: it handles exactly the markdown this repo writes, with no
dependencies. Supported: headings, paragraphs, ordered/unordered lists, tables,
blockquotes, fenced code, links, bold, italic, inline code, and horizontal rules.
"""

import html
import re
from typing import Dict, Optional, Tuple

__all__ = ["inline", "render", "slug", "strip_md", "set_page_map"]

# Markdown source file -> where it actually lands on the site.
#
# Several sources collapse into one page: every sprints/*.md becomes a section
# of notes.html, every assignments/*.md a section of assignments.html. A naive
# "swap .md for .html" rewrite sends those links to pages that do not exist, so
# build.py registers the real mapping here before rendering anything.
#
#     stem -> (page, anchor or None)
_PAGES: Dict[str, Tuple[str, Optional[str]]] = {}


def set_page_map(pages: Dict[str, Tuple[str, Optional[str]]]) -> None:
    _PAGES.clear()
    _PAGES.update(pages)


def slug(name: str) -> str:
    s = re.sub(r"[^\w\s-]", "", name.lower())
    return re.sub(r"[\s_]+", "-", s).strip("-")


def strip_md(text: str) -> str:
    """Plain text, for meta descriptions and search indexes."""
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[*`#>]", "", text)
    return re.sub(r"\s+", " ", text).strip()


def inline(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", _link, text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)
    return text


def _link(m: re.Match) -> str:
    label, href = m.group(1), m.group(2)
    ext = href.startswith("http")
    if not ext:
        # Repo-relative .md links point at the published page instead. Split the
        # fragment off first — "thesis.md#my-edge" is still a .md link.
        path, _, frag = href.partition("#")
        if path.endswith(".md"):
            stem = path.rsplit("/", 1)[-1][:-3]
            page, anchor = _PAGES.get(stem, (f"{stem}.html", None))
            target = frag or anchor
            href = f"{page}#{target}" if target else page
    rel = ' target="_blank" rel="noopener"' if ext else ""
    return f'<a href="{href}"{rel}>{label}</a>'


def _table(rows: list[str]) -> str:
    cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
    if len(cells) < 2:
        return ""
    head, body = cells[0], cells[2:]
    out = ['<div class="table-wrap"><table><thead><tr>']
    out += [f"<th>{inline(c)}</th>" for c in head]
    out.append("</tr></thead><tbody>")
    for row in body:
        out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)


def render(md: str, *, heading_offset: int = 0, skip_h1: bool = True) -> str:
    """Render a markdown document body to HTML."""
    lines = md.split("\n")
    out: list[str] = []
    i = 0
    para: list[str] = []

    def flush():
        if para:
            out.append(f"<p>{inline(' '.join(para))}</p>")
            para.clear()

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            flush()
            i += 1
            continue

        if stripped.startswith("```"):
            flush()
            i += 1
            code = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code.append(html.escape(lines[i]))
                i += 1
            i += 1
            out.append("<pre><code>" + "\n".join(code) + "</code></pre>")
            continue

        if re.match(r"^(---|\*\*\*|___)\s*$", stripped):
            flush()
            out.append("<hr>")
            i += 1
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if m:
            flush()
            level = len(m.group(1))
            if level == 1 and skip_h1:
                i += 1
                continue
            lv = min(6, level + heading_offset)
            text = m.group(2)
            out.append(f'<h{lv} id="{slug(strip_md(text))}">{inline(text)}</h{lv}>')
            i += 1
            continue

        if stripped.startswith("|") and i + 1 < len(lines) and \
                re.match(r"^\|[\s:\-|]+\|$", lines[i + 1].strip()):
            flush()
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(lines[i])
                i += 1
            out.append(_table(rows))
            continue

        if stripped.startswith("> "):
            flush()
            quote = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip().lstrip(">").strip())
                i += 1
            out.append(f"<blockquote><p>{inline(' '.join(quote))}</p></blockquote>")
            continue

        bullet = re.match(r"^[-*]\s+(.*)$", stripped)
        number = re.match(r"^\d+\.\s+(.*)$", stripped)
        if bullet or number:
            flush()
            tag = "ul" if bullet else "ol"
            items: list[str] = []
            pat = r"^[-*]\s+(.*)$" if bullet else r"^\d+\.\s+(.*)$"
            while i < len(lines):
                s = lines[i].strip()
                m2 = re.match(pat, s)
                if m2:
                    items.append(m2.group(1))
                elif s and lines[i].startswith(("  ", "\t")) and items:
                    items[-1] += " " + s
                else:
                    break
                i += 1
            # checkbox lists render as a task list
            body = []
            for it in items:
                cb = re.match(r"^\[([ xX])\]\s*(.*)$", it)
                if cb:
                    done = cb.group(1).lower() == "x"
                    mark = "✓" if done else "○"
                    cls = " class=\"done\"" if done else ""
                    body.append(
                        f'<li{cls}><span class="tick">{mark}</span>{inline(cb.group(2))}</li>'
                    )
                else:
                    body.append(f"<li>{inline(it)}</li>")
            cls = ' class="tasks"' if any("tick" in b for b in body) else ""
            out.append(f"<{tag}{cls}>" + "".join(body) + f"</{tag}>")
            continue

        para.append(stripped)
        i += 1

    flush()
    return "\n".join(out)
