import csv
temperaturas = []
archivo_entrada = 'temperaturas.txt'
archivo_salida = 'resumen_temperaturas.txt'
try:
    with open(archivo_entrada, 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        next(lector_csv)
        for fila in lector_csv:
            try:
                temperatura = float(fila[1])
                temperaturas.append(temperatura)
            except ValueError:
                print(f"Advertencia: No se pudo interpretar la temperatura en la fila: {fila}")
except FileNotFoundError:
    print(f"Error: El archivo {archivo_entrada} no fue encontrado.")
    exit()
if temperaturas:
    temperatura_maxima = max(temperaturas)
    temperatura_minima = min(temperaturas)
    temperatura_promedio = sum(temperaturas) / len(temperaturas)
    try:
        with open(archivo_salida, 'w') as archivo_resumen:
            archivo_resumen.write(f"Temperatura máxima: {temperatura_maxima:.2f}°C\n")
            archivo_resumen.write(f"Temperatura mínima: {temperatura_minima:.2f}°C\n")
            archivo_resumen.write(f"Temperatura promedio: {temperatura_promedio:.2f}°C\n")
        print(f"Resultados guardados en {archivo_salida}")
    except Exception as e:
        print(f"Error al intentar escribir en el archivo: {e}")
else:
    print("No se encontraron registros de temperatura.")
