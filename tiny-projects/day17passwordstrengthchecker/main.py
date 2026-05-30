def main():
    password = input("Enter a password to check: ")
    score = check_strength(password)

    if score <= 2:
        print("Weak")
    elif score == 3:
        print("Medium")
    elif score == 4:
        print("Strong")
    else:
        print("Very Strong")

def check_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    symbols = "!@#$%^&*()-_=+[]{};:'\",.<>/?\\|`~"
    if any(char in symbols for char in password):
        score += 1

    return score

main()
