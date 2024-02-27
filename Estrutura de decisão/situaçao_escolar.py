nota1 = float(input('Digite sua nota do primeiro bimestre: '))
nota2 = float(input('Digite sua nota do segundo bimestre: '))
nota3 = float(input('Digite sua nota do terceiro bimestre: '))
nota4 = float(input('Digite sua nota do quarto bimestre: '))

media = (nota1 + nota2 + nota3 + nota4)/4

print(f'Sua nota no primeiro bimestre foi {nota1} \n No segundo bimestre foi {nota2} \n No terceiro bimestre {nota3} \n No quarto bimestre foi {nota4}')
print(f'Sua media geral foi {media}')

if media >= 9.0 and media <= 10:
    print('Seu conceito foi A \n VOCÊ ESTÁ APROVADO')
elif media >= 7.5 and media <= 8.9:
    print('Seu conceito foi B \n VOCÊ ESTÁ APROVADO')
elif media >= 6.0 and media <= 7.4:
    print('Seu conceito foi C \n VOCÊ ESTÁ APROVADO')
elif media >= 4.0 and media <= 5.9:
    print('Seu conceito foi D \n VOCÊ ESTÁ REPROVADO')
else:
    print('Seu conceito foi E \n VOCÊ ESTÁ REPROVADO')



