lista = []

for i in range(10):
    elemento = int(input(f"Introduce el elemento:  { i +1 }"))
    lista.append(elemento)

    maximo_elem = max(lista)
    contador = lista.count(maximo_elem)

    print(f"El maximo de elementos es : {maximo_elem}")
    print(f"Se repite : {contador} veces")