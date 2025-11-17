nota = float(input("Digite sua nota: "))

if nota <0 :
    print("Acefalo, muito burro")
elif nota < 5:
    print("Reprovado!")
elif nota < 7:
    print("Recuperação.")
elif nota > 10:
    print("Como????????")
else: 
    print("Aprovado!")