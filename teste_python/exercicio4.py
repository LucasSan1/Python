nuns = []

i = 0

while i < 10:
    num = int(input(f"Digite o {i+1}° numero: "))
    nuns.append(num)
    i += 1

par = []
impar = []

for x in nuns:
    vef = x % 2
    if vef == 0:
        par.append(vef)
    else:
        impar.append(vef)

print(f"A quantidade de numeros impares é {len(impar)}") 
print(f"A quantidade de numeros pares é {len(par)}") 