import math  

def input_float(msg):
    while True: 
        try:
            value = float(input(msg))  # Tenta converter a entrada para float
            if value <= 0:  
                raise ValueError("O valor deve ser maior que 0.")  # Lança um erro se a condição não for atendida
            return value 
        except ValueError as e:  
            print(f"Entrada inválida: {e}")  

def input_int(msg):
    while True:  
        try:
            value = int(input(msg))  # Tenta converter a entrada para inteiro
            if value < 0: 
                raise ValueError("O valor deve ser maior que 0.")  # Lança um erro se a condição não for atendida
            return value  
        except ValueError as e:  
            print(f"Entrada inválida: {e}") 

num_lados = input_int("Digite o número de lados do polígono: ")

if num_lados < 3:
    print("NÃO É UM POLÍGONO")

elif num_lados == 3:
   
    lado1 = input_float('Digite o primeiro lado (em cm): ') 
    lado2 = input_float('Digite o segundo lado (em cm): ')  
    base = input_float('Digite a base (em cm): ')  
    
    if (lado1 < lado2 + base) and (lado2 < lado1 + base) and (base < lado1 + lado2):
        if lado1 == lado2 == base:
            tipo = "EQUILÁTERO"  # Todos os lados são iguais

        elif lado1 == lado2 or lado1 == base or lado2 == base:
            tipo = "ISÓSCELES"  # Dois lados são iguais

        else:
            tipo = "ESCALENO"  # Todos os lados são diferentes
        
            altura = input_float('Digite a altura (em cm): ')  
            
        area = 0.5 * base * altura  

        print("")  
        print(f"TRIÂNGULO {tipo}")  
        print(f"Área: {area:.2f} cm²")  

    else:
        print("Não é um triângulo")

elif num_lados == 4:
    lado1 = input_float('Digite a base (em cm): ') 
    lado2 = input_float('Digite o lado (em cm): ')  

    if lado1 == lado2:
        area = lado1 * lado1  

        print("") 
        print("QUADRADO") 
        print(f"Área: {area:.2f} cm²")  
    else:
        base = lado1  
        altura = lado2  
        area = base * altura  

        print("")  
        print("RETÂNGULO")  
        print(f"Área: {area:.2f} cm²")

else:
    print("POLÍGONO NÃO IDENTIFICADO") 