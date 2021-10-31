# coding:utf-8
frutas = ['Banana', 'Maca', 'Pera', 'Uva', 'Melancia', 'Jamelao']

fruta_pedida = input('Qual é a fruta que deseja consultar? ').strip()

if(fruta_pedida.capitalize() in frutas):
  print('Sim, temos a fruta.')
else:
  print('Não temos a fruta.')