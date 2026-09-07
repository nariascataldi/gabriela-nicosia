# Plantilla Web - GitHub + Vercel

Blueprint para crear landing pages rápidas. Arquitectura: HTML/CSS/JS puro + build con Python + deploy en Vercel.

---

## Estructura del proyecto

```
mi-proyecto/
├── .gitignore
├── vercel.json
├── build.py
├── estilos.md
├── README.md
├── image/
├── css/
│   └── style.css
├── js/
│   └── main.js
├── sections/
│   ├── 01-intro.html
│   ├── 02-header.html
│   ├── 03-mobile-drawer.html
│   ├── 04-hero.html
│   ├── 05-about.html
│   ├── 06-servicios.html
│   ├── 07-testimonios.html
│   ├── 08-contacto.html
│   └── 09-footer.html
└── index.html (generado por build.py)
```

---

## vercel.json

```json
{
  "buildCommand": "python3 build.py",
  "outputDirectory": ".",
  "framework": null,
  "installCommand": "echo 'No install needed'"
}
```

---

## .gitignore

```
.vercel
node_modules
.DS_Store
```

---

## build.py

```python
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
    "06-servicios.html",
    "07-testimonios.html",
    "08-contacto.html",
    "09-footer.html",
]

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="es">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="[DESCRIPCION DEL SITIO]">
  <title>[NOMBRE DEL SITIO]</title>

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Montserrat:wght@700;800;900&display=swap" rel="stylesheet">

  <!-- Theme -->
  <meta name="theme-color" content="#111111" media="(prefers-color-scheme: dark)">
  <meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">

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
        with open(path, "r", encoding="utf-8") as f:
            content = f.read().rstrip("\n")
        parts.append(strip_wrappers(content))

    html = HTML_TEMPLATE.format(sections="\n\n".join(parts))

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Build completado: {OUTPUT_FILE} desde {len(parts)} secciones")


if __name__ == "__main__":
    build()
```

---

## css/style.css

