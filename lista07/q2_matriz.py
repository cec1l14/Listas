matriz = [[None]*3 for i in range(0,3)]
linha = []
coluna = []

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input("Informe um valor: "))

for i in range(3):
        linha.append(matriz[1][i])
        coluna.append(matriz[i][1])

for i in range(3):
        matriz[1][i] = coluna[i]
        matriz[i][1] = linha[i]

for i in matriz:
    print(i)