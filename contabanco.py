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

    def __pode_sacar(self, valor_a_sacar):
        disponivel_para_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= disponivel_para_sacar

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino):
        self.saca
        destino.deposita(valor)

    # def get_saldo(self):
    #    return self.__saldo
    # Podemos utilizar propriedades (abaixo) ao invés de usar a terminologia get/set. Assim podemos chamar pelo nome original como se estivesse acessadno atributo. Mas estamos acessadno o método
    @property
    def saldo(self):
        return self.__saldo

    # def get_titular(self):
    #    return self.__titular
    # Podemos utilizar propriedades (abaixo) ao invés de usar a terminologia get/set. Assim podemos chamar pelo nome original como se estivesse acessadno atributo. Mas estamos acessadno o método
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
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': 237}
