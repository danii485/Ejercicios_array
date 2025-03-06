from random import random as r, randint


cuadrada = [[1,2,3,4,5,6][7,8,9,10,11,12]]


for i in range(len(cuadrada)):
    cuadrada.append([i])
    for j in range(len(cuadrada)):
        cuadrada[i].append(cuadrada[i][j])

for fila in cuadrada:
    print(fila)