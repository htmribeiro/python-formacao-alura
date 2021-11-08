# coding:utf-8
frutas = ['banana', 'maçã', 'pêra', 'uva', 'melancia', 'jamelão']

fruta_pedida = input('Qual é a fruta que deseja consultar? ').strip().lower()

if(fruta_pedida in frutas):
  print('Sim, temos {} em nossa lista de frutas. [Item: {}]'.format(
    fruta_pedida.capitalize(), frutas.index(fruta_pedida)))
else:
  print('Desculpe, a {} não está na lista de frutas.'.format(
    fruta_pedida.capitalize()))
