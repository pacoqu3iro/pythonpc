N = int(input("Digite um nº inteiro: "))

soma = 0
for i in range(N):
    numero = float(input(f"Digite o {i + 1}º número: "))
    soma += numero 

media = soma/N
print(f"A média aritimética é: {media}")