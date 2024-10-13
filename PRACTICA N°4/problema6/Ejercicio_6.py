import os
def contar_lineas_codigo(ruta_archivo):
    print(f"Ruta del archivo proporcionada: {ruta_archivo}")
    if not os.path.exists(ruta_archivo):
        print(f"Error: El archivo {ruta_archivo} no se encontró.")
        return
    if not ruta_archivo.endswith('.py'):
        print("Error: El archivo no es un archivo Python (.py).")
        return
    try:
        with open(ruta_archivo, 'r') as archivo:
            lineas = archivo.readlines()
        lineas_codigo = 0
        for linea in lineas:
            linea_limpia = linea.strip()
            if linea_limpia and not linea_limpia.startswith("#"):
                lineas_codigo += 1
        print(f"Número de líneas de código en {ruta_archivo}: {lineas_codigo}")
    except Exception as e:
        print(f"Hubo un error al leer el archivo: {e}")
ruta_archivo = input("Escriba la ruta del archivo .py: ")
contar_lineas_codigo(ruta_archivo)
