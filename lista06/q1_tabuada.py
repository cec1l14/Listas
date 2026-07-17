num = int(input("Informe um número entre 1 e 10:  "))

print(f"Tabuada de {num}:\n")

for i in range(1,11):
    print(num, "X", i, "=", num*i)