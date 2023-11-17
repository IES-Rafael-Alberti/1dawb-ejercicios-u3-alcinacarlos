precios = [50, 75, 46, 22, 80, 65, 8]

def menor_mayor(precios:list) -> str:
    precios.sort()
    return "El menor precio es " + str(precios[0]) + " y el mayor es " + str(precios[len(precios) - 1])

def main():
    print(menor_mayor(precios))
    
if __name__ == "__main__":
    main()