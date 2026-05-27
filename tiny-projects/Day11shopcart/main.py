from logic import add_to_cart, remove_from_cart, calculate_total
from ui import show_menu, show_products_ui, add_product_ui, remove_product_ui, view_cart, checkout, show_message

products = [
    {"product": "Apple", "price": 1.50},
    {"product": "Bread", "price": 3.20},
    {"product": "Milk", "price": 2.80}
]

def main():
    cart = []
    while True:
        choice = show_menu()
        if choice =="1":
            show_products_ui(products)

        elif choice == "2":
            index = add_product_ui(products)
            if index is not None:
                add_to_cart(cart, products, index)
                show_message("Item added to cart.")

        elif choice == "3":
            index = remove_product_ui(cart)
            if index is not None:
                remove_from_cart(cart, index)
                show_message("Removed from cart.")

        elif choice == "4":
            view_cart(cart)

        elif choice == "5":
            total = calculate_total(cart)
            confirmed = checkout(cart, total)
            if confirmed:
                cart.clear()

        elif choice == "6":
            show_message("Goodbye!")
            break
        else:
            show_message("Invalid choice. Please try again")

main()