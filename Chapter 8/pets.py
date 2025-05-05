def describe_pet(pet_name, animal_type='dog'):
    """
    Example of positional arguments
    """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

def describe_pet_keyword(animal_type, pet_name):
    """
    Example of keyword arguments
    """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('hamster', 'billy')
describe_pet('Ralph')
describe_pet_keyword(animal_type='dog', pet_name='ruff')
describe_pet_keyword(pet_name='jerry', animal_type='cat')