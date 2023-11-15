def pedir_palabra() -> str:
    palabra = input("Introduce una palabra: ")
    while palabra.isdigit() == True:
        palabra = input("Error, introduce una palabra válida: ")
    return palabra

def es_palidromo(palabra:str) -> bool:
    return palabra == palabra[::-1]

def main():
    print(es_palidromo(pedir_palabra()))
    
if __name__ == "__main__":
    main()