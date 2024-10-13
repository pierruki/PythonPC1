import os
import csv
import sqlite3
ruta_archivo = os.path.join(os.path.dirname(__file__), 'ventas.csv')
conexion = sqlite3.connect('base.db')
cursor = conexion.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sunat_info (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT,
        compra REAL,
        venta REAL
    )
''')
tipos_cambio = [
    ('2024-10-12', 3.75, 3.85),
    ('2024-10-11', 3.74, 3.84)
]
for fecha, compra, venta in tipos_cambio:
    cursor.execute('''
        INSERT OR IGNORE INTO sunat_info (fecha, compra, venta)
        VALUES (?, ?, ?)
    ''', (fecha, compra, venta))
conexion.commit()
def obtener_tipo_cambio(fecha):
    cursor.execute("SELECT venta FROM sunat_info WHERE fecha = ?", (fecha,))
    resultado = cursor.fetchone()
    if resultado:
        return resultado[0]
    else:
        return None
try:
    with open(ruta_archivo, 'r') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        total_dolares = 0
        total_soles = 0
        for fila in lector_csv:
            producto = fila['producto']
            fecha = fila['fecha']
            precio_usd = float(fila['precio_usd'])
            tipo_cambio = obtener_tipo_cambio(fecha)
            
            if tipo_cambio:

                precio_soles = precio_usd * tipo_cambio
                total_dolares += precio_usd
                total_soles += precio_soles
                print(f"Producto: {producto}, Fecha: {fecha}, Precio en USD: ${precio_usd:.2f}, Precio en soles: S/{precio_soles:.2f}")
            else:
                print(f"No se encontró el tipo de cambio para la fecha {fecha}.")
    print(f"\nTotal en dólares: ${total_dolares:.2f}")
    print(f"Total en soles: S/{total_soles:.2f}")

except FileNotFoundError:
    print(f"Error: No se encontró el archivo {ruta_archivo}")
except Exception as e:
    print(f"Error al procesar el archivo CSV: {e}")
conexion.close()
