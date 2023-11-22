DICCIONARIO = {}

def preguntar_informacion():
    informacion_ok = True
    while informacion_ok:
        try:
            informacion = input("Articulo a añadir (para salir darle al enter): ")
            if informacion == "":
                informacion_ok = False
                return
            if DICCIONARIO.get(informacion) == None:
                precio_ok = True
                while precio_ok:
                    try:
                        precio = int(input(f"Introduce el precio de {informacion}: "))
                        DICCIONARIO[informacion] = precio
                        precio_ok = False
                    except:
                        print("Precio no válido")
            else:
                raise ValueError
        except:
            print("Tipo de dato repetido o inválido.")        
def formatear_diccionario():
    precio_total = 0
    print("Lista de la compra")
    for articulo, precio in DICCIONARIO.items():
        print(f"{articulo} ---- {precio}$")
        precio_total += precio
    print(f"Total --- {precio_total}$")
    

def main():
    preguntar_informacion()
    formatear_diccionario()
if __name__ == "__main__":
    main()