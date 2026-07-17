def remover(variavel):
    result = ''
    for i in variavel:
        if i != '.' and i != '-':
            result += i
    return result


def penultimo(resultado):
    soma = 0
    indice = 0
    for i in range(10, 1, -1):
        soma += (int(resultado[indice]) * i)
        indice += 1

    resto = soma%11

    if resto == 0 or resto == 1:
        penultimo = 0
    else:
        penultimo = 11 - resto

    return penultimo


def ultimo(resultado2):
    soma = 0
    indice = 0
    for i in range(11, 1, -1):
        soma += (int(resultado2[indice]) * i)
        indice += 1
    
    resto = soma%11

    if resto == 0 or resto == 1:
        ultimo = 0
    else:
        ultimo = 11 - resto

    return ultimo


def verificacao(cpf, pen_calc, ult_calc):
    if pen_calc == int(cpf[-2])  and ult_calc == int(cpf[-1]):
        return "é válido"
    else:
        return "não é válido"
    
def main():
    cpf = input("Digite o CPF no formato {xxx.xxx.xxx-xx}: ")
    cpf_limpo = remover(cpf)
    digito_pen = penultimo(cpf_limpo)
    digito_ult = ultimo(cpf_limpo)
    final = verificacao(cpf_limpo, digito_pen, digito_ult)

    print(f"O CPF {cpf} {final}.")

if __name__ == "__main__":
    main()