# def first_func():
#     print("hello")
#
# first_func()
#
# def second_func(username):
#     print(username)
#
# second_func('evgenii')
#
# def display_message():
#     print("Into the function we pass parameter, when call function pass argument ")
#
# display_message()
#
# def favorite_book(title):
#     print(f'One of my favorite books is {title}')
#
#
# favorite_book('Alice in Wonderland')
#
#
# def few_param_func(par_1, par_2):
#     print(par_1, par_2.upper())
#
# few_param_func('Hello', 'I am Evgenii')
#
#
# def home_pets(type_animal, name_pet):
#     print(f"I have a {type_animal} its name is {name_pet}")
#
# home_pets(type_animal='kat', name_pet='Tina')
#
#
# def home_animals(name_pet, type_animal='kat'):
#     print(f"I have a {type_animal} its name is {name_pet}")
#
# home_animals(name_pet='Tina')

# def make_shirt(size, text):
#     size = input("Please enter size: ")
#     text = input("Please enter text: ")
#     print(f"You are ordered shirt size {size} and it will be has text {text.upper()}")
#
# make_shirt(size ='', text = '')

# def make_great_shirt(text, size = 'XL'):
#     # text = input('Please enter yor text: ')
#     print(f'You ordered shirt size {size} with text {text.upper()}')
#
# text = input("Hello my darling: ")
# make_great_shirt(text=text)


def check_city(country, city, list_of_country):
    if country in list_of_country.keys() and city in list_of_country.values():
        for k,v in list_of_country.items():
            if k == country and v == city:
                print(f"{city} is in country {country}")
                break
            elif v != city and k == country :
                print(f"{city} is not in country {country}, in {country} is city {v}")
                break
            # elif k != country and v == city:
            #     print(f"{city} is not in country {country}")
            #     break
    elif city not in list_of_country.values():
            print(f"we could not find this city {city}  in our system")
    elif country not in list_of_country.values():
            print(f"we could not find this country {country}  in our systemm")
    else:
        print(f"{city} and {country} were not found in our system ")








list_of_country = {'usa': 'new york', 'canada': 'toronto', 'uk': 'london', 'russia': 'moscow'}
city = input('Enter name city:')
country = input('enter name country: ')
check_city(country=country, city = city, list_of_country = list_of_country)




































