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


def asignaturas_a_repetir(asignaturas:list, notas:list):
    i = 0
    while i < len(asignaturas):
        if notas[i] >= 5:
            asignaturas.pop(i)
            notas.pop(i)
        else:
            i += 1
    return asignaturas

def listar_asignaturas(asignaturas:list) -> str:
    if len(asignaturas) == 0: return "Has aprobado todo!"
    resultado = "Tienes que repetir: \n"
    for i in range(len(asignaturas)):
        resultado += str(asignaturas[i]) + "\n"
        
    return resultado


def main():
    asignaturas = pedir_asignaturas()
    notas = poner_notas(asignaturas)
    print(listar_asignaturas(asignaturas_a_repetir(asignaturas, notas)))
    
if __name__ == "__main__":
    main()