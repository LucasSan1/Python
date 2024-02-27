# Essa função armazena os dados fornecidos pelo usuario
def dados():
  global nome
  global altura
  global peso

  nome = input('Digite seu nome: ')
  altura = float(input('digite sua altura: '))
  peso = float(input('digite seu peso: '))

# A função abaixo faz o calculo do imc usando o pow pra elevar a altura ao quadrado e o round para arredondar o imc com 1 casa apos a virgula

def calculo_imc(peso, altura):
  imc = peso/ pow(altura, 2)
  return round (imc, 2)

# Essa funçao esta fazendo a analize do imc calculado na função anterior, atraves de uma estrutura de decisao, e retornando a mensagem de como seu imc está

def avalia_imc():
  imc = calculo_imc(peso, altura)
  if imc < 16:
    return 'Magreza grave'
  elif imc >= 16 and imc < 17:
    return 'Magreza moderada'
  elif imc >= 17 and imc < 18.5:
    return 'Magreza leve'
  elif imc >= 18.5 and imc < 25:
    return 'Saudavel'
  elif imc >=25 and imc < 30:
    return 'Sobrepeso'
  elif imc >= 30 and imc < 35:
    return 'Obesidade grau 1'
  elif imc >= 35 and imc < 40:
    return 'Obesidade grau 2(Severa)'
  else: 
    return 'Obesidade grau 3(Mórbida)'

# As funçoes de calculo e de avaliaçao estao sendo atribuidas à variaveis e sendo chamadas para que possam aparecer para o usuario  

dados()
imc = calculo_imc(peso, altura)
msg = avalia_imc()

print(f'{nome} seu imc é de {imc} e você está {msg}')