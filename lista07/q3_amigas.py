codigo = {
    0: " ", 1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h",
    9: "i", 10: "j", 11: "k", 12: "l", 13: "m", 14: "n", 15: "o", 16: "p",
    17: "q", 18: "r", 19: "s", 20: "t", 21: "u", 22: "v", 23: "w", 24: "x",
    25: "y", 26: "z"
}

l_mensagem = []

num = int(input("Informe a mensagem para descodificar (-1 para): "))

while num != -1:
    
    l_mensagem.append(num)
    num = int(input("Informe a mensagem para descodificar (-1 para): "))
    
descod = ''

for i in l_mensagem:
    descod += codigo[i]

print(descod)