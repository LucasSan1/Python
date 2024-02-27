salario = float(input('Digite seu salario: '))

if salario <= 1000:
    reajuste = salario + salario * (20/100)
    aumento = 20
    valorAumento = reajuste - salario 


elif salario <= 1700:
    reajuste = salario + salario * (15/100)   
    aumento = 15
    valorAumento = reajuste - salario

elif salario <= 2300:
     reajuste = salario + salario * (10/100)
     aumento = 10
     valorAumento = reajuste - salario

else:
     reajuste = salario + salario * (5/100)
     aumento = 5
     valorAumento = reajuste - salario


print(f'Seu salário é de R${salario}') 
print(f'Seu aumento foi de {aumento}%') 
print(f'O valor do seu aumento foi R${valorAumento}') 
print(f'Seu novo salário é R${reajuste}')