with open("animais.txt", "r") as arquivo:
    lista_animais = arquivo.readlines()

print("Animais no arquivo:")
for animal in lista_animais:
    print("Animal:", animal.strip())
