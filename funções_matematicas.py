menu = """\n
================ MENU ================
Somar
Subtrair
Multiplicar"""

def somar(v1, v2):
    return v1 + v2

def subtrair(v1, v2):
    return v1 - v2

def multiplicar(v1, v2):
    return v1 * v2
    

def par_ou_impar(v1,v2,funcao):
    resultado = funcao(v1,v2)
    if resultado % 2 == 0:
        return "Par"
    else:
        return "Impar"




#FUNÇÕES CRIADAS ->>>> CRIAR CÓDIGO

print(menu)
while True:
    opcao = input("Escolha uma opção: ").lower().strip()
    valor_1 = float(input("1º valor: "))
    valor_2 = float(input("2º valor: "))

    resultado = par_ou_impar(valor_1, valor_2, multiplicar)
    print(f"O produto de {valor_1} x {valor_2} = {valor_1*valor_2}\nO valor é {resultado}")




    #if opcao == "somar":
        #resultado = somar(valor_1,valor_2)
        #print(resultado)
    #elif opcao == "subtrair":
        #resultado = subtrair(valor_1, valor_2)
        #print(resultado)
    #elif opcao == "multiplicar":
        #resultado = multiplicar(valor_1, valor_2)
        #print(resultado)

