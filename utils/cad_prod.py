# Sistema de cadastros de produtos para mercado

class Produto(object):
  def __init__(self, nome, valor):
    self.__nome = nome
    self.__valor = valor
  
  def __repr__(self):
    return "nome: {} valor: {:f2}".format(self.__nome, self.__valor)
  
  def get_nome(self):
    return self.__nome

  def get_valor(self):
    return self.__valor