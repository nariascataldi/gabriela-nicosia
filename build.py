#!/usr/bin/env python3
"""Build script que ensambla los archivos de secciones en una sola página HTML."""
import os
import re

SECTIONS_DIR = os.path.join(os.path.dirname(__file__), "sections")
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "index.html")

SECTION_ORDER = [
    "01-intro.html",
    "02-header.html",
    "03-mobile-drawer.html",
    "04-hero.html",
    "05-about.html",
    "06-galeria.html",
    "07-proceso.html",
    "08-cuidados.html",
    "09-testimonios.html",
    "10-contacto.html",
    "11-footer.html",
]

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="es">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Gabriela Nicosia - Arte en Fieltro Agujado. Cuadros únicos de fieltro con alma andina: paisajes, fauna y flora.">
  <meta name="theme-color" content="#2B7C9E">
  <title>Gabriela Nicosia | Arte en Fieltro Agujado</title>
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🪡</text></svg>">

  <!-- Google Fonts import is handled in CSS -->

  <!-- Styles -->
  <link rel="stylesheet" href="css/style.css">
</head>

<body>
{sections}

  <!-- JavaScript -->
  <script defer src="js/main.js"></script>
</body>

</html>
"""

HEAD_PATTERN = re.compile(r"<head>.*?</head>\s*", re.DOTALL)
DOCTYPE_PATTERN = re.compile(r"<!DOCTYPE[^>]*>\s*", re.IGNORECASE)
HTML_OPEN_PATTERN = re.compile(r"<html[^>]*>\s*", re.IGNORECASE)
HTML_CLOSE_PATTERN = re.compile(r"</html>\s*", re.IGNORECASE)
BODY_OPEN_PATTERN = re.compile(r"<body[^>]*>\s*", re.IGNORECASE)
BODY_CLOSE_PATTERN = re.compile(r"</body>\s*", re.IGNORECASE)


def strip_wrappers(html_content):
    content = DOCTYPE_PATTERN.sub("", html_content)
    content = HEAD_PATTERN.sub("", content)
    content = HTML_OPEN_PATTERN.sub("", content)
    content = HTML_CLOSE_PATTERN.sub("", content)
    content = BODY_OPEN_PATTERN.sub("", content)
    content = BODY_CLOSE_PATTERN.sub("", content)
    return content


def build():
    parts = []
    for section_file in SECTION_ORDER:
        path = os.path.join(SECTIONS_DIR, section_file)
        if not os.path.exists(path):
            print(f"Warning: Section file not found: {path}")
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read().rstrip("\n")
        parts.append(strip_wrappers(content))

    html = HTML_TEMPLATE.format(sections="\n\n".join(parts))

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Build completado: {OUTPUT_FILE} desde {len(parts)} secciones")


if __name__ == "__main__":
    build()
