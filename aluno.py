class Aluno:

    def cadastro(lista, nome, matricula, notas1, notas2, notas3,):

        aluno = {"nome": nome, "nota1": notas1, "nota2": notas2,"nota3": notas3, "Matricula": matricula}
        lista.append(aluno)

    def listar_alunos(lista):
        for i in range(len (lista)):
            aluno = lista[i]
            print(f" {i + 1}. Nome: {aluno['nome']}, Número de matricula: {aluno['matricula']},  Nota 1: {aluno['notas1']}, Nota 2: {aluno['notas2']}, Nota 3: {aluno['notas3']}")

    alunos = []
    while True:
        print("Nota do aluno")
        nome = input("Nome: ")
        matricula = int(input("Informe sua matricula: "))
        notas1 = float(input("Digite a 1º nota: "))
        notas2 = float(input("Digite a 2º nota: "))
        notas3 = float(input("Digite a 3º nota: "))

        media = (notas1 / 2) + (notas2 / 3) + (notas3 / 5) 

        if  media <= 7 :
            print ("Recuperação")
            
        else:
            media <= 4
            print("Reprovado")


        cadastro(alunos, nome, matricula, media)
