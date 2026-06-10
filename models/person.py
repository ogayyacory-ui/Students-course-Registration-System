
class Person:
    #Represents a person with basic contact information.

    def __init__(self, name, email, phone_number):
        ""#Initialize a Person instance.

        self.name = name.strip()
        self.email = email.strip()
        self.phone_number = phone_number.strip()

    def display(self):
        """Return a readable summary of the person's contact details."""
        return (
            f"Name: {self.name}\n"
            f"Email: {self.email}\n"
            f"Phone: {self.phone_number}"
        )
