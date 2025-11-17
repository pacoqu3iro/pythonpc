class Calculadora:
    def __init__(self):
        pass

    def somar(self, a, b):
        return a + b
    
    def subtrair(self, a , b):
        return a - b
    
    def multipluicacao(self, a ,b):
        return a * b 

    def divisoa(self, a ,b):
        if b== 0 :
            return "Erro: divisão por zero."
        return a / b
calculadora = Calculadora()
print("Soma: ", calculadora.somar(10,5))
print("Subtração: ", calculadora.subtrair(10,5))
print("Multiplicação: ", calculadora.multipluicacao(10,5))
print("Divisão: ", calculadora.divisoa(10,5))
print("Divisão por zero: ", calculadora.divisoa(10,0))