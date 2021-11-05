import random

def carrega_palavra_secreta(nome_arquivo="others\\words.txt"
                            , primeira_linha_valida=0):
    arquivo = open(nome_arquivo, "r", encoding="utf-8")
    
    palavras = [linha.strip() for linha in arquivo]
    
    # for linha in arquivo:
    #   linha = linha.strip()
    #   palavras.append(linha)
      
    arquivo.close()

    numero = random.randrange(primeira_linha_valida, len(palavras))
    palavra_secreta = palavras[numero].upper()

    print(palavra_secreta)

if(__name__ == '__main__'):
  carrega_palavra_secreta("others\\fruits.txt")