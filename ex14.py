contador_pares = 0

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))

    if numero % 2 ==0:
        contador_pares += 1

print(f"\nVocê tem {contador_pares} números pares.")