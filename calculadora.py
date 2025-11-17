def soma(a, b):
    return a + b

def Subtracao(a, b):
        return a - b

def Multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Não pode ser dividido por zero!"
    return a / b
    
def menu():
    print("Calculadora \n")
    print("Selecione uma das opções: \n")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

while True:
    menu()
    escolha = input(" Escolha a operação(de 1 a 5)")

    match escolha:
        case "1" | "2" | "3" | "4" :
            try:
                numero1 = float(input("Digite o 1º número: "))
                numero2 = float(input("Digite seu 2º número: "))
            except ValueError:
                print("Erro: Digite um número válido.")
                continue
            match escolha:
                case "1":
                    resultado = soma(numero1,numero2)
                case "2":
                    resultado = Subtracao(numero1,numero2)
                case "3":
                    resultado = Multiplicacao(numero1,numero2)
                case "4":
                    resultado = divisao(numero1,numero2)
            print(f"Resultado: {resultado}")
        case "5":
            print("Programa Encerrado.")
            break
        case _:
                print("Opção inválida. Por Favor digite um número entre 1 e 5")