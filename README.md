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

## Definicion de Datos

``` python
estudiantes = 
{
    "Estudiante 1": {"codigo": [5, 6, 0, 0, 5, 8, 8], "cedula": [1, 0, 0, 6, 8, 7, 8, 1, 4, 8]},
    "Estudiante 2": {"codigo": [5, 6, 0, 0, 7, 4, 2], "cedula": [1, 0, 1, 9, 9, 0, 2, 6, 8, 4]}
}

``` 

- Se crea un diccionario llamado estudiantes.

 - Cada estudiante tiene dos listas de datos:

  **codigo:** Representa una serie de números utilizados en la convolución.

  **cedula:** Son los valores con los que se aplicará la operación de convolución.


## **Funcion para contar elementos** 

```python
def contar_elementos(lista):
    contador = 0
    for _ in lista:
        contador += 1
    return contador
```
- *Esta función cuenta manualmente la cantidad de elementos en una lista.*

 - *Se usa un contador que aumenta con cada elemento recorrido en el ciclo **for**.*


## **Convolucion de manera manual**

en los comentarios de el codigo se explica mejor que significa cada parte de linea del codigo para un mejor entendimiento

*La convolución es una operación matemática utilizada en procesamiento de señales para analizar cómo una señal de entrada interactúa con otra.*

```python
def convolucion_manual(x, h):
    Lx = contar_elementos(x)  # Obtiene la cantidad de elementos en la señal x
    Lh = contar_elementos(h)  # Obtiene la cantidad de elementos en la señal h
    Ly = Lx + Lh - 1  # Longitud de la señal de salida después de la convolución
    resultado = np.zeros(Ly)  # Inicializa la lista de salida con ceros
    
    for n in range(Ly):  # Recorre cada posición de la señal resultante
        suma = 0  # Inicializa la variable suma para cada punto de la señal resultante
        for k in range(Lh):  # Recorre los valores de h para multiplicarlos con los valores de x
            if 0 <= n - k < Lx:  # Asegura que el índice n-k esté dentro del rango de la señal x
                suma += h[k] * x[n - k]  # Multiplica y suma los valores correspondientes
        resultado[n] = suma  # Guarda el resultado en la posición correspondiente
    return resultado
```

- **Lx** y **Lh**   representan las longitudes de las señales de entrada
- **Ly**    es la longitud de la señal de salida, calculada como la suma de las longitudes de las señales de entrada menos 1.
- **np.zeros(Ly):**     Crea un arreglo de ceros para almacenar los resultados de la convolución.
- **for n in range(Ly):**    se mueve por  cada punto de la señal nueva.
- **for k in range(Lh):**  Recorre la señal h y multiplica sus valores con la señal x desplazada.
- **suma += h[k] * x[n - k]:**   Calcula la suma ponderada de los productos de h y x

## Aplicacion de la Convolusion y Grafica

*Utilizando las funciones de la libreria de matplotlib nombrada como (plt) se utiliza para crear graficos

```python
for nombre, datos in estudiantes.items():
    h = datos["codigo"]  # Obtiene la lista de códigos del estudiante
    x = datos["cedula"]  # Obtiene la lista de cédula del estudiante
    y = convolucion_manual(x, h)  # Aplica la convolución entre la cédula y el código

    plt.figure(figsize=(10, 4))
    plt.stem(y)  # Dibuja el resultado de la convolución en una gráfica
    plt.title(f'Convolución de {nombre}')
    plt.xlabel('n')
    plt.ylabel('y[n]')
    plt.grid()
    plt.show()
```
- Se revisa cada estudiante en el diccionario estudiantes.

- Se obtiene la cédula **(x)** y el código **(h)** de cada estudiante.

- Se aplica la convolución utilizando **convolucion_manual().**

- Se muestra el resultado usando **plt.stem()**, que es una forma de graficar señales discretas con líneas verticales.

### **Grafica 1**
  ![](https://github.com/Daniel-Herrera-1/Laboratorio2-Convolucion-correlacion-y-transformacion/blob/main/Imagenes/Convo1.jpeg)

### **Grafica 2**

![](https://github.com/Daniel-Herrera-1/Laboratorio2-Convolucion-correlacion-y-transformacion/blob/main/Imagenes/Convo2.jpeg)




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
