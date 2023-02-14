music_tools = {'snare drum': 'tama', 'size': '14 x 5.5'}
print(music_tools['snare drum'])
print(music_tools['size'])
drums = [music_tools]
print(drums[0])
new_drum = music_tools['snare drum']
print(new_drum)
music_tools['cost']=1000
for i in music_tools:
    print(i)

print(music_tools)

my_drum_set = {}
my_drum_set['brand'] = 'tama'
my_drum_set['name'] = 'starclassic'
print(my_drum_set)

my_drum_set['name'] = 'superstar'
print(my_drum_set)

alien = {'x-position': 0, 'y-position': 25, 'speed': 'medium'}
print(f"Original position: {alien['x-position']}")
if alien['speed'] == 'slow':
    x_increment = 1
elif alien['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien['x-position'] = alien['x-position'] + x_increment
print(f"New position: {alien['x-position']}")

new_dict = {'sum': 0, 'salary': 20, 'rent': 10}
new_dict['sum'] = new_dict['salary'] - new_dict['rent']
print(new_dict['sum'])
del new_dict['rent']
print(new_dict)

favorite_drums = {
    'chad': 'dw',
    'dave': 'ludvig',
    'lars': 'tama',
    'evgenii':'yamaha',
    'david': 'premier'
}

him_drum = favorite_drums['evgenii'].upper()
print(f"{'Evgenii favorite drum is'} {him_drum}")

# print(favorite_drums['david'])
check_dict = favorite_drums.get('david', 'No name back this massage')
print(check_dict)
