meses = {
    "01": "janeiro",
    "02": "fevereiro",
    "03": "março",
    "04": "abril",
    "05": "maio",
    "06": "junho",
    "07": "julho",
    "08": "agosto",
    "09": "setembro",
    "10": "outubro",
    "11": "novembro",
    "12": "dezembro"
}

def extenso(dia, mes, ano):
    dia2 = int(dia)
    ano2 = int(ano)
    mes2 = meses[mes]

    return f"{dia2} de {mes2} de {ano2}"

def main():
    dia, mes, ano = input("Informe uma data: ").split("/")
    print(f"Data por extenso: {extenso(dia,mes,ano)}.")

if __name__ == "__main__":
    main()
