guitars = ['fender', 'gibson','gretch', 'epiphane']

if 'fnder' in guitars:
    print(f"{guitars[0].upper()} {'is great guitar'}")
elif 'gison' in guitars:
    print(f"{guitars[1].upper()} {'is great guitar'}")
elif 'getch' in guitars:
    print(f"{guitars[2].upper()} {'is great guitar'}")
else:
    print('Does not match')


color = input('Enter color: Green, Red, or Yellow: ').lower()

if color == 'green':
    print('You got 5 points')
if color == 'red':
    print('You got 10 points')
if color == 'yellow':
    print('You got 15 points')
else:
    print('Wrong enter')

