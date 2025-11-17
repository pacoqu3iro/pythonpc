def cadastro(lista, nome, idade, curso):

    aluno = {"nome": nome, "idade": idade, "curso": curso}
    lista.append(aluno)

def listar_alunos(lista):
    for i in range(len (lista)):
        aluno = lista[i]
        print(f" {i + 1}. Nome: {aluno['nome']}, Idade: {aluno['idade']}, Curso: {aluno['curso']}")

alunos = []

while True:
    print("Cadastro de Aluno")
    nome = input("Nome (ou digite sair para encerrar): ")
    if nome.lower() == "sair":
        break
    idade = int(input("Informe sua idade: "))
    curso = input("Informe seu curso: ")
    cadastro(alunos, nome, idade, curso)
    print("Aluno cadastrado com sucesso! \n")

print("\n Lista de alunos cadastrados: ")
listar_alunos(alunos)