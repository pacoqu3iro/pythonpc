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

#solicitar

raca = input("Digite a raça do gato :")
idade = float(input("Digite o nome do gato: "))
nome = input("Digite o nome do gato: ")
peso = float(input("Digite o peso do gato"))

gato = Gato(raca,nome,idade,peso)
gato.mostrar_dados()