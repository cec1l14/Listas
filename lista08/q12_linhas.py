def escada(linhas):
    lista = []
    for i in range(1, linhas + 1):
        for j in range(i):
            lista.append(i)

        print(*lista)
        lista = []

def main():
    n = int(input("Informe um valor: "))
    escada(n)

if __name__ == "__main__":
    main()