class Person:
    company = 'Worklyrow'
    country = 'Pakistan'
    a = 100

    def display_info(self):
        print("Name: Shahid")
        print("Roll No: 23")
        print("Phone No: 03474898122")
        print("Flutter Developer")
        # Here, I use self to access class variables outside the function
        print(self.company)
        print(self.country)

    def calculate_square(self):
        self.square = self.a * self.a
        print("Square:", self.square)


# Create an object for calling the class
person = Person()

# Display the person details using the object
person.display_info()

# Display the product
person.calculate_square()
