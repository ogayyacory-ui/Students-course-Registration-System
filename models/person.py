class Person:
    def __init__(self, name, email, phone_number):
        self.name = name.strip()
        self.email = email.strip()
        self.phone_number = phone_number.strip()

    def display(self):
        return (
            f"Name: {self.name}\n"
            f"Email: {self.email}\n"
            f"Phone: {self.phone_number}"
        )
