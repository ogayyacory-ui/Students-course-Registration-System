class Course:
    # Represents a course in the registration system.
    def __init__(self, course_id, course_name, trainer_name, capacity):
        # Initialize a Course instance.
        # The constructor trims whitespace from all string inputs to ensure stored data is normalized across the application
        # Ensure IDs and names do not contain accidental surrounding spaces
        self.course_id = course_id.strip()
        self.course_name = course_name.strip()
        self.trainer_name = trainer_name.strip()
        # Capacity should be an integer representing the allowed student count
        self.capacity = capacity

    def display(self):
        #Return a human-readable multi-line description of the course.
        return (
            f"Course ID: {self.course_id}\n"
            f"Course Name: {self.course_name}\n"
            f"Trainer: {self.trainer_name}\n"
            f"Capacity: {self.capacity} students"
        )
