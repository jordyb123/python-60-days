def main_menu():
    print("\nMain Menu")
    print("1. Basic Math")
    print("2. Percentage Calculator")
    print("3. BMI Calculator")
    print("4. Unit Converter")
    print("5. Exit")
    return input("Choose an option ")

def math_menu():
    print("\nBasic Math")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Back")
    return input("Choose an option ")

def percentage_menu():
    print("1. Calculate percentage of a number")
    print("2. Calculate percentage increase")
    print("3. Calculate percentage decrease")
    print("4. Back")
    return input("Choose an option ")

def bmi_menu():
    print("BMI Calculator")
    print("Enter weight in kilograms and height in meters.")    

def unit_converter_menu():
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. Back")


def get_user_choice():
    choice = input("Enter your choice: ")
    return choice.strip()

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

