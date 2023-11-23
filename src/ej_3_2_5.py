ASIGNATURAS = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

def mostrar_creditos():
    for asignatura, credito in ASIGNATURAS.items():
        print(f"{asignatura} tiene {credito} créditos")
    total_creditos = sum(ASIGNATURAS.values())
    print(f"Número total de créditos: {total_creditos}")
            

def main():
    mostrar_creditos()
if __name__ == "__main__":
    main()