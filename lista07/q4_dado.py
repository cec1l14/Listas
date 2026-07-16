import random

resultados = []
q1 = q2 = q3 = q4 = q5 = q6 = 0

n = int(input("Informe um número: "))
if n == 0:
    print("Não é possível gerar resultados para 0 lançamentos.")
else:
    for i in range(n):

        if i == 1:
            q1 += 1
        elif i == 2:
            q2 += 1
        elif i == 3:
            q3 += 1
        elif i == 4:
            q4 += 1
        elif i == 5:
            q5 += 1
        else:
            q6 += 1

        resultados.append(random.randint(1,6))

p1 = (q1/n) * 100
p2 = (q2/n) * 100
p3 = (q3/n) * 100
p4 = (q4/n) * 100
p5 = (q5/n) * 100
p6 = (q6/n) * 100

print(f"Porcentagem (face 1): {p1:.2f} %")
print(f"Porcentagem (face 2): {p2:.2f} %")
print(f"Porcentagem (face 3): {p3:.2f} %")
print(f"Porcentagem (face 4): {p4:.2f} %")
print(f"Porcentagem (face 5): {p5:.2f} %")
print(f"Porcentagem (face 6): {p6:.2f} %")