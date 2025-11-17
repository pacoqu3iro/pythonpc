def calcular_media():
    notum = float(input("Digite sua primeira nota: "))
    notdois = float(input("Digite sua segunda nota: "))
    notafinal = (notum * 2) + (notdois * 3) / 5
    print(f"Sua média é {notafinal}")
calcular_media()