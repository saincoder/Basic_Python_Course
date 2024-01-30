class Person:
    # Class variables
    company = 'Worklyrow'
    country = 'Pakistan'
    a = 100

    def display_info(self):
        """
        Display general information about a person.
        """
        print("Name: Shahid")
        print("Roll No: 23")
        print("Phone No: 03474898122")
        print("Flutter Developer")
        # Accessing class variables using self
        print(f"Company: {self.company}")
        print(f"Country: {self.country}")

    def display_info_1(self, name, roll_no, phone_no, role):
        """
        Display detailed information about a person with custom details.
        :param name: Name of the person
        :param roll_no: Roll number
        :param phone_no: Phone number
        :param role: Person's role
        """
        print(f"Name: {name}")
        print(f"Roll No: {roll_no}")
        print(f"Phone No: {phone_no}")
        print(f"Role: {role}")
        # Accessing class variables using self
        print(f"Company: {self.company}")
        print(f"Country: {self.country}")

    def calculate_square(self):
        """
        Calculate and display the square of class variable 'a'.
        """
        self.square = self.a * self.a
        print("Square:", self.square)


# Create an object for calling the class
person = Person()

# Display general person details using the object
person.display_info()

# Display detailed person info using the object through constructor
person.display_info_1('Worklyrow', '23', '03333333333', 'developer')

# Calculate and display the square of 'a'
person.calculate_square()
