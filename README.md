# Laboratorio 2 Convolución,correlación y transformación

Este repositorio contiene un script de Python (`main.py`) que realiza diversas operaciones estadisticas de procesamiento de señales: convolución, correlación y análisis de señales fisiológicas, en este caso de una electromiografia.

## Contenido

El script `main.py` realiza las siguientes tareas:

1. **Convolución:**
   - Calcula la convolución entre la señal del código del estudiante (`h[n]`) y la señal de su número de cédula (`x[n]`) para dos estudiantes.
   - Implementa la convolución de forma manual usando sumatorias.
   - Genera gráficos de la señal resultante de la convolución para cada estudiante.

2. **Correlación:**
   - Calcula la correlación cruzada entre dos señales sinusoidales (`x1[n]` y `x2[n]`).
   - Genera un gráfico de la correlación cruzada.
   - Imprime la secuencia de la correlación cruzada.

3. **Análisis de Señal Fisiológica:**
   - Muestra estadísticos descriptivos de la señal en el dominio del tiempo (media, desviación estándar, coeficiente de variación).
   - Muestra un histograma de la señal.
   - Aplica la transformada de Fourier a la señal.
   - Grafica el espectro de magnitud  de la señal.
   - Calcula y muestra estadísticos descriptivos de la señal en el dominio de la frecuencia.

## Uso

1. **Requisitos:**
   - Python 3
   - Librerías: NumPy, Matplotlib, wfdb

   Puedes instalar las librerías usando `pip`:
   ```bash
   pip install numpy matplotlib wfdb
