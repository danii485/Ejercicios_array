
cantidadalumnos = 15
cantidadasignaturas = 3

notas = []

for asignatura in range (cantidadasignaturas):
    asignaturas = []
    print(f"Las notas de la asignatura son: {asignatura +1}")


    for alumno in range (cantidadalumnos):
        nota = float(input(f"Nota del alumno:  {alumno + 1}: "))
        asignaturas.append(nota)
    notas.append(asignaturas)

print("\n Las notas ingresadas por cada asignatura son: ")
for i in range(cantidadasignaturas):
    print(f"Asignatura {i +1}: {notas[i]}")

print("\nLa nota media de cada alumno es de : ")
media_alumnos = []
for alumno in range(cantidadalumnos):
    suma_notas = 0
    for asignatura in range(cantidadasignaturas):
        suma_notas += notas[asignatura][alumno]
    media_alumno = suma_notas / cantidadasignaturas
    media_alumnos.append(media_alumno)
print(f"El alumno {alumno + 1}: tuvo la media de:  {media_alumno:.2f}")

print("\nLa nota media de cada asignatura: ")
media_asignaturas = []
for asignatura in range(cantidadasignaturas):
    media_asignatura = sum(notas[asignatura]) /cantidadalumnos
    media_asignaturas.append(media_asignatura)
print(f"Asignatura {asignatura + 1}: {media_asignatura:.2f}")

print("\nLa nota media de la clase: ")
total_clase = 0
for asignatura in range (cantidadasignaturas):
    total_clase += sum(notas[asignatura])
media_clase = total_clase / (cantidadasignaturas* cantidadalumnos)
print(f"Nota media de la clase: {media_clase: .2f}")

def mostrar(notitas):
    for notas in notitas:
        print(notas)
mostrar(notitas)



