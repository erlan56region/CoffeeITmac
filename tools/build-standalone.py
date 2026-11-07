#!/usr/bin/env python3
"""Собирает index-standalone.html — версию сайта, в которой все скриншоты
вшиты в HTML как data:URI.

Такой файл не зависит от папки shots/: его можно загрузить на GitHub
(в том числе одним файлом) или открыть локально, и картинки не «отвалятся»
из-за путей, кэша или неполного деплоя.

Требуется ImageMagick (команда convert).

    python3 tools/build-standalone.py
"""
import base64
import re
import subprocess
import tempfile
from pathlib import Path

root = Path(__file__).resolve().parent.parent
html = (root / "index.html").read_text(encoding="utf-8")
refs = sorted(set(re.findall(r'src="(shots/[^"]+)"', html)))

if not refs:
    raise SystemExit("в index.html не найдено ссылок на shots/")

total = 0
with tempfile.TemporaryDirectory() as tmp:
    for i, ref in enumerate(refs, 1):
        out = Path(tmp) / f"{i:03d}.jpg"
        subprocess.run(
            ["convert", str(root / ref), "-auto-orient", "-resize", "900x900>",
             "-strip", "-quality", "78", str(out)],
            check=True,
        )
        raw = out.read_bytes()
        total += len(raw)
        html = html.replace(
            f'src="{ref}"',
            'src="data:image/jpeg;base64,' + base64.b64encode(raw).decode() + '"',
        )

dst = root / "index-standalone.html"
dst.write_text(html, encoding="utf-8")
print(
    f"готово: {dst.name} — {dst.stat().st_size / 1024 / 1024:.2f} МБ "
    f"({len(refs)} картинок вшито, JPEG {total / 1024 / 1024:.2f} МБ)"
)
