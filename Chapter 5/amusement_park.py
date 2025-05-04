import random

# Trying to get spicy (And using list comprehension) [Just learned about _]
age_list = [random.randint(1, 50) for _ in range(55)]

def amusement_park(input_ages):
    for age in input_ages:
        if age < 4:
            price = 0
        elif age < 18:
            price = 25
        elif age < 65:
            price = 40
        else:
            price = 20
        print(f"Your Age: {age}\nYour admission cost is ${price}")

amusement_park(age_list)