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

def listar_asignaturas(asignaturas:list) -> str:
    """
    Devuelve una string con las asignaturas
    
    Args:
        asignaturas (list): lista introducida.
    
    Returns:
        str: lista de asignaturas.
    """
    return ", ".join(asignaturas)


def main():
    print(listar_asignaturas(pedir_asignaturas()))
    
if __name__ == "__main__":
    main()