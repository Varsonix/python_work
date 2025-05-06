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

class Privileges():
    """ Permissions Class """

    def __init__(self, privileges):
        """ Initialize Class """
        self.privileges = privileges

    def show_privileges(self):
        print('Available Privileges: ')
        for privilege in self.privileges:
            print(f' - {privilege}')


class Admin(User):
    """ Child Class for Admin """

    def __init__(self, first_name, last_name):
        """
        Initialize from parent class.
        Initialize privileges attribute.
        """
        super().__init__(first_name, last_name)
        self.privileges = Privileges(['can delete post', 'can add post',
                                      'can ban user', 'can add user'])


my_admin = Admin('Jordan', 'Gibbard')
my_admin.describe_user()
my_admin.privileges.show_privileges()