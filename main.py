"""
Sistema Principal (GitCart)
Unifica los módulos de Gestión de Productos y Proceso de Compras.
"""
import productos
from compras import Purchase

def menu_principal():
    # Instancia única del carrito de compras para la sesión
    carrito = Purchase()

    while True:
        print("\n" + "=" * 45)
        print("           🛒 SISTEMA GITCART 🛒")
        print("=" * 45)
        print("1. Ver catálogo de productos")
        print("2. Consultar producto por ID")
        print("3. Registrar nuevo producto")
        print("4. Agregar producto al carrito")
        print("5. Ver carrito y finalizar compra")
        print("6. Salir")
        print("=" * 45)

        opcion = input("Seleccione una opción (1-6): ").strip()

        if opcion == "1":
            productos.mostrar_productos()

        elif opcion == "2":
            try:
                id_buscar = int(input("\nIngrese el ID del producto: "))
                prod = productos.obtener_producto_por_id(id_buscar)
                if prod:
                    precio_fmt = productos.formatear_precio(prod["precio"])
                    print(f"\n Producto encontrado:")
                    print(f"   ID: {prod['id']} | Nombre: {prod['nombre']} | Precio: {precio_fmt} | Stock: {prod['stock']}")
                else:
                    print(f"\n No se encontró ningún producto con ID {id_buscar}.")
            except ValueError:
                print(" Error: Debe ingresar un ID numérico válido.")

        elif opcion == "3":
            productos.registrar_producto()

        elif opcion == "4":
            productos.mostrar_productos()
            try:
                id_prod = int(input("\nIngrese el ID del producto a comprar: "))
                prod = productos.obtener_producto_por_id(id_prod)
                if prod:
                    carrito.add_product(prod)
                else:
                    print(f" No se encontró ningún producto con ID {id_prod}.")
            except ValueError:
                print(" Error: Ingrese un ID numérico válido.")

        elif opcion == "5":
            carrito.confirm_product()

        elif opcion == "6":
            print("\n ¡Gracias por utilizar GitCart! Hasta pronto.")
            break

        else:
            print(" Opción inválida. Ingrese un número entre 1 y 6.")

if __name__ == "__main__":
    menu_principal()