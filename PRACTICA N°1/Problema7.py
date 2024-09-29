# Calculadora básica con menú
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

print("Elige una opción:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")

opcion = int(input("Introduce una opción: "))

if opcion == 1:
    print(f"La suma es: {num1 + num2}")
elif opcion == 2:
    print(f"La resta es: {num1 - num2}")
elif opcion == 3:
    print(f"La multiplicación es: {num1 * num2}")
else:
    print("Opción no válida")
