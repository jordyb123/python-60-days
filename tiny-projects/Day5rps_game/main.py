from ui import show_menu, show_result, ask_to_play_again
from game_logic import get_computer_choice, convert_choice, determine_winner
from utils import clean, line
        



def main ():
    start_game()

def start_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        line()
        choice = show_menu()
        player_choice = convert_choice(choice)

        if player_choice is None:
            print("Invalid choice. Try again.")
            continue

        computer_choice = get_computer_choice()
        outcome = determine_winner(player_choice, computer_choice)

        show_result(player_choice, computer_choice, outcome)

        if not ask_to_play_again():
            print("Thanks for playing!")
            break
        line()
        input("press enter to continue...")
        line()
        print()

main()