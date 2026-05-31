import os

NOTES_FILE = "notes.txt"

def main():
    while True:
        print("\n--- Notes App ---")
        print("1. Add note")
        print("2. List notes")
        print("3. Delete note")
        print("4. Search notes")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            list_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            search_notes()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            pass

def load_notes():
    ensure_file()
    notes = []
    with open(NOTES_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            note_id_str, text = line.split("|", 1)
            notes.append((int(note_id_str), text))
    return notes

def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        for note_id, text in notes:
            f.write(f"{note_id}|{text}\n")

def get_next_id(notes):
    if not notes:
        return 1
    return max(n[0] for n in notes) + 1

def add_note():
    notes = load_notes()
    text = input("Enter your note: ").strip()
    if not text:
        print("Note cannot be empty.")
        return
    note_id = get_next_id(notes)
    notes.append((note_id, text))
    save_notes(notes)
    print(f"Note added with ID {note_id}.")

def list_notes():
    notes = load_notes()
    if not notes:
        print("No notes yet.")
        return
    print("\n--- Your Notes ---")
    for note_id, text in notes:
        print(f"{note_id}. {text}")

def delete_note():
    notes = load_notes()
    if not notes:
        print("No notes to delete.")
        return
    
    list_notes()
    try:
        note_id = int(input("Enter ID of note to delete: "))
    except ValueError:
        print("invalid ID.")
        return
    
    new_notes = [n for n in notes if n[0] != note_id]

    if len(new_notes) == len(notes):
        print("No note with that ID.")
        return
    
    save_notes(new_notes)
    print(f"Note {note_id} deleted.")

def search_notes():
    notes = load_notes()
    if not notes:
        print("No notes to search.")
        return
    
    term = input("Enter search term: ").lower().strip()
    if not term:
        print("Search term cannot be empty.")
        return
    
    matches = [(i, t) for i, t in notes if term in t.lower()]

    if not matches:
        print("No matching notes found.")
        return
    
    print("\n--- Search Results---")
    for note_id, text in matches:
        print(f"{note_id}. {text}")


if __name__ == "__main__":
    main()