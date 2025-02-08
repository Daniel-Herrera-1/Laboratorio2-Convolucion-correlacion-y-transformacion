import numpy as np
import matplotlib.pyplot as plt

# Datos  estudiantes
estudiantes = {
    "Estudiante 1": {"codigo": [5,6,0,0,5,8,8], "cedula": [1,0,0,6,8,7,8,1,4,8]},
    "Estudiante 2": {"codigo": [5,6,0,0,7,4,2], "cedula": [1,0,1,9,9,0,2,6,8,4]}
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
