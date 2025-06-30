frutas = ("manzana", "pera", "fresa", "kiwi")
buscar = input("Ingresa el nombre de una fruta: ").lower()
if buscar in frutas:
    print("La fruta está en la lista.")
else:
    print("La fruta NO está en la lista.")