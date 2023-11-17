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

def poner_notas(asignaturas:list) -> list:
    """
    Devuelve un lista con las notas de las asignaturas
    
    Args:
        asignaturas (list) -> lista de asignaturas
    
    Returns:
        list -> lista de notas de las asignaturas
    """
    notas = []
    for asignatura in asignaturas:
        salir = False
        while salir == False:
            try:
                nota = int(input(f"Intrduce las notas de {asignatura}: "))
                if nota <= 0 or nota > 10:
                    raise ValueError
                notas.append(nota)
                salir = True
            except:
                print("Introduce un número válido entre 1 y 10.")

    return notas


def listar_asignaturas(asignaturas:list, notas:list) -> str:
    """
    Lista las asignaturas con sus correspondientes notas

    Args:
        asignaturas (list): lista de las asignaturas.
        notas (list): lista de notas.
    
    Returns:
        str: "En <asignatura> has sacado <nota>", donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario..
    """
    resultado = ""
    for i in range(len(asignaturas)):
        resultado += "En " + asignaturas[i] + " has sacado " + str(notas[i]) + "\n"
    return resultado    

def main():
    asignaturas = pedir_asignaturas()
    notas = poner_notas(asignaturas)
    print(listar_asignaturas(asignaturas, notas))
    
if __name__ == "__main__":
    main()