```css
/* =============================================
   PLANTILLA WEB - Estilos Principales
   ============================================= */

/* --- Reset y Variables --- */
:root {
  --color-negro: #0a0a0a;
  --color-gris-oscuro: #1a1a1a;
  --color-gris: #2d2d2d;
  --color-gris-claro: #4a4a4a;
  --color-acento: #ff3c00;
  --color-blanco: #ffffff;
  --color-blanco-rostro: #f5f5f5;
  --color-header-bg: rgba(10, 10, 10, 0.95);
  --color-header-bg-scroll: rgba(10, 10, 10, 0.98);
  --gradiente-logo: linear-gradient(90deg, #FF3C00 0%, #FF6A00 25%, #FFAA00 50%, #FFD700 75%, #FFFF00 100%);
  --font-heading: 'Montserrat', sans-serif;
  --font-body: 'Inter', sans-serif;
}

[data-theme="light"] {
  --color-negro: #ffffff;
  --color-gris-oscuro: #f5f5f5;
  --color-gris: #e0e0e0;
  --color-gris-claro: #666666;
  --color-acento: #ff3c00;
  --color-blanco: #1a1a1a;
  --color-blanco-rostro: #333333;
  --color-header-bg: rgba(255, 255, 255, 0.95);
  --color-header-bg-scroll: rgba(255, 255, 255, 0.98);
  --gradiente-logo: linear-gradient(90deg, #CC3000 0%, #E85D00 25%, #FF7700 50%, #FF9500 75%, #FFAA00 100%);
}

*, *::before, *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  font-family: var(--font-body);
  background-color: var(--color-negro);
  color: var(--color-blanco);
  line-height: 1.6;
  overflow-x: hidden;
}

img { max-width: 100%; height: auto; display: block; }
a { text-decoration: none; color: inherit; }
ul { list-style: none; }

/* --- Intro / Preloader --- */
.intro {
  position: fixed; inset: 0;
  background: var(--color-negro);
  display: flex; align-items: center; justify-content: center;
  z-index: 9999;
  transition: opacity 0.5s ease, visibility 0.5s ease;
}
.intro.hidden { opacity: 0; visibility: hidden; }
.intro__logo {
  font-family: var(--font-heading);
  font-size: 2rem; font-weight: 900; letter-spacing: 2px;
  animation: pulse 1.5s ease-in-out infinite;
  background: var(--gradiente-logo);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
}
@keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.4; } }

/* --- Header --- */
.header {
  position: fixed; top: 0; left: 0; width: 100%;
  padding: 1rem 2rem;
  display: flex; align-items: center; justify-content: space-between;
  background: var(--color-header-bg);
  backdrop-filter: blur(10px);
  z-index: 1000;
  border-bottom: 1px solid var(--color-gris);
}
.header__logo {
  font-family: var(--font-heading);
  font-size: 1.4rem; font-weight: 900;
  background: var(--gradiente-logo);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
}
.header__nav { display: flex; align-items: center; gap: 2rem; }
.header__nav a {
  font-size: 0.9rem; font-weight: 500;
  text-transform: uppercase; letter-spacing: 1px;
  transition: color 0.3s ease;
}
.header__nav a:hover { color: var(--color-acento); }
.header__whatsapp {
  display: flex; align-items: center; gap: 0.5rem;
  background: #25d366; color: var(--color-blanco);
  padding: 0.5rem 1rem; border-radius: 25px;
  font-weight: 600; font-size: 0.85rem;
  transition: transform 0.3s ease;
}
.header__whatsapp:hover { transform: scale(1.05); }

/* --- Theme Toggle --- */
.theme-toggle {
  background: var(--color-gris); border: none;
  width: 40px; height: 40px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  cursor: pointer;
  transition: background 0.3s ease, transform 0.3s ease;
  color: var(--color-blanco); font-size: 1.2rem;
}
.theme-toggle:hover { background: var(--color-acento); transform: scale(1.1); }
.theme-toggle .icon-sun, .theme-toggle .icon-moon { display: none; }
[data-theme="dark"] .theme-toggle .icon-sun, :root:not([data-theme]) .theme-toggle .icon-sun { display: block; }
[data-theme="light"] .theme-toggle .icon-moon { display: block; }

/* --- Mobile Drawer --- */
.mobile-drawer {
  position: fixed; top: 0; right: -100%;
  width: 280px; height: 100vh;
  background: var(--color-gris-oscuro);
  z-index: 2000; padding: 5rem 2rem 2rem;
  transition: right 0.3s ease;
  box-shadow: -5px 0 20px rgba(0,0,0,0.3);
}
.mobile-drawer.open { right: 0; }
.mobile-drawer__close {
  position: absolute; top: 1.5rem; right: 1.5rem;
  background: none; border: none;
  color: var(--color-blanco); font-size: 1.5rem; cursor: pointer;
}
.mobile-drawer__links { display: flex; flex-direction: column; gap: 1.5rem; }
.mobile-drawer__links a {
  font-size: 1.1rem; font-weight: 600;
  text-transform: uppercase; letter-spacing: 1px;
  padding: 0.5rem 0; border-bottom: 1px solid var(--color-gris);
  transition: color 0.3s ease;
}
.mobile-drawer__links a:hover { color: var(--color-acento); }
.mobile-drawer__toggle {
  display: flex; align-items: center; gap: 0.75rem;
  margin-top: 2rem; padding-top: 1.5rem;
  border-top: 1px solid var(--color-gris);
}
.mobile-drawer__toggle-label {
  font-size: 0.9rem; font-weight: 600;
  text-transform: uppercase; letter-spacing: 1px;
}
.hamburger {
  display: none; flex-direction: column; gap: 5px;
  background: none; border: none; cursor: pointer; padding: 0.5rem;
}
.hamburger span {
  width: 25px; height: 2px;
  background: var(--color-blanco);
  transition: all 0.3s ease;
}

/* --- Hero --- */
.hero {
  min-height: 100vh;
  display: flex; align-items: center; justify-content: center;
  text-align: center; padding: 6rem 2rem 4rem;
  background: linear-gradient(135deg, var(--color-negro) 0%, var(--color-gris-oscuro) 100%);
}
.hero__content { max-width: 800px; }
.hero__tagline {
  font-size: 0.9rem; font-weight: 600;
  text-transform: uppercase; letter-spacing: 3px;
  color: var(--color-acento); margin-bottom: 1rem;
}
.hero__title {
  font-family: var(--font-heading);
  font-size: clamp(2rem, 5vw, 3.5rem);
  font-weight: 900; line-height: 1.1; margin-bottom: 1.5rem;
}
.hero__subtitle {
  font-size: 1.1rem; color: var(--color-gris-claro);
  margin-bottom: 2rem; max-width: 600px;
  margin-left: auto; margin-right: auto;
}
.hero__cta {
  display: inline-flex; align-items: center; gap: 0.5rem;
  background: var(--color-acento); color: var(--color-blanco);
  padding: 1rem 2rem; border-radius: 30px;
  font-weight: 700; font-size: 1rem;
  text-transform: uppercase; letter-spacing: 1px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.hero__cta:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 30px rgba(255,60,0,0.3);
}

/* --- About --- */
.about { padding: 5rem 2rem; background: var(--color-gris-oscuro); }
.about__container {
  max-width: 1100px; margin: 0 auto;
  display: grid; grid-template-columns: 1fr 1fr; gap: 4rem;
  align-items: center;
}
.about__label {
  font-size: 0.8rem; font-weight: 700;
  text-transform: uppercase; letter-spacing: 3px;
  color: var(--color-acento); margin-bottom: 1rem;
}
.about__title {
  font-family: var(--font-heading);
  font-size: 2rem; font-weight: 900; margin-bottom: 1.5rem;
}
.about__text { color: var(--color-gris-claro); margin-bottom: 1rem; }
.about__badges { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.5rem; }
.about__badge {
  display: inline-block; padding: 0.5rem 1rem;
  background: var(--color-gris); border-radius: 20px;
  font-size: 0.8rem; font-weight: 600;
  text-transform: uppercase; letter-spacing: 1px;
  color: var(--color-acento); border: 1px solid var(--color-acento);
}
.about__image {
  width: 100%; height: 400px;
  background: var(--color-gris); border-radius: 12px; overflow: hidden;
}
.about__image img { width: 100%; height: 100%; object-fit: cover; }

/* --- Servicios --- */
.servicios { padding: 5rem 2rem; background: var(--color-negro); }
.servicios__header { text-align: center; margin-bottom: 3rem; }
.servicios__label {
  font-size: 0.8rem; font-weight: 700;
  text-transform: uppercase; letter-spacing: 3px;
  color: var(--color-acento); margin-bottom: 0.5rem;
}
.servicios__title {
  font-family: var(--font-heading);
  font-size: 2rem; font-weight: 900;
}
.servicios__grid {
  max-width: 1100px; margin: 0 auto;
  display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}
.servicio-card {
  background: var(--color-gris-oscuro);
  padding: 2rem; border-radius: 12px;
  border: 1px solid var(--color-gris);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.servicio-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 40px rgba(0,0,0,0.4);
}
.servicio-card__icon {
  width: 50px; height: 50px;
  background: var(--color-acento); border-radius: 10px;
  display: flex; align-items: center; justify-content: center;
  color: var(--color-blanco); font-size: 1.5rem; margin-bottom: 1rem;
}
.servicio-card__title {
  font-family: var(--font-heading);
  font-size: 1.2rem; font-weight: 800; margin-bottom: 0.5rem;
}
.servicio-card__desc {
  font-size: 0.9rem; color: var(--color-gris-claro);
}

/* --- Testimonios --- */
.testimonios { padding: 5rem 2rem; background: var(--color-gris-oscuro); }
.testimonios__header { text-align: center; margin-bottom: 3rem; }
.testimonios__label {
  font-size: 0.8rem; font-weight: 700;
  text-transform: uppercase; letter-spacing: 3px;
  color: var(--color-acento); margin-bottom: 0.5rem;
}
.testimonios__title {
  font-family: var(--font-heading);
  font-size: 2rem; font-weight: 900;
}
.testimonios__grid {
  max-width: 1100px; margin: 0 auto;
  display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}
.testimonio {
  background: var(--color-negro);
  padding: 2rem; border-radius: 12px;
  border: 1px solid var(--color-gris);
}
.testimonio__stars { color: #f5a623; font-size: 1.2rem; margin-bottom: 1rem; }
.testimonio__texto {
  font-style: italic; color: var(--color-blanco-rostro);
  margin-bottom: 1.5rem;
}
.testimonio__autor { font-weight: 700; font-size: 0.9rem; }
.testimonio__rol { font-size: 0.8rem; color: var(--color-gris-claro); }

/* --- Contacto --- */
.contacto { padding: 5rem 2rem; background: var(--color-negro); }
.contacto__container { max-width: 900px; margin: 0 auto; }
.contacto__label {
  font-size: 0.8rem; font-weight: 700;
  text-transform: uppercase; letter-spacing: 3px;
  color: var(--color-acento); margin-bottom: 1rem;
}
.contacto__title {
  font-family: var(--font-heading);
  font-size: 2rem; font-weight: 900; margin-bottom: 1.5rem;
}
.contacto__info { display: flex; flex-direction: column; gap: 1rem; }
.contacto__item {
  display: flex; align-items: center; gap: 1rem;
  font-size: 1rem; color: var(--color-blanco-rostro);
}
.contacto__item-icon {
  width: 40px; height: 40px;
  background: var(--color-gris); border-radius: 8px;
  display: flex; align-items: center; justify-content: center;
  color: var(--color-acento); flex-shrink: 0;
}
.contacto__item-link { transition: color 0.3s ease; }
.contacto__item-link:hover { color: var(--color-acento); }

/* --- Footer --- */
.footer {
  padding: 3rem 2rem;
  background: var(--color-gris-oscuro);
  border-top: 1px solid var(--color-gris);
}
.footer__container {
  max-width: 1100px; margin: 0 auto;
  display: flex; align-items: center; justify-content: space-between;
  flex-wrap: wrap; gap: 1.5rem;
}
.footer__logo {
  font-family: var(--font-heading);
  font-size: 1.2rem; font-weight: 900; color: var(--color-acento);
}
.footer__copy { font-size: 0.85rem; color: var(--color-gris-claro); }
.footer__socials { display: flex; gap: 1rem; }
.footer__socials a {
  width: 40px; height: 40px;
  background: var(--color-gris); border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  transition: background 0.3s ease, transform 0.3s ease;
}
.footer__socials a:hover {
  background: var(--color-acento); transform: translateY(-2px);
}

/* --- Responsive --- */
@media (max-width: 768px) {
  .header__nav { display: none; }
  .hamburger { display: flex; }
  .about__container { grid-template-columns: 1fr; }
  .hero__title { font-size: 2rem; }
}
```

