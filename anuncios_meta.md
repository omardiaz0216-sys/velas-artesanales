# Estrategia de Creativos para Meta Ads (Andrómeda CBO)

Este documento contiene los "Planos Técnicos" de los anuncios, diseñados bajo la arquitectura Andrómeda. La segmentación la hará el propio texto y la imagen/video (Deep Learning). 

**Estructura de Campaña:** 1 Sola Campaña CBO (Objetivo: Ventas/Conversiones). 1 Solo Conjunto de Anuncios (Público Abierto, Mujeres 25-55, Segmentación Advantage+ activada).

---

## Anuncio 1: El Invalidador (Rol: TOFU - Ángulo: Dolor / Controversia)
*Este anuncio es tu "Abre-mercados". Tendrá el CPA más alto pero traerá volumen masivo al embudo filtrando curiosos.*

- **Gancho (Hook 2):** "Por esto dejé de regalar mis velas y casi quiebro..."
- **Formato Visual (Imagen Generada por IA):** Pantalla dividida (Split-Screen). Izquierda: Una vela genérica mal derretida con un cartel de $3 (Iluminación oscura/sucia). Derecha: La Vela Iceberg premium brillando sobre mármol con etiqueta de $35 (Iluminación de estudio lujo).
- **Fondo Generado (Fase 0):** Se usará `assets/ad_bg_dolor.webp` en el compilador HTML5.
- **Copy Principal (Texto):**
  > Por esto dejé de regalar mis velas a mis amigas (y casi quiebro en el intento). 📉
  >
  > Durante meses, tiré cientos de dólares a la basura siguiendo tutoriales gratuitos de YouTube. Hacía velas "bonitas", pero nadie me pagaba lo que realmente costaba mi tiempo. Competía por centavos.
  >
  > Hasta que entendí que el secreto no está en la cera... está en el sistema.
  >
  > Descubrí el Sistema de Formulación y Marca Guiada™. Dejé de hacer manualidades baratas y empecé a formular experiencias premium (como esta Vela Iceberg) que mis clientas ahora me suplican comprar a $35.
  >
  > Si estás cansada de perder dinero en materiales y quieres convertir tu cocina en una Eco-Boutique rentable en 14 días...
  > 👉 Toca el botón de abajo y descubre el mapa exacto que YouTube te oculta.
- **Headline (Título):** ❌ El error de las velas a $3
- **Botón CTA:** Más información

---

## Anuncio 2: La Transformación (Rol: TOFU - Ángulo: Inspiración / Deseo)
*Activa el código reptiliano del Estatus y la Libertad.*

- **Gancho (Hook 1):** "Cómo pasé de llorar en mi cocina a facturar mi propia marca..."
- **Fondo Generado (Fase 0):** Se usará `assets/ad_bg_beneficio.webp` en el compilador HTML5 para extraer un fotograma, o el video nativo.
  > *(Seg 0-3)* "Cómo pasé de llorar en mi cocina frustrada por quemar mis materiales... a empacar mi propia marca premium todos los días."
  > *(Seg 3-8)* "El problema es que nos enseñan a derretir cera, pero nadie nos enseña a construir un negocio. Yo estaba atrapada en el Método de Ensayo y Error."
  > *(Seg 8-15)* "Con el Sistema de Formulación y Marca Guiada™, aprendí a crear acabados de lujo, empaques hipnóticos y a vender directo por Instagram sin rogarle a nadie."
  > *(Seg 15-20)* "No necesitas ser una experta. Haz clic abajo y empieza hoy mismo tu propio estudio aromático desde casa."
- **Copy Principal (Texto):**
  > ¿Te imaginas despertar y tener pedidos listos para empacar? 📦✨
  > 
  > El Sistema de Formulación y Marca Guiada™ es el atajo exacto para dejar de ser una "aficionada" y convertirte en la dueña de tu propio Estudio Aromático. 
  > 
  > Olvídate de los tutoriales incompletos. Aquí tienes el currículum completo: desde la alquimia de ceras hasta la venta directa.
  > 👉 Toca aquí para ver el catálogo de técnicas.
- **Headline (Título):** Crea tu Marca Premium desde Casa 🏡
- **Botón CTA:** Ver más

---

## Anuncio 3: El Anclaje de Valor (Rol: BOFU - Ángulo: Lógica / Urgencia)
*Este anuncio persigue a los que visitaron tu landing page pero no compraron. Tiene alta frecuencia y CPA bajo.*

- **Gancho (Hook 3):** "Llevo 14 días en el sistema y ya tengo 3 bonos gratis..."
- **Formato Visual (Imagen Carrusel o Gráfico Estático):** Una imagen gráfica muy limpia (Estilo Apple) mostrando una caja abierta de la que salen íconos brillantes o mockups: El curso principal + 3 Cajas de Regalo rojas.
- **Fondo Generado (Fase 0):** Se usará `assets/ad_bg_curiosidad.webp` en el compilador HTML5.
- **Copy Principal (Texto):**
  > Las inscripciones cierran pronto. 🚨
  >
  > Si estás viendo esto, es porque ya sabes que el Sistema de Formulación y Marca Guiada™ es lo que necesitas para iniciar tu Eco-Boutique.
  > 
  > Pero si entras HOY, no solo te llevas el programa completo. Te activamos 3 BONOS PREMIUM sin costo adicional:
  > 🎁 Masterclass de Velas Navideñas (Valor $47)
  > 🎁 Curso Completo de Jabones Artesanales (Valor $67)
  > 🎁 La Bóveda del Emprendedor (Valor $147)
  > 
  > Todo por una fracción mínima. Protegido por nuestra garantía de hierro.
  > 👉 Haz clic y reclama tus bonos antes de que el contador llegue a cero.
- **Headline (Título):** 🎁 3 Bonos Premium (Desaparecen Hoy)
- **Botón CTA:** Comprar

---

## Directrices de Implementación para el Media Buyer
1. Configura la campaña con **CBO (Presupuesto de la Campaña Advantage)**.
2. Sube estos 3 creativos en el mismo conjunto de anuncios.
3. El enlace de todos los botones debe apuntar a la URL de tu landing page (Asegúrate de que la Estación 5 ya inyectó el tracking para que las conversiones lleguen perfectas).
4. **No apagues el Anuncio 1 (Invalidador)** aunque parezca costoso al principio, es el que entrena a la red neuronal Andrómeda para buscar compradoras frustradas con YouTube.
