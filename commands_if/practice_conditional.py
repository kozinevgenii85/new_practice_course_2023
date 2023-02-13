guitar = 'fender'
print("guitar == fender. I forcast True")
print(guitar == 'fender')

print("guitar == gibson. I forcast False")
print(guitar == 'gibson')

guitars = ['fender', 'gibson','gretch', 'epiphane']

if 'fendr' in guitars:
    print(f"{'It is good guitar'} {guitars[0].upper()}")
else:
    print('i like all guitars')

if 'fener' in guitars and 'gretch' in guitars:
    print('It is True')
else:
    print('It is False')

if 'squier' not in guitars:
    guitars.append('squier')
    print(guitars[-1].title())
else:
    for guitar in guitars:
        print(guitar.title())