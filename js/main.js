/* =============================================
   GABRIELA NICOSIA - JavaScript Principal
   Arte en Fieltro Agujado
   ============================================= */

document.addEventListener('DOMContentLoaded', () => {

  // --- Preloader ---
  const intro = document.querySelector('.intro');
  if (intro) {
    setTimeout(() => {
      intro.classList.add('hidden');
    }, 1800);
  }

  // --- Header scroll effect ---
  const header = document.querySelector('.header');
  if (header) {
    window.addEventListener('scroll', () => {
      header.classList.toggle('scrolled', window.scrollY > 50);
    }, { passive: true });
  }

  // --- Mobile Drawer ---
  const hamburger    = document.querySelector('.hamburger');
  const drawer       = document.querySelector('.mobile-drawer');
  const drawerClose  = document.querySelector('.mobile-drawer__close');
  const drawerLinks  = document.querySelectorAll('.mobile-drawer__links a');

  if (hamburger && drawer) {
    hamburger.addEventListener('click', () => drawer.classList.add('open'));
    drawerClose?.addEventListener('click', () => drawer.classList.remove('open'));
    drawerLinks.forEach(link => {
      link.addEventListener('click', () => drawer.classList.remove('open'));
    });
    // Cerrar con clic afuera
    document.addEventListener('click', (e) => {
      if (drawer.classList.contains('open') &&
          !drawer.contains(e.target) &&
          !hamburger.contains(e.target)) {
        drawer.classList.remove('open');
      }
    });
  }

  // --- Smooth scroll ---
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // --- Animación de entrada con IntersectionObserver ---
  const animEls = document.querySelectorAll('.anim-in');
  if ('IntersectionObserver' in window && animEls.length) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    animEls.forEach((el, i) => {
      el.style.transitionDelay = `${(i % 4) * 0.1}s`;
      io.observe(el);
    });
  } else {
    // Fallback sin IntersectionObserver
    animEls.forEach(el => el.classList.add('visible'));
  }

  // --- Filtros galería ---
  const filterBtns = document.querySelectorAll('.galeria__filter-btn');
  const obraCards  = document.querySelectorAll('.obra-card');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filtro = btn.dataset.filter;
      obraCards.forEach(card => {
        const cat = card.dataset.categoria;
        if (filtro === 'todos' || cat === filtro) {
          card.style.display = '';
          setTimeout(() => card.style.opacity = '1', 10);
        } else {
          card.style.opacity = '0';
          setTimeout(() => card.style.display = 'none', 300);
        }
      });
    });
  });

});
