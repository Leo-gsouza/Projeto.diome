lista = ["Leo","Naty","Luna","Lili"]
print(lista)
#JOIN
print("".join(lista))#LeoNatyLunaLili ▬▬▬ lista em string 

#COUNT
print(lista.count("Naty"))#1 ▬▬▬ Exibi o indice que a string está dentro da lista

#SPLIT
texto = "Leonardo Garcia de Souza"
print (texto.split())#['Leonardo', 'Garcia', 'de', 'Souza'] ▬▬▬ string em lista
print (texto.split("a"))#['Leon', 'rdo G', 'rci', ' de Souz', ''] ▬▬▬ string em lista e removeu a letra "a"

#REPLACE
print(texto.replace("Leonardo","Leo",1))#Leo Garcia de Souza




