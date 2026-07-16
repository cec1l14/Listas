def soma(num1, num2, num3):
    return num1 + num2 + num3

def main():
    n1 = int(input("Informe o primeiro número: "))
    n2 = int(input("Informe o segundo número: "))
    n3 = int(input("Informe o terceiro número: "))

    print(f"A soma entre {n1}, {n2} e {n3} equivale a {soma(n1,n2,n3)}.")

if __name__ == "__main__":
    main()