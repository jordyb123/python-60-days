from logic import roll_multiple_dice
from ui import get_dice_count, get_dice_sides, show_rolls, ask_roll_again

def main():
    print("=== Dice Roller ===")
    while True:
        count = get_dice_count()
        if count is None:
            continue
        sides = get_dice_sides()
        if sides is None:
            continue
        rolls = roll_multiple_dice(count, sides)
        show_rolls(rolls)
        if not ask_roll_again():
            print("Goodbye!!")
            break

main()