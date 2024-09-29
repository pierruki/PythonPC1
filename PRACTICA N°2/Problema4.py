# Problema 4: Registro de alumnos y calificaciones
alum = []
x = int(input("indique la cantidad de alumnos a ingresar: "))
for i in range(x):
        alumno = {}
        nombre = input(f"Indique el nombre del alumno {i+1}: ")
        notas = [int(input(f"Ingrese la calificación {j+1} del alumno {nombre}: ")) for j in range(3)]
        alumno["Alumno"] = nombre
        alumno["Notas"] = notas
        alum.append(alumno)

print("\nAlumnos y sus calificaciones:")
for alumno in alum:
    print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")