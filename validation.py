def validate_grade():
    while True:
        try:
            grade = int(input("Enter student grade = "))

            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")

        except ValueError:
            print("Grade must be a number! Try again.")