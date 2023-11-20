vocales = (["a", 0], ["e", 0], ["i", 0], ["o", 0], ["u", 0])

def pedir_palabra() -> str:
    palabra = input("Introduce una palabra: ")
    while palabra.isdigit():
        palabra = input("Error, introduce una palabra válida: ")
    return palabra

def contar_veces(palabra:str) -> list:
    for i in range(len(vocales)):
        vocales[i][1] = palabra.count(vocales[i][0])
    return vocales

def formatear_algoritmo(vocales:list) -> str:
    resultado = ""
    for i in range(5):
        if vocales[i][1] > 0:
            resultado += "La vocal " + vocales[i][0] + " se repite " + str(vocales[i][1]) + " veces\n"
    return resultado
        

def main():
    print(formatear_algoritmo(contar_veces(pedir_palabra())))
    
if __name__ == "__main__":
    main()