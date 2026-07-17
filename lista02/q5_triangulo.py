lado1 = float(input("Informe o primeiro lado do triângulo: "))
lado2 = float(input("Informe o segundo lado do triângulo: "))
lado3 = float(input("Informe o terceiro lado do triângulo: "))

if (lado1 == lado2) and (lado1 == lado3):
    print("Triângulo Equilátero")
elif (lado1 != lado2) and (lado1 != lado3) and (lado2 != lado3):
    print("Triângulo Escaleno")
else:
    print("Triângulo Isósceles")