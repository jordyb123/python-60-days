import os

def load_students():
    if not os.path.exists("students.txt"):
        return []
    
    students = []
    with open("students.txt", "r") as file:
        for line in file:
            name, grades_str = line.strip().split("|")
            grades = [int(g) for g in grades_str.split(",")] if grades_str else []
            students.append({"name": name, "grades": grades})
    return students

def save_students(students):
    with open("students.txt", "w") as file:
        for s in students:
            grades_str = ",".join(str(g) for g in s["grades"])
            file.write(f"{s['name']}|{grades_str}\n")

def add_student(students, name):
    students.append({"name": name, "grades": []})
    save_students(students)

def add_grade(students, index, grade):
    students[index]["grades"].append(grade)
    save_students(students)

def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)

def is_valid_grade(value):
    return value.isdigit() and 0 <= int(value) <= 100

def student_exists(students, name):
    return any(s["name"].lower() == name.lower() for s in students)