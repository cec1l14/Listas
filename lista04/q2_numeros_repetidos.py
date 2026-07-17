num = int(input("Informe um número: "))
maior = menor = num
soma = 0

while num != -1:
    if num == -1:
        break
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    soma += num
    num = int(input("Informe um número: "))

print(f"O menor número informado foi {menor}.")
print(f"O maior número informado doi {maior}.") 
print(f"A soma dos valores informados foi {soma}.")