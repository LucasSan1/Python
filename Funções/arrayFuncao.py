from array import*

arr = array('i', {})
for i in range(1,6):
    num = int(input(f'Digite o {i}° valor inteiro: '))
    arr.append(num)

def somar_array(vet):
    return sum(vet)

somar_array(arr)
print(f'A soma é {somar_array(arr)}')