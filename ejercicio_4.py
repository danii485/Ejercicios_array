
matriz_n = []

for i in range(4):
    diagonal = []
    for j in range(4):
        """ valor = int(input(f"Introduceel valor para la porsicion {i+1}{i+j}
        diagonal.append(valor)
        matriz.append(fila)
          """
        if i ==j:
            diagonal.append([1])
        else:
            diagonal.append(0)
    matriz_n.append(diagonal)

for fila in matriz_n:
    print(fila)


