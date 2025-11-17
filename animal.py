class Animal:

    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazersom (self):
        print("Algum animal está fazendo barulho!")

class Cachorro(Animal):

    def fazersom(self):
        print("Au au!")

class Gato(Animal):

    def fazersom(self):
        print("Miau")

gato1 = Gato("Paçoca", 0.5)
cachorro1 = Cachorro("Luke", 5)

gato1.fazersom()
cachorro1.fazersom()
Animal.fazersom()