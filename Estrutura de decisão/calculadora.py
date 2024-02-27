import math
print('_=_' * 8)
print('Tabela de operadores \n Adição = + \n Subtração = - \n Multiplicação = x ou * \n Divisão = / ou : \n Potenciação = ^ ou ** \n raiz quadrada = raiz \n Numero par ou Impar = par ou impar')
print('_=_' * 8)
print('')
num_1 =  float(input('Digite o primeiro numero: '))
opera = input('escolha a operaçao: ')


if opera == '+':
    num_2 = float(input('Digite o segundo numero: '))
    resultado = num_1 + num_2
    print(f'{num_1} + {num_2} = {resultado}')

elif opera == '-':
    num_2 = float(input('Digite o segundo numero'))
    resultado = num_1 - num_2
    print(f'{num_1} - {num_2} = {resultado}')

elif opera == 'x' or opera == '*':
    num_2 = float(input('Digite o segundo numero'))
    resultado = num_1 * num_2
    print(f'{num_1} x {num_2} = {resultado}')

elif opera == '^' or opera == '**':
    num_2 = float(input('Digite o segundo numero'))
    resultado = math.pow(num_1, num_2)  
    print(f'{num_1} ^ {num_2} = {resultado}')

elif opera == '/' or opera ==':':
    num_2 = float(input('Digite o segundo numero'))
    resultado = num_1 / num_2
    print(f'{num_1} / {num_2} = {resultado}')

elif opera == 'raiz':
    resultado = math.sqrt(num_1)
    print(resultado)

elif opera == 'par' or opera == 'impar':
    resultado = num_1 %2 
    if resultado == 0:
        print('Numero par')
    else:
        print('Numero impar')
else:
    print('Operaçao invalida')

