marca = input("Marca do veiculo: ")
modelo = input("Modelo do veiculo: ")
veiculo = {"marca": marca, "modelo": modelo }


def exibir_veiculo(data_extenso, *args, **kwargs):
    data = data_extenso.center(30,"▬")
    mensagem = "\n".join(args).title()
    informacoes = "\n".join([f"╣{chave.title()}:{valor.title()}║" for chave, valor in veiculo.items()])
    resultado = f"{data_extenso}\n\n{mensagem}\n\n{informacoes}"
    print (resultado)


exibir_veiculo(
    "17 de setembro de 2023",
    "Meu carro é bom",
    "é bom demais.",
    "Ele vai no ar",
    "se você deixar.",
)