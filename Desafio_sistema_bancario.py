import textwrap
import string

def menu():
    menu = """\n
    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ MENU ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    [1]Depositar          [2]Sacar
    [3]Extrato            [4]Nova conta
    [5]Listar contas      [6]Novo usuário
    [0]Sair
    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):#parametros posicionais
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print(f"\nDepósito de R${valor:.2f} realizado com sucesso!")
    else:
        print("\n\aValor inválido.")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):#parametros nomeados
    excedeu_saldo = valor > saldo
    excedeu_valor = valor > limite
    excedeu_limite_de_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print(f"\nValor de saque = R${valor}.Saldo da conta\nR${saldo}.\n▬▬▬ Saldo insuficiente ▬▬▬")

    elif excedeu_valor:                                                                                     
        print(f"\n\aO limite de saque é de R${limite}.")

    elif excedeu_limite_de_saques:
        print("\nLimite de saques esgotados.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\nSaque de R${valor:.2f} realizado com sucesso!")

    else:
        print("\nValor inválido.")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato, taxa_extrato):
    print("\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ EXTRATO ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    saldo -= taxa_extrato
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    

def criar_usuario(lista_de_usuarios):
    cpf = input("Informe o CPF: ")
    cpf = cpf.translate(str.maketrans('', '', string.punctuation))
    usuario = filtrar_usuario(cpf, lista_de_usuarios)

    if usuario:
        print(f"\n\aEste CPF já foi cadastrado!\nDados informados: {usuario}")
        return

    nome = input("Informe o nome completo: ").capitalize()
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (rua, nº - bairro - cidade/sigla estado): ").capitalize()

    lista_de_usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print(f"Usuário criado com sucesso!\nDados do usuario: {usuario} ")


def filtrar_usuario(cpf, lista_de_usuarios):
    usuario_filtrado = [usuario for usuario in lista_de_usuarios if usuario["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    cpf = cpf.translate(str.maketrans('', '', string.punctuation))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    lista_de_usuarios = []
    contas = []
    taxa_extrato = 0.90

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato, taxa_extrato=taxa_extrato)


        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, lista_de_usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)
        
        elif opcao == "6":
            criar_usuario(lista_de_usuarios)

        elif opcao == "0":
            break

        else:
            print("ERROR! Selecione novamente a operação desejada.")


main()