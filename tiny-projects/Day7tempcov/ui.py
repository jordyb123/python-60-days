

def main_menu():
    print("1.Celsius to Fahreheit")
    print("2.Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Exit")
    return input("Choose an option: ")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def result_menu(result):
    print(f"Result: {result}")
    input("Press Enter to continue...")