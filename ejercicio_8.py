import random

array_numeros = []
for i in range(10):
    array_numeros.append([])
    for j in range(15):
        array_numeros[i].append(random.randint(0,10))

print("Array bidimensional númerico: ")
for fila in array_numeros:
    print(fila)

suma_de_filas =[]
for fila in array_numeros:
    suma_de_filas.append(sum(fila))

print("Suma de las filas: ")
print(suma_de_filas)