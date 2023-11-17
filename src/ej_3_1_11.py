vector1 = (1, 2, 3)
vector2 = (-1, 0, 2)

def producto_escalar(vector1:tuple, vector2:tuple) -> str:
    escalar = [vector1[i] * vector2[i] for i in range(len(vector1))]
    return f"El producto escalar de {vector1} y {vector2} es: {escalar}"

def main():
    print(producto_escalar(vector1, vector2))
    
if __name__ == "__main__":
    main()