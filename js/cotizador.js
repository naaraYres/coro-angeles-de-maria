/* ==========================================================
   COTIZADOR: un formulario, dos formas de enviarlo
   - "Cotizar presentación" → abre WhatsApp con el mensaje escrito.
   - "Enviar por correo"    → manda los datos al correo del coro
                               (servicio gratuito FormSubmit).

   Cómo funciona con assets/system.js:
   system.js revisa los campos y, si el form tiene data-endpoint,
   lo envía por internet. Aquí decidimos ANTES (fase de captura)
   qué botón se tocó:
     · correo   → ponemos data-endpoint y el correo pasa a ser
                  obligatorio; system.js hace el envío.
     · WhatsApp → quitamos data-endpoint; system.js solo revisa y
                  después este archivo abre WhatsApp.
   ========================================================== */

const form = document.getElementById('form-cotizar');
const config = window.CORO || {};

function valor(nombre) {
  const campo = form.elements[nombre];
  if (!campo) return '';
  if (campo instanceof RadioNodeList) {
    return [...campo].filter(c => c.checked).map(c => c.value).join(', ');
  }
  if (campo.type === 'checkbox') return campo.checked ? campo.value : '';
  if (campo.tagName === 'SELECT') return campo.options[campo.selectedIndex]?.text.trim() || '';
  return campo.value.trim();
}

// "2026-12-05" -> "sábado 5 de diciembre de 2026" (la fecha del formulario, más fácil de leer en WhatsApp)
function fechaLegible(v) {
  const m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(v);
  if (!m) return v;
  const d = new Date(+m[1], +m[2] - 1, +m[3]);
  return d.toLocaleDateString('es-PE', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' });
}

function armarMensaje() {
  const lineas = [
    config.saludo || 'Hola, quiero cotizar una presentación.',
    '',
    `Nombre o empresa: ${valor('nombre')}`,
    `Tipo de evento: ${valor('evento')}`,
    `Fecha: ${fechaLegible(valor('fecha'))}`,
    `Distrito: ${valor('distrito')}`
  ];
  const opcionales = [
    ['Instrumentos', valor('instrumentos')],
    ['Correo', valor('correo')],
    ['Detalles', valor('detalles')]
  ];
  opcionales.forEach(([etiqueta, texto]) => { if (texto) lineas.push(`${etiqueta}: ${texto}`); });
  if (config.despedida) lineas.push('', config.despedida);
  return lineas.join('\n');
}

if (form) {
  const correo = form.elements.correo;

  // 1) Antes que system.js: elegir el camino según el botón
  form.addEventListener('submit', evento => {
    const via = evento.submitter?.dataset.enviar || 'whatsapp';
    form.dataset.via = via;
    if (via === 'correo' && config.correo) {
      form.dataset.endpoint = `https://formsubmit.co/ajax/${config.correo}`;
      correo.required = true;
    } else {
      form.dataset.endpoint = '';
      correo.required = false;
    }
  }, true);

  // 2) Después de system.js: si fue WhatsApp y todo está completo, abrir el chat
  form.addEventListener('submit', evento => {
    if (form.dataset.via !== 'whatsapp') return;
    if (evento.defaultPrevented) return; // faltan datos: system.js ya mostró los errores
    evento.preventDefault();
    if (!config.whatsapp) return;
    window.location.href = `https://wa.me/${config.whatsapp}?text=${encodeURIComponent(armarMensaje())}`;
  });
}

/* Las tarjetas "¿Qué evento tiene?" (data-evento) dejan elegido el tipo de evento en el formulario */
document.addEventListener('click', (e) => {
  const enlace = e.target.closest('[data-evento]');
  if (!enlace || !form) return;
  const select = form.elements.evento;
  const opcion = [...select.options].find(o => o.text.trim() === enlace.dataset.evento);
  if (opcion) select.value = opcion.value;
});
