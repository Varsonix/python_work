"""
File just for creating a user/admin
"""

from user import User
from admin import Admin

# NOTE: Testing if I need privileges or not beacuse admin is the one with them

my_user = User('Jordan', 'Gibbard')
my_user.describe_user()
my_user.greet_user()
my_user.increment_login_attempts()
print(f"Incrementing Login Attempts: {my_user.login_attempts}")
my_user.reset_login_attempts()
print(f"Resetting Login Attempts: {my_user.login_attempts}")

my_admin = Admin('Bob', 'Dole')
my_admin.describe_user()
my_admin.greet_user()
my_admin.privileges.show_privileges()
my_admin.increment_login_attempts()
print(f"Incremented Login Attempts: {my_admin.login_attempts}")
my_admin.reset_login_attempts()
print(f"Reset Login Attempts: {my_admin.login_attempts}")