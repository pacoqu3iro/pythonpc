class Veiculo:
    def __init__(self, tipo, modelo, km, cor, precisa_cnh=True):
        self.tipo = tipo
        self.modelo = modelo
        self.km = km
        self.cor = cor
        self.precisa_cnh = precisa_cnh

    def mostrar_dados(self):
        print(f"Tipo: {self.tipo}")
        print(f"Modelo: {self.modelo}")
        print(f"Quilometragem: {self.km} Km/h")
        print(f"Precisa de CNH: {"Sim" if self.precisa_cnh else "Não"}")

class Carro(Veiculo):
    def __init__(self, modelo, km, portas):
        super().__init__("Carro", modelo, km, precisa_cnh=True)
        self.portas = portas

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Portas: {self.portas}")

class Moto(Veiculo):
    def __init__(self, modelo, km, cilindrada, precisa_cnh = True):
        super().__init__("Moto", modelo, km, precisa_cnh)
        self.cilindrada = cilindrada

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Cilindrada: {self.cilindrada} cc")

class Bicicleta(Veiculo):
    def __init__(self, modelo, km, cor, eletrica = False):
        super().__init__("Bike", modelo, km, cor, precisa_cnh = False)
        self.eletrica = eletrica

    def mostrar_dados(self):
        super().mostrar_dados()
        tipo_bike = "Elétrica" if self.eletrica else "Comum"
        print(f"Tipom de Bike; {tipo_bike:}")