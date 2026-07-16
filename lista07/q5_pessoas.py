altura = []
sexo = []
feminino = []
masculino = []

for i in range(10):
    altura.append(float(input("Digite sua altura: ")))
    sexo.append(input("Digite seu sexo [M/F]: "))

maior = menor = altura[0]
indice_maior = indice_menor = 0

for i in range(10):
    if altura[i] > maior:
        maior = altura[i]
        indice_maior = i

    if altura[i] < menor:
        menor = altura[i]
        indice_menor = i

sexo_maior = sexo[indice_maior]
sexo_menor = sexo[indice_menor]

print(f"A maior altura é {maior}, cujo sexo do indivíduo é {sexo_maior}.")
print(f"A menor altura é {menor}, cujo sexo do indivíduo é {sexo_menor}.")

mulheres = homens = soma_mulher = soma_homem = 0

for i in range(10):
    if sexo[i] == 'F':
        mulheres += 1
        feminino.append(i)
        soma_mulher += altura[i]
    else:
        homens += 1
        soma_homem += altura[i]
if mulheres > 0:
    media_mulher = soma_mulher/mulheres
    print(f"A média de altura feminina é {media_mulher:.2f} cm.")
else: 
    print("Não é possível dividir por 0.")


if homens > 0:
    media_homem = soma_homem/homens
    print(f"A média de altura masculina é {media_homem:2f} cm.")
else: 
    print("Não é possível dividir por 0.")


print(f"Há {mulheres} pessoas do sexo feminino.")
print(f"Há {homens} pessoas do sexo masculino.")