---

## js/main.js

```javascript
/* =============================================
   PLANTILLA WEB - JavaScript Principal
   ============================================= */

document.addEventListener('DOMContentLoaded', () => {

  // --- Theme Toggle (Day/Night) ---
  const themeToggle = document.querySelectorAll('.theme-toggle');
  const savedTheme = localStorage.getItem('theme') || 'light';

  function updateThemeColor(theme) {
    const meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.content = theme === 'dark' ? '#111111' : '#ffffff';
  }

  document.body.setAttribute('data-theme', savedTheme);
  updateThemeColor(savedTheme);

  function toggleTheme() {
    const current = document.body.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.body.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    updateThemeColor(next);
  }

  themeToggle.forEach(btn => {
    btn.addEventListener('click', toggleTheme);
  });

  // --- Intro / Preloader ---
  const intro = document.querySelector('.intro');
  if (intro) {
    setTimeout(() => {
      intro.classList.add('hidden');
    }, 1500);
  }

  // --- Mobile Drawer ---
  const hamburger = document.querySelector('.hamburger');
  const drawer = document.querySelector('.mobile-drawer');
  const drawerClose = document.querySelector('.mobile-drawer__close');
  const drawerLinks = document.querySelectorAll('.mobile-drawer__links a');

  if (hamburger && drawer) {
    hamburger.addEventListener('click', () => {
      drawer.classList.add('open');
    });

    drawerClose?.addEventListener('click', () => {
      drawer.classList.remove('open');
    });

    drawerLinks.forEach(link => {
      link.addEventListener('click', () => {
        drawer.classList.remove('open');
      });
    });
  }

  // --- Header scroll effect ---
  const header = document.querySelector('.header');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        header.style.background = 'var(--color-header-bg-scroll)';
      } else {
        header.style.background = 'var(--color-header-bg)';
      }
    });
  }

  // --- Smooth scroll para links internos ---
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });

});
```

