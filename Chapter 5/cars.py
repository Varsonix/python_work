# Working with Cars
cars = ['audio', 'bmw', 'subaru', 'toyota']

# For Loops
for car in cars:
    if (car.lower() == 'bmw'):
        print(car.upper())
    else:
        print(car.title())

my_age = 35

if my_age > 30 and my_age < 40:
    print("Hooray!")


if 'bmw' in cars:
    print(f"We found the {cars[1].upper()}")


banned_users = ['jordan', 'ralph']
login_user = 'radlph'

if login_user not in banned_users:
    print("Welcome aboard, Mr. President")
else:
    print("You're banned")

game_active = True
can_edit = False

if game_active and can_edit:
    print("You can edit the active game")
else:
    print("You cannot edit the active game")


car = 'subaru'

print("Is car == 'subaru'? I predict True")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')