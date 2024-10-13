import os
def leer_tabla_multiplicar(n):
    nombre_archivo = f"tabla-{n}.txt"
    if os.path.exists(nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as archivo:
                print(f"Mostrando la tabla de multiplicar del {n}:")
                print(archivo.read())
        except Exception as e:
            print(f"Hubo un error al intentar leer el archivo: {e}")
    else:
        print(f"No se encontró el archivo {nombre_archivo}.")
try:
    numero = int(input("Escriba un número entre 1 y 10: "))
    if 1 <= numero <= 10:
        leer_tabla_multiplicar(numero)
    else:
        print("Por favor, ingrese un número válido entre 1 y 10.")
except ValueError:
    print("Error: Debe ingresar un número entero.")
