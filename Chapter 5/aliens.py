import random

possible_alien_colors = ['green', 'red', 'yellow', 'blue', 'orange']
# Goal: I'd like to generate an array by randomly 
# choosing one of the indexes from above, 50 times in a row to build out
# a healthy array to run through our function below
killed_aliens = [possible_alien_colors[random.randint(0,4)] for _ in range(50)]

def calculate_points(aliens_killed):
    points = 0
    for alien in aliens_killed:
        if alien == 'green':
            points += 5
            print(f"You got 5 points, bringing your total to: {points}")
        elif alien == 'red':
            points += 10
            print(f"You got 10 points, bringing your total to: {points}")
        elif alien == 'orange':
            points += 50
            print(f"You got 50 points, bringing your total to: {points}")
        else:
            points += 1
            print(f"You got 1 points, bringing your total to: {points}")
    print(f"Final Score: {points}\nThanks for playing!")

# Now let's pass in that array to our function we made
calculate_points(killed_aliens)