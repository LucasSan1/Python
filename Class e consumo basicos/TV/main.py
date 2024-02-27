from TV import Tv

tv = Tv('LG', 'xxx', 2500, '55pol', True)

print(f'Marca: {tv.marca}')
print(f'Modelo: {tv.modelo}')
print(f'Preço: R${tv.preco:.2f}')
print(f'Tela: {tv.tela}')
print(f'É smart?  {tv.smart}\n')

tv.ligar()
tv.assistir()
tv.desligar()