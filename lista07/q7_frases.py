frase = input("Digite uma frase: ")

while frase != "-1":

    dicionario = {}

    for i in frase:
        if i in dicionario:
            dicionario[i] += 1
        else:
            dicionario[i] = 1

    print(f"Dicionário -> {dicionario}")
    

    frase = input("Digite uma frase: ")

