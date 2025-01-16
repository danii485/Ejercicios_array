alumnos = int(input("Introduce el numero de alumnos"))
estaturas = []
suma = 0
contador1 = 0
contador2 = 0
for i in range(alumnos):
    estatura = int(input(f"Dime la estatura de cada alumno {i + 1}"))
    estaturas.append(estatura)
    suma += estaturas[i]

media = suma/alumnos
for j in range(alumnos):
    if estaturas[j]>=media:
        contador1 +=1
    else:
        contador2 +=1

print(f"La media de la estatura es : {suma/len(estaturas)}")
print(f"El mas alto de la media es {contador1} y la media es {media}")
print(f"El mas bajo de la media es {contador2} y la media es {media} ")
