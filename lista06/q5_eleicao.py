num_total = int(input("Informe o número total de eleitores: "))
quant_1 = quant_2 = quant_3 = 0

for i in range(num_total):
    voto = int(input("Informe seu voto [1/2/3]: "))
    if voto == 1:
        quant_1 += 1
    elif voto == 2:
        quant_2 += 1
    else:
        quant_3 += 1

print(f"Candidato 1 recebeu {quant_1} voto(s).")
print(f"Candidato 2 recebeu {quant_2} voto(s).")
print(f"Candidato 3 recebeu {quant_3} voto(s).")