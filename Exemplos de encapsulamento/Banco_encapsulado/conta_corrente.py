class Conta_corrente:
    def __init__(self, numero_conta, cliente, saldo_inicial):
        self.__numero = numero_conta
        self.__cliente = cliente
        self.__saldo = saldo_inicial

    def sacar(self, valor):
        if valor > self.__saldo:
            print('Saldo insuficiente!')
        else:
            self.__saldo -= valor
            print(f'Saque realizado! Novo saldo: R%{self.__saldo}')

    def depositar(self, valor):
        self.__saldo += valor
        print(f'Valor depositado! Novo saldo: R${self.__saldo}')
    
    def extrato(self):
        print(f'Numero da conta: {self.__numero}')
        self.__cliente.exibir_dados()
        print(f'Saldo da conta: R${self.__saldo}')