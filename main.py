from services.school_system import school_system
from models.student import student
from models.course import Course    

def display_menu():
    print("\nStudent Course Registration System")
    print("1. Add Student")
    print("2. view student")
    print("3. search student")
    print("4. Add Course")
    print("5. View Courses")
    print("6. Register Student to Course")
    print("7. View students in a Course")
    print("8. View Courses for a Student")
    print("9. Save Data")
    print("10. Load Data")
    print("0. Exit")

def main():
    system = school_system()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            email = input("Enter student email: ")
            phone_number = input("Enter student phone number: ")
            new_student = student(student_id, name, email, phone_number)
            system.add_student(new_student)
            print("Student added successfully.")
        elif choice == '2':
            student_id = input("Enter student ID to view: ")
            system.view_student(student_id)
        elif choice == '3':
            search_query = input("Enter name or email to search for a student: ")
            system.search_student(search_query)
        elif choice == '4':
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            trainer_name = input("Enter trainer name: ")
            capacity = int(input("Enter course capacity: "))
            new_course = Course(course_id, course_name, trainer_name, capacity)
            system.add_course(new_course)
            print("Course added successfully.")
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
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")