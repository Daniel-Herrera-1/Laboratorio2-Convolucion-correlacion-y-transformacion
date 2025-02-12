import numpy as np
import matplotlib.pyplot as plt

# Datos  estudiantes
estudiantes = {
    "Estudiante 1": {"codigo": [5, 6, 0, 0, 5, 8, 8], "cedula": [1, 0, 0, 6, 8, 7, 8, 1, 4, 8]},
    "Estudiante 2": {"codigo": [5, 6, 0, 0, 7, 4, 2], "cedula": [1, 0, 1, 9, 9, 0, 2, 6, 8, 4]}
}


# Función para contar elementos
def contar_elementos(lista):
    contador = 0
    for _ in lista:
        contador += 1
    return contador


# Punto (a): Convolución entre h[n] y x[n]
def convolucion_manual(x, h):
    Lx = contar_elementos(x)
    Lh = contar_elementos(h)
    Ly = Lx + Lh - 1
    resultado = np.zeros(Ly)
    for n in range(Ly):
        suma = 0
        for k in range(Lh):
            if 0 <= n - k < Lx:
                suma += h[k] * x[n - k]
        resultado[n] = suma
    return resultado


# Aplicar convolución a los datos

for nombre, datos in estudiantes.items():
    h = datos["codigo"]
    x = datos["cedula"]
    y = convolucion_manual(x, h)

    plt.figure(figsize=(10, 4))
    plt.stem(y)
    plt.title(f'Convolución de {nombre}')
    plt.xlabel('n')
    plt.ylabel('y[n]')
    plt.grid()
    plt.show()


# PUNTO B: Sean X1[𝑛𝑇𝑠] = cos(2𝜋100𝑛𝑇𝑠)    𝑝𝑎𝑟𝑎 0 ≤ 𝑛 < 9, y X2[𝑛𝑇𝑠] = sin(2𝜋100𝑛𝑇𝑠)    𝑝𝑎𝑟𝑎 0 ≤ 𝑛 <  9 𝑝𝑎𝑟𝑎 𝑇𝑠 = 1.25𝑚𝑠.  Encuentre la correlación entre ambas señales. Además, encuentre la representación gráfica y secuencial.
ts = 1.25e-3
ns = 9

n = np.arange(ns)
x1 = np.cos(2*np.pi*n*100*ts)
x2 = np.sin(2*np.pi*n*100*ts)
m = np.arange(-ns+1, ns)
RX1X2 = np.correlate(x1, x2, mode='full')


plt.figure(figsize=(10, 6))
plt.stem(m, RX1X2)
plt.xlabel('Desplazamiento (m)')
plt.ylabel('Correlación Cruzada (Rx1x2[m])')
plt.title('Correlación Cruzada entre x1[n] y x2[n]')
plt.grid(True)
plt.show()

print("Relacion secuencial de la correlacion cruzada:")
for i, val in enumerate(RX1X2):
    print(f"RX1X2[{m[i]}] = {val:.3f}")


# señal en physionet :Caracterice la señal en función del tiempo, esto es, calcule sus  estadísticos descriptivos, frecuencia de muestreo, etc.
# ii. Describa la señal en cuanto a su clasificación.
# iii. Aplique la transformada de Fourier de la señal y grafique tanto  su transformada, como su densidad espectral.
# iv. Analice los estadísticos descriptivos en función de la
# frecuencia:   • Frecuencia media, • Frecuencia mediana, • Desviación estándar, • Histograma de frecuencias

import wfdb
record = wfdb.rdrecord('S01')

print("Información del registro")
print(record.__dict__)
original_signal = record.p_signal[:,0] #asumiendo que es un canal único
fs = record.fs #frecuencia de muestreo
num_muestras_60s = fs*60
time_60s = np.arange(num_muestras_60s)/fs #solo se toman los 60 primeros segundos
#time = np.arange(len(original_signal))/fs  #eje de tiempo

plt.figure(figsize=(12,4))
plt.plot(time_60s, original_signal[:num_muestras_60s], label='señal original')
plt.grid()
plt.title('señal fisiologica (cu01)')
plt.xlabel('Tiempo[s]')
plt.ylabel('Amplitud[mV]')


print("Estadisticos descriptivos")
print(record.__dict__)
original_signal = record.p_signal[:,0] #canal único
fs = record.fs
num_muestras_10s = fs*10
time_10s = np.arange(num_muestras_10s)/fs #solo se toman los 10 primeros segundos
#def contador_len(time_10s):
contador = 0

for x in time_10s:
        contador += 1

n = contador

sum_signal = 0
for x in original_signal:
    sum_signal += x
mean_signal = sum_signal / n
suma_cuadrados_diferencias = 0
for x in original_signal:
    suma_cuadrados_diferencias +=(x-mean_signal)**2
varianza = suma_cuadrados_diferencias / (n-1)
std_signal = varianza**0.5
cv_signal = std_signal / mean_signal

plt.figure(figsize=(8, 5))
plt.hist(original_signal, bins=20, alpha=0.7, color='blue', edgecolor='black')
plt.title('Histograma de la señal')
plt.xlabel('Valor de la señal')
plt.ylabel('Frecuencia')
plt.grid()
plt.show()

print("\n")
print(f"Media:{mean_signal}")
print(f"Desviación estándar: {std_signal}")
print(f"Coeficiente de variación: {cv_signal}")



transformada_senal = np.fft.fft(time_60s)

frecuencias = np.fft.fftfreq(n, d=1/fs)

# Cálculo del espectro usando FFT
frequencies = np.fft.fftfreq(len(time_60s), 1/fs)
spectrum = np.fft.fft(original_signal)
magnitude = np.abs(spectrum)[:len(frequencies)//2]  # Magnitud del espectro

# Gráfica del espectro
plt.plot(frequencies[:len(frequencies)//2], magnitude)
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.title('Espectro de la señal')
plt.grid()
plt.show()

# Cálculo del espectro usando FFT NORMALIZADO
N = len(time_60s)  # Número de muestras
frequencies = np.fft.fftfreq(N, 1/fs)
spectrum = np.fft.fft(original_signal) / N  # Normalización por el número de muestras
magnitude = 2 * np.abs(spectrum[:N//2])  # Se toma la mitad del espectro y se ajusta la amplitud

# Gráfica del espectro
plt.plot(frequencies[:N//2], magnitude)
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.title('Espectro de la señal normalizado')
plt.grid()
plt.show()

# 4. Graficar el espectro de magnitud
# Tomamos el valor absoluto de la transformada para obtener la magnitud de cada componente.

plt.figure(figsize=(10, 6))  # Ajustar el tamaño de la figura (opcional)
plt.plot(frecuencias, np.abs(transformada_senal))
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.title('Espectro de Magnitud de la Señal')
plt.grid()
plt.show()

# Calcular la densidad espectral de potencia



sum_senal = 0
for x in transformada_senal:
    sum_senal += x
mean_senal = sum_senal / n
suma_cuadrados_diferencias = 0
for x in transformada_senal:
    suma_cuadrados_diferencias +=(x-mean_senal)**2
varianza = suma_cuadrados_diferencias / (n-1)
std_senal = varianza**0.5
cv_senal = std_senal / mean_senal

print("\n")
print(f"Media en frecuencia:{mean_senal}")
print(f"Desviación estándar en frecuencia: {std_senal}")
print(f"Coeficiente de variación en frecuencia: {cv_senal}")
