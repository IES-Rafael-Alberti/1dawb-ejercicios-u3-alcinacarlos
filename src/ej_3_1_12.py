vector1 = ((1, 2), (3, 4), (5, 6))
vector2 = ((-1, 0), (0, 1) ,(1, 1))

def producto_escalar(vector1: tuple, vector2: tuple) -> tuple:
    resultado = tuple(tuple(vector1[i][x] * vector2[i][x] for x in range(len(vector1[i]))) for i in range(len(vector1)))
    return resultado

def main():
    print(producto_escalar(vector1, vector2))
    
if __name__ == "__main__":
    main()