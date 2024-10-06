from gestion import GestionBiblioteca
from libro import Libro

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Agregar un libro")
    print("2. Listar libros")
    print("3. Buscar un libro por título")
    print("4. Buscar un libro por autor")
    print("5. Salir")

def ingresar_libro():
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    isbn = input("Ingrese el ISBN del libro: ")
    return Libro(titulo, autor, isbn)

if __name__ == "__main__":
    gestion_biblioteca = GestionBiblioteca()

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            libro = ingresar_libro()
            gestion_biblioteca.agregar_libro(libro)
        
        elif opcion == "2":
            gestion_biblioteca.listar_libros()
        
        elif opcion == "3":
            titulo = input("Ingrese el título para buscar: ")
            gestion_biblioteca.buscar_por_titulo(titulo)
        
        elif opcion == "4":
            autor = input("Ingrese el autor para buscar: ")
            gestion_biblioteca.buscar_por_autor(autor)
        
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")