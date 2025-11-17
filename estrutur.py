def saudacao(nome, mensagem = "Olá"):
    return f'{mensagem}, {nome}!'

print(saudacao("Maria"))
print(saudacao("João", "Oi"))