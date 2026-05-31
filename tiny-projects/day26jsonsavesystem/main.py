import json
import os

def main():
    data = load_data()
    

    while True:
        print("\n1. Add")
        print("2. View")
        print("3. Search")
        print("4. Edit")
        print("5. Delete")
        print("6. Quit")

        choice = input("Choose: ")

        if choice == "1":
            add_entry(data)
        elif choice == "2":
            view_all(data)
        elif choice == "3":
            search_entries(data)
        elif choice == "4":
            edit_entry(data)
        elif choice == "5":
            delete_entry(data)
        elif choice == "6":
            break
        else:
            print("Invalid choice.")


def save_data(data, filename="data.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print("Data saved.")

def load_data(filename="data.json"):
    if not os.path.exists(filename):
        print("No file found. Returning empty list.")
        return []
    
    with open(filename, "r") as f:
        return json.load(f)
    
def add_entry(data):
    name = input("Enter name: ")
    score = float(input("Enter score: "))

    if not data:
        entry_id = 1
    else:
        entry_id = max(item["id"] for item in data) + 1

    new_item = {"id": entry_id, "name": name, "score": score}
    data.append(new_item)
    save_data(data)
    print("Entry added.")

def search_entries(data):
    query = input("Search name: ").lower()

    results = [item for item in data if query in item["name"].lower()]

    if not results:
        print("No matches found.")
        return
    
    for item in results:
        print(item)

def edit_entry(data):
    if not data:
        print("No entry")
        return
    for item in data:
        print(item)
    entry_id = int(input("Enter ID to edit: "))

    for item in data:
        if item["id"] == entry_id:
            new_name = input(f"New name ({item['name']}): ") or item["name"]
            new_score = input(f"New score ({item['score']}): ")

            if new_score == "":
                new_score = item["score"]
            else:
                new_score = float(new_score)
            
            item["name"] = new_name
            item["score"] = new_score

            save_data(data)
            print("Entry updated")
            return
    print("ID not found.")

def delete_entry(data):
    if not data:
        print("No entry")
        return
    for item in data:
        print(item)
    entry_id = int(input("Enter ID to delete: "))

    for item in data:
        if item["id"] == entry_id:
            data.remove(item)
            save_data(data)
            print("Entry deleted.")
            return
    print("ID not found.")

def view_all(data):
    if not data:
        print("No entry")
        return
    for item in data:
        print(item)

main()




