/* ==========================================================
   DATOS LEGALES: rellena los espacios [data-negocio] con lo que
   está en js/config.js, y activa el botón del Libro de
   Reclamaciones cuando ya hay un enlace.
   ========================================================== */
(function () {
  const c = window.CORO || {};
  document.querySelectorAll('[data-negocio]').forEach(el => {
    const v = c[el.dataset.negocio];
    if (v) el.textContent = v;
  });
  const url = c.libroReclamaciones;
  const boton = document.querySelector('[data-libro-url]');
  const pendiente = document.querySelector('[data-libro-pendiente]');
  if (url && boton) {
    boton.href = url;
    boton.target = '_blank';
    boton.rel = 'noopener';
    boton.hidden = false;
    if (pendiente) pendiente.hidden = true;
  }
})();
