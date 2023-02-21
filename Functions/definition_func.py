def first_func():
    print("hello")

first_func()

def second_func(username):
    print(username)

second_func('evgenii')

def display_message():
    print("Into the function we pass parameter, when call function pass argument ")

display_message()

def favorite_book(title):
    print(f'One of my favorite books is {title}')


favorite_book('Alice in Wonderland')


def few_param_func(par_1, par_2):
    print(par_1, par_2.upper())

few_param_func('Hello', 'I am Evgenii')


def home_pets(type_animal, name_pet):
    print(f"I have a {type_animal} its name is {name_pet}")

home_pets(type_animal='kat', name_pet='Tina')


def home_animals(name_pet, type_animal='kat'):
    print(f"I have a {type_animal} its name is {name_pet}")

home_animals(name_pet='Tina')