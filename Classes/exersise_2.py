class Restaurant():
    def __init__(self, name_restaurant, type_kitchen):
        self.name_restaurant = name_restaurant
        self.type_kitchen = type_kitchen
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant calls {self.name_restaurant} there is {self.type_kitchen}'s kitchen")

    def open_restaurant(self):
        print(f"Restaurant {self.name_restaurant} is open ")

    def served(self):
        print(f"{self.number_served}")

    def set_number_served(self, set_number):
        self.number_served = set_number

    def increment_served(self, inc_service):
        self.number_served += inc_service


restaurant = 'Sicilian'
kitchen = 'Italian'
describe = Restaurant(restaurant, kitchen)
describe.number_served = 10
describe.describe_restaurant()
describe.open_restaurant()
describe.served()
describe.set_number_served(30)
describe.served()
describe.increment_served(25)
describe.served()
