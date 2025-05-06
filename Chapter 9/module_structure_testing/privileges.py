"""Module for privileges class"""

class Privileges():
    """ Permissions Class """

    def __init__(self, privileges):
        """ Initialize Class """
        self.privileges = privileges

    def show_privileges(self):
        print('Available Privileges: ')
        for privilege in self.privileges:
            print(f' - {privilege}')