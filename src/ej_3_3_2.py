def pedir_alumno(tipo:str) -> list:
    alumnos = []
    print(f"Introduce los nombres de pila de {tipo}: ")
    nombre = input()
    while nombre != "x":
        alumnos.append(nombre)
        nombre = input()
    return alumnos

def sin_repeticiones(primaria:list, secundaria:list):
    primaria = set(primaria)
    secundaria = set(secundaria)
    alumnos = primaria | secundaria
    alumnos = ", ".join(alumnos)
    print("Nombres sin repetirse: ", alumnos)
    
def nombres_repetidos_entre_primaria_secundaria(primaria:list, secundaria:list):
    print()
    
def main():
    primaria = pedir_alumno("primaria")
    secundaria = pedir_alumno("secundaria")
    sin_repeticiones(primaria, secundaria)
    print()
if __name__ == "__main__":
    main()