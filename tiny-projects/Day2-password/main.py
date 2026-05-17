#Password gen project
#ask the user for password length, ask for symbols, build a pool of characters
#Ensure at least 1 latter, 1 digit, 1 symbol, fill the rest with random characters
#shuffle the results and then print the password

import random
import string

def main():
    print("Password Generator")
    length = int(input("Enter password length: "))
    use_symbols = input("include symbols> (y/n): ").lower() == 'y'
    password = generate_password(length, use_symbols)

    print(f"Generated password: {password}")


def generate_password(length, use_symbols):

    min_required = 2 + (1 if use_symbols else 0)
    if length < min_required:
        raise ValueError(f"Password length must be at least {min_required}.")
    
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation if use_symbols else ''

    all_chars = letters + digits + symbols

    password_chars = [random.choice(letters), random.choice(digits)]

    if use_symbols:
        password_chars.append(random.choice(symbols))

    remaining = length - len(password_chars)
    if remaining > 0:
        password_chars += random.choices(all_chars, k = remaining)
    random.shuffle(password_chars)
    return ''.join(password_chars)
main()