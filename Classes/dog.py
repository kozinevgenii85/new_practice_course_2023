class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def dog_info(self):
        print(f'{self.name} {self.age}')

name_dog = input('Enter name dog: ')
age_dog = input('Enter age dog: ')
dog = Dog(name_dog, age_dog)
dog.dog_info()
name_dog = input('Enter name dog: ')
age_dog = input('Enter age dog: ')
your_dog = Dog(name_dog, age_dog)
your_dog.dog_info()



