def show_menu():
    print("\nTo-do list Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")
    choice = input("Choose an option: ")
    return choice

def get_new_task():
    task = input("Enter a task: ")
    return task
    

def view_tasks(tasks):
    print("Tasks:")
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def get_task_index():
    task = input("Enter the task number to remove: ")
    return task

def show_message(message):
    print(message)
    