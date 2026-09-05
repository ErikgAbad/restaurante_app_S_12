class Usuario:
    def __init__(self, identificacion, nombre, correo):
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo

    def to_dict(self):
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo
        }

    @classmethod
    def from_dict(cls, datos):
        return cls(datos["identificacion"], datos["nombre"], datos["correo"])

    def __str__(self):
        return f"[{self.identificacion}] {self.nombre} - 📧 {self.correo}"