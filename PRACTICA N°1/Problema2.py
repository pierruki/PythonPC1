# Solicita el monto del consumo y el porcentaje de propina, luego calcula la propina
consumo = float(input("¿Cuánto fue su consumo en el restaurante? "))
porcentaje_propina = float(input("¿Qué porcentaje de propina desea dejar? "))
propina = consumo * (porcentaje_propina / 100)
print(f"La propina a dejar es: {propina}")