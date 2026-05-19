from utils import is_valid_rps_choice, clean

def show_menu():
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = clean(input("Enter your choice: "))

    if not is_valid_rps_choice(choice):
        return None
    
    return choice
    
def show_result(player, computer, outcome):
    print(f"You chose {player}. ")
    print(f"Computer chose {computer}. ")
    if outcome == "win":
        print("Congratulations! You win!")
    elif outcome == "lose":
        print("Sorry, you got COOKED!")
    else:
        print("Tie!, COOKED AGAIN!")

def ask_to_play_again():
    choice = input("Do you want to play again? (y/n): ")
    return choice.lower() == "y"
    