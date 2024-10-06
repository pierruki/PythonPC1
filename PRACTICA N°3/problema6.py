class Producto:
    def __init__(self, nombre, precio, año):
        self.nombre = nombre
        self.precio = precio
        self.año = año
    
    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio:.2f}, Año: {self.año}"

class Catalogo:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def mostrar_productos(self):
        if self.productos:
            print("\nLista de productos en el catálogo:")
            for producto in self.productos:
                print(producto)
        else:
            print("\nNo hay productos en el catálogo.")
    
    def filtrar_por_año(self, año):
        productos_filtrados = [p for p in self.productos if p.año == año]
        if productos_filtrados:
            print(f"\nProductos del año {año}:")
            for producto in productos_filtrados:
                print(producto)
        else:
            print(f"\nNo se encontraron productos del año {año}.")
    
    def filtrar_por_precio(self, precio_maximo):
        productos_filtrados = [p for p in self.productos if p.precio <= precio_maximo]
        if productos_filtrados:
            print(f"\nProductos con un precio menor o igual a {precio_maximo:.2f}:")
            for producto in productos_filtrados:
                print(producto)
        else:
            print(f"\nNo se encontraron productos con un precio menor o igual a {precio_maximo:.2f}.")

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Ingresar un nuevo producto")
    print("2. Mostrar todos los productos")
    print("3. Filtrar productos por año")
    print("4. Filtrar productos por precio")
    print("5. Salir")

def ingresar_producto(catalogo):
    try:
        nombre = input("\nIngrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        año = int(input("Ingrese el año del producto: "))
        producto = Producto(nombre, precio, año)
        catalogo.agregar_producto(producto)
        print(f"\nProducto '{nombre}' agregado con éxito.")
    except ValueError:
        print("\nError: Asegúrese de ingresar valores numéricos válidos para el precio y el año.")

if __name__ == "__main__":
    catalogo = Catalogo()
    
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            ingresar_producto(catalogo)
        
        elif opcion == "2":
            catalogo.mostrar_productos()
        
        elif opcion == "3":
            try:
                año = int(input("\nIngrese el año para filtrar: "))
                catalogo.filtrar_por_año(año)
            except ValueError:
                print("\nError: Ingrese un valor numérico válido para el año.")
        
        elif opcion == "4":
            try:
                precio_maximo = float(input("\nIngrese el precio máximo para filtrar: "))
                catalogo.filtrar_por_precio(precio_maximo)
            except ValueError:
                print("\nError: Ingrese un valor numérico válido para el precio.")
        
        elif opcion == "5":
            print("\nSaliendo del programa...")
            break
        
        else:
            print("\nOpción no válida. Intente nuevamente.")