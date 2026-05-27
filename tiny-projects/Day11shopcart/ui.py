from logic import calculate_total

def show_menu():
    print("\nShopping Cart Menu:")
    print("1. View products")
    print("2. Add item to cart")
    print("3. Remove item from cart")
    print("4. View cart")
    print("5. Checkout")
    print("6. Exit")
    choice = input("Choose a menu item: ")
    return choice

def show_products_ui(products):
    print("\nProducts: ")
    if not products:
        print("No products found.")
    else:
        for i, product in enumerate(products, start=1):
            print(f"{i}. {product['product']} - ${product['price']:.2f}")

def add_product_ui(products):
    print("Products: ")
    if not products:
        print("No products found.")
    else:
        for i, product in enumerate(products, start=1):
            print(f"{i}. {product['product']}- ${product['price']}")

    choice = input("Enter a product number to add to cart: ")
    if not choice.isdigit():
        print("Please enter a valid number: ")
        return None
    
    index = int(choice) - 1

    if index < 0 or index >= len(products):
        print("Invalid product number.")
        return None
    
    return index

def remove_product_ui(cart):
    print("Shopping Cart: ")
    if not cart:
        print("Cart is empty.")
    else:
        for i, item in enumerate(cart, start=1):
            print(f"{i}. {item['product']} - ${item['price']:.2f}")

    choice = input("Enter a product number to remove: ")
    if not choice.isdigit():
        print("Please enter a valid number.")
        return None
    
    index = int(choice) - 1

    if index < 0 or index >= len(cart):
        print("Invalid product number.")
        return None
    return index

def view_cart(cart):
    print("Shopping Cart")
    if not cart:
        print("Cart is empty.")
    else:
        for i, item in enumerate(cart, start=1):
            print(f"{i}. {item['product']} - ${item['price']:.2f}")

def checkout(cart, total):
    print("Shopping Cart")
    if not cart:
        print("Cart is empty.")
    else:
        for i, item in enumerate(cart, start=1):
            print(f"{i}. {item['product']} - ${item['price']:.2f}")
        print(f"\nTotal: ${total:.2f}")

    choice = input("Proceed to checkout? (y/n): ").strip().lower()
    if choice == "y":
        print("Checkout complete. Thank you for your purchase!")
        return True
    else:
        print("Checkout cancelled.")
        return False

def show_message(message):
    print(message)    