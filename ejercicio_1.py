tabla = []

for i in range(10):
    if i % 2 ==0:
        tabla.append([1] *10)
    else:
        tabla.append([0] *10)

print("Contenido de la matriz:")
for fila in tabla:
    print(fila)
