import math
class C:
    def __init__(self, rad):
        self.rad = rad
    
    def area(self):
        return math.pi * (self.rad ** 2)

if __name__ == "__main__":
    try:
        r1 = float(input("Ingrese el radio del primer círculo: "))
        r2 = float(input("Ingrese el radio del segundo círculo: "))
        c1 = C(r1)
        c2 = C(r2)
        
        print(f"El área calculado de radio {c1.rad} es: {c1.area():.2f}")
        print(f"El área calculado de radio {c2.rad} es: {c2.area():.2f}")
    
    except ValueError:
        print("Error: Ingresar un valor correcto para el radio.")