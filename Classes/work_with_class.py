class Car():
    def __init__(self, manufactured, model, year):
        self.manufactured = manufactured
        self.model = model
        self.year = year
        self.odometer = 0

    def all_info_car(self):
        my_car = f"{self.manufactured} {self.model} {self.year}"
        return my_car.title()

    def read_odo(self):
        odo = f"This car has odometer {self.odometer} km"
        return odo

    def change_odo(self, kilometers):
        self.odometer = kilometers

    def increment_odo(self, kilometer):
        self.odometer += kilometer


made_car = 'ford'
model_car = 'granada'
year_car = 1981
# odo_car = input("Odo: ")
my_new_car = Car(made_car, model_car, year_car)
print(my_new_car.all_info_car().upper())
my_new_car.change_odo(185000)
print(my_new_car.read_odo())
my_new_car.increment_odo(333)
print(my_new_car.read_odo())