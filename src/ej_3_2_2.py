def generar_diccionrio() -> dict:
    informacion = {
    'Nombre': input("Ingresa tu nombre: "),
    'Edad': input("Ingresa tu edad: "),
    'Dirección': input("Ingresa tu dirección: "),
    'Teléfono': input("Ingresa tu número de teléfono: ")
    }
    
    return informacion

def main():
    informacion = generar_diccionrio()
    print(f"{informacion['Nombre']} tiene {informacion['Edad']} años, vive en {informacion['Dirección']} y su número de teléfono es {informacion['Teléfono']}")
    
if __name__ == "__main__":
    main()