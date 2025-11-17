class Pet():
    def __init__ (self, nome, especie, idade):
        self.nome = nome
        self.especie = especie 
        self.idade = idade

class PetAtributos(Pet):

    def __init__(nome, especie, idade):
        super().__init__(nome, especie, idade)

    nome = input("Informe o nome do seu pet: ")
    especie = input("Digite 1 se seu animal for um cachorro e 2 caso seja um gato: ")
    idade = int(input("Qual a idade do seu animal? "))

class Selecao():

    def mostrarinformacoes(self, opcao):
        self.opcao = opcao

class Selecione(Selecao, Pet):
        
    def __init__(opcao, nome, especie, idade):
        super().__init__(nome, especie, idade, opcao)

    opcao = int(input("Deseja finalizar o formulário? 1 para sim e 2 para não"))

    match opcao:
        
        case 1:
            print("Formulário finalizado!")

        case 2: 
            print("Deseja alterar alterar a idade do seu animal ou ver as informações dele?")
            opcaodeidade = int(input("1 para alterar idade e 2 para ver informações "))

            match opcaodeidade:

                case 1:
                    print("Informe a nova idade do seu animal: ")

                case 2: 
                    class Opcaodois(Pet):
                        def __init__(opcao, nome, especie, idade):
                            super().__init__(nome, especie, idade, opcao)

                            print(f"Nome: {nome}, Idade: {idade}, Espécie: {especie}")


                case _:
                    print("Finalizado")
                    
class Opcaodois(Pet):
        def __init__(opcao, nome, especie, idade):
            super().__init__(nome, especie, idade, opcao)
            match especie:

                case 2: 
                    print("Miau Miau")

                case 1:
                    print("Au Au")

                case _:
                    print("")
            
                

        

