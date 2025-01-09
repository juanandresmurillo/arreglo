import json

# Cargar datos desde el archivo JSON
def cargar_datos():
    try:
        with open('campuslands_data.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {"campers": [], "trainers": [], "routes": [], "enrollments": [], "usuarios": {}}

# Guardar datos en el archivo JSON
def guardar_datos(datos):
    with open('campuslands_data.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4)

# Aprobar Camper
def aprobar_camper():
    datos = cargar_datos()
    campers = datos.get("campers", [])
    print("\nLista de Campers Inscritos:")
    inscritos = [camper for camper in campers if camper["estado"] == "Inscrito"]
    for i, camper in enumerate(inscritos):
        print(f"{i + 1}. {camper['nombres']} {camper['apellidos']} (ID: {camper['id']})")
    
    if not inscritos:
        print("No hay campers inscritos para aprobar.")
        return

    try:
        seleccion = int(input("Seleccione el número del camper que desea aprobar: ")) - 1
        if 0 <= seleccion < len(inscritos):
            camper_seleccionado = inscritos[seleccion]
            camper_seleccionado["estado"] = "Aprobado"
            print(f"El camper {camper_seleccionado['nombres']} {camper_seleccionado['apellidos']} ha sido aprobado.")
            guardar_datos(datos)
        else:
            print("Selección inválida.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")

# Listar Campers

# Listar Campers
def listar_campers():
    datos = cargar_datos()
    campers = datos.get("campers", [])
    if not campers:
        print("\nNo hay campers registrados.")
    else:
        print("\nLista de Campers:")
        for camper in campers:
            print(f"ID: {camper['id']}, Nombre: {camper['nombres']} {camper['apellidos']}, Estado: {camper['estado']}")

# Asignar Notas
def asignar_notas():
    datos = cargar_datos()
    campers = datos.get("campers", [])
    print("\nLista de Campers Aprobados:")
    for i, camper in enumerate(campers):
        if camper["estado"] == "Aprobado":
            print(f"{i + 1}. {camper['nombres']} {camper['apellidos']} (ID: {camper['id']})")
    seleccion = int(input("Seleccione el número del camper para asignar notas: ")) - 1
    if 0 <= seleccion < len(campers) and campers[seleccion]["estado"] == "Aprobado":
        nota = float(input(f"Ingrese la nota para {campers[seleccion]['nombres']} {campers[seleccion]['apellidos']}: "))
        campers[seleccion].setdefault("notas", []).append(nota)
        print(f"Nota {nota} asignada a {campers[seleccion]['nombres']} {campers[seleccion]['apellidos']}.")
        guardar_datos(datos)
    else:
        print("Selección inválida.")

# Reprobar Camper
def reprobar_camper():
    datos = cargar_datos()
    campers = datos.get("campers", [])
    print("\nLista de Campers Aprobados:")
    for i, camper in enumerate(campers):
        if camper["estado"] == "Aprobado":
            print(f"{i + 1}. {camper['nombres']} {camper['apellidos']} (ID: {camper['id']})")
    seleccion = int(input("Seleccione el número del camper que desea reprobar: ")) - 1
    if 0 <= seleccion < len(campers) and campers[seleccion]["estado"] == "Aprobado":
        campers[seleccion]["estado"] = "Reprobado"
        print(f"El camper {campers[seleccion]['nombres']} {campers[seleccion]['apellidos']} ha sido reprobado.")
        guardar_datos(datos)
    else:
        print("Selección inválida.")

# Asignar Ruta
def asignar_ruta():
    datos = cargar_datos()
    campers = datos.get("campers", [])
    routes = datos.get("routes", [])
    print("\nLista de Campers Aprobados:")
    for i, camper in enumerate(campers):
        if camper["estado"] == "Aprobado":
            print(f"{i + 1}. {camper['nombres']} {camper['apellidos']} (ID: {camper['id']})")
    seleccion = int(input("Seleccione el número del camper para asignar una ruta: ")) - 1
    if 0 <= seleccion < len(campers) and campers[seleccion]["estado"] == "Aprobado":
        print("\nLista de Rutas Disponibles:")
        for j, route in enumerate(routes):
            print(f"{j + 1}. {route['nombre']}")
        ruta_seleccionada = int(input("Seleccione el número de la ruta: ")) - 1
        if 0 <= ruta_seleccionada < len(routes):
            campers[seleccion]["ruta_asignada"] = routes[ruta_seleccionada]["nombre"]
            print(f"Ruta {routes[ruta_seleccionada]['nombre']} asignada a {campers[seleccion]['nombres']} {campers[seleccion]['apellidos']}.")
            guardar_datos(datos)
        else:
            print("Ruta seleccionada inválida.")
    else:
        print("Selección inválida.")

# Asignar Salón
def asignar_salon():
    salones = ["Sputnik", "Apolo", "Artemisa"]
    datos = cargar_datos()
    campers = datos.get("campers", [])
    print("\nLista de Campers Aprobados:")
    for i, camper in enumerate(campers):
        if camper["estado"] == "Aprobado":
            print(f"{i + 1}. {camper['nombres']} {camper['apellidos']} (ID: {camper['id']})")
    seleccion = int(input("Seleccione el número del camper para asignar un salón: ")) - 1
    if 0 <= seleccion < len(campers) and campers[seleccion]["estado"] == "Aprobado":
        print("\nLista de Salones Disponibles:")
        for j, salon in enumerate(salones):
            print(f"{j + 1}. {salon}")
        salon_seleccionado = int(input("Seleccione el número del salón: ")) - 1
        if 0 <= salon_seleccionado < len(salones):
            campers[seleccion]["salon_asignado"] = salones[salon_seleccionado]
            print(f"Salón {salones[salon_seleccionado]} asignado a {campers[seleccion]['nombres']} {campers[seleccion]['apellidos']}.")
            guardar_datos(datos)
        else:
            print("Salón seleccionado inválido.")
    else:
        print("Selección inválida.")

# Menú del Coordinador
def menu_coordinador():
    while True:
        print("\n--- Menú Coordinador ---")
        print("1. Aprobar Camper")
        print("2. Listar Campers")
        print("3. Asignar notas")
        print("4. Reprobar camper")
        print("5. Asignar ruta")
        print("6. Asignar salón")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            aprobar_camper()
        elif opcion == "2":
            listar_campers()
        elif opcion == "3":
            asignar_notas()
        elif opcion == "4":
            reprobar_camper()
        elif opcion == "5":
            asignar_ruta()
        elif opcion == "6":
            asignar_salon()
        elif opcion == "7":
            print("Saliendo del menú coordinador.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
