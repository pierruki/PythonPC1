class Rect:
    def __init__(self, l, a):
        self.l = l
        self.a = a
    
    def area(self):
        return self.l * self.a

class C(Rect):
    def __init__(self, l):
        super().__init__(l, l)

if __name__ == "__main__":
    try:
        l_rect = float(input("Por favor Insertar el largo del rectangulo: "))
        a_rect = float(input("Por favor Insertar el largo del rectángulo: "))
        lado_c= float(input("Por favor insertar el lado del rectangulo: "))
        r = Rect(l_rect, a_rect)   
        c = C(lado_c)
        print(f"El área del rectángulo es: {r.area():.2f}")
        print(f"El área del cuadrado es: {c.area():.2f}")
    
    except ValueError:
        print("Error: Por favor introducir valores adecuados.")