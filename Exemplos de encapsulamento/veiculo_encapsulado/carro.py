class Carro:
    def __init__(self, num_portas, veiculo):
        self.__num_portas = num_portas
        self.__veiculo = veiculo

    def get_num_portas(self):
        return self.__num_portas
    
    def ligar_radio(self):
        print('Radio ligado!')