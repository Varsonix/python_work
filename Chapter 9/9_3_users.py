class User:
    """ Class for modelling a User """
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    
    def describe_user(self):
        print(
            f"\nFirst name: {self.first_name.title()}"
            f"\nLast Name: {self.last_name.title()}"
        )
    
    def greet_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"\nGreetings, {full_name.title()}!\n")
    
    def increment_login_attempts(self):
        """ Increment Login Attempts attribute. """
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """ Reset login attempts attribute. """
        self.login_attempts = 0

jordan = User('jordan', 'gibbard')
robert = User('robert', 'randalf')
michael = User('michael', 'douglas')

jordan.describe_user()
jordan.greet_user()

robert.describe_user()
robert.greet_user()

michael.describe_user()
michael.greet_user()

new_user = User('Bob', 'Dole')
new_user.describe_user()
print(f"Incrementing Login Attempts by 1")
new_user.increment_login_attempts()
print(f"Login attempts is now {new_user.login_attempts}. Now resetting...")
new_user.reset_login_attempts()
print(f"Login attempts is now {new_user.login_attempts}")