magicians = ['alice', 'david', 'carolina']
print(magicians)

for magician in magicians:
    print(magician)

print('-----')

for magician in magicians:
    print(f"That was a great trick, {magician.title()}!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thanks everyone! That was a great show!\n\n")


pizzas = ['cheese', 'more cheese', 'the most cheese']

for pizza in pizzas:
    print(f"I love {pizza.title()}.")

print("\nI like pizza.\n\n")

animals = ['dog', 'cat', 'hippo']
for animal in animals:
    if (animal == 'hippo'):
        print(f"A {animal.title()} would NOT make a great pet.")
    else:
        print(f"A {animal.title()} would make a great pet.")
print("What these animals have in common is that they have 4 legs.")
print("\n---\n")

# Learning about Range()
for value in range(1, 5):
    print(value)

print('\n')

number_list = list(range(1, 6))
print(number_list)

even_numbers = list(range(2, 11, 2))
odd_numbers = list(range(1, 10, 2))
print(f"Even:{even_numbers}\nOdd:{odd_numbers}")

print('\n')

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# Working with built in functions like min/max
digits = list(range(0, 10))
print(f"{min(digits)}\n{max(digits)}\n{sum(digits)}")

# Advanced Topic Short Look: List Comprehension
square_list = [value ** 2 for value in range(1, 11)]
print(square_list)

# Exercises
for value in range(1, 21):
    print(value)

"""
for value in range(1, 1000000):
    print(value)
"""

# See how quickly Python can sum a million digits together
million_digits = list(range(1,1000001))
print(f"Minimum:{min(million_digits)}\nMaximum:{max(million_digits)}")
print(sum(million_digits))

oddNumbers = list(range(1,20,2))
for number in oddNumbers:
    print(number)

multiples_three = list(range(3,30,3))
for multiple in multiples_three:
    print(multiple)

cube_list = list(range(1, 11))
cube_list_cubed = []
for value in cube_list:
    value_cubed = value ** 3
    cube_list_cubed.append(value_cubed)

for value in cube_list_cubed:
    print(value)

# More comprehension practice
cube_list_comprehended = [value ** 3 for value in range(1,11)]
print(cube_list_comprehended)