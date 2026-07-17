nota1 = float(input("Informe sua primeira nota: "))
nota2 = float(input("Informe sua segunda nota: "))

media = (nota1 + nota2)/2

if media >= 9.0 and media <= 10.0:
    print("Conceito A")
elif media >= 7.5:
    print("Conceito B")
elif media >= 6.0:
    print("Conceito C")
elif media >= 4.0:
    print("Conceito D")
else:
    print("Conceito E")