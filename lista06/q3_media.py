n = int(input("Informe a quantidade de pessoas: "))
soma = 0

for i in range(1, n + 1):
    idade = int(input(f"Informe a idade da pessoa {i}: "))
    soma += idade

media = soma/n

if media >= 0 and media <= 25:
    estado = "jovem" 
elif media <= 60:
    estado = "adulta"
else:
    estado = "idosa"

print(f"A turma é {estado}.")