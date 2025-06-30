import json

with open("datos.json", "r") as archivo:
    datos = json.load(archivo)
    print("Contenido del archivo:", datos)