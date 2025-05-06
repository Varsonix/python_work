from random import randint, choice


class Die:
    """ Represents a die that can be rolled. """
    def __init__(self, sides=6):
        """Initializes a die with a given number of sides (Default 6)."""
        self.sides = sides
        self.sides_secret = [1, 2, 3, 4, 5, 6]
    
    def roll_die(self):
        """ Returns a random roll between 1 and the number of sides. """
        print(f"You rolled: {randint(1, self.sides)}")

    def roll_die_special(self):
        """ Using another way to reach the same conclusion """
        print(f"You rolled: {choice(self.sides_secret)}")