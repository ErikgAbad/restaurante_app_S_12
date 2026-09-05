from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio

class Restaurante:
    def __init__(self):
        self.productos = ArchivoServicio.cargar_productos()
        self.usuarios = ArchivoServicio.cargar_usuarios()
        self.ventas = ArchivoServicio.cargar_ventas()

    # ─── Productos ───
    def registrar_producto(self, producto):
        if self.buscar_producto_por_codigo(producto.codigo):
            raise ValueError(f"⚠️ El producto con código {producto.codigo} ya existe")
        self.productos.append(producto)
        ArchivoServicio.guardar_productos(self.productos)

    def buscar_producto_por_codigo(self, codigo):
        for p in self.productos:
            if p.codigo == codigo:
                return p
        return None

    def listar_productos(self):
        return self.productos

    # ─── Usuarios ───
    def registrar_usuario(self, usuario):
        if self.buscar_usuario_por_id(usuario.identificacion):
            raise ValueError(f"⚠️ El usuario con identificación {usuario.identificacion} ya existe")
        self.usuarios.append(usuario)
        ArchivoServicio.guardar_usuarios(self.usuarios)

    def buscar_usuario_por_id(self, identificacion):
        for u in self.usuarios:
            if u.identificacion == identificacion:
                return u
        return None

    def listar_usuarios(self):
        return self.usuarios

    # ─── Ventas ───
    def registrar_venta(self, id_usuario, codigo_producto, cantidad):
        usuario = self.buscar_usuario_por_id(id_usuario)
        if not usuario:
            raise ValueError(f"Usuario {id_usuario} no encontrado")

        producto = self.buscar_producto_por_codigo(codigo_producto)
        if not producto:
            raise ValueError(f"Producto {codigo_producto} no encontrado")

        if cantidad > producto.stock:
            raise ValueError(f"Stock insuficiente. Disponible: {producto.stock}")

        # Descontar stock
        producto.stock -= cantidad

        # Generar ID de venta
        id_venta = len(self.ventas) + 1

        venta = Venta(
            id_venta,
            usuario.identificacion,
            producto.codigo,
            cantidad,
            producto.precio
        )

        self.ventas.append(venta)
        ArchivoServicio.guardar_productos(self.productos)
        ArchivoServicio.guardar_ventas(self.ventas)
        return venta

    def obtener_ventas_por_usuario(self, identificacion):
        return [v for v in self.ventas if v.identificacion_usuario == identificacion]

    def listar_ventas(self):
        return self.ventas