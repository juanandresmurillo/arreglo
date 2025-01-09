def registrar_notas(data, id_camper, nota_teorica, nota_practica, nota_quiz):
    """
    Registrar las notas de un camper en diferentes evaluaciones: teórica, práctica y quizes/trabajos.
    """
    # Verificar si 'campers' existe en los datos
    if "campers" not in data:
        print("No se encontraron campers en los datos.")
        return data

    camper = next((c for c in data["campers"] if c["id"] == id_camper), None)
    if camper:
        # Calcular la nota final considerando los pesos
        nota_final = (nota_teorica * 0.3) + (nota_practica * 0.6) + (nota_quiz * 0.1)
        camper["nota_final"] = nota_final
        print(f"Notas registradas para el camper {id_camper}. Nota final: {nota_final:.2f}")
    else:
        print(f"Camper con ID {id_camper} no encontrado.")
    return data

def evaluar_camper(camper):
    """
    Evaluar a un camper según su nota final. 
    Si la nota final es >= 60, el camper está aprobado; en caso contrario, está reprobado.
    """
    if camper.get("nota_final", 0) >= 60:
        camper["aprobado"] = True
        print(f"Camper {camper['id']} aprobado con nota final {camper['nota_final']:.2f}.")
    else:
        camper["aprobado"] = False
        print(f"Camper {camper['id']} reprobado con nota final {camper['nota_final']:.2f}.")
    return camper

def evaluar_campers_periodicamente(data):
    """
    Evaluar todos los campers registrados de manera periódica.
    Recorre la lista de campers y aplica la evaluación a cada uno.
    """
    # Verificar si 'campers' existe en los datos
    if "campers" not in data:
        print("No se encontraron campers en los datos.")
        return data

    print("Iniciando evaluación periódica de los campers...")
    for camper in data["campers"]:
        evaluar_camper(camper)
    print("Evaluación periódica completada.")
    return data
