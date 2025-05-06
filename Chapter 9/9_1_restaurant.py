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

class IceCreamStand(Restaurant):
    """ Creating child class for ice cream shop """

    def __init__(self, restaurant_name, cuisine_type):
        """ 
        Initialize off the parent class.
        Add a flavors list (Hard coded for now)
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Chocolate', 'Strawberry', 'Vanilla',
                        'Matcha', 'Peanut Butter', 'Peppermint',
                        'Cookie Dough', 'Sea Salt', 'Neopolitan']
    
    def list_flavors(self):
        """ Print out all the flavors at the ice cream shop. """
        print("Flavors available: ")
        for flavor in self.flavors:
            print(f"- {flavor}")

baskin_robbins = IceCreamStand('Baskin Robins 31 Flavors', 'Ice Cream')
baskin_robbins.describe_restaurant()
baskin_robbins.list_flavors()