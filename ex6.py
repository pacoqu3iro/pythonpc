nome_completo = input("Digite nome e sobrenome: ")

#versão original
print(nome_completo)

# Maiúsculas
print(nome_completo.upper())

# Minúsculas
print(nome_completo.lower())

#retirar o espaço do inicio ou do final
print(nome_completo.strip())

#cria um vetor (cada nome do código vai ser convertido como 1{mostra o objeto})
nomes = nome_completo.split()
print(nomes[0])
print(len(nomes))

#Deixa a primeira letra de cada palavra maiúscula
print(nome_completo.title())

#substituir um texto por outro
print(nome_completo.replace("Ramos", "Senai"))
                            #a palavra que vai ser subistituida , a palavra que vai subistituir


















































