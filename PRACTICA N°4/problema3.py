import requests
import zipfile
import os
url_imagen = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
nombre_imagen = "imagen_descargada.jpg"
try:
    print("Iniciando la descarga de la imagen...")
    respuesta = requests.get(url_imagen)
    respuesta.raise_for_status()
    with open(nombre_imagen, 'wb') as archivo_imagen:
        archivo_imagen.write(respuesta.content)
    print("Imagen descargada correctamente.")
except requests.RequestException as e:
    print(f"Se produjo un error al descargar la imagen: {e}")
nombre_zip = "imagen_comprimida.zip"
try:
    with zipfile.ZipFile(nombre_zip, 'w') as archivo_zip:
        archivo_zip.write(nombre_imagen)
    print(f"La imagen ha sido comprimida en el archivo {nombre_zip}.")
except Exception as e:
    print(f"Se produjo un error al comprimir la imagen: {e}")
try:
    with zipfile.ZipFile(nombre_zip, 'r') as archivo_zip:
        archivo_zip.extractall("imagen_extraida")
    print(f"La imagen se ha extraído en la carpeta 'imagen_extraida'.")
except Exception as e:
    print(f"Se produjo un error al descomprimir el archivo: {e}")
