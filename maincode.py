
def main():
    students = []
    while True:
        print("1. Add student")
        print("2. Display students")
        print("3. Quit")
        option = int(input("Choose an option: "))
        if option == 1:
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grade = float(input("Enter student grade: "))
            add_student(students, name, age, grade)
        elif option == 2:
            display_students(students)
        elif option == 3:
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
