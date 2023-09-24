usuarios = []#lista de usuarios
opcao = "S"

#Função criar usuario
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    filtro = filtrando(cpf, usuarios)#chamou outra função atribuindo o cpf e a lista de usuarios para a variavel filtro

    if filtro: #Se a função filtrando retornar um resultado positivo
        print("\nJá existe usuário com esse CPF!")
        return
    else: 
        usuarios.append({"cpf": cpf})#Se a função filtrando retornar um resultado negativo

    print("=== Usuário criado com sucesso! ===")
    opcao = input("Deseja continuar [S/N]: ")
    if opcao == "N":
        return opcao
        

#Função para consultar se o usuario já está cadastrado
def filtrando(cpf, usuarios):
    checando = [usuario for usuario in usuarios if usuario["cpf"] == cpf]#Buscando na lista USUARIOS o valor do cpf digitado
    return checando[0] if checando else None# se o cpf for encontrado vai retornar valor para checando, caso contrario não

#Execução do código
while opcao !="N":

    criar_usuario(usuarios)

    print(usuarios)