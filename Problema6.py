# Calcula el precio de la entrada basado en la edad del cliente
edad = int(input("Introduce la edad del cliente: "))

if edad < 4:
    print("La entrada es gratis.")
elif edad <= 18:
    print("El precio de la entrada es $5.")
else:
    print("El precio de la entrada es $10.")
