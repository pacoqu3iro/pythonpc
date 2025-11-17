class Livro: #Inicia uma classe
    def __init__(self, titulo, autor): # self (Obrigatorio!), elementos que deseja que tenha
        self.titulo = titulo 
        self.autor = autor

def main(): #Criação de def
    livros = [ #Abre uma lista.
        Livro("Dom Casmurro", "Machado de Assis"), #cada virgula é um dos objetos (titulo e autor.)
        Livro("Senhor dos Anéis", "J. R. R. Tolkien"),
        Livro("Harry Potter", "JK Rowling"),
        Livro("Café Com Deus Pai", "Junior Rostirola"),
        Livro("A menina que roubava livros", "Markus Zusak"),
        Livro("Assasinato do Expresso Oriente", "Agatha Christie"),
        Livro("Fogo e Sangue", "George RR Martins"),
        Livro("Guia do Mochileiro das Galáxias", "Douglas Adams"),
        Livro("Jogos Vorazes", "SUzanne Collins"),
        Livro("Quem é você, Alaska?", "João Verde")

    ]

    nome = input("Digite o seu nome: ") #Solicitar o nome


    print("\n Livros disponíveis para empréstimo: ")
    for i, livro in enumerate(livros, start= 1): 
        print(f"{i}. {livro.titulo} - {livro.autor}")

    while True:
        escolha = int(input("\n Digite o número do livro que deseja pegar emprestado: "))
            
        if 1 <= escolha <= len(livros):
            livro_selecionado = livros[escolha - 1]
            break
        else:
            print(f"Por favor, digite um número entre 1 e {len(livros)}.")

    print("\n Empréstimo confirmado!")
    print(f"{nome} pegou emprestado o livro '{livro_selecionado.titulo}' de {livro_selecionado.autor}")

main()