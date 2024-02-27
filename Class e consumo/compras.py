def adicionar_item(compras, item):
    compras.append(item)
    print('Item adicionado com sucesso!!')

def remover_item(compras, item):
    if item in compras:
        compras.remove(item)
        print('Item removido com sucesso!!')
    else:
        print('Item não encontrado!!')

def mostrar_lista(compras):
    if len(compras) == 0:
        print('Lista vazia!!')
    else:
        print('Lista de compras: ')
        for item in compras:
            print(item)