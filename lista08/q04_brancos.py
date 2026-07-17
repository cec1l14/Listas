def sem_brancos(palavra):
    nova_palavra = ""
    for i in palavra:
      if i != " ":
         nova_palavra += i
    
    return nova_palavra

def main():
   exemplo = input("Informe uma string: ")
   print(sem_brancos(exemplo))

if __name__ == "__main__":
   main()
