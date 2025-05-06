class User:
    """ Class for modelling a User """
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def describe_user(self):
        print(
            f"\nFirst name: {self.first_name.title()}"
            f"\nLast Name: {self.last_name.title()}"
        )
    
    def greet_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"\nGreetings, {full_name.title()}!\n")

jordan = User('jordan', 'gibbard')
robert = User('robert', 'randalf')
michael = User('michael', 'douglas')

jordan.describe_user()
jordan.greet_user()

robert.describe_user()
robert.greet_user()

michael.describe_user()
michael.greet_user()