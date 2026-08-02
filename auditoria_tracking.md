# 🔍 Auditoría de Rastreo y Atribución Avanzada (Meta Ads & Hotmart CAPI)

Este documento analiza minuciosamente las fugas de datos y pérdida de atribución existentes en la integración entre nuestra Landing Page, el Pixel de Meta (navegador), la API de Conversiones (servidor / CAPI) y la pasarela de pagos de Hotmart.

---

## 1. Fuga por Bloqueo de Cookies de Terceros (Safari / iOS / Brave)

### El Problema
Cuando el Pixel de Meta se ejecuta en tu landing page (`tudominio.com`), crea dos cookies persistentes de primera parte:
*   `_fbp` (Identificador único del navegador).
*   `_fbc` (Identificador del clic del anuncio de Meta, basado en el `fbclid`).

Cuando el usuario hace clic en el botón de compra y navega a `pay.hotmart.com` (dominio de Hotmart):
1.  Los navegadores modernos con protección de privacidad (Safari, Brave, Chrome en incógnito o Chrome con cookies de terceros deshabilitadas) **bloquean** el acceso de `hotmart.com` a las cookies creadas en `tudominio.com`.
2.  El Pixel de Meta en el checkout de Hotmart no puede leer tus cookies `_fbp` y `_fbc` originales. Genera unas nuevas, lo que hace que Meta registre esa visita como un usuario completamente diferente.
3.  La API de Conversiones de Hotmart (CAPI) tampoco tiene acceso a estas cookies en el servidor, bajando el **Event Match Quality (EMQ)** a menos del 60%.

### La Solución de Infraestructura (Vital)
Configurar un **Dominio de Checkout Personalizado** en tu cuenta de Hotmart (ej: `checkout.tudominio.com` apuntando a Hotmart por CNAME):
*   Al compartir el dominio raíz (`tudominio.com`), las cookies de Meta se convierten en **cookies de primera parte** compartidas.
*   El checkout de Hotmart y tu landing page podrán leer exactamente las mismas cookies `_fbp` y `_fbc` sin bloqueos del navegador.

---

## 2. El Doble Conteo Irresoluble de `InitiateCheckout`

### El Problema
Hotmart tiene una integración nativa de Meta Pixel que dispara el evento `InitiateCheckout` de forma automática tan pronto como se carga la página de checkout (`pay.hotmart.com`). 
Si nosotros también disparamos `InitiateCheckout` en la landing page al hacer clic en el botón, Meta recibe **dos eventos separados**.

Dado que Hotmart genera su propio `event_id` internamente en su servidor y no permite sobreescribirlo a través de parámetros de la URL, **Meta nunca podrá deduplicar estos dos eventos**. Esto infla artificialmente tu métrica de "Pagos Iniciados" en el Administrador de Anuncios, confundiendo al algoritmo de optimización.

### La Solución en Código
Reemplazar el evento estándar `InitiateCheckout` en el botón de la landing page por un **Evento Personalizado** (ej: `ClickCompra` o `BotonCheckout`).
*   Esto mantiene tu métrica estándar de `InitiateCheckout` limpia (solo cuenta a quienes realmente les cargó el checkout de Hotmart).
*   Te permite medir una nueva métrica intermedia en tu embudo: `ClickCompra` vs. `InitiateCheckout`. Si hay una diferencia de más del 15%, sabes que el checkout de Hotmart está tardando demasiado en cargar o que hay abandonos en la redirección.

---

## 3. Fuga por Apertura en Nueva Pestaña (`sessionStorage` vs `localStorage`)

### El Problema
Actualmente, el motor de rastreo de la landing guarda el `fbclid` y las UTMs en el `sessionStorage`:
*   `sessionStorage` es específico de la pestaña actual.
*   Si el usuario hace clic derecho en el botón de compra y selecciona *"Abrir enlace en una nueva pestaña"*, o si el navegador móvil fuerza la apertura del checkout en una ventana nueva independiente, el `sessionStorage` se limpia por completo en la nueva pestaña.
*   Hotmart se carga sin ningún parámetro de rastreo, perdiendo la atribución por completo.

### La Solución en Código
Espejar el almacenamiento de parámetros utilizando **ambos** mecanismos: `sessionStorage` (temporal y rápido) y `localStorage` (persistente entre pestañas y sesiones). Si la pestaña nueva detecta que `sessionStorage` está vacío, recupera inmediatamente los valores respaldados en `localStorage`.

---

## 4. Pérdida de Atribución en Visitas Recurrentes (Recuperación desde Cookie `_fbc`)

### El Problema
Si un usuario ve tu anuncio de Meta en la mañana, hace clic, entra a la landing, revisa la información, pero no compra. Cierra la página.
En la noche, decide comprar. Entra a tu landing buscando tu URL directamente o desde un marcador (bookmark).
1.  Como entra directo, la URL **no trae el parámetro `fbclid`**.
2.  `sessionStorage` está vacío.
3.  El usuario hace clic en el botón de compra y va a Hotmart. Hotmart se carga sin `fbclid`, y si compra, la venta se registra como "Tráfico Orgánico" o "Directo", perdiendo la atribución en tus campañas de Meta.

### La Solución en Código
Meta Pixel guarda el identificador del clic original en la cookie `_fbc` con el formato `fb.1.[timestamp].[fbclid]`.
Podemos programar nuestro script para que, si no encuentra un `fbclid` en la URL o en el almacenamiento local, lea la cookie `_fbc` del navegador, extraiga el `fbclid` original y lo re-inyecte en el enlace de Hotmart. Esto recupera conversiones que de otro modo se perderían como orgánicas.

---

## 5. Falta de Parámetros Avanzados de Usuario (EMQ)

Para eventos donde no tenemos datos de formulario (como `PageView` y `ClickCompra` en la landing page), podemos mejorar el emparejamiento con Meta Ads enviando parámetros adicionales del navegador que el Pixel oficial a veces no recolecta automáticamente o recolecta tarde:
*   `client_user_agent` (User Agent del dispositivo).
*   `client_ip_address` (IP del usuario, requiere una consulta externa rápida o configuración de servidor).
