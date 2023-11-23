FRUTAS = {'platano': 1.35, 'manzana': 0.80, 'pera': 0.85, 'naranja': 0.70}
def preguntar_kilos() -> int:
    try:
        kg = int(input("Introduce los kg: "))
        return kg
    except:
        print("No has introducido bien los kilos")

def calcular_precio() -> float:
    fruta = input("Introduce una fruta: ").lower()
    if fruta in FRUTAS:
        kg = preguntar_kilos()
        precio_total = FRUTAS[fruta] * kg
        print(f"Precio total: {precio_total} $")
    else:
        print("Fruta no válida")

def main():
    calcular_precio()
if __name__ == "__main__":
    main()