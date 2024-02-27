from compras import adicionar_item, remover_item, mostrar_lista

compras = []
# loop principal da aplicaçao
while True:
    # Mostrar as opções do menu:
    print('Selecione uma opçao: ')
    print('1 - Adicionar itens à lista de compras')
    print('2 - Remover itens da lista de compras')
    print('3 - Mostrar os itens da lista de compras')
    print('4 - Sair')

    #  ler a opçao do menu selecionado pelo usuario
    opcao = int(input('Opção selecionada: '))

    if opcao == 1:
        # adicionar itens à lista de compras
        item = input('Digite o item a ser adicionado na lista de compras: ')
        adicionar_item(compras, item)
    elif opcao == 2:
        #  remover itens da lista
         if len(compras) == 0:
             print('Não há itens na lista de compras.')
         else:
              item = input('Digite o a ser removido da lista de compras: ')
              remover_item(compras, item)
    elif opcao == 3:
        #  mostrar os itens da lista
        mostrar_lista(compras)
    elif opcao == 4:
        # sair da aplicaçao
        print('Saindo ...')
        break

    else:
        # mostar uma mensagem caso a opçao digitada não estiver no menu
        print('Opção invalida, tente novamente!')
