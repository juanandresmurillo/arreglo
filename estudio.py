import json
import os

# Archivo donde se guardará el inventario
ARCHIVO_JSON = "inventario.json"

def cargar_datos():
    """Carga los datos del archivo JSON. Si no existe, crea uno vacío."""
    if not os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, 'w') as archivo:
            json.dump([], archivo)
    with open(ARCHIVO_JSON, 'r') as archivo:
        return json.load(archivo)

def guardar_datos(datos):
    """Guarda los datos en el archivo JSON."""
    with open(ARCHIVO_JSON, 'w') as archivo:
        json.dump(datos, archivo, indent=4)

def generar_id(productos):
    """Genera un ID único para un nuevo producto."""
    return max([producto['id'] for producto in productos], default=0) + 1

def crear_producto(productos):
    """Crea un nuevo producto."""
    nombre = input("Nombre del producto: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return
    try:
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))
        if cantidad < 0 or precio <= 0:
            raise ValueError
    except ValueError:
        print("Cantidad o precio inválidos.")
        return

    nuevo_producto = {
        "id": generar_id(productos),
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
    }
    productos.append(nuevo_producto)
    guardar_datos(productos)
    print("Producto creado con éxito.")

def leer_productos(productos):
    """Lee y muestra todos los productos."""
    if not productos:
        print("No hay productos en el inventario.")
        return
    for producto in productos:
        print(f"ID: {producto['id']} | Nombre: {producto['nombre']} | Cantidad: {producto['cantidad']} | Precio: {producto['precio']:.2f}")

def leer_producto_por_id(productos):
    """Muestra un producto por su ID."""
    try:
        id_producto = int(input("ID del producto: "))
        producto = next((p for p in productos if p['id'] == id_producto), None)
        if producto:
            print(f"ID: {producto['id']} | Nombre: {producto['nombre']} | Cantidad: {producto['cantidad']} | Precio: {producto['precio']:.2f}")
        else:
            print("Producto no encontrado.")
    except ValueError:
        print("ID inválido.")

def actualizar_producto(productos):
    """Actualiza un producto existente."""
    try:
        id_producto = int(input("ID del producto a actualizar: "))
        producto = next((p for p in productos if p['id'] == id_producto), None)
        if not producto:
            print("Producto no encontrado.")
            return

        print("Deja en blanco un campo si no deseas modificarlo.")
        nuevo_nombre = input(f"Nuevo nombre (actual: {producto['nombre']}): ").strip() or producto['nombre']
        nueva_cantidad = input(f"Nueva cantidad (actual: {producto['cantidad']}): ").strip()
        nuevo_precio = input(f"Nuevo precio (actual: {producto['precio']}): ").strip()

        if nueva_cantidad:
            nueva_cantidad = int(nueva_cantidad)
            if nueva_cantidad < 0:
                raise ValueError("La cantidad no puede ser negativa.")
            producto['cantidad'] = nueva_cantidad
        if nuevo_precio:
            nuevo_precio = float(nuevo_precio)
            if nuevo_precio <= 0:
                raise ValueError("El precio debe ser mayor a 0.")
            producto['precio'] = nuevo_precio

        producto['nombre'] = nuevo_nombre
        guardar_datos(productos)
        print("Producto actualizado con éxito.")
    except ValueError as e:
        print(f"Error: {e}")

def eliminar_producto(productos):
    """Elimina un producto por su ID."""
    try:
        id_producto = int(input("ID del producto a eliminar: "))
        producto = next((p for p in productos if p['id'] == id_producto), None)
        if producto:
            productos.remove(producto)
            guardar_datos(productos)
            print("Producto eliminado con éxito.")
        else:
            print("Producto no encontrado.")
    except ValueError:
        print("ID inválido.")

def menu():
    """Muestra el menú y ejecuta las acciones."""
    productos = cargar_datos()
    opciones = {
        "1": crear_producto,
        "2": leer_productos,
        "3": leer_producto_por_id,
        "4": actualizar_producto,
        "5": eliminar_producto,
        "6": lambda _: print("Saliendo del programa.")
    }
    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Crear producto")
        print("2. Leer productos")
        print("3. Leer producto por ID")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")
        accion = opciones.get(opcion)
        if accion:
            if opcion == "6":
                accion(productos)
                break
            else:
                accion(productos)
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
import json
import os

# """
# Crear Producto:

# Debe ser posible añadir nuevos productos al inventario.
# Cada producto tendrá los siguientes campos:
# id (único para cada producto, generado automáticamente)
# nombre (cadena, no puede estar vacío)
# cantidad (entero, mayor o igual a 0)
# precio (flotante, mayor a 0)

