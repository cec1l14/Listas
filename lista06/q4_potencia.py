base = int(input("Informe a base do valor a ser calculado: "))
expoente = int(input("Informe o expoente do valor a ser calculado: "))
result = 1

for i in range(expoente):
    result *= base

print(f"{base}^{expoente} = {result}")