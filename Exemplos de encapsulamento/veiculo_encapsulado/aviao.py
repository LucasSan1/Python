class Aviao:
    def __init__(self, num_assentos, veiculo):
        self.__num_assentos = num_assentos
        self.__veiculo = veiculo

    def get_assentos(self):
        return self.__num_assentos

    def decolar(self):
        print('Decolando ....')