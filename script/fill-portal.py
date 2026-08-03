#!/usr/bin/env python3
"""Turn the Sunday agent's answers into a paste-ready browser snippet.

The Sunday agent runs in the cloud and cannot reach fi.co — that needs an
authenticated browser session. So it writes weekly/YYYY-MM-DD-fill.json, and
this turns that into one blob you paste into Chrome's console on the
assignment page. Every Trix editor gets filled; nothing is submitted.

    vc fill                 latest fill file, copied to clipboard
    vc fill 2026-08-09      a specific date
    vc fill --print         print instead of copying
"""

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WEEKLY = ROOT / "weekly"

TEMPLATE = """(() => {
  const answers = %s;
  const editors = document.querySelectorAll('trix-editor');
  if (!editors.length) return 'No editors found — are you on the assignment page?';
  let filled = [];
  Object.entries(answers).forEach(([k, text]) => {
    const i = parseInt(k, 10);
    const el = editors[i];
    if (!el || !el.editor) return;
    const html = text.split('\\n\\n')
      .map(p => '<div>' + p.split('\\n').join('<br>') + '</div>')
      .join('<div><br></div>');
    el.editor.loadHTML(html);
    filled.push('Set ' + (i + 1) + ': ' + el.innerText.trim().length + ' chars');
  });
  return 'FILLED (not submitted)\\n' + filled.join('\\n') +
    '\\n\\nReview each set, then click Save Draft / Submit yourself.';
})();"""


def latest_fill() -> Path | None:
    files = sorted(WEEKLY.glob("*-fill.json"))
    return files[-1] if files else None


def main() -> int:
    args = [a for a in sys.argv[1:] if a != "--print"]
    do_print = "--print" in sys.argv[1:]

    if args:
        path = WEEKLY / f"{args[0]}-fill.json"
        if not path.exists():
            sys.exit(f"no fill file at {path}")
    else:
        path = latest_fill()
        if not path:
            sys.exit(
                "No fill file yet.\n"
                "The Sunday agent writes weekly/<date>-fill.json.\n"
                "Pull latest first:  git -C ~/Projects/active/vc-lab pull"
            )

    data = json.loads(path.read_text())
    answers = data.get("answers", data)
    # keys must be editor indexes as strings
    answers = {str(k): v for k, v in answers.items()}

    snippet = TEMPLATE % json.dumps(answers, ensure_ascii=False)

    if do_print:
        print(snippet)
        return 0

    try:
        subprocess.run(["pbcopy"], input=snippet.encode(), check=True)
        copied = True
    except Exception:
        copied = False

    sets = ", ".join(f"Set {int(k) + 1}" for k in sorted(answers, key=int))
    print(f"\n  {path.name} — {len(answers)} answers ({sets})")
    if copied:
        print("  copied to clipboard\n")
    else:
        print("  (clipboard failed — rerun with --print)\n")
    print("  1. Open the assignment page in Chrome")
    print("  2. Option+Cmd+J for the console")
    print("  3. Paste, hit Enter")
    print("  4. Review every set, then Save Draft / Submit yourself\n")
    if data.get("notes"):
        print(f"  Agent notes: {data['notes']}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
