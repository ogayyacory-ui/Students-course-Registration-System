import json
import os

from models.student import Student
from models.course import Course


class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.registrations = []

    def find_student(self, student_id):
        student_id = student_id.strip()
        return next((student for student in self.students if student.student_id == student_id), None)

    def find_course(self, course_id):
        course_id = course_id.strip()
        return next((course for course in self.courses if course.course_id == course_id), None)

    def student_registered(self, student_id, course_id):
        student_id = student_id.strip()
        course_id = course_id.strip()
        return any(
            reg for reg in self.registrations
            if reg["student_id"] == student_id and reg["course_id"] == course_id
        )

    def registration_count(self, course_id):
        course_id = course_id.strip()
        return sum(1 for reg in self.registrations if reg["course_id"] == course_id)

    def add_student(self, student):
        if not isinstance(student, Student):
            print("Invalid student object.")
            return False

        if not student.student_id:
            print("Student ID cannot be empty.")
            return False
        if not student.name:
            print("Student name cannot be empty.")
            return False
        if "@" not in student.email or not student.email:
            print("Student email must be valid and contain '@'.")
            return False
        if not student.phone_number:
            print("Student phone number cannot be empty.")
            return False
        if self.find_student(student.student_id):
            print("A student with this ID already exists.")
            return False

        self.students.append(student)
        print(f"Student {student.name} added successfully.")
        return True

    def add_course(self, course):
        if not isinstance(course, Course):
            print("Invalid course object.")
            return False

        if not course.course_id:
            print("Course ID cannot be empty.")
            return False
        if not course.course_name:
            print("Course name cannot be empty.")
            return False
        if not course.trainer_name:
            print("Trainer name cannot be empty.")
            return False
        if not isinstance(course.capacity, int) or course.capacity <= 0:
            print("Course capacity must be a number greater than 0.")
            return False
        if self.find_course(course.course_id):
            print("A course with this ID already exists.")
            return False

        self.courses.append(course)
        print(f"Course {course.course_name} added successfully.")
        return True

    def register_student_to_course(self, student_id, course_id):
        student = self.find_student(student_id)
        if not student:
            print("Student not found.")
            return False

        course = self.find_course(course_id)
        if not course:
            print("Course not found.")
            return False

        if self.student_registered(student.student_id, course.course_id):
            print(f"{student.name} is already registered for this course.")
            return False

        if self.registration_count(course.course_id) >= course.capacity:
            print("Registration failed. This course is already full.")
            return False

        self.registrations.append({"student_id": student.student_id, "course_id": course.course_id})
        print(f"{student.name} successfully registered for {course.course_name}.")
        return True

    def view_students(self):
        if not self.students:
            print("No students found.")
            return

        print("\nStudents:")
        for student in self.students:
            print(student.display())
            print("-" * 30)

    def view_courses(self):
        if not self.courses:
            print("No courses found.")
            return

        print("\nCourses:")
        for course in self.courses:
            print(course.display())
            print("-" * 30)

    def view_student(self, student_id):
        student = self.find_student(student_id)
        if not student:
            print("Student not found.")
            return

        print(student.display())

    def search_student(self, query):
        query = query.strip().lower()
        results = [
            student for student in self.students
            if query in student.student_id.lower()
            or query in student.name.lower()
            or query in student.email.lower()
        ]

        if not results:
            print("No student matches found.")
            return

        print(f"\nSearch results for '{query}':")
        for student in results:
            print(student.display())
            print("-" * 30)

    def view_students_in_course(self, course_id):
        course = self.find_course(course_id)
        if not course:
            print("Course not found.")
            return

        enrolled = [
            self.find_student(reg["student_id"])
            for reg in self.registrations
            if reg["course_id"] == course.course_id
        ]
        enrolled = [student for student in enrolled if student]

        if not enrolled:
            print(f"No students are registered in {course.course_name}.")
            return

        print(f"\nStudents registered in {course.course_name}:")
        for student in enrolled:
            print(student.display())
            print("-" * 30)

    def view_courses_for_student(self, student_id):
        student = self.find_student(student_id)
        if not student:
            print("Student not found.")
            return

        enrolled_courses = [
            self.find_course(reg["course_id"])
            for reg in self.registrations
            if reg["student_id"] == student.student_id
        ]
        enrolled_courses = [course for course in enrolled_courses if course]

        if not enrolled_courses:
            print(f"{student.name} is not registered in any courses.")
            return

        print(f"\nCourses registered by {student.name}:")
        for course in enrolled_courses:
            print(course.display())
            print("-" * 30)

    def save_data(self, filename):
        if not filename:
            print("Filename cannot be empty.")
            return False

        data = {
            "students": [
                {
                    "student_id": student.student_id,
                    "name": student.name,
                    "email": student.email,
                    "phone_number": student.phone_number,
                }
                for student in self.students
            ],
            "courses": [
                {
                    "course_id": course.course_id,
                    "course_name": course.course_name,
                    "trainer_name": course.trainer_name,
                    "capacity": course.capacity,
                }
                for course in self.courses
            ],
            "registrations": self.registrations,
        }

        try:
            os.makedirs(os.path.dirname(filename), exist_ok=True)
        except Exception:
            pass

        try:
            with open(filename, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
            print(f"Data saved successfully to {filename}.")
            return True
        except Exception as exc:
            print(f"Error saving data: {exc}")
            return False

    def load_data(self, filename):
        if not filename:
            print("Filename cannot be empty.")
            return False

        if not os.path.exists(filename):
            return False

        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)

            self.students = [
                Student(**student_data)
                for student_data in data.get("students", [])
            ]
            self.courses = [
                Course(**course_data)
                for course_data in data.get("courses", [])
            ]
            self.registrations = data.get("registrations", [])
            print(f"Data loaded successfully from {filename}.")
            return True
        except Exception as exc:
            print(f"Error loading data: {exc}")
            return False
