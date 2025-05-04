# First, do a test to figure out if I can understand multiples of 10
# Theory is, this list multiples_of_ten should be nothing but zeros
multiples_of_ten = [value % 10 for value in range(0, 111, 10)]
print(multiples_of_ten)
# Ok, so effectively, if value % 10 == 0, that's a multiple of 10. Got it.

user_input = int(input("Please enter a number: "))

# Just testing ternary operators here from the Python syntax. Not used
is_multiple = True if user_input % 10 == 0 else False

# if is_multiple:
#     print(f"\nCongratulations! {user_input} is a multiple of 10!")
# else:
#     print(f"\nSorry, {user_input} is not a multiple of 10. Try again!")




# Another silly way to do it. I'm not a huge fan of it, but was fun to golf.
print(f"\n{user_input} is {'' if user_input % 10 == 0 else "not "}a multiple "
      f"of 10!")