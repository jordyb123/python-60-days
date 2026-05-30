def main():
    while True:
        choice = menu()

        if choice == 1:
            km = float(input("Enter kilometers to convert: "))
            miles = km_to_miles(km)
            print(f"{km} kilometeres = {miles:.2f} miles")

        elif choice == 2:
            miles = float(input("Enter miles to convert: "))
            km = miles_to_km(miles)
            print(f"{miles} miles = {km:.2f} kilometeres")

        elif choice == 3:
            c = float(input("Enter celsius to convert: "))
            f = c_to_f(c)
            print(f"{c} celsius = {f:.2f} fahrenheit")

        elif choice == 4:
            f = float(input("Enter fahrenheit to convert: "))
            c = f_to_c(f)
            print(f"{f} fahrenheit = {c:.2f} celsius")

        elif choice == 5:
            print("Goodbye!!")
            break
        else:
            print("Enter a valid number.")


def menu():
    print("\nUNIT CONVERSION APP")
    print("Unit Conversion Menu")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. Exit")

    choice = int(input("Choose a number to navigate: "))
    return choice


def km_to_miles(km):
    miles = km * 0.621371
    return miles
    
def miles_to_km(miles):
    km = miles / 0.621371
    return km
    
def c_to_f(c):
    f = (c * 9/5) + 32
    return f
    
def f_to_c(f):
    c = (f - 32) * 5/9
    return c




main()