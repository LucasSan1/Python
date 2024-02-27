import math

def potencia(a, b):
    return math.pow(a, b)

a = int(input('Digite o numero para a base: '))
b = int(input('Digite o numero para o exponente: '))

print(f'{a} ^ {b} = {potencia(a, b)}')
