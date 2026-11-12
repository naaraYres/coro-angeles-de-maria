/* ==========================================================
   COTIZADOR
   Toma los datos del formulario #form-cotizar y abre WhatsApp
   con el mensaje ya escrito.

   Orden: assets/system.js revisa primero que los campos estén
   completos (y muestra los errores). Si todo está bien, este
   archivo arma el mensaje y abre WhatsApp.
   Sin JavaScript, el formulario igual abre el chat de WhatsApp
   (action del form), solo que sin el mensaje escrito.
   ========================================================== */

const form = document.getElementById('form-cotizar');
const config = window.CORO || {};

function valor(nombre) {
  const campo = form.elements[nombre];
  if (!campo) return '';
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
    `Distrito: ${valor('distrito')}`,
    `Paquete: ${valor('paquete')}`
  ];
  const detalles = valor('detalles');
  if (detalles) lineas.push(`Detalles: ${detalles}`);
  return lineas.join('\n');
}

if (form && config.whatsapp) {
  form.addEventListener('submit', evento => {
    // system.js ya canceló el envío si falta algún campo
    if (evento.defaultPrevented) return;
    evento.preventDefault();
    const url = `https://wa.me/${config.whatsapp}?text=${encodeURIComponent(armarMensaje())}`;
    window.location.href = url;
  });
}
