pop_X = 70000
pop_Y = 180000
anos = 0

while pop_X < pop_Y:
    pop_X = pop_X + (0.035 * pop_X)
    pop_Y = pop_Y + (0.015 * pop_Y)
    anos += 1

print(f"Serão necessários {anos} anos para que a população do país X seja superior à do país Y.")