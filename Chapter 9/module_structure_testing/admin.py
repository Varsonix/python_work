"""
Module for Admin Class
"""
from user import User
from privileges import Privileges

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