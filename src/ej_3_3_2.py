def pedir_alumno(tipo:str) -> list:
    alumnos = []
    print(f"Introduce los nombres de pila de {tipo}, x para salir: ")
    nombre = input()
    while nombre != "x":
        alumnos.append(nombre)
        nombre = input().strip()
    return set(alumnos)

def sin_repeticiones(primaria:set, secundaria:set):
    alumnos = primaria | secundaria
    alumnos = ", ".join(alumnos)
    print("Nombres sin repetirse de primaria y secundaria:", alumnos)
    
def nombres_repetidos_entre_primaria_secundaria(primaria:set, secundaria:set):
    alumnos = primaria.intersection(secundaria)
    alumnos = ", ".join(alumnos)
    print("Nombres repetidos entre primaria y secundaria:", alumnos)
    
def nombres_no_repetidos_entre_primaria_secundaria(primaria:set, secundaria:set):
    alumnos = primaria.difference(secundaria)
    alumnos = ", ".join(alumnos)
    print("Nombres no repetidos entre primaria y secundaria:", alumnos)

def alumnos_primaria_estan_secundaria(primaria:set, secundaria:set) -> bool:
    if primaria <= secundaria:
        print("Todos los alumnos de primaria están en secundaria")
    else:
        print("Todos los alumnos de primaria NO están en secundaria")

def main():
    primaria = pedir_alumno("primaria")
    secundaria = pedir_alumno("secundaria")
    sin_repeticiones(primaria, secundaria)
    nombres_repetidos_entre_primaria_secundaria(primaria, secundaria)
    nombres_no_repetidos_entre_primaria_secundaria(primaria, secundaria)
    alumnos_primaria_estan_secundaria(primaria, secundaria)
if __name__ == "__main__":
    main()