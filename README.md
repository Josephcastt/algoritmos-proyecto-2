# Proyecto 2

## Introducción

Este programa ha sido diseñado para gestionar un inventario de productos de manera eficiente y accesible, y está implementado en dos lenguajes: C++ y Python. Desarrollado por Marlon Armando López Díaz y José Luis Castillo Virula, estudiantes de la Universidad Mariano Gálvez de Guatemala, este software permite a los usuarios agregar, buscar y modificar productos dentro de un límite de 100 entradas, asegurando que cada producto tenga un código único.

El programa utiliza un enfoque basado en clases, definiendo un objeto Producto que contiene atributos esenciales como nombre, código, precio, proveedor, existencia, estado y descuento. Todos los productos ingresados se guardan en un archivo, lo que facilita su almacenamiento y posterior recuperación.

Entre las funcionalidades principales del programa se incluyen:

- Agregar Producto: Permite al usuario ingresar nuevos productos al inventario, verificando que no se repitan los códigos.
- Buscar Producto: Facilita la búsqueda de productos por nombre o código, mostrando información detallada sobre cada uno.
- Modificar Producto: Permite actualizar la información de productos existentes, garantizando que los datos se mantengan al día.

Con una interfaz sencilla y clara, este programa está diseñado para ser utilizado en entornos donde la gestión de inventario sea necesaria, optimizando el manejo de productos y simplificando el proceso de administración. La disponibilidad en ambos lenguajes asegura que los usuarios puedan elegir la opción que mejor se adapte a sus necesidades y habilidades.

## Requisitos
Antes de utilizar el programa, Antes de utilizar el programa, asegúrate de tener instalado:

- Python (para la versión en Python).
- Compilador de C++ (cualquier IDE que soporte C++ como Visual Studio) para la versión en C++.

## Menú principal
Al ejecutar el programa, se mostrará un menú principal con las siguientes opciones:

1. Agregar producto: Permite añadir un nuevo producto al inventario.
2. Buscar producto: Facilita la búsqueda de productos por nombre o código.
3. Modificar producto: Permite actualizar la información de un producto existente.
4. Salir: Cierra el programa.

## Funcionalidades 
###  1. Agregar producto
- Descripción: Permite ingresar un nuevo producto al inventario.
- Pasos:
    1. Selecciona la opción "1. Agregar producto".
    2. Introduce el nombre del producto.
    3. Ingresa un código único para el producto.
    4. Proporciona el precio del producto.
    5. Indica el proveedor del producto.
    6. Especifica la cantidad disponible (existencia).
    7. Indica el estado del producto (A para Aprobado, N para No aprobado).
    8. Si aplica, ingresa el descuento del producto.
    9. El producto se guardará automáticamente en el archivo.
 
### 2. Buscar Producto
- Descripción: Permite encontrar un producto existente mediante su código o nombre.
- Pasos:
    1. Selecciona la opción "2. Buscar producto".
    2. Introduce el código o nombre del producto que deseas buscar.
    3. El programa mostrará los detalles del producto encontrado. Si no se encuentra, se mostrará un mensaje indicando que el producto no fue encontrado.

### 3. Modificar Producto
- Descripción: Permite actualizar la información de un producto que ya se encuentra en el inventario.
- Pasos:
    1. Selecciona la opción "3. Modificar producto".
    2. Ingresa el código del producto que deseas modificar.
    3. El programa mostrará los atributos actuales del producto y solicitará que ingreses los nuevos valores para cada atributo.
    4. Los cambios se guardarán automáticamente en el archivo.

### 4. Salir
- Descripción: Cierra el programa.
- Pasos:
    1. Selecciona la opción "4. Salir".
    2. El programa se cerrará y se regresará a la terminal.

## Notas Importantes
+ Límite de Productos: El programa permite un máximo de 100 productos. Si intentas agregar más productos, recibirás un mensaje indicando que no se pueden agregar más.
+ Códigos Únicos: Cada producto debe tener un código único. Si intentas ingresar un código que ya existe, recibirás un mensaje de error.

## Conclusión
Este programa de inventario es una herramienta útil para la gestión de productos. Siguiendo este manual, deberías poder utilizar todas las funcionalidades del programa de manera efectiva en ambas versiones. Si tienes preguntas adicionales o problemas técnicos, consulta con el desarrollador o busca recursos adicionales sobre Python y C++.

