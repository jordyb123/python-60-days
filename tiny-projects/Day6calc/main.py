from calculator import *
from ui import *


def main():
    print("Calculator App")
    while True:
        choice = main_menu()
    
        if choice == "1":
            handle_math_menu()
        elif choice == "2":
            handle_percentage_menu()
        elif choice == "3":
            handle_bmi_menu()
        elif choice == "4":
            handle_unit_converter_menu()
        elif choice == "5":
            print("Exiting...")
            break   
        else:
            print("Invalid choice. Please try again.")

def handle_math_menu():
    while True:
        choice = math_menu()
        if choice == "1":
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            result = add(a, b)
            print(f"Result: {result}")
        elif choice == "2":
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            result = subtract(a, b)
            print(f"Result: {result}")
        elif choice == "3":
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            result = multiply(a, b) 
            print(f"Result: {result}")
        elif choice == "4":
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            result = divide(a, b)
            print(f"Result: {result}")
            if result is None:
                print("Error: Division by zero is not allowed.")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def handle_percentage_menu():
    while True:
        choice = percentage_menu()
        if choice == "1":
            x = get_number("Enter Percentage: ")
            y = get_number("Enter the number: ")
            result = percent_of(x, y)
            print("Result:", result)

        elif choice == "2":
            value = get_number("Enter the value: ")
            percent = get_number("Enter the percentage to increase by: ")
            result = increase_by_percent(value, percent)
            print("Result:", result)

        elif choice == "3":
            value = get_number("Enter the value: ")
            percent = get_number("Enter the percentage to decrease by: ")
            result = decrease_by_percent(value, percent)
            print("Result:", result)

        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def handle_bmi_menu():
    while True:
        choice = bmi_menu()
        if choice == "1":
            weight = get_number("Enter weight in kilograms: ")
            height = get_number("Enter height in meters: ")
            result = bmi(weight, height)
            print("Your BMI is:", result)
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")

def handle_unit_converter_menu():
    while True:
        choice = unit_converter_menu()
        if choice == "1":
            kg = get_number("Enter weight in kilograms: ")
            print("Weight in pounds:", kg_to_lb(kg))

        elif choice == "2":
            lb = get_number("Enter weight in pounds: ")
            print("Weight in kilograms:", lb_to_kg(lb))
        elif choice == "3":
            c = get_number("Enter temperature in Celsius: ")
            print("Temperature in Fahrenheit:", c_to_f(c))
        elif choice == "4":
            f = get_number("Enter temperature in Fahrenheit: ")
            print("Temperature in Celsius:", f_to_c(f))
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

main()