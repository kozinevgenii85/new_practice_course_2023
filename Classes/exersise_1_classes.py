class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant {self.restaurant_name} with {self.cuisine_type}'s kitchen")


    def open_restaurant(self):
        print(f'The restaurant {self.restaurant_name} is open')


restaurant = Restaurant('McDonalds', 'Fast food')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant = Restaurant('Sicilia', 'Italian')
restaurant.describe_restaurant()

restaurant = Restaurant('Oldmen and Sea', 'Sea foods')
restaurant.describe_restaurant()

### EXERSISE USERS ###

class User():
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe(self):
        print(f"{self.first_name} {self.last_name} age is {self.age} years old, city is {self.city}")

    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}')

your_first_name = input("What is your first name: ")
your_last_name = input("What is your last name: ")
your_age = input("How old are you: ")
your_city = input("Where are you from: ")
user = User(your_first_name, your_last_name, your_age, your_city)
user.describe()
user.greet_user()