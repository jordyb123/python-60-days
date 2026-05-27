import random

def roll_die(sides):
    return random.randint(1, sides)

def roll_multiple_dice(count, sides):
    rolls = []
    for _ in range(count):
        rolls.append(roll_die(sides))
    return rolls