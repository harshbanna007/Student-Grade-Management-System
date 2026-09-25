def add_student(student_grade, name, grade):
    if name in student_grade:
        print("Student already exists!")
    else:
        student_grade[name] = grade
        print("Student added successfully!")


def update_student(student_grade, name, grade):
    if name in student_grade:
        student_grade[name] = grade
        print("Student grade updated successfully!")
    else:
        print("Student not found!")


def delete_student(student_grade, name):
    if name in student_grade:
        del student_grade[name]
        print("Student deleted successfully!")
    else:
        print("Student not found!")


def display_all_students(student_grade):
    if not student_grade:
        print("No students found!")
    else:
        print("\nStudent Grades:")
        for name, grade in student_grade.items():
            print(name, ":", grade)


def search_student(student_grade, name):
    if name in student_grade:
        print("Student:", name)
        print("Grade:", student_grade[name])
    else:
        print("Student not found!")