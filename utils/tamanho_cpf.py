"""
Python 3
OO Avançado
Aula 08
Atributos de classe
"""
class Pessoa:
  tamanho_cpf = 11
  
p = Pessoa()

print(p.tamanho_cpf)

p.tamanho_cpf = 12

print(p.tamanho_cpf)

print(Pessoa.tamanho_cpf)