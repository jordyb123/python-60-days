from logic import add_student, add_grade, calculate_average, is_valid_grade, student_exists, load_students
from ui import show_menu, add_student_ui, add_grade_ui, view_students, view_grades_ui, calc_avg_ui, show_message

def main():
    students = load_students()
    while True:
        choice = show_menu()
        if choice == "1":
            name = add_student_ui()
            add_student(students, name)
            show_message("Student Added.")
        elif choice == "2":
            index, grade = add_grade_ui(students)
            add_grade(students,index, grade)
        elif choice == "3":
            view_students(students)
        elif choice == "4":
            view_grades_ui(students)
        elif choice == "5":
            grades = calc_avg_ui(students)
            avg = calculate_average(grades)
            show_message(f"Average: {avg:.2f}")
        elif choice == "6":
            show_message("Goodbye!")
            break
        else:
            show_message("Invalid choice. Please try again.")

main()




