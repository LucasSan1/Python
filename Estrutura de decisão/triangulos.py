lado_1 = int(input('Digite o primeiro lado do triangulo'))
lado_2 = int(input('Digite o segundo lado do triangulo'))
base= int(input('Digite a base do triangulo'))

if (lado_1 < lado_2 + base) and (lado_2 < lado_1 + base) and (base < lado_1 +lado_2):
    
    if (lado_1 == lado_2) and (lado_1 == base):
        print('Triangulo equilatero')
    elif (lado_1 == lado_2 and lado_1 != base) or (lado_2 == base and lado_2 != lado_1) or (lado_1 == base and lado_1 != lado_2):
        print('Triangulo isoseles')       
    elif (lado_1 != lado_2) and (lado_1 != base) and (lado_2 != base):
        print('Triangulo escaleno')  
else:
    print('Não é um triangulo')

 
