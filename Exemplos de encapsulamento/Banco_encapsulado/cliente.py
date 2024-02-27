class Cliente:
    # Atributos da classe encapsulados
    def __init__(self,nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def exibir_dados(self):
        print(f'Nome: {self.__nome}')
        print(f'CPF: {self.__cpf}')