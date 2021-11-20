class Conta:
    def __init__(self, numero, titular, saldo=0.0, limite=1000.0):
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__tarifaTransferencia = 8.0

    def extrato(self):
        print("Olá {}, seu saldo é R${}".format(
            self.__titular,
            self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor

    def __saldo_disponivel(self, valor):
        return valor <= self.__saldo + self.__limite        
    
    def saca(self, valor):
        if valor < 10:
            print("Valor incorreto...\nSaque mínimo de R$10,00") 
        elif self.__saldo_disponivel(valor):
            self.__saldo -= valor
            print("Saque efetado com sucesso!")
        else:
            print("Saldo insuficiente.")

    def transfere(self, valor, destino):
        valor_total = valor + self.__tarifaTransferencia
        if valor <= 0:
            print("Valor incorreto...")
        elif self.__saldo_disponivel(valor_total):
            self.__saldo -= valor_total
            destino.deposita(valor)
            print("Transferência efetuada com sucesso!")
        else:
            print("Saldo insuficiente.")

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"
    
    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}