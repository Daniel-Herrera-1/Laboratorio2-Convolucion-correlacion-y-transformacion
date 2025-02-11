# Laboratorio 2 Convolución,correlación y transformación

### Este repositorio contiene un script de Python (`main.py`) que realiza diversas operaciones estadisticas de procesamiento de señales: convolución, correlación y análisis de señales fisiológicas, en este caso de una electromiografia.
## Objetivos
● Reconocer la convolución como una operación entre señal y sistema

● Reconocer la correlación como una operación entre señales

● Reconocer la transformada como herramienta de análisis en el dominio de lafrecuencia.

## Requisitos

Para ejecutar este código en tu computadora, necesitas instalar lo siguiente:

- Python 3.x (versión recomendada 3.9 o superior)
  
- Bibliotecas:
```
   wfdb: Para leer archivos de PhysioNet.

    matplotlib: Para crear gráficos.

    numpy: Para realizar operaciones numéricas.
```
  - Datos de PhysioNet: Para el análisis de señales,  descarga una señal desde PhysioNet (electromiografia) .

# Procedimiento

# *1. Instalacion librerias y Explicacion del codigo*

Para instalar las librerias copia lo siguiente en la terminal 

``` python
pip install numpy matplotlib wfdb
```
## Crear un archivo en python con las siguiente lineas para el uso de las librerias
``` python
 import numpy as np  # Para cálculos matemáticos y manipulación de matrices
import matplotlib.pyplot as plt  # Para graficar los resultados
import wfdb  # Para leer señales desde PhysioNet
```
- **numpy (np):** Biblioteca utilizada para trabajar con arreglos de números y realizar cálculos matemáticos avanzados de manera eficiente.

- **matplotlib.pyplot (plt):** Herramienta para generar gráficos que permiten visualizar datos de forma clara.

- **wfdb:** Biblioteca utilizada para leer y procesar señales fisiológicas desde PhysioNet.

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
