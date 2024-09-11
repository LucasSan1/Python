from datetime import datetime

def input_data(msg): # Valida o input da data de nascimento e converte em formato valido
    while True:
        try:
            data_str = input(msg)
            data = datetime.strptime(data_str, "%d/%m/%Y")  # Converte a string para um objeto datetime
            return data
        except ValueError:
            print("Formato inválido. Por favor, use o formato DD/MM/AAAA.")

def calcular_idade(data_nascimento):
    hoje = datetime.today()  # Data atual
    idade = hoje.year - data_nascimento.year  # Calcula a diferença de anos
    
    if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day): # Ajusta a idade se o aniversário ainda não ocorreu este ano
        idade -= 1
    
    return idade

data_nascimento = input_data("Digite sua data de nascimento (DD/MM/AAAA): ")

idade = calcular_idade(data_nascimento)

print(f"Sua idade é: {idade} anos")
