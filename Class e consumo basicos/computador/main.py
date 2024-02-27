from computador import Computador

Pc = Computador('Dell', 'Latitude 3420', 4000, 'Intel', 'I5', 'notebook', 'Externa', '14 polegadas')

print(f'Marca: {Pc.marca}')
print(f'Modelo: {Pc.modelo}')
print(f'Preço: {Pc.preco}')
print(f'Placa mae: {Pc.placa_mae}')
print(f'Procesador: {Pc.procesador}')
print(f'Gabinete: {Pc.gabinete}')
print(f'Fonte: {Pc.fonte}')
print(f'Monito: {Pc.monitor}')

Pc.ligar()
Pc.estudar()
Pc.desligar()
Pc.jogar()
