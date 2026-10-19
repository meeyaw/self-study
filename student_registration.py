# ***********************************************************************************************************
# Part 9: Student Registration System (Mini CRUD)
# Optional Assignment

# Banner portion
print("\n")
print(("-" * 79))
print("|" + (" " * 25) + "STUDENT REGISTRATION SYSTEM" + (" " * 25) + "|")
print(("-" * 79))

students = {}             # empty dictionary of students

while True:
    # Giving user system options
    print("Options: [1] Register  [2] View  [3] Update  [4] Delete  [5] Exit \n")
    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Exiting ...")                        
        break

    elif choice == 4:
        id_number = input("\nEnter student ID to delete: ")
        if id_number in students:
            del students[id_number]
            print("Student record deleted.\n")
        else:
            print("Student not found.\n")

    elif choice == 3:
        id_number = input("\nEnter student ID to update: ")
        if id_number in students:
            new_age = input("Enter student age: ")
            students[id_number] ["age"] = new_age
            print("Student age info updated.\n")
        else:
            print("Student not found.\n")

    elif choice == 2:
        id_number = input("\nEnter student ID to view: ")
        if id_number in students:
            print("Student Info")
            print(f"Name: {students[id_number]["name"]}")
            print(f"Age: {students[id_number]["age"]}")
            print("")
        else:
            print("Student not found.\n")

    elif choice == 1:                       
        id_number = input("\nEnter student ID: ")
        if id_number in students:
            print("Student ID already exists.")
        else:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            print("Student registered successfully.\n")

            students[id_number] = {
                "name": name,
                "age": age
            }
    
    else:
        print("Error. Invalid choice.\n")
        print("Select again here")
    
print(students)