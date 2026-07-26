import re
import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 3. Comentario HTML Hipotesis
hipotesis = '''<!-- 
HIPÓTESIS ASUMIDAS (CÓDIGOS REPTILIANOS):
1. LIBERTAD: Escapar de la rutina y ser dueña de tu tiempo.
2. CONTROL: Dominar una habilidad comprobada sin perder dinero.
3. RECONOCIMIENTO: Crear un producto premium digno de admirar.
-->
'''
html = html.replace('<body class="', hipotesis + '<body class="')

# 4. Bloque 1
html = html.replace('Reporte Confidencial para Futuras Emprendedoras', 'Reporte Confidencial 2026')
html = html.replace('Por: El Equipo de Expertas del Sistema Eco-Boutique', 'Por: La Creadora del Sistema Eco-Boutique 360')

# 5 y 1. Bloque 2: Retraso de mecanismo y limites
# H1
old_h1 = 'El <span class="text-gradient">Secreto</span> Para Convertir Tu Cocina en una Boutique de Velas y Jabones <span class="text-accent">Altamente Rentable</span> en 14 Días'
new_h1 = 'El <span class="text-gradient">Descubrimiento</span> Para Crear Tu Propio Negocio <span class="text-accent">Altamente Rentable</span> Desde Casa En 14 Días'
html = html.replace(old_h1, new_h1)

# H2
old_h2 = 'Incluso si nunca has derretido cera en tu vida. No necesitas meses de prueba y error: en 14 días tendrás tu primera colección lista para fotografiar y vender con técnicas premium como las Velas Iceberg o Marmolizadas.'
new_h2 = 'Incluso si empiezas desde cero absoluto. Olvida la prueba y error: en 14 días exactos tendrás tu primera colección premium lista para fotografiar y vender con un alto margen.'
html = html.replace(old_h2, new_h2)

# Boton Hero
html = html.replace('Sí, quiero lanzar mi Eco-Boutique', 'Sí, quiero desatar mi potencial creativo')

# 2. Bloque 3: Glosario (Descubrimiento, Desata/Inunda, Derrite/Aplasta, Sobrevivir)
# Bloque 3 replace jabones/velas
html = html.replace('Invertir en materiales para terminar con la casa llena de jabones que nadie compra es un riesgo que no quieres correr.', 'Invertir ahorros intentando sobrevivir en un mercado saturado es un riesgo que aplasta tu motivación.')

# Inunda/Derrite
html = html.replace('Y sientes esa punzada de culpa. <strong class="text-slate-900">"Yo podría hacer eso"</strong>, piensas. "Tengo el talento y la creatividad". Pero el miedo te paraliza.', 'La frustración inunda tu mente. <strong class="text-slate-900">"Yo podría hacer eso"</strong>, piensas. "Tengo el talento". Pero el miedo derrite tu confianza.')

# 6. Bloque 5 H1
old_b5_h1_part1 = 'El Alivio Que Buscabas: Recupera El Control De Tu Tiempo Y Crea Tu Propia <span class="text-accent">Eco-Boutique 360</span>'
html = html.replace(old_b5_h1_part1, 'El Alivio Que Buscabas: Descubre el Método de Bucle Cerrado Eco-Boutique 360')

# 7. Bloque 6: Puente Lógico
html = html.replace('MÓDULO 1: CÓMO CONSUMIR EL PROGRAMA', 'FASE 1: DÍAS 1 A 3 - ALQUIMIA BÁSICA')
html = html.replace('MÓDULO 2: TU PRIMERA VELA ARTESANAL', 'FASE 2: DÍAS 4 A 6 - FORMULACIÓN EXACTA')
html = html.replace('MÓDULO 3: VELAS BÁSICAS', 'FASE 3: DÍAS 7 A 9 - CREACIÓN DE CATÁLOGO')
html = html.replace('MÓDULO 4: VELAS INTERMEDIAS', 'FASE 4: DÍAS 10 A 11 - TÉCNICAS PREMIUM')
html = html.replace('MÓDULO 5: VELAS AVANZADAS', 'FASE 5: DÍAS 12 A 13 - ACABADOS DE LUJO')
html = html.replace('MÓDULO 6: MOLDES EN 3D', 'FASE 6: DÍA 14 - MODELADO Y LANZAMIENTO')

# Remove "Lección X: " globally
html = re.sub(r'Lección \d+: ', '', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
