from models.person import Person

class Student(Person):
    """Represents a student in the registration system."""
    def __init__(self, student_id, name, email, phone_number):
        """Initialize a Student instance.
        The constructor trims whitespace from all string inputs to ensure   stored data is normalized across the application.
        """
        super().__init__(name, email, phone_number)
        self.student_id = student_id.strip()

    def display(self):
        """Return a readable multi-line summary of the student."""
        return (
            f"Student ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Email: {self.email}\n"
            f"Phone: {self.phone_number}"
        )
