def crear_pagina_web(titulo, contenido, imagen):
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{titulo}</title>
    </head>
    <body>
        <h1>{titulo}</h1>
        <div>{contenido}</div>
        <img src="{imagen}" alt="Resultados">
    </body>
    </html>
    """
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_template)

import matplotlib.pyplot as plt
import pandas as pd

# Crear gráfico
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [2, 5, 3, 8, 7]
})

plt.figure(figsize=(10, 6))
plt.plot(df['x'], df['y'], marker='o')
plt.title('Resultados del Análisis')
plt.savefig('grafico.png', dpi=150, bbox_inches='tight')

# Crear página web automáticamente
crear_pagina_web(
    "Mi Análisis Python",
    "Resultados obtenidos del análisis de datos...",
    "grafico.png"
)