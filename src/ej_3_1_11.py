vector1 = (1, 2, 3)
vector2 = (-1, 0, 2)

def producto_escalar(vector1:tuple, vector2:tuple) -> str:
    escalar = [vector1[i] * vector2[i] for i in range(len(vector1))]
    return escalar

def main():
    escalar = producto_escalar(vector1, vector2)
    print("El prodcuto escalar de {} y {} es: {}".format(vector1, vector2, escalar))
    
if __name__ == "__main__":
    main()