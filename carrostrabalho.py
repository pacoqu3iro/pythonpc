class Veiculo:

    def __init__(self, modelo, cor, ano, marca, tracao):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.marca = marca
        self.tracao = tracao

carro1 = Veiculo("Civic", "Cinza", 2014, "Honda", "Dianteria")
carro2 = Veiculo("Uno", "Prata", 1989, "Fiat", "Dianteira")
carro3 = Veiculo("Gol", "Azul", 1999, "Volkswagen", "Dianteira")

class Moto(Veiculo):

    def __init__(self, modelo, cor, ano, marca, tracao):
        super().__init__(modelo, cor, ano, marca, tracao)

moto1 = Moto("Faizer", "Vermelho",2015, "Yamaha", "Traseira")
moto2 = Moto("R9", "Azul", 2023, "Yamaha", "Traseira")
moto3 = Moto("Titã", "Branca", 2017, "Honda", "Traseira")

class Bicicleta(Veiculo):
    def __init__(self, modelo, cor, ano, marca, tracao):
        super().__init__(modelo, cor, ano, marca, tracao)

bicicleta1 = Bicicleta("", "Azul", 2023, "Caloi", 26)
bicicleta2 = Bicicleta("", "Cinza", 2014, "Sense", 22)
bicicleta3 = Bicicleta("", "Rosa", 2019, "Oggi", 29)



print("Carros: ")
print(f"Modelo: {carro1.modelo}, Cor: {carro1.cor}, Ano: {carro1.ano}, Marca:  {carro1.marca}, Tração: {carro1.tracao}")
print(f"Modelo: {carro2.modelo}, Cor: {carro2.cor}, Ano: {carro2.ano}, Marca:  {carro2.marca}, Tração: {carro2.tracao}")
print(f"Modelo: {carro3.modelo}, Cor: {carro3.cor}, Ano: {carro3.ano}, Marca:  {carro3.marca}, Tração: {carro3.tracao}\n")

print("Motos: ")
print(f"Modelo: {moto1.modelo}, Cor: {moto1.cor}, Ano: {moto1.ano}, Marca:  {moto1.marca}, Tração: {moto1.tracao}")
print(f"Modelo: {moto2.modelo}, Cor: {moto2.cor}, Ano: {moto2.ano}, Marca:  {moto2.marca}, Tração: {moto2.tracao}")
print(f"Modelo: {moto3.modelo}, Cor: {moto3.cor}, Ano: {moto3.ano}, Marca:  {moto3.marca}, Tração: {moto3.tracao}\n")

print("Bicicleta :")
print(f"Cor: {bicicleta1.cor}, Ano: {bicicleta1.ano}, marca: {bicicleta1.marca}, aro: {bicicleta1.tracao} ")
print(f"Cor:{bicicleta2.cor}, Ano: {bicicleta2.ano}, marca: {bicicleta2.marca}, aro: {bicicleta2.tracao} ")
print(f"Cor: {bicicleta3.cor}, Ano: {bicicleta3.ano}, marca: {bicicleta3.marca}, aro: {bicicleta3.tracao} \n")