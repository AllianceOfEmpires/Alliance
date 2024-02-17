class Email:
    def __init__(self):
        self.emails = []
    def add_email(self, email):
        if email in self.emails:
            raise ValueError("This email address already exists.")
        self.emails.append(email)

    def edit_email(self, old_email, new_email):
        if old_email not in self.emails:
            raise ValueError("This email address was not found.")
        if new_email in self.emails:
            raise ValueError("The new email address already exists.")
        index = self.emails.index(old_email)
        self.emails[index] = new_email

    def remove_email(self, email):
        if email not in self.emails:
            raise ValueError("This email address was not found")
        self.emails.remove(email)
    


