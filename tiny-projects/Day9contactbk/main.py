from logic import add_contact, remove_contact, load_contacts
from ui import show_menu, get_new_contact, view_contacts, get_contact_index, show_message, search_contacts_ui

def main ():
    contacts = load_contacts()
    while True:
        choice = show_menu()
        if choice == "1":
            contact = get_new_contact()
            add_contact(contacts, contact)
            show_message("Contact added.")
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contacts_ui(contacts)
        elif choice == "4":
            contact = get_contact_index(contacts)
            if contact.isdigit():
                contact = int(contact) - 1
                if remove_contact(contacts, contact):
                    show_message("Contact removed.")
                else:
                    show_message("Invalid contact number.")
            else:
                show_message("Please enter a valid number.")
        elif choice == "5":
            show_message("Goodbye!")
            break   
        else:
            show_message("Invalid choice. Please try again.")

main()
