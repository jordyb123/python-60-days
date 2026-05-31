import os
from logger import log_message

EXPENSES = "expenses.txt"



def main():
    expenses = load_expenses()
    log_message("Program started")

    while True:
        print("\nExpense Tracker")
        print("1. Add expense")
        print("2. View expenses")
        print("3. View total spent")
        print("4. View spending by category")
        print("5. Delete expense")
        print("6. Save expenses")
        print("7. Exit")

        choice = input("Choose and option: ")
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_total_spent(expenses)
        elif choice == "4":
            view_spending_by_category(expenses)
        elif choice == "5":
            delete_expense(expenses)
        elif choice == "6":
            save_expenses(expenses)
            print("Expenses saved!")
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Try again")

def load_expenses():
    if not os.path.exists(EXPENSES):
        return []

    expenses = []
    with open(EXPENSES, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            id_str, amount_str, category, note = line.split("|")
            expenses.append((int(id_str), float(amount_str), category, note))

    return expenses

def save_expenses(expenses):
    with open(EXPENSES, "w") as f:
        for id, amount, category, note in expenses:
            f.write(f"{id}|{amount}|{category}|{note}\n")

def add_expense(expenses):
    while True:
        amount_str = input("Enter the amount ")
        
        try:
            amount = float(amount_str)
            if amount < 0:
                print("Amount cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid input. Try again.")

    category = input("Enter a category: ")
    note = input("Enter a note: ")
    if not expenses:
        expense_id = 1

    else:
        expense_id = max(e[0] for e in expenses) + 1
    expenses.append((expense_id, amount, category, note))
    save_expenses(expenses)
    log_message(f"Added expense {expense_id} | {amount} | {category}")
    print(f"Expense added: {expense_id}, {amount}, {category}, {note}")

def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return
    
    print("\n--- All Expenses ---")
    for expense_id, amount, category, note in expenses:
        print(f"ID: {expense_id} | Amount: {amount} | Category: {category} | Note: {note}")
    log_message("Viewed all expenses")

def view_total_spent(expenses):
    if not expenses:
        print("No expenses found.")
        return
    
    total = sum(amount for _, amount, _, _ in expenses)
    log_message("Calculated total spent")
    print(f"Total spent: {total}")

def view_spending_by_category(expenses):
    if not expenses:
        print("No expenses found.")
        return
    
    totals = {}

    for _, amount, category, _ in expenses:
        if category not in totals:
            totals[category] = 0
        totals[category] += amount

    print("\n--- Total by Category ---")
    for category, total in totals.items():
        print(f"{category}: {total}")

    log_message("Calculated totals by category")

def delete_expense(expenses):
    if not expenses:
        print("No expenses to delete.")
        return
    
    print("\n--- All Expenses ---")
    for expense_id, amount, category, note in expenses:
        print(f"ID: {expense_id} | Amount: {amount} | Category: {category} | Note: {note}")
    
    id_str = input("Enter the ID of the expense to delete: ")

    try:
        expense_id = int(id_str)
    except ValueError:
        print("Invalid ID.")
        return
    
    for expense in expenses:
        if expense[0] == expense_id:
            expenses.remove(expense)
            save_expenses(expenses)
            log_message(f"Deleted expense {expense_id}")
            print(f"Expense with ID {expense_id} deleted.")
            return
        
    print("Expense ID not found.")

main()



    
    






    






