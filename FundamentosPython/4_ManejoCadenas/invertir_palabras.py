
frase = input("Escribe una frase: ")
palabras = frase.split()
invertidas = [palabra[::-1] for palabra in palabras]
print("Frase con palabras invertidas:", ' '.join(invertidas))