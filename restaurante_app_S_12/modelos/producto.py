class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }

    @classmethod
    def from_dict(cls, datos):
        return cls(datos["codigo"], datos["nombre"], datos["precio"], datos["stock"])

    def __str__(self):
        return f"[{self.codigo}] {self.nombre} - ${self.precio:.2f} | Stock: {self.stock}"