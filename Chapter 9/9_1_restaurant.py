class Restaurant:
    """Creating a class for a restaurant model."""

    def __init__(self, restaurant_name, cuisine_type):
        """ Initialize the name and type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(
            f"{self.restaurant_name} is a {self.cuisine_type} based "
            "restaurant operating out of San Marcos."
        )

    
    def open_restaurant(self):
        print("The restaurant is now open!\n")

applebees = Restaurant("Applebee's Bar and Grill", "Neighborhood")
chilis = Restaurant("Chili's Bar and Grill", "Baby Back Ribs")
mcdonalds = Restaurant("McDonalds", "Fast Food")
print('\n')
applebees.describe_restaurant()
applebees.open_restaurant()

chilis.describe_restaurant()
chilis.open_restaurant()

mcdonalds.describe_restaurant()
mcdonalds.open_restaurant()