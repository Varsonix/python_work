""" Module for representing a User Class """

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