class Tv:
    def __init__(self, marca, modelo, preco, tela, smart):
        self.marca = marca
        self.modelo = modelo
        self.preco = preco
        self.tela = tela
        self.smart = smart

    def ligar(self):
        print('ligando....')
    def desligar(self):
        print('desligando....')
    def assistir(self):
        print('assistindo....')