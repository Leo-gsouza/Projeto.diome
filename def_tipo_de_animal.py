a = "vertebrado"
b = "mamifero"
c = "herbivoro"

if a == 'vertebrado':
  if b == "ave":
    tipo_de_animal = "aguia" if c == "carnivoro" else "pomba"
    print(tipo_de_animal)
  elif b == "mamifero":
    tipo_de_animal = "homem" if c == "onivoro" else "vaca"
    print(tipo_de_animal)

elif a == 'invertebrado':
  if b == "inseto":
    tipo_de_animal = "pulga" if c == "hematofago" else "lagarta"
    print(tipo_de_animal)
  elif b == "anelideo":
    tipo_de_animal = "sanguessuga" if c == "hematofago" else "minhoca"
    print(tipo_de_animal)