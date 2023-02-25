# val = 100
# var = val + 25
#
# def sum_return(val, var):
#     sum = val%var
#     return sum
#
# sum_print = sum_return(val, var)
# print(sum_print)
#
#
# first_name = 'Evgenii'
# last_name = 'kozin'
#
# def full_name(first, last):
#     full_name = f"{first} {last}"
#     return full_name.title()
#
# full_name_for_print = full_name(first_name, last=last_name)
# print(full_name_for_print)

first_name = input()
last_name = input()
middle_name = input()

def format_name(first, last, middle = ''):
    full_name = f'{first} {last} {middle}'
    return full_name.title()

p_full_name = format_name(first_name, last_name, middle_name)
print(p_full_name)