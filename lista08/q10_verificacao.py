def verificacao(valor):
    if valor > 0:
        return 'P'
    else:
        return 'N'
    
def main():
    exemplo = int(input("Informe um valor: "))
    print(verificacao(exemplo))