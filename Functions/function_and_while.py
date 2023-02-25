def full_name_format(first, last):
    person = f'{first} {last}'
    return person.title()

while True:
    first_name = input('Please enter first name for continue or enter stop: ')
    if first_name == 'stop':
        break
    last_name = input('Please enter last name or command stop: ')
    if last_name == 'stop':
        break

    print_full_name = full_name_format(first_name, last_name)
    print(print_full_name)
    break