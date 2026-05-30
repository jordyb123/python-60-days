import random

def main():
    coins = ["head", "tail"]
    while True:
        choice = show_menu()
        
        if choice == 1:
            coin = flip_coin(coins)
            print(coin)

        elif choice == 2:
            times = int(input("How many times do you want to flip a coin? "))
            head, tail = flip_multiple(coins, times)
            print(f"Head: {head}")
            print(f"Tail: {tail}")

        elif choice == 3:
            print("Goodbye!")
            break
        else:
            print("Please enter a number.")


def flip_coin(coins):
    coin = random.choice(coins)
    return coin
    
def flip_multiple(coins, times):
    i = 0
    head = 0
    tail = 0

    while i < times:
        coin = flip_coin(coins)
        if coin == "head":
            head += 1
        else:
            tail += 1
        i += 1
    
    return head, tail

def show_menu():
    while True:

        print("Coin Flip Menu")
        print("1. Flip single coin.")
        print("2. Flip multiple coins.")
        print("3. Exit")
        choice = input("Choose a menu item.: ")

        if choice.isdigit():
            return int(choice)
        else:
            print("You must enter a number.")

main()