---

## sections/01-intro.html

```html
<section class="intro" id="intro">
  <div class="intro__logo">MI MARCA</div>
</section>
```

---

## sections/02-header.html

```html
<header class="header" id="header">
  <a href="#" class="header__logo">MI MARCA</a>

  <nav class="header__nav">
    <a href="#inicio">Inicio</a>
    <a href="#nosotros">Nosotros</a>
    <a href="#servicios">Servicios</a>
    <a href="#testimonios">Testimonios</a>
    <a href="#contacto">Contacto</a>
    <a href="https://wa.me/549XXXXXXXXXX" class="header__whatsapp" target="_blank">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
        <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
      </svg>
      WhatsApp
    </a>
    <button class="theme-toggle" aria-label="Cambiar tema">
      <svg class="icon-sun" width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
        <path d="M12 7c-2.76 0-5 2.24-5 5s2.24 5 5 5 5-2.24 5-5-2.24-5-5-5zM2 13h2c.55 0 1-.45 1-1s-.45-1-1-1H2c-.55 0-1 .45-1 1s.45 1 1 1zm18 0h2c.55 0 1-.45 1-1s-.45-1-1-1h-2c-.55 0-1 .45-1 1s.45 1 1 1zM11 2v2c0 .55.45 1 1 1s1-.45 1-1V2c0-.55-.45-1-1-1s-1 .45-1 1zm0 18v2c0 .55.45 1 1 1s1-.45 1-1v-2c0-.55-.45-1-1-1s-1 .45-1 1zM5.99 4.58c-.39-.39-1.03-.39-1.42 0-.39.39-.39 1.03 0 1.42l1.06 1.06c.39.39 1.03.39 1.42 0s.39-1.03 0-1.42L5.99 4.58zm12.03 12.02c-.39-.39-1.03-.39-1.42 0-.39.39-.39 1.03 0 1.42l1.06 1.06c.39.39 1.03.39 1.42 0 .39-.39.39-1.03 0-1.42l-1.06-1.06zm1.06-10.96c.39-.39.39-1.03 0-1.42-.39-.39-1.03-.39-1.42 0l-1.06 1.06c-.39.39-.39 1.03 0 1.42s1.03.39 1.42 0l1.06-1.06zM7.05 18.36c.39-.39.39-1.03 0-1.42-.39-.39-1.03-.39-1.42 0l-1.06 1.06c-.39.39-.39 1.03 0 1.42s1.03.39 1.42 0l1.06-1.06z"/>
      </svg>
      <svg class="icon-moon" width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
        <path d="M12 3c-4.97 0-9 4.03-9 9s4.03 9 9 9 9-4.03 9-9c0-.46-.04-.92-.1-1.36-.98 1.37-2.58 2.26-4.4 2.26-2.98 0-5.4-2.42-5.4-5.4 0-1.81.89-3.42 2.26-4.4-.44-.06-.9-.1-1.36-.1z"/>
      </svg>
    </button>
  </nav>

  <button class="hamburger" aria-label="Abrir menú">
    <span></span>
    <span></span>
    <span></span>
  </button>
</header>
```

