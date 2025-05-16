import random

with open('animais.txt', 'r') as arquivo:
    animais = [linha.strip() for linha in arquivo]

animal_sorteado = random.choice(animais)
print(f"Animal sorteado: {animal_sorteado}")
