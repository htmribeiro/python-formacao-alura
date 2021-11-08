"""
Python 3
Parte 2
Aula 07
Atividade 04
Sintaxe das funções
"""
def calculadora():
  while(True):
    primeiro_numero = float(input("Digite: ").strip())
    segundo_numero = float(input("Digite: ").strip())
    print("Digite o símbolo da operação desejada?")
    print("(+) | (-) | (*) | (/)")
    
    operador = input("").strip().upper()

    """ Implementar chamada das funções """
    if(operador == "+"):
      soma(primeiro_numero, segundo_numero)
    
    elif(operador == "-"):
      subtrai(primeiro_numero, segundo_numero)
      
    elif(operador == "*"):
      multiplica(primeiro_numero, segundo_numero)
    
    elif(operador == "/"):
      divide(primeiro_numero, segundo_numero)
  
    print()
    entrada = input("(S) para SAIR.\n").strip().upper()
    if (entrada == "S"):
      break

""" Declaração das funções """
def soma(primeiro_numero, segundo_numero):
  print(primeiro_numero + segundo_numero)


def subtrai(primeiro_numero, segundo_numero):
  print(primeiro_numero - segundo_numero)


def multiplica(primeiro_numero, segundo_numero):
  print(primeiro_numero * segundo_numero)


def divide(primeiro_numero, segundo_numero):
  print(primeiro_numero / segundo_numero)


if(__name__ == "__main__"):
  calculadora()
"""
Python 3
Parte 2
Aula 07
Atividade 04
Sintaxe das funções
"""
def calculadora():
  while(True):
    primeiro_numero = float(input("Digite: ").strip())
    segundo_numero = float(input("Digite: ").strip())
    print("Digite o símbolo da operação desejada?")
    print("(+) | (-) | (*) | (/)")
    
    operador = input("").strip().upper()

    """ Implementar chamada das funções """
    if(operador == "+"):
      soma(primeiro_numero, segundo_numero)
    
    elif(operador == "-"):
      subtrai(primeiro_numero, segundo_numero)
      
    elif(operador == "*"):
      multiplica(primeiro_numero, segundo_numero)
    
    elif(operador == "/"):
      divide(primeiro_numero, segundo_numero)
  
    print()
    entrada = input("(S) para SAIR.\n").strip().upper()
    if (entrada == "S"):
      break

""" Declaração das funções """
def soma(primeiro_numero, segundo_numero):
  print(primeiro_numero + segundo_numero)


def subtrai(primeiro_numero, segundo_numero):
  print(primeiro_numero - segundo_numero)


def multiplica(primeiro_numero, segundo_numero):
  print(primeiro_numero * segundo_numero)


def divide(primeiro_numero, segundo_numero):
  print(primeiro_numero / segundo_numero)


if(__name__ == "__main__"):
  calculadora()
