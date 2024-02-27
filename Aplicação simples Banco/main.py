from conta_corrente import *

contas = []
class Main:
    print('Bem vindo ao banco IANES, Selecione uma opção: \n1 - Criar a conta \n2 - Sacar \n3 - depositar \n4 - Extrato \n5 - Sair')
   
while True:
    opcao = int(input('Digite a opção desejada: '))
       
    if opcao == 1:
        nome = input('Digite o nome do titular: ')
        numero = input('Digite o numero da conta: ')
        saldo = float(input('Digite o saldo da conta: '))
        cc1 = Conta_corrente(nome, numero, saldo)
        contas.append(cc1)
        print('Conta criada')

    elif opcao == 2:
        if len(contas) == 0:
            print('Não há conta criada')
        else:    
            valor_saque = float(input('Digite um valor para o saque: '))
            cc1.sacar(valor_saque)

    elif opcao == 3:
        if len(contas) == 0:
            print('Não há conta criada')
        else:    
            deposito = float(input('Digite o valor do deposito: '))
            cc1.depositar(deposito)

    elif opcao == 4:
        if len(contas) == 0:
            print('Não há conta criada')
        else:    
            cc1.imprimir_extrato()

    elif opcao == 5:
        print('Saindo....')
        break