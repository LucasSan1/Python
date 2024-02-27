class Conta_corrente:
    # atributos
    def __init__(self, nome_titular, numero_conta, saldo):
        self.titular = nome_titular
        self.numero = numero_conta
        self.saldo = saldo
    
    # metodos
    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo insuficiente')
        else:
            self.saldo -= valor
            print(f'O saldo atual é de R${self.saldo:.2f}')
    def depositar(self, valor):
        self.saldo += valor
        print(f'O Saldo atual é de R${self.saldo:.2f}')
    def imprimir_extrato(self):
        print(f'Seu saldo é de R${self.saldo:.2f}')

