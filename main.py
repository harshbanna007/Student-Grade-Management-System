from functions import add_student, update_student, delete_student, display_all_students, search_student


def validate_grade():
    while True:
        try:
            grade = int(input("Enter student grade = "))
            return grade
        except ValueError:
            print("Grade must be a number! Try again.")


student_grade = {}


def main():
    while True:
        print("\n=== Student Grade Management System ===")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Search Student")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice = "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice == 1:
            name = input("Enter student name = ").strip()
            grade = validate_grade()
            add_student(student_grade, name, grade)

        elif choice == 2:
            name = input("Enter student name = ").strip()
            grade = validate_grade()
            update_student(student_grade, name, grade)

        elif choice == 3:
            name = input("Enter student name = ").strip()
            delete_student(student_grade, name)

        elif choice == 4:
            display_all_students(student_grade)

        elif choice == 5:
            name = input("Enter student name = ").strip()
            search_student(student_grade, name)

        elif choice == 6:
            print("Closing the program....")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()