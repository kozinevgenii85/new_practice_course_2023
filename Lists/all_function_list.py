famous_persons = ['john Fruschianto', 'Billy Idol', 'Antony Kidis', 'Elton John']
famous_persons.extend(['gain ais', 'curt cobain'])
del famous_persons[-2]
print(sorted(famous_persons))
print(sorted(famous_persons, reverse=True))
new_list = famous_persons.copy()
print(new_list)
for i in new_list:
    famous_persons.append(i)

print(famous_persons)
famous_persons.count('curt cobain')
famous_persons.pop(-4)
famous_persons.sort()
print(famous_persons)
famous_persons.sort(reverse=True)
print(famous_persons)
print(len(famous_persons))

for i in famous_persons:
    print(i.title())
famous_persons.remove('Billy Idol')
print(len(famous_persons))

