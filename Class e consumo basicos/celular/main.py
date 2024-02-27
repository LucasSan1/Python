from celular import Celular

cel = Celular('Samsung', 'S9', 1000, 'Android 10', '5.8 polegadas')

print(f'Marca: {cel.marca}')
print(f'Modelo: {cel.modelo}')
print(f'Preço: {cel.preco}')
print(f'Sistema operacional: {cel.So}')
print(f'Tela: {cel.tela}\n')

cel.ligar()
cel.desligar()
cel.telefonar()
cel.jogar()

