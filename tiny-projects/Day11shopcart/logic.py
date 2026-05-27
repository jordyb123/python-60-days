def add_to_cart(cart, products, index):
    cart.append(products[index])

def remove_from_cart(cart, index):
    cart.pop(index)

def calculate_total(cart):
    return sum(item["price"] for item in cart)
    