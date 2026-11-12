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

function armarMensaje() {
  const lineas = [
    config.saludo || 'Hola, quiero cotizar una presentación.',
    '',
    `Nombre o empresa: ${valor('nombre')}`,
    `Tipo de evento: ${valor('evento')}`,
    `Fecha: ${valor('fecha')}`,
    `Distrito: ${valor('distrito')}`
  ];
  const opcionales = [
    ['Instrumentos', valor('instrumentos')],
    ['Correo', valor('correo')],
    ['Detalles', valor('detalles')]
  ];
  opcionales.forEach(([etiqueta, texto]) => { if (texto) lineas.push(`${etiqueta}: ${texto}`); });
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
