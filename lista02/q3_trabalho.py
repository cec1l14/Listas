ganho_hora = float(input("Informe o ganho por hora: "))
num_horas = int(input("Informe o número de horas trabalhadas no mês: "))

salario_bruto = ganho_hora * num_horas
ir = (11 * salario_bruto)/100
inss = (8 * salario_bruto)/100
sindicato = (5 * salario_bruto)/100
salario_liquido = salario_bruto - (ir + inss + sindicato)

print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"IR (11%): R$ {ir:.2f}")
print(f"INSS (8%): R$ {inss:.2f}")
print(f"Sindicato (5%): R$ {sindicato:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")