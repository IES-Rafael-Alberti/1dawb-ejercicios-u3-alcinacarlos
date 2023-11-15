def pedir_reintegro() -> int:
    """
    Pregunta el reintegro y lo valida por si el usuario lo introduce mal
    
    Returns:
        int: reintegro
    
    """
    salir = True
    while salir == True:
        try:
            numero = int(input("Introduce el reintegro: "))
            if numero < 1 or numero > 9:
                raise ValueError
            else:
                salir = False
        except:
            print("Introduce un número válido entre 1 el 9")
    return numero

def pedir_loteria() -> str:
    """
    Pregunta al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
    
    Returns:
        str: Numeros ganadores de la primitiva ordenados de menor a mayor
    """
    numeros_ganadores = []    
    for i in range(6):
        salir = False
        while salir == False:
            try:
                numero = int(input(f"Ingrese el número ganador {i + 1}: "))
                #comprobar si el número está entre el 1 y el 49 y si es único en la lista
                if numero < 1 or numero > 49: raise ValueError
                if numeros_ganadores.count(numero) >= 1: raise ValueError
                numeros_ganadores.append(numero)
                salir = True
            except:
                print("Introduce un número válido único entre 1 al 49")
    
    numeros_ganadores.sort()
    return numeros_ganadores

def mostrar_loteria(numeros_loteria:list, reintegro:int) -> str:
    resultado = "Los numero ganadores ordenados de mayor a menor:\n" + ", ".join(str(numero) for numero in numeros_loteria) + "\n"
    resultado += "El reintegro es " + str(reintegro)
    return resultado

def main():
    print(mostrar_loteria(pedir_loteria(), pedir_reintegro()))
    
if __name__ == "__main__":
    main()