from datetime import datetime

class Venta:
    def __init__(self, id_venta, identificacion_usuario, codigo_producto, cantidad, precio_unitario, fecha=None):
        self.id_venta = id_venta
        self.identificacion_usuario = identificacion_usuario
        self.codigo_producto = codigo_producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.fecha = fecha if fecha else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.total = self.cantidad * self.precio_unitario

    def to_dict(self):
        return {
            "id_venta": self.id_venta,
            "identificacion_usuario": self.identificacion_usuario,
            "codigo_producto": self.codigo_producto,
            "cantidad": self.cantidad,
            "precio_unitario": self.precio_unitario,
            "fecha": self.fecha,
            "total": self.total
        }

    @classmethod
    def from_dict(cls, datos):
        return cls(
            datos["id_venta"],
            datos["identificacion_usuario"],
            datos["codigo_producto"],
            datos["cantidad"],
            datos["precio_unitario"],
            datos["fecha"]
        )

    def __str__(self):
        return f"📅 {self.fecha} | Usuario: {self.identificacion_usuario} | Producto: {self.codigo_producto} | Cantidad: {self.cantidad} | Total: ${self.total:.2f}"