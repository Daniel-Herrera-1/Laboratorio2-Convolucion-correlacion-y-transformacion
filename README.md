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
![image](https://github.com/user-attachments/assets/44deb2df-cb75-4a13-9f0b-d84c6b899745)


### **Grafica 2**

![image](https://github.com/user-attachments/assets/e0d15272-3628-4b4b-82d7-4484ab4471f7)



## Correlación Cruzada entre Señales

```python
ts = 1.25e-3  # Intervalo de muestreo en segundos
ns = 9  # Número total de muestras

n = np.arange(ns)  # Crea una lista con valores de 0 a ns-1
x1 = np.cos(2 * np.pi * n * 100 * ts)  # Señal coseno con frecuencia de 100 Hz
x2 = np.sin(2 * np.pi * n * 100 * ts)  # Señal seno con frecuencia de 100 Hz
m = np.arange(-ns+1, ns)  # Rango de desplazamiento para la correlación
RX1X2 = np.correlate(x1, x2, mode='full')  # Calcula la correlación cruzada
````
- **ts** es el período de muestreo, es decir, cada cuánto se toma una muestra.

- **n = np.arange(ns):** Crea una lista con valores de 0 a ns-1.

- **x1 = np.cos(2 * np.pi * n * 100 * ts):** Genera una señal de coseno con frecuencia de 100 Hz.

- **x2 = np.sin(2 * np.pi * n * 100 * ts):** Genera una señal de seno con la misma frecuencia.

- **np.correlate(x1, x2, mode='full'):** Calcula la correlación cruzada entre **x1** y **x2**, comparando cuánto se parecen las señales al desplazarlas en el tiempo.

```python
print("Relacion secuencial de la correlacion cruzada:")
for i, val in enumerate(RX1X2):
    print(f"RX1X2[{m[i]}] = {val:.3f}")
```

- Se imprimen los valores de la correlación cruzada de manera ordenada.

- **for i, val in enumerate(RX1X2):** Se recorre cada valor en RX1X2 y se muestra junto con su desplazamiento correspondiente m[i].

- **print(f"RX1X2[{m[i]}] = {val:.3f}"):** Muestra los valores con tres decimales para mayor claridad

  
## Grafico de Correlacion Cruzada
*Usando las funciones de matplotlib se grafica*

```python
plt.figure(figsize=(10, 6))
plt.stem(m, RX1X2)
plt.xlabel('Desplazamiento (m)')
plt.ylabel('Correlación Cruzada (Rx1x2[m])')
plt.title('Correlación Cruzada entre x1[n] y x2[n]')
plt.grid(True)
plt.show()
```
![image](https://github.com/user-attachments/assets/6add12de-b49b-4cae-86f9-bff03b7f7715)


## Análisis de una Señal Biomédica desde PhysioNet 

*En este caso se esta usando una señal de electromiografia*

```python
record = wfdb.rdrecord('S01')  # Carga una señal desde un archivo en PhysioNet
print("Estadísticos descriptivos")
print(record.__dict__)
```

- wfdb.rdrecord('S01'): Carga la señal desde un archivo en PhysioNet, identificado como 'S01'.

- El archivo contiene datos biomédicos, como señales de electrocardiogramas u otras mediciones fisiológicas.
- record.__dict__: Muestra toda la información contenida en la señal, como la frecuencia de muestreo, duración y otros detalles.

## **Siguiente parte**

```python
original_signal = record.p_signal[:,0]  # Extrae la primera señal del archivo
fs = record.fs  # Obtiene la frecuencia de muestreo
num_muestras_60s = fs * 60  # Calcula cuántas muestras hay en 60 segundos
time_60s = np.arange(num_muestras_60s) / fs  # Crea un vector de tiempo para los primeros 60 segundos

plt.figure(figsize=(12,4))
plt.plot(time_60s, original_signal[:num_muestras_60s], label='señal original')
plt.grid()
plt.title('Señal fisiológica (s01)')
plt.xlabel('Tiempo[s]')
plt.ylabel('Amplitud[mV]')
```
- **record.p_signal[:,0]:** Extrae la primera señal del archivo, ya que puede haber múltiples canales de datos.

- **record.fs:** Obtiene la frecuencia de muestreo, que indica cuántas mediciones por segundo se registraron.

- **num_muestras_60s = fs * 60:** Calcula la cantidad de muestras que hay en los primeros 60 segundos de la señal.

- **np.arange(num_muestras_60s) / fs:** Crea una lista de valores de tiempo, que representa los primeros 60 segundos de la señal.

- Se grafica la señal original en los primeros 60 segundos.

- **plt.plot(time_60s, original_signal[:num_muestras_60s]):** Dibuja la señal en función del tiempo.

- Se agregan etiquetas a los ejes y título al gráfico para mejor interpretación

  ![image](https://github.com/user-attachments/assets/b83a5d7f-ac77-4518-bd55-cdf56312aa2c)

## **Historigrama**

```python
num_muestras_60s = fs * 60
time_60s = np.arange(num_muestras_60s)/fs  # Solo se toman los primeros 60 segundos ( Se puede cambiar el valor del tiempo)

contador = 0
for x in time_60s:
        contador += 1
n = contador  # Almacena el número total de muestras

sum_signal = sum(original_signal)
mean_signal = sum_signal / n  # Calcula la media de la señal

suma_cuadrados_diferencias = sum((x - mean_signal) ** 2 for x in original_signal)
varianza = suma_cuadrados_diferencias / (n-1)  # Calcula la varianza de la señal
std_signal = varianza ** 0.5  # Calcula la desviación estándar de la señal
cv_signal = std_signal / mean_signal  # Calcula el coeficiente de variación

Media:491090.0863371477
Desviación estándar: 2626379.3668135363
Coeficiente de variación: 5.348060243697223

```
*Explicacion en orden*

- Se cuenta cuántos valores hay en time_10s para obtener la cantidad total de muestras en 10 segundos.
- Se calcula la media de la señal sumando todos sus valores y dividiendo entre la cantidad total de muestras n.
- Se calcula la varianza, la desviación estándar y el coeficiente de variación de la señal.

## **Luego se grafica el Histograma con las funciones de matplotlib como los anteriores graficas**

![image](https://github.com/user-attachments/assets/2fd58951-d063-466e-9d81-042a327d2b18)


## **Transformada de Fourier y Espectro de Frecuencia**

```python
transformada_senal = np.fft.fft(time_60s)
frecuencias = np.fft.fftfreq(n, d=1/fs)
```
- **np.fft.fft(time_60s):** Aplica la Transformada Rápida de Fourier (FFT) a la señal en el dominio del tiempo para convertirla al dominio de la frecuencia.

- **np.fft.fftfreq(n, d=1/fs):** Calcula las frecuencias asociadas a la transformada, donde n es el número total de muestras y fs es la frecuencia de muestreo.

### Cálculo del espectro usando FFT
```python
frequencies = np.fft.fftfreq(len(time_60s), 1/fs)
spectrum = np.fft.fft(original_signal)
magnitude = np.abs(spectrum)[:len(frequencies)//2]  # Magnitud del espectro
```

- **np.fft.fft(original_signal):** Calcula la FFT de la señal original para obtener su contenido en frecuencia.

- **np.abs(spectrum)[:len(frequencies)//2]:** Obtiene la magnitud del espectro y solo se considera la mitad de los valores, ya que la FFT es simétrica para señales reales.

## Grafica del espectro de la señal

![image](https://github.com/user-attachments/assets/22e3cbad-0082-48c8-9066-68d210aff442)

## Grafica del espectro de la señal normalizado

 Cálculo del espectro usando FFT NORMALIZADO
```python
N = len(time_60s)  # Número de muestras
frequencies = np.fft.fftfreq(N, 1/fs)
spectrum = np.fft.fft(original_signal) / N  # Normalización por el número de muestras
magnitude = 2 * np.abs(spectrum[:N//2])  # Se toma la mitad del espectro y se ajusta la amplitud
```
- **N = len(time_60s):** Calcula el número total de muestras de la señal.

- **np.fft.fft(original_signal) / N:** Normaliza la FFT dividiendo por el número de muestras para obtener valores más representativos.

- **2 * np.abs(spectrum[:N//2]):** Multiplica por 2 para compensar la pérdida de información en la parte negativa del espectro y toma solo la mitad del espectro positivo.

  ![image](https://github.com/user-attachments/assets/117a8da3-3283-47b3-bb90-cc6761a94c41)

  ## **Grafica del espectro de la magnitud**
```python
  transformada_senal = np.fft.fft(time_60s)
frecuencias = np.fft.fftfreq(n, d=1/fs)
plt.figure(figsize=(10, 6))  # Ajustar el tamaño de la figura (opcional)
plt.plot(frecuencias, np.abs(transformada_senal))
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.title('Espectro de Magnitud de la Señal')
plt.grid()
plt.show()
```
- **np.abs(transformada_senal): Toma el valor absoluto de la transformada para obtener la magnitud de cada componente de frecuencia.**

## **Se grafica el espectro de magnitud para visualizar la distribución de las frecuencias en la señal.**

![image](https://github.com/user-attachments/assets/5d62f92f-4627-497c-aa39-e2d19d93e02f)


## Calculo de la densidad espectral de potencia y calculos 

```python
psd = np.abs(spectrum)**2 / N

plt.figure(figsize=(10, 6))
plt.plot(frequencies[:N//2], psd[:N//2])
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Densidad espectral de potencia')
plt.title('Densidad espectral de la señal de EMG')
plt.grid()
plt.show()
````

- np.abs(spectrum)**2 / N: Calcula la densidad espectral de potencia (PSD), que muestra cómo se distribuye la energía de la señal en el dominio de la frecuencia.
- Se grafica la densidad espectral de potencia (PSD) para analizar la distribución de energía en función de la frecuencia.
- Se usa plt.plot(frequencies[:N//2], psd[:N//2]) para mostrar solo la mitad del espectro, ya que para señales reales, la PSD es simétrica.

  ![image](https://github.com/user-attachments/assets/9d8e3507-190c-4ec8-8602-1e315130be5e)

  ## **Calculos estadisticos**

  
```python
  sum_senal = 0
for x in transformada_senal:
    sum_senal += x
mean_senal = sum_senal / n  # Media de la señal en el dominio de la frecuencia

suma_cuadrados_diferencias = 0
for x in transformada_senal:
    suma_cuadrados_diferencias += (x - mean_senal) ** 2
varianza = suma_cuadrados_diferencias / (n-1)  # Cálculo de la varianza
std_senal = varianza ** 0.5  # Desviación estándar de la señal en frecuencia
cv_senal = std_senal / mean_senal  # Coeficiente de variación
```

- Se calcula la varianza sumando los cuadrados de las diferencias entre cada valor y la media.

- La desviación estándar se obtiene tomando la raíz cuadrada de la varianza.

- El coeficiente de variación (cv_senal) es la relación entre la desviación estándar y la media, lo que indica la dispersión relativa de la señal en frecuencia.

## **Mostrar los valores estadisticos obtenidos con print**

 ```python 
print("\n")
print(f"Media en frecuencia: {mean_senal}")
print(f"Desviación estándar en frecuencia: {std_senal}")
print(f"Coeficiente de variación en frecuencia: {cv_senal}")

Media en frecuencia:(-2938.924852566685+2.64681875705719e-10j)
Desviación estándar en frecuencia: (67612011.25495158-3.580164213609727e-09j)
Coeficiente de variación en frecuencia: (-23005.69584006315-2.070692810445543e-09j)

````


## Licencia Universidad Militar Nueva Granada https://physionet.org/content/cudb/1.0.0/

**est.daniela.herreraa@unimilitar.edu.co**
**est.juan.ortiz4@unimilitar.edu.co**




