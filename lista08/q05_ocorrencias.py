def ocorrencia(frase):
    dicionario = {}

    for i in frase:
        if i in dicionario:
            dicionario[i] += 1
        else:
            dicionario[i] = 1
    
    return dicionario

def main():
    texto = input("Informe um frase: ")
    print(ocorrencia(texto))

if __name__ == "__main__":
    main()