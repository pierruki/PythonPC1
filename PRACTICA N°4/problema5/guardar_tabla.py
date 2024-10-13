def guardar_tabla_multiplicar(n):
    nombre_archivo = f"tabla-{n}.txt"
    try:
        with open(nombre_archivo, 'w') as archivo:
            for i in range(1, 11):
                archivo.write(f"{n} x {i} = {n * i}\n")
        print(f"Tabla de multiplicar del {n} guardada en {nombre_archivo}.")
    
    except Exception as e:
        print(f"Error al guardar la tabla: {e}")
try:
    numero = int(input("Ingrese un número entre 1 y 10: "))
    if 1 <= numero <= 10:
        guardar_tabla_multiplicar(numero)
    else:
        print("Por favor, ingrese un número válido entre 1 y 10.")
except ValueError:
    print("Error: Debe ingresar un número entero.")
