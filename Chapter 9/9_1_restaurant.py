class Restaurant:
    """Creating a class for a restaurant model."""

    def __init__(self, restaurant_name, cuisine_type):
        """ Initialize the name and type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(
            f"{self.restaurant_name} is a {self.cuisine_type} based "
            "restaurant operating out of San Marcos "
            f"and has served {self.number_served} customers."
        )

    
    def open_restaurant(self):
        print("The restaurant is now open!\n")
    
    def set_number_served(self, customers):
        """Update the number of customers served."""
        self.number_served = customers
    
    def increment_number_served(self, customers):
        """Increment customers"""
        self.number_served += customers

applebees = Restaurant('Applebees Bar and Grill', 'Bad Food')
applebees.describe_restaurant()
applebees.set_number_served(33)
applebees.describe_restaurant()
applebees.increment_number_served(7)
applebees.describe_restaurant()