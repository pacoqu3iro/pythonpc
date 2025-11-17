class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_notas(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)

    def calcular_media(self):
        return sum(self.notas)/len(self.notas) if self.notas else 0
    
    def mostrar_resultado(self):
        media = self.calcular_media()
    
    def listar_notas(self):
        return self.notas
    
nome = input("Nome: ")
matricula = input("Matrícula: ")
aluno = Aluno(nome, matricula)

while True:
    nota = input("Nota (ou enter para sair): ")
    if nota == "":
        break
    try:
        aluno.adicionar_notas(float(nota))
    except:
        print("insira um número válido!")

    print(f"Notas: {aluno.listar_notas()}")
    print(f"Media: {aluno.calcular_media():.2f}")
    print(f"Resultado: {aluno.mostrar_resultado()}")