# Leer Productos:

# Mostrar todos los productos en el inventario.
# Mostrar un producto específico al buscar por su id.

# Actualizar Producto:

# Permitir actualizar cualquier campo de un producto existente dado su id.
# Asegurarse de validar los datos antes de actualizar.

# Eliminar Producto:

# Permitir eliminar un producto del inventario dado su id.

# Persistencia:

# Los datos deben guardarse en un archivo JSON llamado inventario.json.
# Si el archivo no existe al iniciar el programa, debe crearse automáticamente con un inventario vacío.

# Validaciones:

# Asegúrate de validar todos los datos ingresados por el usuario.
# Maneja errores como intentar actualizar o eliminar un producto que no existe.

# Interfaz de Usuario:

# Implementa un menú simple en consola que permita al usuario realizar las operaciones del CRUD.
# Cuando termines tu código, avísame y te compartiré una solución modulada junto con una explicación. ¡Buena suerte y disfruta el reto! 🚀
# """

# """
# Explicación Paso a Paso
# Carga y Guardado de Datos:

# cargar_datos y guardar_datos manejan la lectura y escritura del archivo JSON, asegurando persistencia de datos.
# Si el archivo no existe, se crea vacío.

# Operaciones CRUD:

# Cada operación (crear_producto, leer_productos, leer_producto_por_id, actualizar_producto, eliminar_producto) realiza una acción específica sobre la lista de productos, manipulando datos y validando entradas.

# Generación de IDs:

# generar_id asegura que cada producto tenga un identificador único.

# Validaciones:

# Se verifica que los campos ingresados sean válidos antes de realizar cualquier operación.

# Interfaz de Usuario:

# menu ofrece un sistema basado en consola para interactuar con el CRUD, utilizando un diccionario de opciones para organizar las funciones.
# """

# """
# Estructura del Proyecto
# project_management/
# │
# ├── main.py             # Archivo principal que ejecuta el programa
# ├── data_manager.py     # Manejo de persistencia en JSON
# ├── board_manager.py    # Gestión de tableros
# ├── list_manager.py     # Gestión de listas dentro de tableros
# ├── card_manager.py     # Gestión de tarjetas dentro de listas
# └── inventario.json     # Archivo JSON para almacenar los datos
# """

ARCHIVO_JSON = "inventario.json"

# Cargar datos desde el archivo JSON
def cargar_datos():
    "Carga los datos del archivo JSON."
    if not os.path.exists(ARCHIVO_JSON):
        guardar_datos({"productos": []})  # Si el archivo no existe, se crea vacío
    with open(ARCHIVO_JSON, 'r') as archivo:
        return json.load(archivo)

# Guardar los datos en el archivo JSON
def guardar_datos(datos):
    "Guarda los datos en el archivo JSON."
    with open(ARCHIVO_JSON, 'w') as archivo:
        json.dump(datos, archivo, indent=4)

# Generar un ID único para un producto
def generar_id():
    "Genera un ID único para cada producto."
    datos = cargar_datos()
    return len(datos["productos"]) + 1

# Crear un nuevo producto
def crear_producto(nombre, cantidad, precio):
    "Añade un nuevo producto al inventario."
    if not nombre or cantidad < 0 or precio <= 0:
        print("Datos inválidos.")
        return
    producto = {
        "id": generar_id(),
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
    }
    datos = cargar_datos()
    datos["productos"].append(producto)
    guardar_datos(datos)
    print(f"Producto '{nombre}' agregado al inventario.")

# Leer todos los productos
def leer_productos():
    "Muestra todos los productos en el inventario."
    datos = cargar_datos()
    if not datos["productos"]:
        print("No hay productos en el inventario.")
        return
    for producto in datos["productos"]:
        print(f"ID: {producto['id']} | Nombre: {producto['nombre']} | Cantidad: {producto['cantidad']} | Precio: {producto['precio']}")

# Leer un producto por su ID
def leer_producto_por_id(id):
    "Muestra un producto específico al buscarlo por su ID."
    datos = cargar_datos()
    producto = next((p for p in datos["productos"] if p["id"] == id), None)
    if producto:
        print(f"ID: {producto['id']} | Nombre: {producto['nombre']} | Cantidad: {producto['cantidad']} | Precio: {producto['precio']}")
    else:
        print("Producto no encontrado.")