---

## sections/03-mobile-drawer.html

```html
<aside class="mobile-drawer" id="mobile-drawer">
  <button class="mobile-drawer__close" aria-label="Cerrar menú">&times;</button>

  <nav class="mobile-drawer__links">
    <a href="#inicio">Inicio</a>
    <a href="#nosotros">Nosotros</a>
    <a href="#servicios">Servicios</a>
    <a href="#testimonios">Testimonios</a>
    <a href="#contacto">Contacto</a>
    <a href="https://wa.me/549XXXXXXXXXX" target="_blank">WhatsApp</a>
  </nav>

  <div class="mobile-drawer__toggle">
    <button class="theme-toggle" aria-label="Cambiar tema">
      <svg class="icon-sun" width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
        <path d="M12 7c-2.76 0-5 2.24-5 5s2.24 5 5 5 5-2.24 5-5-2.24-5-5-5zM2 13h2c.55 0 1-.45 1-1s-.45-1-1-1H2c-.55 0-1 .45-1 1s.45 1 1 1zm18 0h2c.55 0 1-.45 1-1s-.45-1-1-1h-2c-.55 0-1 .45-1 1s.45 1 1 1zM11 2v2c0 .55.45 1 1 1s1-.45 1-1V2c0-.55-.45-1-1-1s-1 .45-1 1zm0 18v2c0 .55.45 1 1 1s1-.45 1-1v-2c0-.55-.45-1-1-1s-1 .45-1 1zM5.99 4.58c-.39-.39-1.03-.39-1.42 0-.39.39-.39 1.03 0 1.42l1.06 1.06c.39.39 1.03.39 1.42 0s.39-1.03 0-1.42L5.99 4.58zm12.03 12.02c-.39-.39-1.03-.39-1.42 0-.39.39-.39 1.03 0 1.42l1.06 1.06c.39.39 1.03.39 1.42 0 .39-.39.39-1.03 0-1.42l-1.06-1.06zm1.06-10.96c.39-.39.39-1.03 0-1.42-.39-.39-1.03-.39-1.42 0l-1.06 1.06c-.39.39-.39 1.03 0 1.42s1.03.39 1.42 0l1.06-1.06zM7.05 18.36c.39-.39.39-1.03 0-1.42-.39-.39-1.03-.39-1.42 0l-1.06 1.06c-.39.39-.39 1.03 0 1.42s1.03.39 1.42 0l1.06-1.06z"/>
      </svg>
      <svg class="icon-moon" width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
        <path d="M12 3c-4.97 0-9 4.03-9 9s4.03 9 9 9 9-4.03 9-9c0-.46-.04-.92-.1-1.36-.98 1.37-2.58 2.26-4.4 2.26-2.98 0-5.4-2.42-5.4-5.4 0-1.81.89-3.42 2.26-4.4-.44-.06-.9-.1-1.36-.1z"/>
      </svg>
    </button>
    <span class="mobile-drawer__toggle-label">Modo día/noche</span>
  </div>
</aside>
```

