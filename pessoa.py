class Pessoa:
    def __init__ (self, nome, idade): 
        
        self.nome = input(nome)
        self.idade = int(input(idade))
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

pessoa1 = Pessoa("Ana", 25)
pessoa2 = Pessoa("The Weekend", 19)

pessoa1.apresentar()
pessoa2.apresentar()
