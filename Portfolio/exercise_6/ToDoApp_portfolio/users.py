class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"User: {self.name} ({self.email})"


class Owner(User):
    def __init__(self, name, email):
        super().__init__(name, email)

    def __str__(self):
        return f"Owner: {self.name} ({self.email})"
