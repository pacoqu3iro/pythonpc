def somarImposto():

    ImpostoInicial = float(input("Digite o valor do seu item: "))
    TaxaImposto = float(input("Digite a porcentagem da taxa: "))
    imposto =  (TaxaImposto / 100) * ImpostoInicial
    novovalor = ImpostoInicial + imposto
    print(f"O valor com imposto é {novovalor}")

somarImposto()