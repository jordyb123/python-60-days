import os

def load_contacts():
    if not os.path.exists("contacts.txt"):
        return []
    
    contacts = []
    with open("contacts.txt", "r") as file:
        for line in file:
            name, phone, email = line.strip().split("|")
            contacts.append({"name": name, "phone": phone, "email": email})
    return contacts
    
def save_contacts(contacts):
    with open("contacts.txt", "w") as file:
        for contact in contacts:
            line = f"{contact['name']}|{contact['phone']}|{contact['email']}\n"
            file.write(line)

def add_contact(contacts, contact):
    contacts.append(contact)
    save_contacts(contacts)

def remove_contact(contacts, index):
    if 0 <= index < len(contacts):
        contacts.pop(index)
        save_contacts(contacts)
        return True
    return False

def search_contacts(contacts, query):
    query = query.lower()
    return [
        contact
        for contact in contacts
        if query in contact["name"].lower()
        or query in contact["phone"].lower()
        or query in contact["email"].lower()
    ]