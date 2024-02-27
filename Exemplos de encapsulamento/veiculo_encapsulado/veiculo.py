class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano

    def get_marca(self):
        return self.__marca
    
    def get_modelo(self):
        return self.__modelo
    
    def get_ano(self):
        return self.__ano

    def acelerar(self):
        print('Acelerando!!')

    def frear(self):
        print('Freando!!')