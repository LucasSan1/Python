def inputValidation(msg):
    while True:
        value = input(msg).strip().lower()

        if value in ('sim', 'nao'):
            return value
        else:
            print('Responda apenas com "sim" ou "nao"!! \n')

perguntas = [
    'Telefonou para a vitima?', 
    'Esteve no local do crime?',
    'Mora perto da vitima?',
    'Devia para a vitima?',
    'Já trabalhou com a vitima?',
]

res_sim = 0

for pergunta in perguntas:
    print(pergunta)
    resposta = inputValidation("Sim ou Não? \n")
    print("")
    
    if resposta == 'sim':
        res_sim += 1
 
if res_sim < 2:
    print('Inocente')

elif res_sim == 2:
    print('Suspeito')   
elif res_sim <= 4:
    print('Cumplice')
else: 
    print('Assassino')
