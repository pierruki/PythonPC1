# Problema 3: Ingresar números y contar pares e impares
p = 0
i = 0
numeros = []

while True:
    desea_ingresar = input("¿Desea ingresar un número? (SI/NO): ").upper()
    if desea_ingresar == 'NO':
        break
    
    numero = int(input("Ingrese el número: "))
    numeros.append(numero)
    
    if numero % 2 == 0:
        p += 1
    else:
        i+= 1

print(f"Números ingresados: {numeros}")
print(f"Cantidad de números pares: {p}")
print(f"Cantidad de números impares: {i}")