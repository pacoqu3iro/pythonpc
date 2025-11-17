diadesemana = input("digite o dia da semana: ").strip().lower()

if diadesemana.lower() == "segunda feira" or diadesemana.lower() == "segunda" or diadesemana.lower() == "segunda-feira":
    print("É um dia útil!")

elif diadesemana.lower() == "terça feira" or diadesemana.lower() == "terça" or diadesemana.lower() == "terça-feira":
    print("É um dia útil!")

elif diadesemana.lower() == "quarta feira" or diadesemana.lower() == "quarta" or diadesemana.lower() == "quarta-feira":
    print("É um dia útil!")

elif diadesemana.lower() == "quinta feira" or diadesemana.lower() == "quinta" or diadesemana.lower() == "quinta-feira":
    print("É um dia útil!")

elif diadesemana.lower() == "sexta feira" or diadesemana.lower() == "sexta" or diadesemana.lower() == "sexta-feira":
    print("É um dia útil!")

elif diadesemana.lower() == "sabado" or diadesemana.lower() == "sábado":
    print("É um fim de semana!")

elif diadesemana.lower() == "domingo":
    print("É um fim de semana!")

else:
    print("Resposta inválida!")