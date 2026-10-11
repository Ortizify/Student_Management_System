import menu
import actions

def main():
    print("Welcome to the Student Management System!")
    actions.import_students()
    menu.show_menu()


if __name__ == "__main__":
    main()