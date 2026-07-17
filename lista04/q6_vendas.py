cod = int(input("Informe o código da compra (1/2/3/4/5): "))
quantidade = total_1 = total_2 = total_3 = total_4 = total_5 = total = 0

while cod != 0:
    if cod != 1 and cod != 2 and cod != 3 and cod != 4 and cod != 5: 
        print("Código inválido.")
    elif cod == 1:
        quantidade = int(input("Informe a quantidade de produtos que você deseja: "))
        total_1 = quantidade * 5.5
    elif cod == 2: 
        quantidade = int(input("Informe a quantidade de produtos que você deseja: "))
        total_2 = quantidade * 2.3
    elif cod == 3:
        quantidade = int(input("Informe a quantidade de produtos que você deseja: "))
        total_3 = quantidade * 4.75
    elif cod == 4:
        quantidade = int(input("Informe a quantidade de produtos que você deseja: "))
        total_4 = quantidade * 6.8
    elif cod == 5:
        quantidade = int(input("Informe a quantidade de produtos que você deseja: "))
        total_5 = quantidade * 9.3
    cod = int(input("Informe o código da compra (1/2/3/4/5): "))

total = total_1 + total_2 + total_3 + total_4 + total_5
print(f"O valor total das compras foi R$ {total:.2f}.")