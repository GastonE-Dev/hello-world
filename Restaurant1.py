class Restaurant:

    """A class to signify if a restaurant of a specific cuisine type is open or closed"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant's attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describes the restaurant attributes"""
        print("Restaurant name:", self.restaurant_name)
        print("Cuisine type:", self.cuisine_type)



    def open_restaurant(self):
        """Simulate opening the restaurant"""
        print("The restaurant has just opened!")

    def close_restaurant(self):
        """Simulate the closing of the restaurant"""
        print("This restaurant has closed for today")


# Create an instance of the Restaurant class

restaurant = Restaurant('La internacional', 'International')

print()

print("This restaurant's name is " + restaurant.restaurant_name + ".")
print("This restaurant serves " + str(restaurant.cuisine_type) + ' food')
restaurant.open_restaurant()


print()


restaurant2 = Restaurant("Rup's Kitchen", 'Indian')


print()


print("This other restaurant is called " + restaurant2.restaurant_name + ".")
print("They serve " + str(restaurant2.cuisine_type) + " food. ")
restaurant.close_restaurant()

# This is the first version













