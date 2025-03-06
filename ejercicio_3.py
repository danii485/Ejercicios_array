import random
filas = 5
columnas = 3

matriz = []

for i in range(columnas):
    columnas = []
    for j in range(filas):
        columnas.append(random.randint(0,40))
    matriz.append(columnas)

print("Matriz orginal: ")
for columnas in matriz:
    print(columnas)

def transponer(matriz2):
    columna = len(matriz2)
    fila =len(matriz[0])
    matriztransponer = []

    for j in range(fila):
        columnanueva = []
        for i in range(columna):
            columnanueva.append(matriz[i][j])
        matriztransponer.append(columnanueva)
    return matriztransponer

matriztransponer = transponer(matriz)

print("\nMatriz transponer")
for columna in matriztransponer:
    print(columna)


