
lista = []

tam = int(input('Qual o tamanho da lista? '))

def vericalista(): 
    while len(lista) <= tam - 1:
        cont = int(input('Adicione os itens à lista: '))
        lista.append(cont)
   
    print('*' * 5, 'Verificando a lista', '*' * 5)
    print(f'O menor termo da lista é {min(lista)} \nO maior termo da lista é {max(lista)}')
    print(f'A soma dos termos da lista é {sum(lista)} \nA media dos termos é {sum(lista)/tam}')
    
vericalista()
