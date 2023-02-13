bike = ['merida','track', 'redline', 'specialized']
print(bike)
print(bike[1])
print(bike[0].title())
message = f"My bike was {bike.pop()}"
print(message)
print(bike)
bike.append('specialized')
print(bike)
bike.extend(['sport', 'tundercat'])
print(bike)
bike.remove('sport')
print(bike)
bike.clear()
print(bike)
bike.extend(['merida','track', 'redline', 'specialized', 'sport', 'tundercat'])
print(bike)
print(bike.index('redline'))
bike.pop(3)
print(bike)
bike.extend(['merida','track', 'redline'])
print(bike)
print(bike.count('merida'))
bike.sort()
print(bike)
print(bike)
bike.reverse()
print(bike)
new_bike = bike.copy()
print(f"{'It is copied list'} {new_bike}")
#new_bike.pop()
new_list =[]

for i in new_bike:
    new_list.append(i)
    if new_list.count(i) > 1:
        new_list.remove(i)
    else:
        pass

print(new_list)

friends = ['antonio', 'evgenii', 'Alex', 'Sergio']
friends.insert(0, 'alona')
for i in friends:
    #print(i.title())
    print(f"{'Hello my friend'} {i.title()}")

del new_list[0]
print(new_list)

