from logic import add_task, remove_task, load_tasks
from ui import show_menu, get_new_task, view_tasks, get_task_index, show_message

def main ():
    tasks = load_tasks()
    while True:
        choice = show_menu()
        if choice == "1":
            task = get_new_task()
            add_task(tasks, task)
            show_message("Task added.")
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            task = get_task_index()

            if task.isdigit():
                task = int(task) - 1
                if remove_task(tasks, task):
                    show_message("Task removed.")
                else:
                    show_message("Invalid task number.")
            else:
                show_message("Please enter a valid number.")
        elif choice == "4":
            show_message("Goodbye!")
            break
        else:
            show_message("Invalid choice. Please try again.")

main()