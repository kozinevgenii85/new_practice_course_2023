class Car():
    def __init__(self, manufactured, model, year):
        self.manufactured = manufactured
        self.model = model
        self.year = year
        self.odometer = 0

    def describe_car(self):
        full_name = f" {self.manufactured} {self.model} {self.year}"
        return full_name

    def read_odometer(self):
        odo = self.odometer
        return odo

    def update_odometer(self, kilometers):
        self.odometer += kilometers


made_car = "Toyota"
model_car = "Avensis"
year_car = 2007
my_car = Car(made_car, model_car, year_car)
my_car.odometer = 185000
print(my_car.describe_car())
print(my_car.read_odometer())
my_car.update_odometer(333)
print(my_car.read_odometer())
