#O que é um argumento = É a informação que a função vai receber tratar e retornar 

frutas = ["uva","maça","pera"]#lista
fruta = "aBACAXI"#variavel

def tratar_texto(texto):#Função com objetivo de remover espaços e deixar o texto maiusculo
    texto = texto.strip()
    texto = texto.upper()
    return texto

fruta = tratar_texto(fruta)
print(fruta)

for indice, item in enumerate(frutas):#Como tratar os itens dentro de uma lista
    frutas[indice] = tratar_texto(item)
print(frutas)