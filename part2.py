class Product:
    def __init__(self, name, stock, threshold):
        self.name = name
        self.stock = stock
        self.threshold = threshold
    
    def reduce_stock(self, quantity):
        self.stock -= quantity
        if self.stock < self.threshold:
            print(f"Alert: {self.name} needs restocking. Current stock: {self.stock} units.")
    
    def restock(self, quantity):
        self.stock += quantity
        print(f"{self.name} has been restocked. New stock: {self.stock} units.")
    
    def __repr__(self):
        return f"{self.name}: {self.stock} units"


class Inventory:
    def __init__(self):
        self.products = {}
    
    def add_product(self, product):
        self.products[product.name] = product
    
    def process_sales_orders(self, sales_orders):
        for product_name, quantity in sales_orders.items():
            if product_name in self.products:
                product = self.products[product_name]
                product.reduce_stock(quantity)
            else:
                print(f"Product {product_name} not found in inventory.")
    
    def restock_items(self, restock_list):
        for product_name, quantity in restock_list.items():
            if product_name in self.products:
                product = self.products[product_name]
                product.restock(quantity)
            else:
                print(f"Product {product_name} not found in inventory.")
    
    def display_inventory(self):
        print("\nCurrent Inventory:")
        for product in self.products.values():
            print(product)


inventory = Inventory()

inventory.add_product(Product("ProductA", 50, 10))
inventory.add_product(Product("ProductB", 20, 10))
inventory.add_product(Product("ProductC", 5, 10))

sales_orders = {
    "ProductA": 45,
    "ProductB": 5,
    "ProductC": 3
}
inventory.process_sales_orders(sales_orders)

restock_list = {
    "ProductA": 50,
    "ProductC": 20
}
inventory.restock_items(restock_list)

inventory.display_inventory()
