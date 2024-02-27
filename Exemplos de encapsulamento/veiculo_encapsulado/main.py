from carro import *
from aviao import *
from veiculo import *

veiculo1 = Veiculo('Marca1', 'Modelo 1', 2021)
veiculo2 = Veiculo('Marca 2', 'modelo 2', 2022)

car1 = Carro(5, veiculo1)
car2 = Carro(3, veiculo2)

aviao1 = Aviao(300, veiculo1)
aviao2 = Aviao(30, veiculo2)

print('Dados do carro 1')
print(f'Marca:  {veiculo1.get_marca()}')
print(f'Modelo: {veiculo1.get_modelo()}')
print(f'Ano:    {veiculo1.get_ano()}')
print(f'Portas: {car1.get_num_portas()}')
print()
print('Dados do carro 2')
print(f'Marca:  {veiculo2.get_marca()}')
print(f'Modelo: {veiculo2.get_modelo()}')
print(f'Ano:    {veiculo2.get_ano()}')
print(f'Portas: {car2.get_num_portas()}')
print()
print('Dados do aviao 1')
print(f'Marca:  {veiculo1.get_marca()}')
print(f'Modelo: {veiculo1.get_modelo()}')
print(f'Ano:    {veiculo1.get_ano()}')
print(f'Portas: {aviao1.get_assentos()}')
print()
print('Dados do aviao 2')
print(f'Marca:  {veiculo2.get_marca()}')
print(f'Modelo: {veiculo2.get_modelo()}')
print(f'Ano:    {veiculo2.get_ano()}')
print(f'Portas: {aviao2.get_assentos()}')