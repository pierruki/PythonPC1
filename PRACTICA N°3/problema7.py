import math

class Coordenada:
    def __init__(self, coord_x=0, coord_y=0):
        self.coord_x = coord_x
        self.coord_y = coord_y

    def __str__(self):
        return f"({self.coord_x}, {self.coord_y})"
    
    def ubicacion(self):
        if self.coord_x == 0 and self.coord_y == 0:
            return "El punto se localiza en el origen"
        elif self.coord_x == 0:
            return "El punto está sobre el eje vertical (Y)"
        elif self.coord_y == 0:
            return "El punto está sobre el eje horizontal (X)"
        elif self.coord_x > 0 and self.coord_y > 0:
            return "El punto se encuentra en el primer cuadrante"
        elif self.coord_x < 0 and self.coord_y > 0:
            return "El punto se encuentra en el segundo cuadrante"
        elif self.coord_x < 0 and self.coord_y < 0:
            return "El punto está ubicado en el tercer cuadrante"
        elif self.coord_x > 0 and self.coord_y < 0:
            return "El punto está en el cuarto cuadrante"

    def calcular_vector(self, otro_punto):
        return Coordenada(otro_punto.coord_x - self.coord_x, otro_punto.coord_y - self.coord_y)

    def calcular_distancia(self, otro_punto):
        return math.sqrt((otro_punto.coord_x - self.coord_x) ** 2 + (otro_punto.coord_y - self.coord_y) ** 2)

class FiguraRectangular:
    def __init__(self, esquina_inicial=Coordenada(), esquina_final=Coordenada()):
        self.esquina_inicial = esquina_inicial
        self.esquina_final = esquina_final

    def longitud(self):
        return abs(self.esquina_final.coord_x - self.esquina_inicial.coord_x)

    def ancho(self):
        return abs(self.esquina_final.coord_y - self.esquina_inicial.coord_y)

    def area(self):
        return self.longitud() * self.ancho()

# Función para pedir las coordenadas de un punto
def ingresar_coordenada(nombre_punto):
    try:
        coord_x = float(input(f"Ingrese el valor de X para el punto {nombre_punto}: "))
        coord_y = float(input(f"Ingrese el valor de Y para el punto {nombre_punto}: "))
        return Coordenada(coord_x, coord_y)
    except ValueError:
        print("Error: Por favor, ingrese un valor numérico válido.")
        return ingresar_coordenada(nombre_punto)

# Función para determinar qué punto está más distante del origen
def mas_distante_al_origen(punto1, punto2, punto3):
    origen = Coordenada(0, 0)
    distancia1 = punto1.calcular_distancia(origen)
    distancia2 = punto2.calcular_distancia(origen)
    distancia3 = punto3.calcular_distancia(origen)

    distancias = [(distancia1, "Punto 1"), (distancia2, "Punto 2"), (distancia3, "Punto 3")]
    max_distancia = max(distancias, key=lambda x: x[0])
    return max_distancia[1], max_distancia[0]

# Ejemplo de uso con entrada por teclado
if __name__ == "__main__":
    # Ingresar las coordenadas de los puntos 1, 2, 3 y 4
    punto_1 = ingresar_coordenada("1")
    punto_2 = ingresar_coordenada("2")
    punto_3 = ingresar_coordenada("3")
    punto_4 = ingresar_coordenada("4")

    # Imprimir los puntos
    print(f"\nPunto 1: {punto_1}")
    print(f"Punto 2: {punto_2}")
    print(f"Punto 3: {punto_3}")
    print(f"Punto 4: {punto_4}")

    # Identificar en qué cuadrante se encuentran los puntos 1, 3 y 4
    print(f"\nEl punto 1 está en: {punto_1.ubicacion()}")
    print(f"El punto 3 está en: {punto_3.ubicacion()}")
    print(f"El punto 4 está en: {punto_4.ubicacion()}")

    # Calcular los vectores del punto 1 al 2 y viceversa
    vector_12 = punto_1.calcular_vector(punto_2)
    vector_21 = punto_2.calcular_vector(punto_1)
    print(f"\nVector del punto 1 al 2: {vector_12}")
    print(f"Vector del punto 2 al 1: {vector_21}")

    # Calcular la distancia entre los puntos 1 y 2, y 2 y 1
    distancia_12 = punto_1.calcular_distancia(punto_2)
    distancia_21 = punto_2.calcular_distancia(punto_1)
    print(f"\nDistancia entre el punto 1 y 2: {distancia_12:.2f}")
    print(f"Distancia entre el punto 2 y 1: {distancia_21:.2f}")

    # Determinar cuál de los puntos 1, 2 o 3 está más distante del origen
    punto_mas_lejos, distancia_mas_lejos = mas_distante_al_origen(punto_1, punto_2, punto_3)
    print(f"\nEl {punto_mas_lejos} es el más lejano del origen con una distancia de {distancia_mas_lejos:.2f}")

    # Crear un rectángulo utilizando los puntos 1 y 2
    rectangulo = FiguraRectangular(punto_1, punto_2)
    print(f"\nLongitud del rectángulo: {rectangulo.longitud()}")
    print(f"Ancho del rectángulo: {rectangulo.ancho()}")
    print(f"Área del rectángulo: {rectangulo.area()}")
