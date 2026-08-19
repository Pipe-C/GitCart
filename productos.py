"""
Módulo de Gestión de Productos (GitCart)
Permite listar, consultar por ID y registrar nuevos productos en el catálogo.
"""

import random

# Listas base para combinar y crear nombres aleatorios
CATEGORIAS = ["Mouse", "Teclado", "Monitor", "Auriculares", "Webcam", "Micrófono", "Impresora", "Pad Mouse"]
MARCAS = ["Logitech", "Razer", "Corsair", "HyperX", "SteelSeries", "Asus", "Acer", "Dell", "HP", "Lenovo"]

def generar_productos_aleatorios(cantidad: int = 5) -> list:
    """Genera una lista de productos aleatorios con nombres, precios y stock."""
    productos_generados = []
    
    for i in range(cantidad):
        id_prod = i + 1
        nombre = f"{random.choice(MARCAS)} {random.choice(CATEGORIAS)}"
        precio = random.randint(20, 300) * 1000
        stock = random.randint(5, 50)

        productos_generados.append({
            "id": id_prod,
            "nombre": nombre,
            "precio": precio,
            "stock": stock
        })

    # El return debe estar FUERA del for para generar los 5 productos
    return productos_generados

# Catálogo inicial cargado aleatoriamente
PRODUCTOS = generar_productos_aleatorios(5)


# --- FUNCIONES DE CONSULTA Y MOSTRADO ---

def formatear_precio(precio: float) -> str:
    """Formatea un precio en formato de moneda colombiana (COP)."""
    return f"${precio:,.0f}".replace(",", ".")

def mostrar_productos():
    """Muestra en consola el catálogo de productos disponibles."""
    print("\n" + "=" * 52)
    print("           === PRODUCTOS DISPONIBLES ===")
    print("=" * 52)
    print(f"{'ID':<4} {'NOMBRE':<25} {'PRECIO':<12} {'STOCK':<5}")
    print("-" * 52)

    for prod in PRODUCTOS:
        precio_fmt = formatear_precio(prod["precio"])
        print(f"{prod['id']:<4} {prod['nombre']:<25} {precio_fmt:<12} {prod['stock']:<5}")
    
    print("=" * 52)

def obtener_producto_por_id(id_producto: int) -> dict | None:
    """Busca y retorna un producto por su ID."""
    for prod in PRODUCTOS:
        if prod["id"] == id_producto:
            return prod
    return None

def registrar_producto():
    """Permite ingresar un nuevo producto manualmente (Requisito de la guía)."""
    print("\n--- Registrar Nuevo Producto ---")
    nombre = input("Nombre del producto: ").strip()
    
    if not nombre:
        print(" Error: El nombre no puede estar vacío.")
        return

    try:
        precio = float(input("Precio ($): "))
        stock = int(input("Stock inicial: "))
        if precio <= 0 or stock < 0:
            print(" Error: Ingrese valores válidos de precio y stock.")
            return
    except ValueError:
        print(" Error: Ingrese valores numéricos válidos.")
        return

    nuevo_id = max([p["id"] for p in PRODUCTOS], default=0) + 1
    
    PRODUCTOS.append({
        "id": nuevo_id,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    })
    print(f" Producto '{nombre}' registrado exitosamente con ID {nuevo_id}.")