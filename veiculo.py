class Veiculo:
    def __init__(self, marca, modelo, velocidade, codigo_interno):
        self.marca = marca
        self.modelo = modelo
        self.__velocidade = velocidade #protegido
        self.__codigo_interno = "Pacoqu3iro" #privado

    def _calcular_desempenho(self):
        #métoo protegido, complexidade oculta
        return f"O veículo pode atingir {self.__velocidade} km/h"
    
    def mostrar_informações(self):
        #interface pública que abstrai os detalhes internos
        desempenho = self._calcular_desempenho
        return f"Marca: {self.marca}, Modelo: {self.modelo}, {desempenho}"
    
    def __metodo_privado(self):
        return "Esse método é privado."

carro = Veiculo("Toyota", "Corolla", 180)
print(carro.mostrar_informações())

