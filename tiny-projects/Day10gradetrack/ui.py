def show_menu():
    print("1. Add a student")
    print("2. Add grades for a student")
    print("3. View all students")
    print("4. View a student's grades")
    print("5. Calculate student average")
    print("6. Exit")
    return input("Choose an option: ")

def add_student_ui(students):
    student = input("Enter student name: ")
    return student

def add_grade_ui(students):
    print("\nStudents:")
    for i, s in enumerate(students, start=1):
        print(f"{i}. {s['name']}")

    choice = input("Enter student number: ")
    if not choice.isdigit():
        print("Invalid number.")
        return None, None
    index = int(choice) - 1
    if index < 0 or index >= len(students):
        print("Invalid student number.")
        return None, None
    
    grade = input("Enter grade (0-100): ")
    grade = int(grade)
    return index, grade

def view_students(students):
    print("Students: ")
    if not students:
        print("No students found.")
    else:
        for i, student in enumerate(students, start=1):
            print(f"{i}. Name: {student['name']}")
            
def view_grades_ui(students):
    print("\nStudents: ")
    for i, student in enumerate(students, start=1):
        print(f"{i}. {student['name']}")

    choice = input("Which student number: ")

    if not choice.isdigit():
        print("Please enter a valid number: ")
        return
    
    index = int(choice) - 1

    if index < 0 or index >= len(students):
        print("Invalid student number.")
        return
    
    grades = students[index]["grades"]

    if not grades:
        print(f"{students[index]['name']} has no grades yet.")
    else:
        print(f"Grades for {students[index]['name']}")
        for g in grades:
            print(f"- {g}")

def calc_avg_ui(students):
    print("\nStudents:")
    for i, s in enumerate(students, start=1):
        print(f"{i}. {s['name']}")
    choice = input("Enter a student number: ")

    if not choice.isdigit():
        print("Invalid number.")
        return []
    
    index = int(choice) - 1

    if index < 0 or index >= len(students):
        print("invalid student number")
        return []
    
    return students[index]["grades"]

def show_message(message):
    print(message)
    




