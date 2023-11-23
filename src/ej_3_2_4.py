MESES = {
    1: 'Enero',
    2: 'Febrero',
    3: 'Marzo',
    4: 'Abril',
    5: 'Mayo',
    6: 'Junio',
    7: 'Julio',
    8: 'Agosto',
    9: 'Septiembre',
    10: 'Octubre',
    11: 'Noviembre',
    12: 'Diciembre'
}

def preguntar_fecha() -> tuple:
    fecha_ok = True
    while fecha_ok:
        try:
            fecha = input("Introduce la fecha en este formato (dd/mm/aaaa): ")
            partes = fecha.split('/')
            dia = int(partes[0])
            mes = int(partes[1])
            año = int(partes[2])
            if 1 <= dia <= 31 and 1 <= mes <= 12 and 2000 <= año <= 3000:
                mes = MESES[mes]
                return dia, mes, año
            raise ValueError
        except:
            print("Formato fecha inválida, vuelve a intentarlo")
            

def main():
    dia, mes ,año = preguntar_fecha()
    print(f"{dia} de {mes} de {año}")
if __name__ == "__main__":
    main()