class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome 
        self.idade = idade 
        self.__cpf = cpf

    def mostrar_dado(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")
        print(f"CPF (Privado): {self.__cpf}")

    def alterar_cpf(self, novo_cpf):
            self.__cpf = novo_cpf

pessoa1 = Pessoa("Iracema", 74, "123456789-00")
pessoa1.mostrar_dado()

pessoa1.alterar_cpf("987654321-00")
pessoa1.mostrar_dado()