---

## sections/04-hero.html

```html
<section class="hero" id="inicio">
  <div class="hero__content">
    <p class="hero__tagline">[TAGLINE / LEMA]</p>
    <h1 class="hero__title">[TITULO PRINCIPAL]</h1>
    <p class="hero__subtitle">
      [DESCRIPCION CORTA DEL NEGOCIO O SERVICIO]
    </p>
    <a href="https://wa.me/549XXXXXXXXXX" class="hero__cta" target="_blank">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
        <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
      </svg>
      [TEXTO CTA]
    </a>
  </div>
</section>
```

---

## sections/05-about.html

```html
<section class="about" id="nosotros">
  <div class="about__container">
    <div class="about__content">
      <p class="about__label">Sobre nosotros</p>
      <h2 class="about__title">[TITULO SOBRE NOSOTROS]</h2>
      <p class="about__text">
        [DESCRIPCION DEL NEGOCIO - PARRAFO 1]
      </p>
      <p class="about__text">
        [DESCRIPCION DEL NEGOCIO - PARRAFO 2]
      </p>
      <div class="about__badges">
        <span class="about__badge">[BADGE 1]</span>
        <span class="about__badge">[BADGE 2]</span>
      </div>
    </div>
    <div class="about__image">
      <img src="image/[IMAGEN].jpeg" alt="[ALT TEXT]" loading="lazy">
    </div>
  </div>
</section>
```

