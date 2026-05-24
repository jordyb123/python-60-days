import os

def load_tasks():
    if not os.path.exists("tasks.txt"):
        return []
    
    with open("tasks.txt", "r") as file:
        return [line.strip() for line in file.readlines()]
    
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks, task):
    tasks.append(task)
    save_tasks(tasks)

def remove_task(tasks, task):
    if 0 <= task < len(tasks):
        tasks.pop(task)
        save_tasks(tasks)
        return True
    return False

