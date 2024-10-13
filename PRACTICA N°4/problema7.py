import requests
import sqlite3
from datetime import datetime
url_sunat = "https://api.apis.net.pe/v1/tipo-cambio-sunat"
try:
    response = requests.get(url_sunat)
    response.raise_for_status()
    tipo_cambio_data = response.json()
    fecha = tipo_cambio_data['fecha']
    compra = tipo_cambio_data['compra']
    venta = tipo_cambio_data['venta']
    print(f"Fecha: {fecha}, Compra: {compra}, Venta: {venta}")
except requests.RequestException as e:
    print(f"Error al obtener los datos de la API: {e}")
    exit()
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
try:
    cursor.execute('''
        INSERT INTO sunat_info (fecha, compra, venta)
        VALUES (?, ?, ?)
    ''', (fecha, compra, venta))
    conexion.commit()
    print("Datos almacenados en la base de datos.")
except sqlite3.Error as e:
    print(f"Error al guardar los datos en la base de datos: {e}")
    conexion.rollback()
try:
    cursor.execute('SELECT * FROM sunat_info')
    filas = cursor.fetchall()

    print("\nContenido de la tabla sunat_info:")
    for fila in filas:
        print(f"ID: {fila[0]}, Fecha: {fila[1]}, Compra: {fila[2]}, Venta: {fila[3]}")
except sqlite3.Error as e:
    print(f"Error al leer los datos de la base de datos: {e}")
conexion.close()
