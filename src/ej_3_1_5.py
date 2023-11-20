def numeros_del_1_al_10() -> str:
    numeros = tuple(i for i in range(1, 11))
    return numeros
    
def main():
    print(numeros_del_1_al_10()[::-1])
    
if __name__ == "__main__":
    main()