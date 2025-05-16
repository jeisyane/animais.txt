with open("animais.txt", "w") as arquivo:
    animais = ["gato", "cachorro", "leão", "tigre", "elefante"]
    for animal in animais:
        arquivo.write(animal + "\n")

