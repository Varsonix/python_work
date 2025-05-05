#NOTE: * creates a tuple, but ** creates a dictionary for kvpairs
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    return user_info # The rest will be handled in the arguments of the call

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
my_user_profile = build_profile('jordan', 'gibbard',
                                location='california',
                                field='quality assurance',
                                likes='programming')
print(user_profile)
print(my_user_profile)