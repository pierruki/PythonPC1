# Calcula el peso total de los payasos y muñecas vendidos
peso_payaso = 112  # gramos
peso_muneca = 75  # gramos

payasos_vendidos = int(input("Introduce el número de payasos vendidos: "))
munecas_vendidas = int(input("Introduce el número de muñecas vendidas: "))

peso_total = (payasos_vendidos * peso_payaso) + (munecas_vendidas * peso_muneca)
print(f"El peso total del paquete es: {peso_total} gramos")
