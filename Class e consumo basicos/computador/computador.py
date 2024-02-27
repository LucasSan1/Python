class Computador:
    def __init__(self, marca, modelo, preco, placa_mae, procesador, gabinete, fonte, monitor):      
        self.marca = marca
        self.modelo = modelo
        self.preco = preco
        self.placa_mae = placa_mae
        self.procesador = procesador
        self.gabinete = gabinete
        self.fonte = fonte
        self.monitor = monitor

    def ligar(self):
        print('Ligando....')
    def estudar(self):
        print('Estudando....')
    def desligar(self):
        print('Desligando....')
    def jogar(self):
        print('Jogando....')