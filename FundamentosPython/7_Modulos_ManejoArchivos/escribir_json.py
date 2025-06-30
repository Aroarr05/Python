import json

datos = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

with open("datos.json", "w") as archivo:
    json.dump(datos, archivo)