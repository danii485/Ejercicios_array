import random

matriz = []
for i in range(5):
    columna=[]
    for j in range(5):
        columna.append(random.randint(0,10))
    matriz.append(columna)

for matrizuno in matriz:
    print(matrizuno)

suma_columnas = [0] *5
for i in range(5):
    suma = sum(matriz[i])
    print(f"La suma de {i + 1} es {suma}")

for j in range(5):
    for i in range(5):
        suma_columnas[j] += matriz[i][j]

print("Suma de las columnas:")
for j in range(5):
    print(f"La suma de la columna {j + 1} es {suma_columnas[j]}")










