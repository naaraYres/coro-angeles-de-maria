/* ==========================================================
   CONFIGURACIÓN DEL CORO
   Lo único que hay que tocar para cambiar datos de contacto.
   ========================================================== */

window.CORO = {
  nombre: "Coro Ángeles de María",

  // Número de WhatsApp: código de país + número, sin espacios ni "+".
  whatsapp: "51939942404",

  // Correo donde llegan las cotizaciones enviadas desde la web.
  // Si se cambia, cambiar también el "action" del formulario en index.html.
  correo: "angelesdemaria.eventos@gmail.com",

  // DATOS LEGALES (aparecen en el pie, la política de privacidad, los
  // términos y el Libro de Reclamaciones). Completar con los datos reales.
  razonSocial: "",      // nombre en SUNAT (persona o empresa), ej. "María ... " o "Ángeles de María E.I.R.L."
  ruc: "",              // 11 dígitos
  direccion: "",        // domicilio fiscal
  actualizacion: "12 de noviembre de 2026",

  // Enlace del Libro de Reclamaciones virtual (por ejemplo, el que da la
  // plataforma gratuita del Indecopi "Tu Libro de Reclamaciones").
  // Mientras esté vacío, la página explica cómo reclamar por correo.
  libroReclamaciones: "",

  // Saludo con el que empieza el mensaje de cotización.
  saludo: "Hola, quiero cotizar una presentación del Coro Ángeles de María."
};
