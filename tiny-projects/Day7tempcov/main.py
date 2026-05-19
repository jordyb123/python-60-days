
from logic import *
from ui import *

def main():
    print("Welcome to the Temperature Converter App!")
    while True:
        choice = main_menu()
        if choice == "1":
            celsius = get_number("Enter temperature in Celsius: ")
            result = celsius_to_fahrenheit(celsius)
            result_menu(result)

        elif choice == "2":
            fahrenheit = get_number("Enter temperature in Fahrenheit: ")
            result = fahrenheit_to_celsius(fahrenheit)
            result_menu(result)

        elif choice == "3":
            celsius = get_number("Enter temperature in Celsius: ")
            result = celsius_to_kelvin(celsius)
            result_menu(result)

        elif choice == "4":
            kelvin = get_number("Enter temperature in Kelvin: ")
            result = kelvin_to_celsius(kelvin)
            result_menu(result)
        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")


main()