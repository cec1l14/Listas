num = 1
soma = 0

while num < 501:
    if num%2 != 0 and num%3 == 0:
        soma += num
    num += 1

print(f"A soma dos ímpares múltiplos de 3 em [1,500] é igual a {soma}.")