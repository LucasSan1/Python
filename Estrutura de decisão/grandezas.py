print('*' * 30)
print('CÁLCULO DE GRANDEZAS ELÉTRICAS')
print('*' * 30)
print(' 1. Tensão (em volts) \n 2. Resistência (em Ohm) \n 3. Corrente (em Ampére) \n 4. Sair do programa')
print('*' * 30)
grandeza = input('Qual grandeza deseja calcular? ')

if grandeza == '1':
    r = int(input('Qual valor da resistência? '))
    i = int(input('Qual valor da corrente? '))
    u = r * i
    print(f'A tensão é de {u} Volts')
elif grandeza == '2':
    u = int(input('Qual valor da Tensão? '))
    i = int(input('Qual valor da corrente? '))
    r =  u / i
    print(f'A resistência é de {r} Ohm')
elif grandeza == '3':
    u = int(input('Qual valor da Tensão? '))
    r = int(input('Qual valor da Resistência? '))
    i =  u / r
    print(f'O valor da corrente é de {i} Ampéres')
elif grandeza == '4': 
    print('Você escolheu a opção sair')
else:
    print('Escolha invalida')