from functions import add_student, update_student, delete_student


students = {}

print("Testing Add Student:")
add_student(students, "Rahul", 85)
print(students)

print("\nTesting Update Student:")
update_student(students, "Rahul", 90)
print(students)

print("\nTesting Delete Student:")
delete_student(students, "Rahul")
print(students)