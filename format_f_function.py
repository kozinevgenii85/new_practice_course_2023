# first_name = 'alona'
# last_name = ' kozin'
# full_name = format(first_name + ' ' + last_name.lstrip())
# print(full_name.title())
# my_name = format('evgenii' + " " + 'kozin')
# print(my_name)
# daughter_name = f"{'maria'} \n{'kozin'}"
# print(daughter_name.title())
# print("Maria Kozin,\tis My daughter")
# print(full_name.rstrip())

enter = str(input("Hello, what's your name?"))
answer = str(input(f"{'It is cool'} {enter} {',nice to met you. What is last name?'} "))
print(f"{'Hello'} {enter.title()} {answer.title()}")
print(f"{'Hello'} {enter.upper()} {answer.lower()}")
print(f"{'Hello'} \t{enter.upper()} \n{answer.lower()}")


