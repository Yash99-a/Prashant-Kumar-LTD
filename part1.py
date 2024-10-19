class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.orders = []  # List to hold all orders created by the user

    def create_order(self, products):
        """Creates a new order for the user."""
        order_id = len(self.orders) + 1
        new_order = Order(order_id, self, products)
        self.orders.append(new_order)
        return new_order

    def view_orders(self):
        """Displays all orders for the user."""
        for order in self.orders:
            order.display_order_details()

    def __str__(self):
        return f"User ID: {self.user_id}, Name: {self.name}, Email: {self.email}"


class Product:
    def __init__(self, product_id, name, price, description):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Description: {self.description}"


class Order:
    def __init__(self, order_id, user, products):
        self.order_id = order_id
        self.user = user  # Reference to the user who created the order
        self.products = products  # List of Product objects
        self.status = 'pending'  # Initial status of the order
        self.payment = None  # Payment object will be associated later

    def update_status(self, status):
        """Updates the status of the order."""
        self.status = status

    def add_payment(self, payment):
        """Associates a payment with the order."""
        self.payment = payment

    def display_order_details(self):
        """Displays the details of the order."""
        print(f"Order ID: {self.order_id}")
        print(f"User: {self.user.name}")
        print(f"Status: {self.status}")
        print("Products:")
        for product in self.products:
            print(f" - {product.name} (${product.price})")
        if self.payment:
            print(f"Payment Status: {self.payment.status}, Amount Paid: ${self.payment.amount}")
        else:
            print("Payment: Not made yet")
        print()

    def __str__(self):
        return f"Order ID: {self.order_id}, Status: {self.status}, Number of Products: {len(self.products)}"


class Payment:
    def __init__(self, payment_id, order, amount, status='pending'):
        self.payment_id = payment_id
        self.order = order  # Reference to the order being paid for
        self.amount = amount
        self.status = status

    def process_payment(self):
        """Processes the payment for the order."""
        if self.status == 'pending':
            # Simulate payment processing logic
            self.status = 'completed'
            self.order.update_status('completed')
            print(f"Payment of ${self.amount} for Order ID {self.order.order_id} has been processed successfully.")
        else:
            print("Payment has already been processed.")

    def __str__(self):
        return f"Payment ID: {self.payment_id}, Status: {self.status}, Amount: {self.amount}"


# Example usage of the classes
def main():
    # Create some products
    product1 = Product(1, "Laptop", 1000, "High performance laptop")
    product2 = Product(2, "Headphones", 100, "Noise-cancelling headphones")
    product3 = Product(3, "Mouse", 20, "Wireless mouse")

    # Create a user
    user1 = User(1, "Yash", "yash@gmail.com")

    # User creates an order
    order1 = user1.create_order([product1, product2])

    # Display orders for the user
    print("User's Orders:")
    user1.view_orders()

    # Process payment for the order
    payment1 = Payment(1, order1, amount=1100)
    order1.add_payment(payment1)
    payment1.process_payment()

    # Update order status and display the updated details
    order1.update_status('shipped')
    print("\nUpdated Order Details:")
    user1.view_orders()


if __name__ == "__main__":
    main()
