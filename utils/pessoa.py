""" 
Python 3
OO Intro
Aula 02
O problema de Chalita
"""

class Pessoa:
	def __init__(self, nome, sobrenome):
		self.nome = nome
		self.sobrenome = sobrenome

	def exibe_nome_sobrenome(self):
		print("{0} {1}".format(self.nome, self.sobrenome))
