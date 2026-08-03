"""Shared page shell for the vc-lab site.

One nav, one footer, one head. Every page goes through here so the whole site
stays consistent and the information architecture is enforced in one place.

The IA is four sections, mutually exclusive and collectively exhaustive:

    THESIS    who I am and what I invest in — the spine
    LEARN     knowledge in: glossary, curriculum, drills
    PRACTICE  the work itself: pipeline, memos, impact
    PROOF     evidence out: the package a fund can read
"""

NAV = [
    ("thesis", "Thesis", "thesis.html", []),
    ("learn", "Learn", "glossary.html", [
        ("glossary.html", "Glossary"),
        ("notes.html", "Curriculum"),
        ("structure.html", "How a fund works"),
        ("drills.html", "Drills"),
    ]),
    ("practice", "Practice", "pipeline.html", [
        ("pipeline.html", "Pipeline"),
        ("memo.html", "Deal memo"),
        ("impact.html", "Founder impact"),
    ]),
    ("proof", "Proof", "proof.html", [
        ("proof.html", "Proof package"),
        ("assignments.html", "VC Lab record"),
    ]),
]

THEME_JS = """
(function () {
  var key = 'vclab-theme';
  var stored = localStorage.getItem(key);
  var prefersDark = window.matchMedia &&
    window.matchMedia('(prefers-color-scheme: dark)').matches;
  if (stored === 'dark' || (!stored && prefersDark)) {
    document.body.classList.add('dark-mode');
  }
  var btn = document.getElementById('theme-toggle');
  if (btn) btn.addEventListener('click', function () {
    document.body.classList.toggle('dark-mode');
    localStorage.setItem(key,
      document.body.classList.contains('dark-mode') ? 'dark' : 'light');
  });
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('sw.js').catch(function () {});
  }
})();
"""


def nav_html(active_section: str, current_page: str) -> str:
    """Primary nav plus a sub-nav for the active section."""
    top = []
    for key, label, href, _ in NAV:
        cls = ' class="active"' if key == active_section else ""
        top.append(f'<a href="{href}"{cls}>{label}</a>')

    sub = ""
    for key, _, _, children in NAV:
        if key == active_section and children:
            items = []
            for href, label in children:
                cls = ' class="active"' if href == current_page else ""
                items.append(f'<a href="{href}"{cls}>{label}</a>')
            sub = f'<div class="subnav"><div class="subnav-inner">{"".join(items)}</div></div>'
            break

    return f"""<nav class="main-nav">
  <div class="nav-bar">
    <a href="index.html" class="nav-home" aria-label="Home">vc</a>
    <div class="nav-links-wrapper">
      <div class="nav-links">{''.join(top)}</div>
    </div>
    <div class="nav-theme-container">
      <button id="theme-toggle" class="theme-btn" aria-label="Toggle dark mode">◐</button>
    </div>
  </div>
</nav>
{sub}"""


def page(*, title: str, description: str, section: str, current: str,
         hero: str = "", body: str = "", extra_css: str = "",
         extra_js: str = "") -> str:
    """Wrap page content in the shared shell."""
    css = f"\n<style>\n{extra_css}\n</style>" if extra_css else ""
    js = f"\n<script>\n{extra_js}\n</script>" if extra_js else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="author" content="Emmanuel Chan">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<link rel="stylesheet" href="style.css">{css}
</head>
<body>

{nav_html(section, current)}

{hero}

<main class="container">
{body}
</main>

<footer>
  <p><a href="index.html">VC companion</a> &middot; Emmanuel Chan &middot;
  <a href="https://emanchan.com">emanchan.com</a> &middot;
  <a href="https://github.com/EmanxChan/vc-lab">source</a></p>
</footer>

<script>{THEME_JS}</script>{js}

</body>
</html>
"""


def hero(title_plain: str, title_hl: str, sub: str, eyebrow: str = "") -> str:
    eb = f'<div class="eyebrow">{eyebrow}</div>' if eyebrow else ""
    return f"""<header class="hero">
  {eb}
  <h1 class="fluid">{title_plain} <span class="hl">{title_hl}</span></h1>
  <p class="hero-sub">{sub}</p>
</header>"""
