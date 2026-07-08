lista1 = []
lista2 = []
lista3 = [0]*10

for i in range(1,6):
    lista1.append(int(input(f"Lista{[i]}: ")))

for i in range(1,6):
    lista2.append(int(input(f"Lista{[i]}: ")))

for i in range(5):
    lista3[i*2] = lista1[i]
    lista3[i*2+1] = lista2[i]

print(lista3)