class Contabancaria():

    def __init__ (self, nometitular, saldo, depositar, sacar, senha):
        self.nometitular = nometitular
        self.saldo = saldo
        self.depositar = depositar
        self.sacar = sacar
        self.senha = senha

class Opções(Contabancaria):

    def __init__(self, nometitular, saldo, depositar, sacar,senha):
        super().__init__(nometitular, saldo, depositar, sacar, senha)

    nometitular = input("Informe seu nome: ")
    saldo = 0
    sacar = 0
    depositar = 0
    senha = 281108
    opcao = int(input("Selecione uma opção 1 para depositar e 2 para sacar e 3 para consultar seu saldo."))
        
    match opcao:
        case 1:
            depositar = (int(input("Digite o valor do deposito que deseja realizar: ")))

            if opcao == 1 and saldo <= 0:
                print(f"O Depósito de {depositar} Reais não pode ser realizado")

            else:
                print(f"Depósito de {depositar} Reais realizado com sucesso!")
    
        case 2:
            sacar = (int(input("Digite o valor que deseja sacar: ")))

            if opcao == 2 and saldo <= 0:
                print("Valor de saque indisponivel")

            else:
                print(f"Saque de {sacar} Reais realizado com sucesso!")
  
        case 3: 
            senha = (int(input("Digite sua senha de 6 digitos (Somente números):  ")))
            
            if senha == 281108:
                print(f"Saldo atual: {saldo} ")
            else:
                print("Senha incoreta! Seu saldo não pode ser visualizado.")

        case _:
            print("Seleção Inválida!")


"""No código o nome de usúario não pode mais ser visualizado após escrever ele já o saldo da conta só pode ser consultado caso o úsuario informe a senha da conta!"""