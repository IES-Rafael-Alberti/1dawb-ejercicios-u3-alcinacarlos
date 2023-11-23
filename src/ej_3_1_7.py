def obtener_abecedario() -> list:
    return list(chr(i) for i in range(ord("A"), ord("Z") + 1))

def eliminar_multiplos_3(abecedario:list) -> list:
    for i in range(len(abecedario) - 3, -1, -3):
        abecedario.pop(i)
    return abecedario

def main():
    print(eliminar_multiplos_3(obtener_abecedario()))
    
if __name__ == "__main__":
    main()