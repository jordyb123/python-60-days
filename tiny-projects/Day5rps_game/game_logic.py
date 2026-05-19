import random
from utils import map_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def convert_choice(choice):
    return map_choice(choice)

def determine_winner(player, computer):
    if player == computer:
        return "draw"
    
    rules = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    if rules[player] == computer:
        return "win"
    else:
        return "lose"