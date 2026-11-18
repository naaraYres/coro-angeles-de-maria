/* ==========================================================
   ANIMACIONES SUAVES AL BAJAR
   Títulos, tarjetas y fotos aparecen una sola vez al entrar en
   pantalla (suben 18px y se hacen visibles). Los grupos de tarjetas
   salen en cascada, 100 ms entre una y otra.

   - Sin librerías: IntersectionObserver nativo.
   - Solo se anima transform y opacity (rápido en celulares).
   - Con "reducir movimiento" activado en el sistema no corre:
     el script del <head> no pone la clase "anim-js" y todo se ve
     desde el inicio.
   - Si el observador nunca responde, a los 4 s se muestra todo.
   ========================================================== */
(function () {
  var raiz = document.documentElement;
  if (!raiz.classList.contains('anim-js')) return;

  // Lo que aparece solo
  var solos = [
    'main h2',
    '.ej-banda__lead', '.ej-sub2', '.ej-h3', '.ej-frase',
    '.ej-split__texto > p', '.ej-split__texto > .ej-btn', '#eventos .ej-btn',
    '.ej-marcas'
  ];
  // Grupos que aparecen en cascada (cada hijo con 100 ms de diferencia)
  var grupos = [
    '.ej-datos > div', '.ej-puntos > li', '.ej-cards > .ej-card',
    '.ej-servicios > li', '.ej-pills > li', '.ej-lista > li',
    '.ej-duo > .ej-zoom', '.ej-galeria > .ej-zoom', '.faq > .faq__item'
  ];

  var elementos = [];
  function marcar(el, retraso) {
    if (el.classList.contains('al-entrar')) return;
    el.classList.add('al-entrar');
    el.style.setProperty('--retraso', retraso + 'ms');
    elementos.push(el);
  }
  document.querySelectorAll(solos.join(',')).forEach(function (el) { marcar(el, 0); });
  grupos.forEach(function (sel) {
    var vistos = new Map();
    document.querySelectorAll(sel).forEach(function (el) {
      var i = vistos.get(el.parentNode) || 0;
      vistos.set(el.parentNode, i + 1);
      marcar(el, Math.min(i, 6) * 100);
    });
  });

  function mostrar(el) {
    if (el.classList.contains('visible')) return;
    el.classList.add('visible');
    // al terminar se quitan las clases, así el elemento vuelve a sus
    // transiciones normales (hover de tarjetas y botones)
    var limpiar = function () {
      el.classList.remove('al-entrar', 'visible');
      el.style.removeProperty('--retraso');
    };
    el.addEventListener('transitionend', function fin(e) {
      if (e.target !== el || e.propertyName !== 'opacity') return;
      el.removeEventListener('transitionend', fin);
      limpiar();
    });
    setTimeout(limpiar, 1600); // por si transitionend no llega
  }

  var respondio = false;
  var io = new IntersectionObserver(function (entradas) {
    respondio = true;
    entradas.forEach(function (e) {
      if (!e.isIntersecting) return;
      io.unobserve(e.target);
      mostrar(e.target);
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });
  elementos.forEach(function (el) { io.observe(el); });

  // red de seguridad: si el observador nunca respondió, se muestra todo
  setTimeout(function () { if (!respondio) elementos.forEach(mostrar); }, 4000);
})();
