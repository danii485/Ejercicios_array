
clases = 3
alumnos = 30

notas = []
for i in range(clases):
    notas.append([0]* alumnos)

for i in range(clases):
    print(f"Las notas para la clase : {i + 1}")
    for j in range(alumnos):
        notas[i][j]= float(input(f"Nota del alumno {j +1} "))

print("\nNotas ingresadas:")
for i in range(clases):
    print(f"clase {i+1}:{notas[i]}")

for i in range(clases):
    max_clase = max(notas[i])  # Nota máxima en la clase i
    min_clase = min(notas[i])  # Nota mínima en la clase i
    print(f"Clase {i + 1} - Nota máxima: {max_clase}, Nota mínima: {min_clase}")

for j in range(alumnos):

    notas_alumno = []
    for i in range(clases):
        notas_alumno.append(notas)
    max_alumno = max(notas_alumno)
    min_alumno = min(notas_alumno)
    print(f"Alumno {j + 1} - Nota máxima: {max_alumno}, Nota mínima: {min_alumno}")

todas_las_notas =[]
for clase in notas:
    for nota in clase:
        todas_las_notas.append(nota)

maximo_notas = max(todas_las_notas)
minimo_notas = min(todas_las_notas)

print(f"Nota máxima: {maximo_notas}")
print(f"Nota mínima: {minimo_notas}")




