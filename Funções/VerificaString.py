frase = input('Digite uma frase: ')

def maiuscula(a):
    global mai
    mai = 0
    for x in a:
        if x.isupper():
         mai += 1

def minuscula(a):
    global minu
    minu = 0
    for x in a:
        if x.islower():
            minu +=1
def espacos(a):
    global spa
    spa = 0
    for x in a:
        x.isspace()
        spa +=1
    
maiuscula(frase)
minuscula(frase)
espacos(frase)
print(f'O numero de letras maiusculas é {mai} \n O numero de letras minusculas é {minu} \n O numero de espaços é {spa}')
