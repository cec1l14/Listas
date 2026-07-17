valor_divida = float(input("Informe o valor inicial da dívida: "))
juro_mensal = float(input("Informe o valor dos juros mensais: "))
valor_mensal = float(input("Informe o valor mensal que será pago: "))
total_pago = meses = total_juros = 0
valor_fixo = valor_divida
 
while valor_divida > 0:
    juros = (juro_mensal/100) * valor_divida
    valor_juros = valor_divida + juros
    total_juros += juros

    if valor_mensal > valor_juros:
        valor_mensal = valor_juros

    valor_divida = valor_juros - valor_mensal
    meses += 1
  
total_pago = valor_fixo + total_juros

print(f"A dívida será paga em {meses} meses.")
print(f"O total pago foi equivalente a R$ {total_pago:.2f}.")
print(f"O total de juros pago foi equivalente a R$ {total_juros:.2f}.")