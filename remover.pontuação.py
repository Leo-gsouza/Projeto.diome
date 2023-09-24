import string
cpf = input("Informe o CPF (somente número): ")
cpf = cpf.translate(str.maketrans('', '', string.punctuation))

print(cpf)
