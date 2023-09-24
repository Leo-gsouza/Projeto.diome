def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args).upper()
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)


exibir_poema(
    "14 de setembro de 2023",#data_extenso
    "liberdade na vida",#*args
    "é ter um amor.",#*args
    "para se prender.",#*args
   
    autor="Fabrício Carpinejar",#**kwargs
    ano=1972,#**kwargs
    local= "Brasil",
)