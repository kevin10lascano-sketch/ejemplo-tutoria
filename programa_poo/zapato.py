class  Zapato:
    def __init__(self, marca, talla, color):
        self.marca = marca
        self.talla = talla
        self.color = color

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Talla: {self.talla}")
        print(f"Color: {self.color}")

