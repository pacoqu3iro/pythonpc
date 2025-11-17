import os
nome = str(input("Digite seu nome completo:"))
ano = int(input("Digite o ano atual :"))
curso = input("Digite o nome do seu curso :")
matriculado_input = input = input("Você está matriculado? (sim/não) ")

#converte resposta para bool
# if = se
# else = senao
#matriculado_input = True if matriculado_input.lower() == "sim" else False

if matriculado_input.lower() == "sim":
    matriculado = True
elif matriculado_input.lower() == "não" or matriculado_input.lower() == "nao": 
    matriculado = False
else:
    matriculado = False
    print("Resposta inválida para matrícula, não matriculado")

if matriculado:
    print(f"{nome} está matriculado(a) no curso")
else:
    print(f"{nome} não está matriculado(a) no curso")

os.system("cls" if os.name == "nt" else "clear")