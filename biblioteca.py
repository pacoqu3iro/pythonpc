class Biblioteca:
    def __init__(self, titulo, autor, ano, volume):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano 
        self.volume = volume

class Livro(Biblioteca):
    
    def __init__(self, titulo, autor, ano, volume):
        super().__init__(titulo, autor, ano, volume)

livro1 = Biblioteca ("Harry Potter And The Chamber Of Secrets", "J. K. Rowling", 2018, "2º")
livro2 = Biblioteca ("A Guerra dos Tronos : As Crônicas de Gelo e Fogo", "George R. R. Martin", 2019,"1º")
livro3 = Biblioteca ("Abigail", "Catherine Rayner ", 2013, "Único")
livro4 = Biblioteca ("Uzumaki", "Junji Ito", 200, "3º")
livro5 = Biblioteca ("O Pequeno Príncipe", "Le Petit Prince", 1943, "Único")
livro6 = Biblioteca ("One Piece", "Oda", 2025, "106")
livro7 = Biblioteca ("A Cabana", "William P. Young", 2007, "Único")
livro8 = Biblioteca ("Ordem Paranormal: O Espreitador e Outras Histórias", "Rafael Lange", 2025, "Único")
livro9 = Biblioteca ("Diário da Minha Experiência Comigo Mesma", "Kabi Nagata", 2020, "1º")
livro0 = Biblioteca ("One Piece", "Oda", 1999, "1º")


print("Livros disponiveis: ")
print(f"Livro 1: Titulo: {livro1.titulo}, Autor: {livro1.autor}, Ano: {livro1.ano}, Volume: {livro1.volume}")
print(f"Livro 2: Titulo: {livro2.titulo}, Autor: {livro2.autor}, Ano: {livro2.ano}, Volume: {livro2.volume}")
print(f"Livro 3: Titulo: {livro3.titulo}, Autor: {livro3.autor}, Ano: {livro3.ano}, Volume: {livro3.volume}")
print(f"Livro 4: Titulo: {livro4.titulo}, Autor: {livro4.autor}, Ano: {livro4.ano}, Volume: {livro4.volume}")
print(f"Livro 5: Titulo: {livro5.titulo}, Autor: {livro5.autor}, Ano: {livro5.ano}, Volume: {livro5.volume}")
print(f"Livro 6: Titulo: {livro6.titulo}, Autor: {livro6.autor}, Ano: {livro6.ano}, Volume: {livro6.volume}")
print(f"Livro 7: Titulo: {livro7.titulo}, Autor: {livro7.autor}, Ano: {livro7.ano}, Volume: {livro7.volume}")
print(f"Livro 8: Titulo: {livro8.titulo}, Autor: {livro8.autor}, Ano: {livro8.ano}, Volume: {livro8.volume}")
print(f"Livro 9: Titulo: {livro9.titulo}, Autor: {livro9.autor}, Ano: {livro9.ano}, Volume: {livro9.volume}")
print(f"Livro 10: Titulo: {livro0.titulo}, Autor: {livro0.autor}, Ano: {livro0.ano}, Volume: {livro0.volume}")
print(f"Livro 11: Titulo: Jogos Vorazes, Autor: Suzanne Collins, Ano: 2016, Volume: 1")

nome = input("Digite seu nome: ")
opcoes = int(input("Seleciona um livro (De 1 à 10): "))

print(f"{nome} pegou o livro: ")


match opcoes:
    case 1: 
        print(f"Titulo: {livro1.titulo}, Autor: {livro1.autor}, Ano: {livro1.ano}, Volume: {livro1.volume}")
    case 2: 
        print(f"Titulo: {livro2.titulo}, Autor: {livro2.autor}, Ano: {livro2.ano}, Volume: {livro2.volume}")
    case 3: 
        print(f"Titulo: {livro3.titulo}, Autor: {livro3.autor}, Ano: {livro3.ano}, Volume: {livro3.volume}")
    case 4: 
        print(f"Titulo: {livro4.titulo}, Autor: {livro4.autor}, Ano: {livro4.ano}, Volume: {livro4.volume}")
    case 5: 
        print(f"Titulo: {livro5.titulo}, Autor: {livro5.autor}, Ano: {livro5.ano}, Volume: {livro5.volume}")
    case 6: 
        print(f"Titulo: {livro6.titulo}, Autor: {livro6.autor}, Ano: {livro6.ano}, Volume: {livro6.volume}")
    case 7: 
        print(f"Titulo: {livro7.titulo}, Autor: {livro7.autor}, Ano: {livro7.ano}, Volume: {livro7.volume}")
    case 8: 
        print(f"Titulo: {livro8.titulo}, Autor: {livro8.autor}, Ano: {livro8.ano}, Volume: {livro8.volume}")
    case 9: 
        print(f"Titulo: {livro9.titulo}, Autor: {livro9.autor}, Ano: {livro9.ano}, Volume: {livro9.volume}")
    case 10: 
        print(f"Titulo: {livro0.titulo}, Autor: {livro0.autor}, Ano: {livro0.ano}, Volume: {livro0.volume}")
    case _: 
        print("Livro indisponivel ou seleção inexistente.")