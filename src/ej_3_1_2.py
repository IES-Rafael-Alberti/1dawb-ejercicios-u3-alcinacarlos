def listar_asignaturas(asignaturas:list) -> str:
    """
    Devuelve una string con las asignaturas
    
    Args:
        asignaturas (list): lista de las asignaturas.
    
    Returns:
        str: "Yo estudio" más todas las asignaturas de la lista.
    """
    resultado = ""
    for asignatura in asignaturas:
        resultado += f"Yo estudio {asignatura}\n"
    
    return resultado

def pedir_asignaturas() -> list:
    asignaturas = []
    salir = False
    print("Introduce las asignaturas que quieras (enter para salir): ")
    while salir == False:
        asignatura = input()
        if asignatura == "":
            salir = True
        else:
            asignaturas.append(asignatura)
    return asignaturas

def main():
    print(listar_asignaturas(pedir_asignaturas()))
    
if __name__ == "__main__":
    main()