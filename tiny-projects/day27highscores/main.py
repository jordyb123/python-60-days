import json
import os

def main():
    scores = load_scores()

    while True:
        print("\n1. Add Score")
        print("2. View High Scores")
        print("3. Quit")

        choice = input("Choose: ")

        if choice == "1":
            add_score(scores)
        elif choice == "2":
            view_scores(scores)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")



def save_scores(scores, filename="scores.json"):
    with open(filename, "w") as f:
        json.dump(scores, f, indent=4)
    print("Data saved.")


def load_scores(filename="scores.json"):
    if not os.path.exists(filename):
        print("No file found. Creating an empty list")
        return []
    
    with open(filename, "r")as f:
        return json.load(f)
    
def add_score(scores):
    name = input("Enter your name: ")
    player_score = float(input("What was your score: "))

    if not scores:
        entry_id = 1
    else:
        entry_id = max(item["id"] for item in scores) + 1
    
    new_item = {"id": entry_id, "name": name, "score": player_score}
    scores.append(new_item)
    scores.sort(key=lambda item: item["score"], reverse=True)
    save_scores(scores)
    print("Score added.")

def view_scores(scores):
    if not scores:
        print("No high scores.")
        return
    
    for position, item in enumerate(scores, start=1):
        print(f"Position: {position} | Name: {item['name']} | Score: {item['score']}")    

main()