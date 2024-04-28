import csv

class ShoppingCart:
    def __init__(self):
        self.inventory = {}
        self.cart = {}

    def load_inventory(self):
        with open('catalogue.csv', 'r') as file:
            reader = csv.DictReader(file)
            self.inventory = {row['Product']: {'price': float(row['Price']), 'quantity': int(row['Quantity'])} for row in reader}

    def display_commands(self):
        print("Commands: List, Cart, Add, Remove, Checkout")

    def display_items(self, items):
        for item, details in items.items():
            print("{}\t\t${}\t{}".format(item, details['price'], details['quantity']))

    def add_to_cart(self, product, quantity):
        if product in self.inventory and self.inventory[product]['quantity'] >= quantity:
            self.cart[product] = {'price': self.inventory[product]['price'], 'quantity': quantity}
            self.inventory[product]['quantity'] -= quantity
            print("{} {} added to cart.".format(quantity, product))
        else:
            print("Product not available or insufficient quantity.")

    def remove_from_cart(self, product):
        if product in self.cart:
            del self.cart[product]
            print("{} removed from cart.".format(product))
        else:
            print("Product not found in cart.")

    def checkout(self):
        total_price = sum(details['price'] * details['quantity'] for details in self.cart.values())
        total_price *= 1.07  # Apply 7% tax
        for product, details in self.cart.items():
            if details['quantity'] >= 3:
                total_price -= (details['price'] * details['quantity'] * 0.10)
        print("Total Price (including tax): ${:.2f}".format(total_price))

    def run(self):
        self.load_inventory()
        self.display_commands()
        while True:
            command = input("Enter a command: ").strip().lower()
            if command == "list":
                self.display_items(self.inventory)
            elif command == "cart":
                self.display_items(self.cart)
            elif command == "add":
                product = input("Enter product to add: ").strip()
                quantity = int(input("Enter quantity: "))
                self.add_to_cart(product, quantity)
            elif command == "remove":
                product = input("Enter product to remove: ").strip()
                self.remove_from_cart(product)
            elif command == "checkout":
                self.checkout()
                break
            else:
                print("Invalid command.")

if __name__ == "__main__":
    cart = ShoppingCart()
    cart.run()
