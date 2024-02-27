def par_impar(a):
    if a %2 == 0:
        return 'é par'
    else:
        return 'é impar'
    
def positivo_negativo(b):
    if b > 0:
        print(f'o numero {b} é positivo e {par_impar(b)}')
    elif b < 0:
        print(f'O numero {b} é negativo e {par_impar(b)}')
    else:
        print(f'O numero {b} é neutro')
    
n = int(input('Digite um numero: '))

par_impar(n)
positivo_negativo(n)