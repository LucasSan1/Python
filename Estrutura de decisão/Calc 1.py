while True:
    try:
        num1 = float(input('Digite o primeiro número: '))
        operacao = input('Escolha a operação (+, -, x, /): ').strip()
        if operacao in ('+', '-', 'x','/'):
            break
        else:
            print('Operação inválida.')
    except ValueError:
        print('Valor invalido!')

while True:
    try:
        num2 = float(input('Digite o segundo número: '))
        break
    except ValueError:
        print('O valor deve ser numerico!')

if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao in ('x', '*'):
    resultado = num1 * num2
elif operacao in ('/', ':'):
    if num2 == 0:
        resultado = 'Divisão por zero não permitida.'
    else:
        resultado = num1 / num2
else:
    resultado = 'Operação inválida'

print(f'O resultado é {resultado}')
