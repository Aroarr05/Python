texto = input("Ingresa un texto: ").lower()
vocales = "aeiou"

for vocal in vocales:
    print(f"{vocal}: {texto.count(vocal)}")