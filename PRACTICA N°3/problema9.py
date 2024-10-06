import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * (self.radio ** 2)

class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def calcular_area(self):
        return self.largo * self.ancho

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un rectángulo")
    print("3. Calcular el área de un cuadrado")
    print("4. Salir")

def ingresar_numero_positivo(mensaje):
    try:
        valor = float(input(mensaje))
        if valor <= 0:
            print("Error: El número debe ser positivo.")
            return ingresar_numero_positivo(mensaje)
        return valor
    except ValueError:
        print("Error: Ingrese un valor numérico válido.")
        return ingresar_numero_positivo(mensaje)

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            radio = ingresar_numero_positivo("Ingrese el radio del círculo: ")
            circulo = Circulo(radio)
            print(f"El área del círculo es: {circulo.calcular_area():.2f}")
        
        elif opcion == "2":
            largo = ingresar_numero_positivo("Ingrese el largo del rectángulo: ")
            ancho = ingresar_numero_positivo("Ingrese el ancho del rectángulo: ")
            rectangulo = Rectangulo(largo, ancho)
            print(f"El área del rectángulo es: {rectangulo.calcular_area():.2f}")
        
        elif opcion == "3":
            lado = ingresar_numero_positivo("Ingrese el lado del cuadrado: ")
            cuadrado = Cuadrado(lado)
            print(f"El área del cuadrado es: {cuadrado.calcular_area():.2f}")
        
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")