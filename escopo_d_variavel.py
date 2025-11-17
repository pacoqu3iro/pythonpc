#as variáveis têm diferentes escopos (visibilidade)
x= 10
#variável global
def funcao():
#variável local
    y = 5
    print(f" Dentro da função - x {x}, y: {y}")

y= funcao()
funcao() #saida:Dentro da função - x: 10, Y: 5
#a variável y não está disponível
print(f"Fora da função - x: {x}")
print(f"y: {y}")
#erro : nome y não está definido