# Actualizar un producto
def actualizar_producto(id, nombre=None, cantidad=None, precio=None):
    "Actualiza los campos de un producto existente dado su ID."
    datos = cargar_datos()
    producto = next((p for p in datos["productos"] if p["id"] == id), None)
    if producto:
        if nombre:
            producto["nombre"] = nombre
        if cantidad is not None:
            producto["cantidad"] = cantidad
        if precio is not None:
            producto["precio"] = precio
        guardar_datos(datos)
        print(f"Producto con ID {id} actualizado.")
    else:
        print("Producto no encontrado.")

# Eliminar un producto
def eliminar_producto(id):
    "Elimina un producto del inventario dado su ID."
    datos = cargar_datos()
    datos["productos"] = [p for p in datos["productos"] if p["id"] != id]
    guardar_datos(datos)
    print(f"Producto con ID {id} eliminado.")

# Interfaz de usuario: menú principal
def menu():
    while True:
        print("\n1. Crear producto")
        print("2. Leer productos")
        print("3. Leer producto por ID")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            crear_producto(nombre, cantidad, precio)
        elif opcion == "2":
            leer_productos()
        elif opcion == "3":
            id_producto = int(input("Introduce el ID del producto: "))
            leer_producto_por_id(id_producto)
        elif opcion == "4":
            id_producto = int(input("Introduce el ID del producto: "))
            nombre = input("Nuevo nombre del producto (deja vacío para no cambiar): ")
            cantidad = input("Nueva cantidad del producto (deja vacío para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = input("Nuevo precio del producto (deja vacío para no cambiar): ")
            precio = float(precio) if precio else None
            actualizar_producto(id_producto, nombre, cantidad, precio)
        elif opcion == "5":
            id_producto = int(input("Introduce el ID del producto: "))
            eliminar_producto(id_producto)
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
    
    
    """
    Aquí está la estructura completa de los archivos para que el sistema funcione adecuadamente. Se separarán en diferentes archivos de Python para modularidad y fácil mantenimiento.

Estructura del Proyecto

project/
│
├── main.py                  # Archivo principal (menú interactivo)
├── tableros.py              # Funciones para gestionar tableros
├── listas.py                # Funciones para gestionar listas
├── tarjetas.py              # Funciones para gestionar tarjetas
├── persistencia.py          # Funciones para manejar el archivo JSON
└── tableros.json            # Archivo de datos persistentes

1. Archivo persistencia.py

Este archivo contiene las funciones para cargar y guardar datos en el archivo JSON.

import json

FILE_PATH = "tableros.json"

def cargar_datos():
    """Carga los datos del archivo JSON."""
    try:
        with open(FILE_PATH, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def guardar_datos(tableros):
    """Guarda los datos en el archivo JSON."""
    with open(FILE_PATH, 'w') as archivo:
        json.dump(tableros, archivo, indent=4)

2. Archivo tableros.py

Este archivo incluye todas las funciones relacionadas con la gestión de tableros.

from persistencia import guardar_datos

def crear_tablero(tableros, nombre):
    nuevo_id = max([tablero['id'] for tablero in tableros], default=0) + 1
    tablero = {"id": nuevo_id, "nombre": nombre, "listas": []}
    tableros.append(tablero)
    guardar_datos(tableros)

def ver_tableros(tableros):
    for tablero in tableros:
        print(f"ID: {tablero['id']}, Nombre: {tablero['nombre']}")

def actualizar_tablero(tableros, id_tablero, nuevo_nombre):
    for tablero in tableros:
        if tablero['id'] == id_tablero:
            tablero['nombre'] = nuevo_nombre
            guardar_datos(tableros)
            return
    raise ValueError(f"No se encontró el tablero con ID {id_tablero}.")

def eliminar_tablero(tableros, id_tablero):
    for tablero in tableros:
        if tablero['id'] == id_tablero:
            tableros.remove(tablero)
            guardar_datos(tableros)
            return
    raise ValueError(f"No se encontró el tablero con ID {id_tablero}.")

3. Archivo listas.py

Este archivo contiene funciones para la gestión de listas dentro de los tableros.

from persistencia import guardar_datos

def crear_lista(tableros, id_tablero, nombre_lista):
    for tablero in tableros:
        if tablero['id'] == id_tablero:
            nuevo_id = max([lista['id'] for lista in tablero['listas']], default=0) + 1
            lista = {"id": nuevo_id, "nombre": nombre_lista, "tarjetas": []}
            tablero['listas'].append(lista)
            guardar_datos(tableros)
            return
    raise ValueError(f"No se encontró el tablero con ID {id_tablero}.")

def ver_listas(tableros, id_tablero):
    for tablero in tableros:
        if tablero['id'] == id_tablero:
            for lista in tablero['listas']:
                print(f"ID: {lista['id']}, Nombre: {lista['nombre']}")
            return
    raise ValueError(f"No se encontró el tablero con ID {id_tablero}.")

def actualizar_lista(tableros, id_tablero, id_lista, nuevo_nombre):
    for tablero in tableros:
        if tablero['id'] == id_tablero:
            for lista in tablero['listas']:
                if lista['id'] == id_lista:
                    lista['nombre'] = nuevo_nombre
                    guardar_datos(tableros)
                    return
    raise ValueError(f"No se encontró la lista con ID {id_lista} en el tablero {id_tablero}.")

def eliminar_lista(tableros, id_tablero, id_lista):
    for tablero in tableros:
        if tablero['id'] == id_tablero:
            for lista in tablero['listas']:
                if lista['id'] == id_lista:
                    tablero['listas'].remove(lista)
                    guardar_datos(tableros)
                    return
    raise ValueError(f"No se encontró la lista con ID {id_lista} en el tablero {id_tablero}.")

4. Archivo tarjetas.py

Este archivo incluye funciones para gestionar las tarjetas dentro de las listas.

from persistencia import guardar_datos

def crear_tarjeta(tableros, id_tablero, id_lista, titulo, descripcion, estado):
    for tablero in tableros:
        if tablero['id'] == id_tablero:
            for lista in tablero['listas']:
                if lista['id'] == id_lista:
                    nuevo_id = max([tarjeta['id'] for tarjeta in lista['tarjetas']], default=0) + 1
                    tarjeta = {"id": nuevo_id, "titulo": titulo, "descripcion": descripcion, "estado": estado}
                    lista['tarjetas'].append(tarjeta)
                    guardar_datos(tableros)
                    return
    raise ValueError(f"No se encontró la lista con ID {id_lista} en el tablero {id_tablero}.")

def ver_tarjetas(tableros, id_tablero, id_lista):
    for tablero in tableros:
        if tablero['id'] == id_tablero:
            for lista in tablero['listas']:
                if lista['id'] == id_lista:
                    for tarjeta in lista['tarjetas']:
                        print(f"ID: {tarjeta['id']}, Título: {tarjeta['titulo']}, Estado: {tarjeta['estado']}")
                    return
    raise ValueError(f"No se encontró la lista con ID {id_lista} en el tablero {id_tablero}.")

def actualizar_tarjeta(tableros, id_tablero, id_lista, id_tarjeta, campo, nuevo_valor):
    for tablero in tableros:
        if tablero['id'] == id_tablero:
            for lista in tablero['listas']:
                if lista['id'] == id_lista:
                    for tarjeta in lista['tarjetas']:
                        if tarjeta['id'] == id_tarjeta:
                            if campo in tarjeta:
                                tarjeta[campo] = nuevo_valor
                                guardar_datos(tableros)
                                return
                            else:
                                raise ValueError("Campo inválido.")
    raise ValueError(f"No se encontró la tarjeta con ID {id_tarjeta} en la lista {id_lista}.")

def eliminar_tarjeta(tableros, id_tablero, id_lista, id_tarjeta):
    for tablero in tableros:
        if tablero['id'] == id_tablero:
            for lista in tablero['listas']:
                if lista['id'] == id_lista:
                    for tarjeta in lista['tarjetas']:
                        if tarjeta['id'] == id_tarjeta:
                            lista['tarjetas'].remove(tarjeta)
                            guardar_datos(tableros)
                            return
    raise ValueError(f"No se encontró la tarjeta con ID {id_tarjeta} en la lista {id_lista}.")

5. Archivo main.py

Este es el archivo principal, que sirve como un menú interactivo.

from persistencia import cargar_datos
from tableros import *
from listas import *
from tarjetas import *

def menu():
    tableros = cargar_datos()

    while True:
        print("\n=== Menú Principal ===")
        print("1. Gestionar Tableros")
        print("2. Gestionar Listas")
        print("3. Gestionar Tarjetas")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            # Lógica para gestionar tableros
            pass
        elif opcion == "2":
            # Lógica para gestionar listas
            pass
        elif opcion == "3":
            # Lógica para gestionar tarjetas
            pass
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()

Con esta estructura, puedes implementar un sistema modular, bien organizado, y fácil de mantener. ¿Te gustaría que detalle la lógica del menú para cada función?
    
"""
    