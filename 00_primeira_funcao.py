nome = input("Seu nome: ")

def exibir_mensagem():
    print("Olá mundo!")
exibir_mensagem()#Olá mundo!

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")
exibir_mensagem_2(nome="Guilherme")#Seja bem vindo Guilherme!
exibir_mensagem_2(nome)#Seja bem vindo leonardo!

def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")
exibir_mensagem_3()#Seja bem vindo Anônimo!
exibir_mensagem_3(nome="Chappie")#Seja bem vindo Chappie!