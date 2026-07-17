import random

def sorteio(listas):
    result = random.choice(listas)

    return result

def tentativas(variavel):
    tentativas = 0
    lista = ['_']*(len(variavel))

    while tentativas < 7:
        letra = input("Digite uma letra: ")

        if letra not in variavel:
            tentativas += 1
            if tentativas == 6:
                print("Você perdeu!")
                break
            print(f"Você errou pela {tentativas}ª vez. Tente de novo!")
    
        else: 
            for i in range(len(variavel)):
                if variavel[i] == letra:
                    lista[i] = letra
            print(f"A palavra é: {lista}")


        if '_' not in lista:
            print("Parabéns! Você venceu!")
            break   

def main():
    lista = []
    palavra = input("Digite uma palavra [-1 para]: ")
    
    while palavra != "-1":
        lista.append(palavra)
        palavra = input("Digite uma palavra [-1 para]: ")

    sorteada = sorteio(lista)

    tentativas(sorteada)

if __name__ == "__main__":
    main()