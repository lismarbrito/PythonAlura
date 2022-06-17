# Aprendendo sobre funções contrutoras


class Conta:
    # Esta é a função contrutora que é chamada automaticamente após a constução do objeto.
    # "Self" é a referência que sabe o endereço da memória onde está o objeto.
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...{}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("O saldo de {} do titular {}".format(self.saldo, self.titular))

    def deposito(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor

