famous_persons = ['john Fruschianto', 'Billy Idol', 'Antony Kidis', 'Elton John']
for i in famous_persons:
    print(f"{'Hello'} {i} {'I wont to invite you on our event'}")

print(f"{famous_persons[1]} {' can not come to event'}")
del famous_persons[1]
famous_persons.insert(1, 'chad smith')
famous_persons.insert(0, 'feel colins')
famous_persons.insert(2, 'Flea')
famous_persons.append('Billy Joel')

for i in famous_persons:
    print(f"\n{'Hello'} {i.title()} {'I wont to invite you on our event'}")

while len(famous_persons) > 2:
    print(f"{famous_persons[-1]} {'We are so sorry but our event can not get much more gest'}")
    famous_persons.pop()

for i in famous_persons:
    print(f"\n{i.title()} {'You are still invited on our event'}")

while len(famous_persons) > 0:
    famous_persons.pop()

print(famous_persons)
print(len(famous_persons))

