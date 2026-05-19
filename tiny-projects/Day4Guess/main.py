import random

def main():
    start_game()

def start_game():
    print("Welcome to the Guessing Game!")
    choose_range()

def choose_range():
    print("Choose a range for the max number. The higher the number the more attempts you have to guess.")
    print("1. 50 - 7 attempts - Easy")
    print("2. 100 - 10 attempts - Standard")
    print("3. 500 - 12 attempts - Hard")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        range_max = 50
    elif choice == 2:
        range_max = 100
    elif choice == 3:
        range_max= 500
    else:
        print("Invalid choice. Try again.")
        return choose_range()
    
    attempts_based_on_range(range_max)


def attempts_based_on_range(range_max):
    if range_max == 50:
        attempts = 7
    elif range_max == 100:
        attempts = 10
    elif range_max == 500:
        attempts = 12
    play_round(range_max, attempts)

def play_round(range_max, attempts):
    secret = random.randint(1, range_max)
    print(f"You have {attempts} attempts to guess the number between 1 and {range_max}.")
    while attempts > 0:
        guess = int(input("Enter your guess "))
        if guess < secret:
            print("Too low!")
            attempts -= 1
        elif guess > secret:
            print("Too high!")
            attempts -= 1
        else:
            print("Congratulations! You guessed the correct number!")
            break

        print(f"you have {attempts} attempts left.")
        if attempts == 0:
            print(f"Game Over! The correct number was {secret}.")

     
    ask_to_play_again()

def ask_to_play_again():
    choice = input("Do you want to play again? (y/n) ").lower()
    if choice == "y":
        start_game()
    elif choice == "n":
        print("Thanks for playing! Goodbye!")
    else:
        print("Invalid choice. Enter either y or n.")
        ask_to_play_again()

main()
        
        