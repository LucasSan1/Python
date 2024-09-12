print('Para o seu cadastro digite seu nome e sua senha')

n = input('Digite seu nome')
s = input('digite sua senha')

def login():
  global N
  global S
  
  print('Para logar digite seu nome e senha')

  N = ''
  S = ''

  while(n != N) or (s != S):
  
    N = input('Digite seu nome') 
    S = input('Digite sua senha')


    if n == N and s == S:
      return 'Aguarde enquanto é logado'
    else: 
      return 'Nome ou Senha incorretos'
  

login()
