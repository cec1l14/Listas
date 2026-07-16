N = int(input("Informe a quantidade de coordenadas: "))
coordenadas = []
distancias = []

for i in range(1, N + 1):
    X = int(input(f"Informe o valor de x{i}: "))
    Y = int(input(f"Informe o valor de y{i}: "))
    coordenada = (X, Y)

    coordenadas.append(coordenada)

for i in range(N):
    for j in range(i + 1, N):
        dist = dist = (((coordenadas[j][0] - coordenadas[i][0]) ** 2) + ((coordenadas[j][1] - coordenadas[i][1]) ** 2)) ** 0.5
        distancias.append(dist)

maior = menor = distancias[0]
soma = 0

for i in distancias:

    soma += i

    if i > maior:
        maior = i
    if i < menor:
        menor = i

media = soma/len(distancias)

print(f"A maior distância entre os pontos foi {maior:.2f} u.d.")
print(f"A menor distância entre os pontos foi {menor:.2f} u.d.")
print(f"A média das distâncias calculadas é {media:.2f}.")

print(coordenadas)
print(distancias)