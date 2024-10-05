#Programa para inventario de productos segun lo que ingrese el usuario.
#Realizado por Marlon Armando Lopez Diaz y Jose Luis Castillo Virula estudiantes de la universidad Mariano Galvez de Guatemala de la faculta de Ingenieria en Sistemas 
import csv
import os

MAX_PRODUCTOS = 100 #Limite de productos que el usuario podra ingresar, sin que se repita el codgio asignado.
# Definicion de la clase de producto
class Producto: #Clase de producto
    def __init__(self, nombre="", codigo="", precio=0.0, proveedor="", existencia=0, estado='A', descuento=0.0):
        #Nombre del producto
        self.nombre = nombre 
        self.codigo = codigo #Codigo unico del producto
        self.precio = precio #Precio del producto
        self.proveedor = proveedor #Proveedor del producto
        self.existencia = existencia #Cantidad disponible
        #Estado del producto (A: Aprobado N: No aprobado)
        self.estado = estado 
        #Descuento aplicable al producto
        self.descuento = descuento 

# Metodo para convertir un objeto Producto a un diccionario
    def to_dict(self):
        return {
            'nombre': self.nombre,
            'codigo': self.codigo,
            'precio': self.precio,
            'proveedor': self.proveedor,
            'existencia': self.existencia,
            'estado': self.estado,
            'descuento': self.descuento,
        }
    # Metodo para crear un objeto Producto a partir de un diccionario
    @classmethod
    def from_dict(cls, data):
        return cls(**data)
# Funcion para guardar productos en un archivo CSV
def guardar_productos_csv(productos):
    with open("productos.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        # Escribir encabezados
        writer.writerow(['nombre', 'codigo', 'precio', 'proveedor', 'existencia', 'estado', 'descuento'])
        # Escribir los productos
        for producto in productos:
            writer.writerow([producto.nombre, producto.codigo, producto.precio, producto.proveedor, producto.existencia, producto.estado, producto.descuento])

# Funcion para cargar productos desde un archivo CSV
def cargar_productos_csv():
    productos = []
    if os.path.exists("productos.csv"): # Verifica si el archivo existe
        with open("productos.csv", mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                productos.append(Producto(**row))
    return productos
# Funcion para verificar si una cadena contiene otra cadena (criterio de busqueda)
def contiene(texto, palabra):
    return palabra in texto
# Funcion para verificar si el codigo de un producto ya existe
def codigo_existente(productos, codigo):
    return any(producto.codigo == codigo for producto in productos)
# Funcion para agregar un nuevo producto
def agregar_producto(productos):
    if len(productos) >= MAX_PRODUCTOS:
        print("No se pueden agregar más productos.")
        return

    # Solicitar datos del nuevo producto
    nuevo = Producto()
    nuevo.nombre = input("Ingrese el nombre del producto: ")
    nuevo.codigo = input("Ingrese el codigo del producto: ")

   # Verificar si el codigo ya existe
    if codigo_existente(productos, nuevo.codigo):
        print("Error: El codigo ya existe.")
        return
    
    # Ingresar los demas atributos
    nuevo.precio = float(input("Ingrese el precio: "))
    nuevo.proveedor = input("Ingrese el proveedor: ")
    nuevo.existencia = int(input("Ingrese la existencia: "))
    nuevo.estado = input("Ingrese el estado (A/N): ").upper()
    nuevo.descuento = float(input("Ingrese el descuento: "))

    # Agregar el producto a la lista y guardar en CSV
    productos.append(nuevo)
    guardar_productos_csv(productos)

# Funcion para buscar un producto por codigo o nombre
def buscar_producto(productos):
    criterio = input("Ingrese el codigo o nombre del producto a buscar: ")

    encontrado = False
    # Mostrar encabezado de resultados
    print(f"{'Nombre':<25}{'Codigo':<15}{'Precio':<15}{'Proveedor':<15}{'Existencia':<15}{'Estado':<10}{'Descuento':<10}")

    # Buscar el producto
    for producto in productos:
        if producto.codigo == criterio or contiene(producto.nombre, criterio): # Mostrar detalles del producto encontrado
            print(f"{producto.nombre:<25}{producto.codigo:<15}{producto.precio:<15.2f}{producto.proveedor:<15}{producto.existencia:<15}{producto.estado:<10}{producto.descuento:<10.2f}")
            encontrado = True

    if not encontrado:
        print("Producto no encontrado.")

# Funcion para modificar un producto existente
def modificar_producto(productos):
    codigo = input("Ingrese el codigo del producto a modificar: ")

    # Buscar el producto por codigo
    for producto in productos:
        if producto.codigo == codigo:
            # Solicitar nuevos valores para cada atributo
            producto.nombre = input(f"Ingrese el nuevo nombre (actual: {producto.nombre}): ")
            producto.precio = float(input(f"Ingrese el nuevo precio (actual: {producto.precio}): "))
            producto.proveedor = input(f"Ingrese el nuevo proveedor (actual: {producto.proveedor}): ")
            producto.existencia = int(input(f"Ingrese la nueva existencia (actual: {producto.existencia}): "))
            producto.estado = input(f"Ingrese el nuevo estado (A/N) (actual: {producto.estado}): ").upper()
            producto.descuento = float(input(f"Ingrese el nuevo descuento (actual: {producto.descuento}): "))
            # Guardar cambios en el archivo CSV
            guardar_productos_csv(productos)
            print("Producto modificado.")
            return

    print("Producto no encontrado.")

# Funcion principal que controla del programa
def main():
    productos = cargar_productos_csv()

    while True:
        print("\nMenu:")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Modificar producto")
        print("4. Salir")
        opcion = int(input("Seleccione una opcion: "))

        # Ejecutar la opcion seleccionada
        if opcion == 1:
            agregar_producto(productos)
        elif opcion == 2:
            buscar_producto(productos)
        elif opcion == 3:
            modificar_producto(productos)
        elif opcion == 4:
            print("Saliendo...")
            break
        else:
            print("Opcion no valida.")

# Comprobar si el archivo es ejecutado directamente
if __name__ == "__main__":
    main()
