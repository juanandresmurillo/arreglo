def generar_reporte_estado(datos):
    print("\n--- CAMPERS EN ESTADO DE INSCRITO ---")
    for camper in datos["campers"]:
        if camper["estado"] == "Inscrito":
            print(f"{camper['id']} - {camper['nombres']} {camper['apellidos']}")

def generar_reporte_rendimiento(datos):
    print("\n--- CAMPERS EN RENDIMIENTO BAJO ---")
    for camper in datos["campers"]:
        if camper.get("riesgo"):
            print(f"{camper['id']} - {camper['nombres']} {camper['apellidos']} (Riesgo)")

    print("\n--- CAMPERS Y TRAINERS ASOCIADOS A RUTAS ---")
    for ruta in datos["rutas"]:
        print(f"\nRuta: {ruta['nombre']}")
        print("Campers:")
        for id_camper in ruta["campers"]:
            camper = next((c for c in datos["campers"] if c["id"] == id_camper), None)
            if camper:
                print(f"  {camper['id']} - {camper['nombres']} {camper['apellidos']}")
        print("Trainers:")
        for id_trainer in ruta["trainers_asignados"]:
            trainer = next((t for t in datos["trainers"] if t["id"] == id_trainer), None)
            if trainer:
                print(f"  {trainer['id']} - {trainer['nombres']} {trainer['apellidos']}")

def generar_reporte_resultados(datos):
    print("\n--- RESULTADOS POR RUTA Y TRAINER ---")
    for ruta in datos["rutas"]:
        print(f"\nRuta: {ruta['nombre']}")
        aprobados = 0
        perdidos = 0

        for evaluacion in datos["evaluaciones"]:
            if evaluacion["id_ruta"] == ruta["id"]:
                if evaluacion["nota_final"] >= 60:
                    aprobados += 1
                else:
                    perdidos += 1

        print(f"Aprobados: {aprobados}")
        print(f"Perdidos: {perdidos}")
