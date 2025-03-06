
exponentes = []
valores = []
for i in range(2):
    exponente = int(input(f"Introduce el exponente de la potencia de 2 {i + 1} "))

    if exponente == -1000:
        print("Quieres salir del programa")
    else:
        print("Correcto")

        exponentes.append([exponente])
        valor = 2 ** exponente
        valores.append([valor])

print("Tabla de potencias de 2:")
print("Exponente | Valor")
for i in range(len(exponentes)):
    print(f"{exponentes[i][0]} | {valores[i][0]}")


