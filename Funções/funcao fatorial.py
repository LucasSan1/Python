def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n -1)

fat = int(input('Digite o numero do fatorial a ser calculado: '))
print(f'O fatorial de {fat} = {fatorial(fat)}')