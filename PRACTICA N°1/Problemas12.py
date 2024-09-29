nombre = input("introduzca el nombre del archivo: ").lower()

tipos = {
    
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

for sufijo, mime in tipos.items():
    
    if nombre.endswith(sufijo):
        
        break

else:
    mime = "application/octet-stream"

print(f"El tipo MIME introducido es: {mime}")