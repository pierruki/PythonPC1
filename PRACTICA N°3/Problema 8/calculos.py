import Operaciones

def desplegar_opciones():
    print("\nOpciones disponibles:")
    print("1. Realizar suma")
    print("2. Realizar resta")
    print("3. Realizar multiplicación")
    print("4. Realizar división")
    print("5. Terminar programa")

def obtener_numeros():
    try:
        num1 = float(input("Por favor, introduzca el primer número: "))
        num2 = float(input("Por favor, introduzca el segundo número: "))
        return num1, num2
    except ValueError:
        print("Error: Ingrese solo números válidos.")
        return obtener_numeros()  # Repetir solicitud si ocurre un error

if __name__ == "__main__":
    while True:
        desplegar_opciones()
        eleccion = input("\nElija una opción: ")
        
        if eleccion == "1":
            num1, num2 = obtener_numeros()
            resultado = Operaciones.agregar(num1, num2)
            print(f"Resultado de la suma: {resultado}")
        
        elif eleccion == "2":
            num1, num2 = obtener_numeros()
            resultado = Operaciones.restar(num1, num2)
            print(f"Resultado de la resta: {resultado}")
        
        elif eleccion == "3":
            num1, num2 = obtener_numeros()
            resultado = Operaciones.multiplicar(num1, num2)
            print(f"Resultado de la multiplicación: {resultado}")
        
        elif eleccion == "4":
            num1, num2 = obtener_numeros()
            resultado = Operaciones.dividir(num1, num2)
            print(f"Resultado de la división: {resultado}")
        
        elif eleccion == "5":
            print("Cerrando el programa...")
            break
        
        else:
            print("Selección no válida. Por favor, intente de nuevo.")
