class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

c = Coche("Toyota", "Corolla")
c.descripcion()