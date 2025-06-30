nombre_completo = input("Ingresa tu nombre y apellidos: ")
iniciales = [palabra[0].upper() for palabra in nombre_completo.split()]
print("Iniciales:", ''.join(iniciales))