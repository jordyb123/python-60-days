from logic import search_contacts

def show_menu():
    print("\nContact Book Menu ")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Search contacts")
    print("4. Remove contact")
    print("5. Exit")
    return input("Choose an option: ")

def get_new_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    return {"name": name, "phone": phone, "email": email}

def view_contacts(contacts):
    print("Contacts: ")
    if not contacts:
        print("No contacts found.")
    else:
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def search_contacts_ui(contacts):
    query = input("Search for anything (name, phone, email): ")
    results = search_contacts(contacts, query)
    view_contacts(results)

def get_contact_index(contacts):
    for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    contact = input("Enter the contact number you wish to remove: ")
    return contact

def show_message(message):
    print(message)