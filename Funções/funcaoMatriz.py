from array import *
matriz = [[0,0,0],
          [0,0,0],
          [0,0,0]
]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input('Digite um valor: '))
print(f'Matriz = {matriz}')