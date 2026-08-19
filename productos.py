"""
Módulo de Gestión de Productos (GitCart)
Permite listar, consultar por ID y registrar nuevos productos en el catálogo.
"""

# Librerías
import random

# Listas base para combinar y crear nombres aleatorios.
CATEGORIAS = ["Mouse", "Teclado", "Monitor", "Auriculares", "Monitor", "Webcam", "Micrófono", "Impresora", "Pad Mouse"]
MARCAS = ["Logitech", "Razer", "Corsair", "HyperX", "SteelSeries", "Asus", "Acer", "Dell", "HP", "Lenovo"]

def generar_productos_aleatorios(cantidad: int = 5) -> list:
    """
    Genera una lista de productos aleatorios con nombres, precios y stock aleatorios
    """
    productos = []
    for i in range(cantidad):
            "id": i + 1,
            "nombre": f"{random.choice(MARCAS)} {random.choice(CATEGORIAS)}",
            # Genera un precio aleatorio entre $20.00 y $300.000 redondeado a miles
            "precio": random.randint(20, 300) * 1000,
            "stock": random.randint(5, 50)

            productos_generados.append({
                "id": i,
                "nombre": nombre,
                "precio": precio,
                "stock": stock
            })

            return productos_generados

# Catálogo inicial cargado aleatoriamente
PRODUCTOS = generar_productos_aleatorios(5)


# --- FUNCIONES DE CONSULTA Y MOSTRADO ---

def formatear_precio(precio: float) -> str:
    """
    Formatea un precio en formato de moneda colombiana (COP).
    """
    return f"${precio:,.0f}".replace(",", ".")

def mostrar_productos():
    """ 
    Muestra en consola el catálogo de productos disponibles.
    """
    print("\n" + "=" * 48)
    print("        === PRODUCTOS DISPONIBLES ===")
    print("=" * 48)
    print(f"{'ID':<4} {'NOMBRE':<22} {'PRECIO':<12} {'STOCK':<5}")
    print("-" * 48)

    for prod in PRODUCTOS:
        preci_fmt = formatear_precio(prod["precio"]
        print(f"{prod['id']:<4} {prod['nombre']:<22} {preci_fmt:<12} {prod['stock']:<5}")

def obtener_productos_por_id(id_productos: int) -> dict | None:
    """
    Busca y retorna un producto por su ID.
    """
    for prod in PRODUCTOS:
        if prod["id"] == id_productos:
            return prod
    return None


