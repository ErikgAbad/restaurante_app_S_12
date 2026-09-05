from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.usuario import Usuario

def menu():
    print("\n" + "=" * 52)
    print("      🍽️  RESTAURANTE APP — SEMANA 12")
    print("=" * 52)
    print("1. Registrar producto")
    print("2. Registrar usuario")
    print("3. Registrar venta")
    print("4. Buscar producto por código")
    print("5. Buscar usuario por identificación")
    print("6. Consultar ventas de un usuario")
    print("7. Listar todos los productos")
    print("8. Listar todos los usuarios")
    print("9. Listar todas las ventas")
    print("0. Salir")
    print("-" * 52)
    return input("Seleccione una opción: ")

def main():
    app = Restaurante()

    while True:
        opcion = menu()

        # ─── 1. Registrar producto ───
        if opcion == "1":
            print("\n--- Registrar Producto ---")
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            texto_precio = input("Precio: $")
            precio = float(texto_precio.replace("$", "").replace(",", "."))
            stock = int(input("Stock inicial: "))

            try:
                producto = Producto(codigo, nombre, precio, stock)
                app.registrar_producto(producto)
                print("✅ Producto registrado correctamente!")
            except ValueError as err:
                print(f"❌ {err}")

        # ─── 2. Registrar usuario ───
        elif opcion == "2":
            print("\n--- Registrar Usuario ---")
            identificacion = input("Identificación: ")
            nombre = input("Nombre completo: ")
            correo = input("Correo electrónico: ")

            try:
                usuario = Usuario(identificacion, nombre, correo)
                app.registrar_usuario(usuario)
                print("✅ Usuario registrado correctamente!")
            except ValueError as err:
                print(f"❌ {err}")

        # ─── 3. Registrar venta ───
        elif opcion == "3":
            print("\n--- Registrar Venta ---")
            id_usuario = input("Identificación del usuario: ")
            codigo_producto = input("Código del producto: ")
            cantidad = int(input("Cantidad: "))

            try:
                venta = app.registrar_venta(id_usuario, codigo_producto, cantidad)
                print(f"✅ Venta registrada! Total: ${venta.total:.2f}")
            except ValueError as err:
                print(f"❌ Error: {err}")

        # ─── 4. Buscar producto por código ───
        elif opcion == "4":
            print("\n--- Buscar Producto ---")
            codigo = input("Código del producto: ")
            prod = app.buscar_producto_por_codigo(codigo)
            if prod:
                print(prod)
            else:
                print("❌ Producto no encontrado")

        # ─── 5. Buscar usuario por identificación ───
        elif opcion == "5":
            print("\n--- Buscar Usuario ---")
            ide = input("Identificación del usuario: ")
            usu = app.buscar_usuario_por_id(ide)
            if usu:
                print(usu)
            else:
                print("❌ Usuario no encontrado")

        # ─── 6. Consultar ventas de un usuario ───
        elif opcion == "6":
            print("\n--- Ventas de Usuario ---")
            ide = input("Identificación del usuario: ")
            ventas = app.obtener_ventas_por_usuario(ide)
            if ventas:
                for v in ventas:
                    print(v)
            else:
                print("ℹ️ No hay ventas para este usuario")

        # ─── 7. Listar todos los productos ───
        elif opcion == "7":
            print("\n--- Lista de Productos ---")
            prods = app.listar_productos()
            if prods:
                for p in prods:
                    print(p)
            else:
                print("ℹ️ No hay productos registrados")

        # ─── 8. Listar todos los usuarios ───
        elif opcion == "8":
            print("\n--- Lista de Usuarios ---")
            usus = app.listar_usuarios()
            if usus:
                for u in usus:
                    print(u)
            else:
                print("ℹ️ No hay usuarios registrados")

        # ─── 9. Listar todas las ventas ───
        elif opcion == "9":
            print("\n--- Lista de Todas las Ventas ---")
            vents = app.listar_ventas()
            if vents:
                for v in vents:
                    print(v)
            else:
                print("ℹ️ No hay ventas registradas")

        # ─── 0. Salir ───
        elif opcion == "0":
            print("👋 ¡Gracias por usar el sistema!")
            break

        else:
            print("⚠️ Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    main()