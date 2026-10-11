import actions
def show_menu():
    print("===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add students")
    print("2. View all students")
    print("3. View top 3 students")
    print("4. View average grade")
    print("5. Export students to CSV")
    print("6. Import students from CSV")
    print("7. Exit")
    while True:
        choice = input("Select an option (1-7): ")

        if choice == "1":
            actions.add_student()
        
        elif choice == "2":
            actions.view_students()

        
        elif choice == "3":
            actions.view_top_students()

        
        elif choice == "4":
            actions.view_average_grade()


        elif choice == "5":
            actions.export_students()

        elif choice == "6":
            actions.import_students()
        
        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please select a number from 1 to 7.")
