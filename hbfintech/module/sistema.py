class Sistema:
  
	def __init__(self):
		self.texto = ''

	def le_entrada(self):
		self.texto = input("Digite o Texto: ")

	def exibe_saida(self):
		print(self.texto)