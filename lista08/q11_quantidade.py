def quantidade(numero):
    digitos = len(str(numero))

    return digitos

def main():
    num = int(input("Informe um número: "))
    print(f"O número {num} possui {quantidade(num)} dígitos.")

if __name__ == "__main__":
    main()

