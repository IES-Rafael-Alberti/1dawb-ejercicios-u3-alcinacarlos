DICCIONARIO = {}

def preguntar_informacion():
    informacion_ok = True
    while informacion_ok:
        try:
            informacion = input("Tipo de dato a introducir(ej nombre), para salir darle al enter: ")
            if informacion == "":
                informacion_ok = False
                return
            if DICCIONARIO.get(informacion) == None:
                DICCIONARIO[informacion] = input(f"Introduce tu {informacion}: ")
            else:
                raise ValueError
            print(DICCIONARIO)
        except:
            print("Tipo de dato repetido o inválido.")        


def main():
    preguntar_informacion()
if __name__ == "__main__":
    main()