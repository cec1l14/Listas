num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
num_tela = num1
divisao = 0

while (num1 - num2) >= 0:
    if (num1 - num2) >= 0:
        divisao += 1
        num1 -= num2
    

print(f"A divisão entre {num_tela} e {num2} é igual a {divisao}.")
print(f"O resto da divisão é {num1}.")