class Conta:
    def __init__(self, numero, titular, saldo, limite = 1000.0):
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
    def extrato(self):
        print("Olá {}, seu saldo é R${}".format(
            self.titular, 
            self.saldo))
        
    def deposita(self, valor):
        self.saldo += valor
        
    def saca(self, valor):
        self.saldo -= valor
