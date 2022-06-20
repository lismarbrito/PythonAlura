class Conta:

    # Esta é a função contrutora que é chamada automaticamente após a constução do objeto.
    def __init__(self, numero, titular, saldo, limite):
        # "Self" é a referência que sabe o endereço da memória onde está o objeto.
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
