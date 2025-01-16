sumapar = 0
sumaimpar = 0
vector = []
for i in range(10):
    numero = int(input("Introduce un número"))
    vector.append(numero)

for i in range(len(vector)):
    if i % 2 == 0:
        sumapar += vector[i]
    else:
        sumaimpar += vector[i]

print(f"la media de las posiciones pares del vector son {sumapar/len(vector)} y la media de los impartes es {sumaimpar/len(vector)}")