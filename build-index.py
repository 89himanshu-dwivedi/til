"""Regenerate the index in README.md from the note files themselves."""

import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
README = ROOT / "README.md"
START, END = "<!-- INDEX:START -->", "<!-- INDEX:END -->"

SKIP = {"README.md", "_template.md"}

notes = []
for p in sorted(ROOT.rglob("*.md")):
    if p.name in SKIP or p.parent == ROOT:
        continue
    text = p.read_text(encoding="utf-8")
    title = next((l[2:].strip() for l in text.splitlines() if l.startswith("# ")), p.stem)
    m = re.search(r"^\*(\d{4}-\d{2}-\d{2})", text, re.M)
    notes.append(
        {
            "title": title,
            "date": m.group(1) if m else "",
            "category": p.parent.name,
            "path": p.relative_to(ROOT).as_posix(),
        }
    )

by_cat: dict[str, list] = {}
for n in notes:
    by_cat.setdefault(n["category"], []).append(n)

lines = [START, "", f"## {len(notes)} notes", ""]
for cat in sorted(by_cat):
    items = sorted(by_cat[cat], key=lambda n: n["date"], reverse=True)
    lines.append(f"### {cat}  <sub>{len(items)}</sub>")
    lines.append("")
    for n in items:
        lines.append(f"- [{n['title']}]({n['path']}) <sub>{n['date']}</sub>")
    lines.append("")

lines.append("### Latest")
lines.append("")
for n in sorted(notes, key=lambda n: n["date"], reverse=True)[:10]:
    lines.append(f"- `{n['date']}` **{n['category']}** - [{n['title']}]({n['path']})")
lines += ["", f"*Index rebuilt {date.today().isoformat()}*", "", END]

readme = README.read_text(encoding="utf-8")
readme = re.sub(
    re.escape(START) + r".*?" + re.escape(END), "\n".join(lines), readme, flags=re.S
)
README.write_text(readme, encoding="utf-8")

print(f"{len(notes)} notes across {len(by_cat)} categories -> README.md updated")
