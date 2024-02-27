class Celular:
    def __init__(self, marca, modelo, preco, So, tela):
        self.marca = marca
        self.modelo = modelo
        self.preco = preco
        self.So = So
        self.tela = tela

    def ligar(self):
        print(f'Ligando....')
    def desligar(self):
        print(f'Desligando....')
    def telefonar(self):
        print(f'Telefonando....')
    def jogar(self):
        print(f'Jogando....')