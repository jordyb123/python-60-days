import random


words = ["python", "variable", "function", "loop", "hangman"]

def main():
    word = choose_word()
    scrambled = scramble_word(word)
    print(scrambled)
    while True:
        guess = get_guess()
        if guess == word:
            print("Correct!")
            break
        else:
            print("try again!")

def choose_word():
    word = random.choice(words)
    return word

def scramble_word(word):

    scrambled = word
    while scrambled == word:
        letters = list(word)
        random.shuffle(letters)
        scrambled = "".join(letters)
    return scrambled

def get_guess():
    while True:
        guess = input("Guess the word: ").lower()
        
        if len(guess) <= 1:
            print("Guess must be more than one character.")
        elif guess.isalpha():
            print("Guess cannot be a number.")
        else:
            return guess

main()