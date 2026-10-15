import menu
import data

def main():
    print("Welcome to the Student Management System!")
    data.import_students()
    menu.show_menu()


if __name__ == "__main__":
    main()