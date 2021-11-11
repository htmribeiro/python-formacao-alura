"""
python 3
OO Intro
Aula 09
Desafio Opcional
"""

class Data:
    
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        
    def formatada(self):
        print("{}/{}/{}".format(self.dia, self.mes, self.ano))