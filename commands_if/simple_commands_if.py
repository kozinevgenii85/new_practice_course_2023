alien_color = 'green'
if alien_color == 'green':
    print(5)
else:
    print('You are did not win')

if alien_color == 'red':
    print(5)
else:
    print('You are did not win')

age = int(input('Enter your age: '))

if age <=2:
    print(f"{'Your age is'} {age} {'ticket is free'}")
elif age > 2 and age <= 13:
    print(f"{'Your age is'} {age} {'ticket costs 20 dollars'}")
elif age >= 14 and age <= 17:
    print(f"{'Your age is'} {age} {'ticket costs 25 dollars'}")
elif age >= 18 and age <= 74:
    print(f"{'Your age is'} {age} {'ticket costs 35 dollars'}")
else:
    print(f"{'Your age is'} {age} {'enter is free'}")
