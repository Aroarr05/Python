
with open("datos.txt", "r") as archivo:
    lineas = archivo.readlines()
    print(f"Cantidad de líneas: {len(lineas)}")