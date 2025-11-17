class Gato:
    def __init__(self, raca, nome, peso, idade):
        self.raca = raca
        self.nome = nome
        self.idade = idade
        self.peso = peso

    def mostrar_dados(self):
        print(f"Raça: {self.raca}")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Peso: {self.peso} ")

gato1 = Gato("Siamês", "Luna", 4.5, 3)
gato2 = Gato("Gato Branco", "Alemão", 3.4, 5)
gato3 = Gato("Gato Laranja", "Garfield", 7.8, 4.5)

#exibir gatos
gato1.mostrar_dados()
print("")
gato2.mostrar_dados()
print("")
gato3.mostrar_dados()
print("")