---

## sections/06-servicios.html

```html
<section class="servicios" id="servicios">
  <div class="servicios__header">
    <p class="servicios__label">Nuestros servicios</p>
    <h2 class="servicios__title">[TITULO SERVICIOS]</h2>
  </div>

  <div class="servicios__grid">
    <div class="servicio-card">
      <div class="servicio-card__icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
        </svg>
      </div>
      <h3 class="servicio-card__title">[SERVICIO 1]</h3>
      <p class="servicio-card__desc">[DESCRIPCION SERVICIO 1]</p>
    </div>

    <div class="servicio-card">
      <div class="servicio-card__icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
          <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/>
        </svg>
      </div>
      <h3 class="servicio-card__title">[SERVICIO 2]</h3>
      <p class="servicio-card__desc">[DESCRIPCION SERVICIO 2]</p>
    </div>

    <div class="servicio-card">
      <div class="servicio-card__icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z"/>
        </svg>
      </div>
      <h3 class="servicio-card__title">[SERVICIO 3]</h3>
      <p class="servicio-card__desc">[DESCRIPCION SERVICIO 3]</p>
    </div>
  </div>
</section>
```

---

## sections/07-testimonios.html

```html
<section class="testimonios" id="testimonios">
  <div class="testimonios__header">
    <p class="testimonios__label">Opiniones</p>
    <h2 class="testimonios__title">Lo que dicen nuestros clientes</h2>
  </div>

  <div class="testimonios__grid">
    <div class="testimonio">
      <div class="testimonio__stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
      <p class="testimonio__texto">
        "[TESTIMONIO 1]"
      </p>
      <p class="testimonio__autor">[NOMBRE 1]</p>
      <p class="testimonio__rol">[ROL / EMPRESA 1]</p>
    </div>

    <div class="testimonio">
      <div class="testimonio__stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
      <p class="testimonio__texto">
        "[TESTIMONIO 2]"
      </p>
      <p class="testimonio__autor">[NOMBRE 2]</p>
      <p class="testimonio__rol">[ROL / EMPRESA 2]</p>
    </div>

    <div class="testimonio">
      <div class="testimonio__stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
      <p class="testimonio__texto">
        "[TESTIMONIO 3]"
      </p>
      <p class="testimonio__autor">[NOMBRE 3]</p>
      <p class="testimonio__rol">[ROL / EMPRESA 3]</p>
    </div>
  </div>
</section>
```

---

## sections/08-contacto.html

```html
<section class="contacto" id="contacto">
  <div class="contacto__container">
    <p class="contacto__label">Contacto</p>
    <h2 class="contacto__title">¿Cómo nos encontrás?</h2>

    <div class="contacto__info">
      <div class="contacto__item">
        <div class="contacto__item-icon">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/>
          </svg>
        </div>
        <span>[DIRECCION]</span>
      </div>

      <div class="contacto__item">
        <div class="contacto__item-icon">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
            <path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/>
          </svg>
        </div>
        <span>[TELEFONO]</span>
      </div>

      <div class="contacto__item">
        <div class="contacto__item-icon">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
            <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
          </svg>
        </div>
        <a href="mailto:[EMAIL]" class="contacto__item-link" target="_blank">[EMAIL]</a>
      </div>

      <div class="contacto__item">
        <div class="contacto__item-icon">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/>
          </svg>
        </div>
        <a href="https://www.instagram.com/[USUARIO]" class="contacto__item-link" target="_blank">@[USUARIO]</a>
      </div>
    </div>
  </div>
</section>
```

