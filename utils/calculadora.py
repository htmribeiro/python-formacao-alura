"""
Python 3
Parte 2
Aula 07
Atividade 04
Sintaxe das funções
"""
def calculadora():
  primeiro_numero = float(input("Digite: ").strip())
  segundo_numero = float(input("Digite: ").strip())
  print("Digite o símbolo da operação desejada?")
  print("(+) | (-) | (*) | (/)")
  operador = input("")

  """ Implementar chamada das funções """
  if(operador == "+"):
    soma(primeiro_numero, segundo_numero)

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
