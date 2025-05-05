def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)

usernames = ['hannah', 'jordan', 'fry', 'margot', 'ty']
greet_users(usernames)