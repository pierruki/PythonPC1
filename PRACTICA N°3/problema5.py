class Alumno:
    def __init__(self, nombre, registro):
        self.nombre = nombre
        self.registro = registro
        self.edad = None
        self.nota = None
    
    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de Registro: {self.registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        if self.nota is not None:
            print(f"Nota: {self.nota}")
    
    def set_age(self, edad):
        self.edad = edad
    
    def set_nota(self, nota):
        self.nota = nota

if __name__ == "__main__":
    nombre = input("Ingrese el nombre del alumno: ")
    registro = input("Ingrese el número de registro del alumno: ")

    alumno = Alumno(nombre, registro)

    print("\nInformación inicial del alumno:")
    alumno.display()
    
    try:
        edad = int(input("Ingrese la edad del alumno: "))
        alumno.set_age(edad)
        
        nota = float(input("Ingrese la nota del alumno: "))
        alumno.set_nota(nota)
    
    except ValueError:
        print("Error: Ingrese valores numéricos válidos para la edad y la nota.")
    
    print("\nInformación actualizada del alumno:")
    alumno.display()