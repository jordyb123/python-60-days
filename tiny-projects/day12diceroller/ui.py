def get_dice_count():
    choice = input("How many dice do you want to roll? ")
    if not choice.isdigit():
        print("Please enter a valid number.")
        return None
    return int(choice)

def get_dice_sides():
    choice = input("How many sides should the dice have? (6, 10, 20 etc.) ")
    if not choice.isdigit():
        print("Please enter a valid number.")
    return int(choice)

def show_rolls(rolls):
    print("\nResults: ")
    for i, roll in enumerate(rolls, start=1):
        print(f"die {i}: {roll}")
    print(f"Total: {sum(rolls)}")

def ask_roll_again():
    choice = input("\nRoll again? (y/n): ").strip().lower()
    return choice == "y"