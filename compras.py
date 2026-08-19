class Purchase()

    def __init__(self, products):
        self.products = products

    def add_product(product):
        self.products.append(product)

    def confirm_product():
        total_price = 0
 
        print("=== Compras ===")
        print(" === Lista productos ===")
       
        for product_i in self.products:
            
            print("id: ", product_i["id"])
            print("nombre: ", product_i["nombre"])
            print("precio: ", product_i["precio"])
            print("stock: ", product_i["stock"])
            total_price += product_i["precio"]

        print("Precio total: ", total_price)


        input("Confirm product: ")

