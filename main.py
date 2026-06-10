"""Entry point for the Student Course Registration System."""

from services.school_system import SchoolSystem
from models.student import Student
from models.course import Course


def display_menu():
    # Displays the main menu options to the user.
    print(" Student Course Registration System ")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Add Course")
    print("5. View Courses")
    print("6. Register Student to Course")
    print("7. View Students in a Course")
    print("8. View Courses for a Student")
    print("9. Save Data")
    print("10. Load Data")
    print("0. Exit")


def main():
    """Run the interactive registration system loop."""
    system = SchoolSystem()
    default_file = "data/data.json"
    system.load_data(default_file)

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            email = input("Enter student email: ")
            phone_number = input("Enter student phone number: ")
            new_student = Student(student_id, name, email, phone_number)
            system.add_student(new_student)
        elif choice == '2':
            system.view_students()
        elif choice == '3':
            search_query = input("Enter student ID, name, or email to search: ")
            system.search_student(search_query)
        elif choice == '4':
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            trainer_name = input("Enter trainer name: ")
            capacity_text = input("Enter course capacity: ")
            if not capacity_text.isdigit():
                print("Capacity must be a positive number.")
                continue
            capacity = int(capacity_text)
            new_course = Course(course_id, course_name, trainer_name, capacity)
            system.add_course(new_course)
        elif choice == '5':
            system.view_courses()
        elif choice == '6':
            student_id = input("Enter student ID to register: ")
            course_id = input("Enter course ID to register for: ")
            system.register_student_to_course(student_id, course_id)
        elif choice == '7':
            course_id = input("Enter course ID to view students: ")
            system.view_students_in_course(course_id)
        elif choice == '8':
            student_id = input("Enter student ID to view courses: ")
            system.view_courses_for_student(student_id)
        elif choice == '9':
            filename = input("Enter filename to save data (e.g., data.json): ")
            system.save_data(filename)
        elif choice == '10':
            filename = input("Enter filename to load data (e.g., data.json): ")
            system.load_data(filename)
        elif choice == '0':
            save_choice = input("Save before exit? (y/n): ").strip().lower()
            if save_choice == 'y':
                system.save_data(default_file)
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
