# Análisis Estereográfico de Planos y Eigenvectores

Este repositorio contiene un script en Python para graficar datos estructurales geológicos (planos y polos) en un diagrama estereográfico, calcular los eigenvectores principales de la distribución y visualizarlos con personalización avanzada usando la librería `mplstereonet`.

## Características

- Lee datos estructurales (strike, dip) desde un archivo CSV.
- Grafica planos y sus polos en un diagrama estereográfico.
- Calcula y representa los eigenvectores principales (E₁, E₂, E₃) con colores y bordes personalizados.
- Muestra leyendas diferenciadas: una para los nombres de los eigenvectores y otra con sus valores numéricos.
- Permite personalizar la ubicación y el formato de los textos y leyendas.
- Oculta la leyenda azimutal (números de grados alrededor del círculo).

## Requisitos

- Python 3.x
- [mplstereonet](https://mplstereonet.readthedocs.io/en/latest/)
- matplotlib
- pandas
- numpy

Instala los requisitos con:

```bash
pip install mplstereonet matplotlib pandas numpy
```

## Uso

1. Prepara tu archivo CSV con al menos las columnas `strike` y `dip` (encabezado en la primera fila).

   **Ejemplo:**
   ```csv
   strike,dip
   120,30
   80,45
   200,60
   ```

2. Ejecuta el script pasando el nombre de tu archivo CSV como argumento:

   ```bash
   python tu_script.py datos.csv
   ```

3. Se abrirá una ventana con el diagrama estereográfico mostrando:
   - Polos y planos en negro.
   - Eigenvectores como estrellas de colores distintos, cada uno con su leyenda y valores numéricos.

## Personalización

- Cambia los colores de los eigenvectores editando la lista `colors` en el script.
- Modifica las etiquetas (`labels`) si prefieres nombres diferentes.
- Ajusta la posición de la leyenda numérica modificando las coordenadas y el argumento `transform` en la función `ax.text()`.
- Para mostrar/ocultar elementos cosméticos, modifica o comenta las líneas correspondientes en el script.


## Créditos

- Script desarrollado con [mplstereonet](https://mplstereonet.readthedocs.io/en/latest/).

---

¿Dudas, sugerencias o mejoras? ¡Abre un issue o contribuye!
