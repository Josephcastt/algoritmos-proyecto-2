//Programa para inventario de productos segun lo que ingrese el usuario
//Realizado por Marlon Armando López Díaz y José Luis Castillo Virula estudiantes de la universidad Mariano Galvez de Guatemala de la faculta de Ingenieria en Sistemas
#include <iostream>
#include <fstream>
#include <string>
#include <limits> 
#include <iomanip>

using namespace std;

const int MAX_PRODUCTOS = 100;

struct Producto {
    string nombre;
    string codigo;
    double precio;
    string proveedor;
    int existencia;
    char estado;
    double descuento;
};

void guardarProductos(Producto productos[], int count) {
    ofstream file("productos.dat", ios::binary);
    file.write(reinterpret_cast<const char*>(productos), count * sizeof(Producto));
    file.close();
}

int cargarProductos(Producto productos[]) {
    ifstream file("productos.dat", ios::binary);
    int count = 0;
    while (file.read(reinterpret_cast<char*>(&productos[count]), sizeof(Producto)) && count < MAX_PRODUCTOS) {
        count++;
    }
    file.close();
    return count;
}

bool contiene(const string& texto, const string& palabra) {
    return texto.find(palabra) != string::npos;
}

bool codigoExistente(Producto productos[], int count, const string& codigo) {
    for (int i = 0; i < count; i++) {
        if (productos[i].codigo == codigo) {
            return true;
        }
    }
    return false;
}

void agregarProducto(Producto productos[], int& count) {
    if (count >= MAX_PRODUCTOS) {
        cout << "No se pueden agregar m?s productos." << endl;
        return;
    }

    Producto nuevo;
    cout << "Ingrese el nombre del producto: ";
    cin.ignore();
    getline (cin, nuevo.nombre);
    cout << "Ingrese el codigo del producto: ";
    cin >> nuevo.codigo;

    if (codigoExistente(productos, count, nuevo.codigo)) {
        cout << "Error: El codigo ya existe." << endl;
        return;
    }

    cout << "Ingrese el precio: ";
    cin >> nuevo.precio;
    cout << "Ingrese el proveedor: ";
    cin.ignore();
    getline (cin, nuevo.proveedor);
    cout << "Ingrese la existencia: ";
    cin >> nuevo.existencia;
    cout << "Ingrese el estado (A/N): ";
    cin >> nuevo.estado;
    cout << "Ingrese el descuento: ";
    cin >> nuevo.descuento;

    productos[count] = nuevo;
    count++;
    guardarProductos(productos, count);
}

void buscarProducto(Producto productos[], int count) {
    string criterio;
    cout << "Ingrese el codigo o nombre del producto a buscar: ";
    cin >> criterio;

    bool encontrado = false;

  
    cout << left << setw(15) << "Nombre"
         << setw(15) << "Codigo"
         << setw(15) << "Precio"
         << setw(15) << "Proveedor"
         << setw(15) << "Existencia"
         << setw(10) << "Estado"
         << setw(10) << "Descuento" << endl;

    for (int i = 0; i < count; i++) {
        if (productos[i].codigo == criterio || contiene(productos[i].nombre, criterio)) {
            cout << left << setw(20) << productos[i].nombre
                 << setw(11) << productos[i].codigo
                 << setw(14)<<productos[i].precio
                 //<< fixed << setprecision(2) << setw(8) << productos[i].precio
                 << setw(15) << productos[i].proveedor
                 << setw(16) << productos[i].existencia
                 << setw(15) << productos[i].estado
                 << setw(15) << productos[i].descuento << endl;
            encontrado = true;
        }
    }

    if (!encontrado) {
        cout << "Producto no encontrado." << endl;
    }
}

void modificarProducto(Producto productos[], int count) {
    string codigo;
    cout << "Ingrese el codigo del producto a modificar: ";
    cin >> codigo;

    for (int i = 0; i < count; i++) {
        if (productos[i].codigo == codigo) {
            cout << "Ingrese el nuevo nombre (actual: " << productos[i].nombre << "): ";
            cin >> productos[i].nombre;
            cin.ignore();
            getline (cin, productos[i].nombre);
            cout << "Ingrese el nuevo precio (actual: " << productos[i].precio << "): ";
            cin >> productos[i].precio;
            cout << "Ingrese el nuevo proveedor (actual: " << productos[i].proveedor << "): ";
            cin >> productos[i].proveedor;
            cin.ignore();
            getline (cin, productos[i].proveedor);
            cout << "Ingrese la nueva existencia (actual: " << productos[i].existencia << "): ";
            cin >> productos[i].existencia;
            cout << "Ingrese el nuevo estado (A/N) (actual: " << productos[i].estado << "): ";
            cin >> productos[i].estado;
            cout << "Ingrese el nuevo descuento (actual: " << productos[i].descuento << "): ";
            cin >> productos[i].descuento;

            guardarProductos(productos, count);
            cout << "Producto modificado." << endl;
            return;
        }
    }
    cout << "Producto no encontrado." << endl;
}

int main() {
    Producto productos[MAX_PRODUCTOS];
    int count = cargarProductos(productos);

    int opcion;
    do {
        cout << "\nMenu:" << endl;
        cout << "1. Agregar producto" << endl;
        cout << "2. Buscar producto" << endl;
        cout << "3. Modificar producto" << endl;
        cout << "4. Salir" << endl;
        cout << "Seleccione una opcion: ";
        cin >> opcion;

        switch (opcion) {
            case 1:
                agregarProducto(productos, count);
                break;
            case 2:
                buscarProducto(productos, count);
                break;
            case 3:
                modificarProducto(productos, count);
                break;
            case 4:
                cout << "Saliendo..." << endl;
                break;
            default:
                cout << "Opcion no valida." << endl;
        }
    } while (opcion != 4);

    return 0;
}