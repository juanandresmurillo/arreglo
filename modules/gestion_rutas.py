def crear_ruta(datos):
    ruta = {
        "id": input("ID de la ruta: "),
        "nombre": input("Nombre de la ruta (Ejemplo: Ruta NodeJS): "),
        "modulos": {
            "fundamentos": ["Introducción a la algoritmia", "PSeInt", "Python"],
            "web": ["HTML", "CSS", "Bootstrap"],
            "formal": ["Java", "JavaScript", "C#"],
            "bd": {
                "principal": input("SGDB principal (Ejemplo: MySQL): "),
                "alternativo": input("SGDB alternativo (Ejemplo: MongoDB): ")
            },
            "backend": ["NetCore", "Spring Boot", "NodeJS", "Express"]
        },
        "capacidad_maxima": 33,
        "campers": [],
        "trainers_asignados": []
    }
    datos["rutas"].append(ruta)
    print("¡Ruta creada con éxito!")

def asignar_camper_a_ruta(datos):
    id_camper = input("Ingrese el ID del camper a asignar: ")
    id_ruta = input("Ingrese el ID de la ruta: ")

    # Buscar el camper
    camper = next((c for c in datos["campers"] if c["id"] == id_camper), None)
    if not camper:
        print("El ID del camper no existe.")
        return

    # Verificar el estado del camper
    if camper["estado"] != "Aprobado":
        print("El camper no puede ser asignado porque no está aprobado.")
        return

    # Buscar la ruta
    ruta = next((r for r in datos["rutas"] if r["id"] == id_ruta), None)
    if not ruta:
        print("El ID de la ruta no existe.")
        return

    # Verificar capacidad de la ruta
    if len(ruta["campers"]) >= ruta["capacidad_maxima"]:
        print("La ruta ya alcanzó su capacidad máxima.")
        return

    # Asignar el camper
    ruta["campers"].append(camper["id"])
    print(f"¡Camper {camper['nombres']} asignado a la ruta {ruta['nombre']}!")
