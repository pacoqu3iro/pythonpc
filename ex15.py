homens_18 = 0
mulherers = 0
while True:
    genero = input("Informe o gênero do aluno (M/F)").strip().upper()
    idade = int(input("Informe sua idade (Nº negativo para encerrar o progrema): "))

    if idade < 0:
        break
match genero:

    case 'M':
        if idade > 18:
            homens_18 += 1

    case 'F':
        mulherers += 1

    case _:
        print("Resposta inválida. Digite M ou F")

print(f"Existem {homens_18}Homens acima dos 18 anos e existem {mulherers} Mulheres ")