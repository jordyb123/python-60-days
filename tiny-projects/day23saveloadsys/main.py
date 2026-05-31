import os

SETTINGS_FILE = "settings.txt"

DEFAULT_SETTINGS = {
        "theme": "light",
        "volume": "50",
        "username": "player",
        "difficulty": "medium",
        "autosave": "off"
}

def main():
    settings = load_settings()
    while True:
        print("\nLoad/Save Settings Menu")
        print("1. View settings")
        print("2. Change settings")
        print("3. Reset to defaults")
        print("4. Save settings")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            view_settings(settings)

        elif choice == "2":
            change_settings(settings)

        elif choice == "3":
            settings = DEFAULT_SETTINGS.copy()
            print("Settings reset to defaults.")

        elif choice == "4":
            save_settings(settings)
            print("Settings saved.")

        elif choice =="5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        return DEFAULT_SETTINGS.copy()
    
    settings = {}

    with open(SETTINGS_FILE, "r") as f:
        for line in f:
            if "=" in line:
                key, value = line.strip().split("=", 1)
                settings[key] = value

    for key, value in DEFAULT_SETTINGS.items():
        settings.setdefault(key, value)

    return settings

def save_settings(settings):
    with open(SETTINGS_FILE, "w") as f:
        for key, value in settings.items():
            f.write(f"{key}={value}\n")

def view_settings(settings):
    print("\n--- Current Settings ---")
    for key, value in settings.items():
        print(f"{key}: {value}")

def change_settings(settings):
    print("\nWhich settings do you want to change?")
    for key in settings:
        print(f"- {key}")

    key = input("Enter setting name: ")

    if key not in settings:
        print("Invalid settings.")
        return
    
    new_value = input(f"Enter new value for '{key}': ")
    settings[key] = new_value
    print(f"{key} updated.")

if __name__ == "__main__":
    main()
