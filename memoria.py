import random

class Memoria:
    def __init__(self, cantidad=50, ordenado=False):
        if ordenado:
            self.datos = sorted(random.sample(range(1, 1001), cantidad))
        else:
            self.datos = random.sample(range(1, 1001), cantidad)

    def mostrar(self, limite=None):
        if limite is None:
            print("Contenido completo de memoria:", self.datos)
        else:
            print(f"Primeros {limite} elementos de memoria:", self.datos[:limite])

    def obtener_datos(self):
        return self.datos


