d_inicial = float(input("Informe o valor do depósito inicial: "))
taxa_juros = float(input("Informe a taxa de juros (em %): ")) / 100
total_juros = 0

for i in range(1,25):
    total_juros += taxa_juros * d_inicial
    d_inicial = (taxa_juros * d_inicial) + d_inicial
    print(f"O valor referente ao mês {i} é igual a R$   {d_inicial:.2f}.")
  
print(f"O valor total de juros foi equivalente a R$ {total_juros:.2f}.")