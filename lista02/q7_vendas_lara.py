valor_produto = float(input("Informe o valor do produto: "))
forma_pagamento = input("Informe a forma de pagamento (Dinheiro/Cheque): ")

if forma_pagamento != "Dinheiro" and forma_pagamento != "Cheque":
    print("Forma de pagamento inválida")

else:
    if valor_produto >= 100.0 and forma_pagamento == "Dinheiro":
        valor_final = valor_produto - (valor_produto * 0.10)
    else:
        valor_final = valor_produto
        
    print(f"R$ {valor_final:.2f}")