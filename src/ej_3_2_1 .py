diccionario_divisas = {'Euro': '€', 'Dolar': '$', 'Yen': '¥'}

def comprobar_divisa(divisa:str) -> str:
    simbolo = diccionario_divisas.get(divisa, "Divisa no encontrada")
    print(simbolo)

def main():
    divisa_usuario = input("Ingresa el nombre de una divisa: ").capitalize()
    comprobar_divisa(divisa_usuario)
    
if __name__ == "__main__":
    main()