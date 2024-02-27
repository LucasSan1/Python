salario = float(input('Informe seu salario: '))

if salario <= 1302:
    desconto = 7.50 / 100 
    porcenINSS = '7.50%'
elif salario <= 2571.29:
    desconto =  (9 / 100)
    porcenINSS = '9%'
elif salario <= 3856.94:
    desconto =  (12 / 100)
    porcenINSS = '12%'
elif salario <= 7507.49:
    desconto =  (14 / 100)
    porcenINSS = '14%'
else:
    desconto = (14 / 100)
    porcenINSS = '14%'

desINSS = salario - (salario * desconto)
valorDescontado = salario - desINSS
    
if desINSS <= 1903.98:
    desIRRF =  desINSS
    porcem = 'Insento'
elif desINSS >= 1903.99 and desINSS <= 2826.65:
    desIRRF = (7.5/100)
    porcem = '7.5%'
elif desINSS >= 2826.66 and desINSS <= 3751.05:
    desIRRF =  (15 / 100)
    porcem = '15%'
elif desINSS >= 3751.05 and desINSS <= 4664.68:
    desIRRF = (22.5 / 100)
    porcem = '22.5%'
else:
    desIRRF = (27.5 /100)
    porcem = '27.5%'

descontoIRRF = desINSS -  (desINSS * desIRRF) 
valorIRRF = desINSS - descontoIRRF

print(f'Seu salario sem descontos é de R${salario}')
print(f'Desconto do INSS {porcenINSS}, o valor do desconto é de R${valorDescontado}')

if porcem == 'Insento':
    print(f'Desconto do IRRF {porcem}')
else: 
     print(f'Desconto do IRRF {porcem}, o valor do desconto é de R${valorIRRF:.2f}')

print(f'Seu salario após descontos é de R${descontoIRRF:.2f}')


