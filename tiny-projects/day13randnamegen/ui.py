print("Name Generator")

def show_menu():
    print("1. Generate one name")
    print("2. Generate multiple names")
    print("3. Add first name")
    print("4. Add last name")
    print("5. Exit")
    choice = input("Choose an menu item. ")
    return int(choice)

def generate_name_ui(full_name):
    print(full_name)

def how_many_names():
    choice = input("how many names do you want to generate? ")
    if not choice.isdigit():
        print("Please enter a valid number.")
        return None
    return int(choice)

def generate_multiple_names_ui(names):
    for i, name in enumerate(names, start=1):
        print(i, name)
        
def add_name_ui():
    choice = input("Enter a new name: ")
    return choice

def show_message(message):
    print(message)