# 1. Identidad Cromática Principal
* **Color Base Oscuro:** HEX `#0F1714` (Verde bosque casi negro - Botánico profundo)
* **Color Claro Neutro:** HEX `#FDFBF7` (Blanco crema orgánico)
* **Color de Acento (Disruptor):** HEX `#E07A5F` (Terracota vibrante - Acción)
* **Acento Secundario (Textos/Lujo):** HEX `#D4AF37` (Dorado metálico suave)
* **Justificación Psicológica:** El verde profundo `#0F1714` ancla la marca en la naturaleza y el lujo (botánico premium, no manualidad escolar). El `#FDFBF7` da respiro visual y pureza para los bloques claros. El terracota `#E07A5F` actúa como el disparador reptiliano para la acción (cálido, urgencia sutil, orgánico) perfecto para los CTAs y marcadores.

# 2. Arquitectura de Componentes (Estándar Alma)
*Instrucciones obligatorias para la Estación 5 (Tailwind CSS).*

## A. Tablero de Ajedrez (Fondos)
* **Oscuro:** `bg-[#0F1714] text-white`
* **Claro:** `bg-[#FDFBF7] text-slate-900`
* **Acento Block (Bloque de Garantía/Oferta Especial):** `bg-[#E07A5F] text-white`

## B. Tipografía y Highlighting
* **Fuente:** `Outfit` (Google Font - Moderna, geométrica y extremadamente legible). Opcional para subtítulos lujosos: `Playfair Display`.
* **Titulares Gradiente:** `text-transparent bg-clip-text bg-gradient-to-r from-[#D4AF37] to-[#FDE08B]`
* **Marcador en Párrafos (Highlighting):** `<strong class="bg-[#E07A5F]/20 text-[#E07A5F] px-2 rounded-sm font-semibold">`

## C. Efectos y Tarjetas
* **Orbes Glow (Atmósfera):** `absolute bg-[#E07A5F]/20 blur-[150px]` o `bg-[#D4AF37]/15 blur-[120px]`
* **Glassmorphism (Tarjetas en fondos oscuros):** `bg-white/5 border border-white/10 rounded-3xl backdrop-blur-md shadow-2xl`
* **Sello de Garantía (CSS puro):** Sello simple circular o escudo en código HTML/CSS, fondo `#0F1714`, bordes/detalles `#D4AF37`, texto "7 Días de Garantía Incondicional".

# 3. Prompts Visuales Emocionales (Fotorrealismo)
* **Hero Image (Aspiracional):** "A highly photorealistic, cinematic shot of a young elegant woman standing in a pristine, bright modern kitchen. She is smiling softly while holding a beautifully crafted, minimalist botanical soy candle in a premium frosted glass jar. The candle is sitting on a marble countertop next to natural dried flowers and essential oil bottles. Soft, natural morning light filtering through the window, shallow depth of field, 8k resolution, commercial lifestyle photography, luxurious eco-boutique aesthetic."
* **Pain Image (Frustración):** "A photorealistic, cinematic shot of a stressed woman sitting at a cluttered dining table late at night. The table is a mess of spilled cheap wax, broken plastic molds, and stained notebooks with desperate calculations. She is rubbing her temples in frustration, lit by a harsh overhead lamp. Deep shadows, cold tones, conveying a sense of overwhelm and financial anxiety, 8k resolution."
* **Solution Image (Alivio):** "A photorealistic, cinematic shot of a cohesive collection of luxury botanical soaps and candles, arranged aesthetically on a smooth travertine stone slab. The packaging is minimalist, with elegant typography and organic textures. Warm golden hour lighting highlighting the natural ingredients embedded in the soaps. Soft, soothing, and highly premium atmosphere, high-end product photography, 8k resolution."
