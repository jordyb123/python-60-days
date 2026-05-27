from logic import generate_name, generate_multiple_names, add_name
from ui import show_menu, generate_name_ui, how_many_names, generate_multiple_names_ui, add_name_ui, show_message

def main():
    first_names = ['John', 'Bob', 'Steve', 'Bryan']
    last_names = ['Jobs', 'Touchy', 'Cheese', 'Maidenless']

    while True:
        choice = show_menu()
        if choice == 1:
            full_name = generate_name(first_names, last_names)
            generate_name_ui(full_name)

        elif choice == 2:
            count = how_many_names()
            names = generate_multiple_names(first_names, last_names, count)
            generate_multiple_names_ui(names)

        elif choice == 3:
            name = add_name_ui()
            add_name(first_names, name)
            show_message("First name added.")

        elif choice == 4:
            name = add_name_ui()
            add_name(last_names, name)
            show_message("Last name added.")
        
        elif choice == 5:
            show_message("Goodbye!!")
            break
        
        else:
            show_message("Invalid choice. Please try again")

main()
