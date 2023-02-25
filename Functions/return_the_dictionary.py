first_name = input('first')
last_name = input('last')
middle_name = input('middle')

def return_dictionary(first,last):
    person = {'first name': first, 'last_name': last,}
    if middle_name:
        person["middle_name"] = middle_name
    return person

my_full_name = return_dictionary(first_name, last_name)
print(my_full_name)

