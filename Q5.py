class Customer:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

c1 = Customer("John Doe", 30, "john.doe@example.com")
c1.display_info()
