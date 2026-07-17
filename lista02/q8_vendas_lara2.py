valor_produto = float(input("Informe o valor do produto: "))
forma_pagamento = input("Informe a forma de pagamento (Dinheiro/Cheque/Cartão): ")

if forma_pagamento != "Dinheiro" and forma_pagamento != "Cheque" and forma_pagamento != "Cartão":
    print("Forma de pagamento inválida")

elif forma_pagamento == "Cartão":
    funcao_cartao = input("Informe a função do cartão (Débito/Crédito): ")

    if funcao_cartao == "Crédito":
        num_parcelas = int(input("Informe o número de parcelas desejadas (1/2/3): "))

        if num_parcelas < 1 or num_parcelas > 3:
            print("Quantidade de parcelas inválida")
        else:
            valor_parcela = valor_produto/num_parcelas
            print(f"R$ {valor_produto:.2f}")
            print(f"{num_parcelas} parcelas de R$ {valor_parcela:.2f}")

    else:
        print(f"R$ {valor_produto:.2f}")

elif valor_produto >= 100.0 and forma_pagamento == "Dinheiro":
    valor_final = valor_produto - (valor_produto * 0.10)
    print(f"R$ {valor_final:.2f}")
    
else:
    print(f"R$ {valor_produto:.2f}")