"""
Python 3 
parte 2 
Aula 05 
Atividade 02 
Calculando o total de caracteres em um loop
"""
total = 0
palavra = "python rocks!"
acabou = False
while(not acabou):
  acabou = ( total == len(palavra) )
  total += 1
print(total - 1)
