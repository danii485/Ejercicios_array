import random as a

lista = []
contador = lista.count(lista)
for i in range(10):
    lista.append(a.randint(0,10))
    if lista[i] % 2 == 0:
        print(f"El numero es par {lista[i]} y pertenece en la posicion { i }")
    else:
        print("No es par")