---

## sections/09-footer.html

```html
<footer class="footer">
  <div class="footer__container">
    <a href="#" class="footer__logo">MI MARCA</a>

    <p class="footer__copy">&copy; 2026 [NOMBRE MARCA]. Todos los derechos reservados.</p>

    <div class="footer__socials">
      <a href="https://www.instagram.com/[USUARIO]/" target="_blank" aria-label="Instagram">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/>
        </svg>
      </a>
      <a href="https://wa.me/549XXXXXXXXXX" target="_blank" aria-label="WhatsApp">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
          <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
        </svg>
      </a>
    </div>
  </div>
</footer>
```

---

## estilos.md

```markdown
# Guía de Identidad de Marca

## Paleta de colores

| Color | Hex | Uso |
|-------|-----|-----|
| Negro | #0a0a0a | Fondo principal (dark mode) |
| Gris oscuro | #1a1a1a | Secciones alternas |
| Gris | #2d2d2d | Bordes, cards |
| Gris claro | #4a4a4a | Texto secundario |
| Acento | #ff3c00 | Botones, links, highlights |
| Blanco | #ffffff | Texto principal (dark mode) |

## Tipografía

- **Headings:** Montserrat (700, 800, 900)
- **Body:** Inter (400, 500, 600)

## BEM Naming

```
 bloque__elemento--modificador
 .hero__title
 .servicio-card__icon
 .header__whatsapp
```

## Modo día/noche

- Dark: fondo negro, texto blanco
- Light: fondo blanco, texto negro
- Toggle con localStorage
- Variable `data-theme` en `<body>`

## Spacing

- Secciones: `padding: 5rem 2rem`
- Cards: `padding: 2rem`
- Gap grid: `2rem`
- Border radius: `12px` (cards), `25px` (botones), `50%` (iconos circulares)

## Breakpoints

- Desktop: > 768px (nav horizontal)
- Mobile: ≤ 768px (hamburger + drawer)
```

---

## README.md

```markdown
# [NOMBRE DEL PROYECTO]

[DESCRIPCIÓN CORTA]

## Estructura del proyecto

├── css/           # Estilos principales
├── js/            # JavaScript
├── sections/      # Secciones HTML separadas
├── image/         # Imágenes
├── build.py       # Script de build
├── vercel.json    # Configuración Vercel
└── estilos.md     # Guía de identidad de marca

## Desarrollo local

```bash
python3 build.py
```

Esto genera `index.html` desde las secciones de `sections/`.

## Deploy

1. Crear repo en GitHub
2. `git init && git add . && git commit -m "init"`
3. `git remote add origin <URL>`
4. `git push -u origin main`
5. Conectar repo en Vercel → deploy automático

## Personalización

1. Reemplazar `MI MARCA` en todas las secciones
2. Cambiar `549XXXXXXXXXX` por número de WhatsApp real
3. Actualizar colores en `css/style.css` (variables CSS)
4. Agregar imágenes reales en `image/`
5. Editar testimonios y datos de contacto
```

---

## Pasos para crear un proyecto nuevo

1. **Copiar esta plantilla** a una nueva carpeta
2. **Reemplazar placeholders:**
   - `MI MARCA` → nombre del negocio
   - `549XXXXXXXXXX` → número de WhatsApp
   - `[USUARIO]` → usuario de Instagram
   - `[EMAIL]` → email de contacto
   - `[DIRECCION]` → dirección física
   - `[TELEFONO]` → teléfono
   - `[TAGLINE]`, `[TITULO]`, `[DESCRIPCION]` → textos del negocio
   - `[SERVICIO 1-3]` → servicios que ofrece
   - `[TESTIMONIO 1-3]` → opiniones de clientes
3. **Personalizar colores** en `css/style.css` (sección `:root`)
4. **Correr build:** `python3 build.py`
5. **Subir a GitHub** y conectar en Vercel
