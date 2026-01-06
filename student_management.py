# Student Management System
# Created by: Vaishnavi Khaire
# Beginner project – Add, Display, Exit

students = []  # list to store student data

while True:
    print("\n---- Student Management System ----")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    # ADD STUDENT
    if choice == "1":
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")

        student = [roll, name, marks]
        students.append(student)

        print("Student added successfully.")

    # DISPLAY STUDENTS
    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            print("\nRoll | Name | Marks")
            print("-------------------")
            for s in students:
                print(s[0], "|", s[1], "|", s[2])

    # EXIT
    elif choice == "3":
        print("Exiting Student Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
