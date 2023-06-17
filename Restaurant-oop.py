class Restaurant:

    """A class to signify if a restaurant of a specific cuisine type is open or closed"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant's attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

        # Added the following attribute to indicate the default number of customers served

        self.number_served = 0

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

        # Added the following method to set the number of customers served in each object/instance

    def set_number_served(self):
        """Set number of customers that have been served"""
        print("This restaurant has served " + str(self.number_served) + " customers.")

    def increment_number_served(self):
        """Increment number of customers that were served in a day of business"""
        self.number_served += 5



# Create an instance of the Restaurant class

restaurant = Restaurant('La internacional', 'International')

print("This restaurant's name is " + restaurant.restaurant_name + ".")
print("This restaurant serves " + str(restaurant.cuisine_type) + ' food')
restaurant.open_restaurant()
restaurant.set_number_served()
restaurant.increment_number_served()
restaurant.set_number_served()


print()


restaurant2 = Restaurant("Rup's Kitchen", 'Indian')

print("This other restaurant is called " + restaurant2.restaurant_name + ".")
print("They serve " + str(restaurant2.cuisine_type) + " food. ")
restaurant2.set_number_served()
restaurant2.close_restaurant()


print()

# The following restaurants will only call the describe_restaurant method
# to fill out their specific attributes


restaurant3 = Restaurant('Asado Argento', 'Argentina!')
restaurant3.describe_restaurant()
restaurant3.set_number_served()
restaurant3.increment_number_served()
restaurant3.set_number_served()
restaurant3.increment_number_served()
restaurant3.set_number_served()
restaurant3.set_number_served()
restaurant3.increment_number_served()
restaurant3.set_number_served()
restaurant3.close_restaurant()



print()

restaurant4 = Restaurant('Ye olde Americana', 'American')
restaurant4.describe_restaurant()
restaurant4.open_restaurant()
restaurant4.set_number_served()
restaurant4.increment_number_served()
restaurant4.set_number_served()
restaurant4.close_restaurant()

print()

restaurant5 = Restaurant('The Great Wall', 'Chinese')
restaurant5.describe_restaurant()
restaurant5.open_restaurant()
restaurant5.set_number_served()
restaurant5.increment_number_served()
restaurant5.set_number_served()
restaurant5.increment_number_served()
restaurant5.set_number_served()

print()


# Added the following class defining users by attribute
# and added a personalized greeting for each

class User:
    """ This class will define users by attributes in their profile
    and create a personalized greeting for each"""

# DOB = Date of Birth

    def __init__(self, user_id, first_name, last_name, dob):
        """Initialize general user attributes"""
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        # Added the following attribute and methods later

        self.login_attempts = 0

    def increment_login_attempts(self):
        """Increment the value of login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset value of login attempts to 0"""
        self.reset_login_attempts = 0


    def describe_user(self):
        """This method prints a summary of users's information"""
        print('User id is ' + self.user_id + ".")
        print('This user\'s first name is ' + self.first_name + ".")
        print('This user\'s last name is ' + self.last_name + ".")
        print('This user\'s date of birth is ' + self.dob + ".")

    def greet_user(self):
        """This method will print a personalized greeting to the user"""
        print('Welcome Mr/Mrs ' + self.first_name + ' ' + self.last_name + '!' ' please check our list of restaurants. ')




user1 = User('101100', 'Bruce', 'Wayne', '08-25-1988')
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
print('This user has ' + str(user1.login_attempts) + ' login attempts.')
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print('This user has ' + str(user1.login_attempts) + ' login attempts.')
user1.reset_login_attempts()
print('Current login attempts ' + str(user1.reset_login_attempts) )


print()


user2 = User('101200', 'Commander', 'Shepard', '03-25-2140')
user2.describe_user()
user2.greet_user()
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()
print('This user has ' + str(user2.login_attempts) + ' login attempts.')
user2.reset_login_attempts()
print('Current login attempts ' + str(user2.reset_login_attempts) )

print()

user3 = User('101300', 'Tony', 'Stark', '05-29-1970')
user3.describe_user()
user3.greet_user()
user3.increment_login_attempts()
user3.increment_login_attempts()
print('This user has ' + str(user3.login_attempts) + ' login attempts.')
user3.reset_login_attempts()
print('Current login attempts ' + str(user3.reset_login_attempts) )


print()


user4 = User('101400', 'Mark', 'Smith', '06-12-2000')
user4.describe_user()
user4.greet_user()
user4.increment_login_attempts()
user4.increment_login_attempts()
user4.increment_login_attempts()
user4.increment_login_attempts()
print('This user has ' + str(user4.login_attempts) + ' login attempts.')
user4.reset_login_attempts()
print('Current login attempts ' + str(user4.reset_login_attempts) )
