def vertical(palavra):
    for i in range(len(palavra)+1):
        print(palavra[:i])

def main():
    texto = input("Informe uma palavra: ")
    vertical(texto)

if __name__ == "__main__":
    main()