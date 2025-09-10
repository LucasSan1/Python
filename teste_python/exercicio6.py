nuns = []

while True:
    try:
        num = int(input("Digite um numero, para sair aperte enter: "))
        if num >= 0 and num <= 1000:
            nuns.append(num)
        else:
            print("O numero deve estar entre 0 e 1000")
    except ValueError as e:
        menor = min(nuns)
        maior = max(nuns)
        soma = sum(nuns)

        print(f" O maior numero é {maior} \n O menor numero é {menor} \n A soma de todos os numeros é {soma}")
        break
        