import random

def main():
    word = choose_word()
    guessed_letters = set()
    lives = 5

    while True:
        game = display_word(word, guessed_letters)
        print(game)
        print(f"Lives left: {lives}")


        guess = get_guess(guessed_letters)
        guessed_letters, lives = update_state(guess, guessed_letters, lives, word)

        if all(letter in guessed_letters for letter in word):
            print(f"You win! The word was '{word}'.")
            break

        if lives <= 0:
            print(f"You lose! The world was '{word}'.")
            break

def choose_word():
    words = ["python", "hangman", "variable", "function", "loop"]
    word = random.choice(words)
    return word

def display_word(word, guessed_letters):
    return  " ".join(letter if letter in guessed_letters else "_" for letter in word)
    

def get_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Enter one letter only.")
        elif guess in guessed_letters:
            print("You already guessed that.")
        elif guess.isdigit():
            print("Guess cannot be a number.")
        else: 
            return guess


def update_state(guess, guessed_letters, lives, word):   
    guessed_letters.add(guess)
    if guess in word:
        print("Correct guess!")
    else: 
        print("Wrong guess!")
        lives -= 1
    
    return guessed_letters, lives

main()