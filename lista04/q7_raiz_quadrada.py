b = 2
n = int(input("Informe um número para o cáculo da raiz quadrada: "))
p = (b + (n/b))/2

while abs(b-p) >= 0.0001:
    b = p
    p = (b + (n/b))/2

print(f"{b} e {p} representam o valor da raiz quadrada de {n}.")