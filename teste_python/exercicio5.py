nuns = []

while True:
    try:
        num = int(input("Digite um numero, para sair aperte enter: "))
        nuns.append(num)
    except ValueError as e:
        menor = min(nuns)
        maior = max(nuns)
        soma = sum(nuns)

        print(f" O maior numero é {maior} \n O menor numero é {menor} \n A soma de todos os numeros é {soma}")
        break
        

   


