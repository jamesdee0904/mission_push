class Product:
    inventory = []  # Class variable to hold product instances
    product_counter = 1  # To auto-generate unique product IDs

    def __init__(self, product_id, name, category, quantity, price, supplier):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.supplier = supplier

    @classmethod
    def add_product(cls, name, category, quantity, price, supplier):
        product_id = cls.product_counter
        new_product = cls(product_id, name, category, quantity, price, supplier)
        cls.inventory.append(new_product)
        cls.product_counter += 1
        return "Product added successfully!"

    @classmethod
    def view_products(cls):
        if not cls.inventory:
            print("Inventory is empty.")
            return

        print("\n Current Inventory:")
        for product in cls.inventory:
            print(f"ID: {product.product_id}, Name: {product.name}, "
                  f"Category: {product.category}, Quantity: {product.quantity}, "
                  f"Price: ₱{product.price:.2f}, Supplier: {product.supplier}")

    @classmethod
    def update_product(cls, product_id, quantity=None, price=None, supplier=None):
        for product in cls.inventory:
            if product.product_id == product_id:
                if quantity is not None:
                    product.quantity = quantity
                if price is not None:
                    product.price = price
                if supplier is not None:
                    product.supplier = supplier
                return "Product information updated successfully!"
        return "Product not found."

    @classmethod
    def delete_product(cls, product_id):
        for product in cls.inventory:
            if product.product_id == product_id:
                cls.inventory.remove(product)
                return "Product deleted successfully!"
        return "Product not found."


class Order:
    order_counter = 1  # Auto-generate order IDs

    def __init__(self, product_id, quantity, customer_info=None):
        self.order_id = Order.order_counter
        self.product_id = product_id
        self.quantity = quantity
        self.customer_info = customer_info or "Guest"
        Order.order_counter += 1

    def place_order(self):
        for product in Product.inventory:
            if product.product_id == self.product_id:
                if product.quantity >= self.quantity:
                    product.quantity -= self.quantity
                    return (f"Order placed successfully!\nOrder ID: {self.order_id}, "
                            f"Product: {product.name}, Quantity: {self.quantity}, "
                            f"Customer: {self.customer_info}")
                else:
                    return "Not enough stock to fulfill the order."
        return "Product not found."


def main_menu():
    while True:
        print("\n=== Inventory & Order Management ===")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Place Order")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Product name: ")
            category = input("Category: ")
            quantity = d
            price = float(input("Price: "))
            supplier = input("Supplier: ")
            print(Product.add_product(name, category, quantity, price, supplier))

        elif choice == '2':
            Product.view_products()

        elif choice == '3':
            try:
                product_id = int(input("Enter product ID to update: "))
                quantity = input("New quantity (leave blank to skip): ")
                price = input("New price (leave blank to skip): ")
                supplier = input("New supplier (leave blank to skip): ")

                quantity = int(quantity) if quantity else None
                price = float(price) if price else None
                supplier = supplier if supplier else None

                print(Product.update_product(product_id, quantity, price, supplier))
            except ValueError:
                print("Invalid input format.")

        elif choice == '4':
            try:
                product_id = int(input("Enter product ID to delete: "))
                print(Product.delete_product(product_id))
            except ValueError:
                print("Invalid product ID.")

        elif choice == '5':
            try:
                product_id = int(input("Enter product ID to order: "))
                quantity = int(input("Enter quantity: "))
                customer_info = input("Enter customer name (optional): ")

                order = Order(product_id, quantity, customer_info)
                print(order.place_order())
            except ValueError:
                print("Invalid input format.")

        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main_menu()
