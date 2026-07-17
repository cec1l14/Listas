def mostrar(palavra):
    tamanho = len(palavra)
    return palavra, tamanho

def tamanho(palavra1, palavra2):
    if len(palavra1) == len(palavra2):
        return "possuem o mesmo comprimento"
    else:
        return "não possuem o mesmo comprimento"

def conteudo(palavra1, palavra2):
    if palavra1 == palavra2:
        return "possuem o mesmo conteúdo"
    else:
        return "não possuem o mesmo conteúdo"
    
def main():
    primeira = input("Informe a primeira palavra: ")
    segunda = input("Informe a segunda palavra: ")
    print(mostrar(primeira))
    print(mostrar(segunda))
    print(f"As strings '{primeira}' e '{segunda}' {tamanho(primeira,segunda)}.")
    print(f"As strings '{primeira}' e '{segunda}' {conteudo(primeira,segunda)}.")

if __name__ == "__main__":
    main()