from classes import Field

class Email(Field):
    def __init__(self):
        super().__init__([])

    def add_email(self, email):
        if email in self.value:
            raise ValueError("This email address already exists.")
        self.value.append(email)

    def edit_email(self, old_email, new_email):
        if old_email not in self.value:
            raise ValueError("This email address was not found.")
        if new_email in self.value:
            raise ValueError("The new email address already exists.")
        index = self.value.index(old_email)
        self.value[index] = new_email

    def remove_email(self, email):
        if email not in self.value:
            raise ValueError("This email address was not found")
        self.value.remove(email)

