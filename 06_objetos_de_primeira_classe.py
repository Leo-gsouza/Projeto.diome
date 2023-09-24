def multiplicar(a, b):
    return a * b
#função multiplicar vai retonar o valor de a * b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)# o parametro funcao será preenchido com a função criada acima = multiplicação
    print(f"O resultado da operação {a} + {b} = {resultado}")


exibir_resultado(5, 7, multiplicar)  # O resultado da operação 10 + 10 = 35