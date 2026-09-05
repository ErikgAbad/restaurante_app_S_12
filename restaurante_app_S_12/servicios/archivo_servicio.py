import json
from pathlib import Path
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

# ✅ RUTA FIJA — NO FALLA
BASE = Path(__file__).parent.parent
RUTA_DATOS = BASE / "datos"

class ArchivoServicio:
    @staticmethod
    def cargar_productos():
        ruta = RUTA_DATOS / "productos.json"
        ruta.parent.mkdir(parents=True, exist_ok=True)
        if not ruta.exists() or ruta.stat().st_size == 0:
            with open(ruta, "w", encoding="utf-8") as f:
                f.write("[]")
            return []
        with open(ruta, "r", encoding="utf-8") as f:
            datos = json.load(f)
        return [Producto.from_dict(item) for item in datos]

    @staticmethod
    def guardar_productos(productos):
        ruta = RUTA_DATOS / "productos.json"
        ruta.parent.mkdir(parents=True, exist_ok=True)
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump([p.to_dict() for p in productos], f, indent=2, ensure_ascii=False)
        print(f"✅ Guardado en: {ruta.resolve()}")  # ← TE DICE DÓNDE GUARDA

    @staticmethod
    def cargar_usuarios():
        ruta = RUTA_DATOS / "usuarios.json"
        ruta.parent.mkdir(parents=True, exist_ok=True)
        if not ruta.exists() or ruta.stat().st_size == 0:
            with open(ruta, "w", encoding="utf-8") as f:
                f.write("[]")
            return []
        with open(ruta, "r", encoding="utf-8") as f:
            datos = json.load(f)
        return [Usuario.from_dict(item) for item in datos]

    @staticmethod
    def guardar_usuarios(usuarios):
        ruta = RUTA_DATOS / "usuarios.json"
        ruta.parent.mkdir(parents=True, exist_ok=True)
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump([u.to_dict() for u in usuarios], f, indent=2, ensure_ascii=False)

    @staticmethod
    def cargar_ventas():
        ruta = RUTA_DATOS / "ventas.json"
        ruta.parent.mkdir(parents=True, exist_ok=True)
        if not ruta.exists() or ruta.stat().st_size == 0:
            with open(ruta, "w", encoding="utf-8") as f:
                f.write("[]")
            return []
        with open(ruta, "r", encoding="utf-8") as f:
            datos = json.load(f)
        return [Venta.from_dict(item) for item in datos]

    @staticmethod
    def guardar_ventas(ventas):
        ruta = RUTA_DATOS / "ventas.json"
        ruta.parent.mkdir(parents=True, exist_ok=True)
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump([v.to_dict() for v in ventas], f, indent=2, ensure_ascii=False)