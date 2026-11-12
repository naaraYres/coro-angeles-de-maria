# Coro Ángeles de María · web de cotización

Web de una sola página para vender presentaciones del coro en eventos corporativos, centros comerciales y municipalidades. El botón principal arma un mensaje de WhatsApp con los datos del evento.

## Archivos

```
coro-angeles-de-maria/
├── index.html          La página (todas las secciones)
├── favicon.svg         Ícono de la pestaña
├── css/
│   ├── fuentes.css     Carga las fuentes guardadas en /fonts
│   └── coro.css        Estilos propios del coro
├── js/
│   ├── config.js       Número de WhatsApp y saludo  ← aquí se cambia el número
│   └── cotizador.js    Arma el mensaje y abre WhatsApp
├── fonts/              Source Serif 4 y Libre Franklin (licencia libre)
├── assets/             Sistema de diseño (skill Taste): grilla, botones, animaciones. No se edita.
└── .claude/skills/     Skills de diseño: Impeccable, Taste, Emil Kowalski
```

## Secciones

1. **Inicio:** qué es el coro, dónde se ha presentado, botón de cotizar.
2. **Paquetes:** Villancico express, Encendido de árbol, Navidad corporativa, Temporada en centro comercial.
3. **Trayectoria:** frase que se pinta palabra por palabra al bajar.
4. **Cotizar:** 3 pasos y el formulario que abre WhatsApp.
5. **Preguntas frecuentes.**
6. **Cierre y pie de página.**

## Pendiente (lo tiene que pasar el coro)

- [ ] **Fotos y videos** del coro: con uniforme, en un encendido de árbol, en Canal 4 o Saga Falabella. Es lo que más falta: hoy la web va solo con texto.
- [ ] **Logo** en archivo (el del flyer: óvalo, clave de sol, ángel dorado). Hoy lleva un ícono temporal.
- [ ] **Lista de trayectoria** (años, lugares, clientes).
- [ ] Confirmar si la nota de RPP (Miraflores) es de este coro.
- [ ] **Precios** de cada paquete. Hoy dice "el precio depende de la fecha, el distrito y el paquete".
- [ ] Confirmar las duraciones (20-30, 45 y 60 min) y las respuestas del FAQ: sonido, viajes fuera de Lima, villancico con el nombre de la empresa.
- [ ] Dominio propio (cuando exista, se activa la línea `canonical` en `index.html`).

## Cambiar el número de WhatsApp

Editar `js/config.js` (campo `whatsapp`) y los dos enlaces `wa.me/...` en `index.html` (formulario y pie de página).
