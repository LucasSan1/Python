from cliente import *
from conta_corrente import *

cliente1 = Cliente('Fulano', 1234)
cliente2 = Cliente('Beltrano', 5678)

cc1 = Conta_corrente(1, cliente1, 100)
cc2 = Conta_corrente(2, cliente2, 200)

print('Dados do cliente 1')
cliente1.exibir_dados()
print('Dados da conta corrente 1')
cc1.extrato()
print('*' * 10)
print('Dados do cliente 2')
cliente2.exibir_dados()
print('Dados da conta corrente 2')
cc2.extrato()