music_tools = {'guitar':['fender', 'music man', 'gibson','gretch', 'epiphane','squire'],
               'drums':['tama', 'dw', 'yamaha'],
               'piano' :'roland'}

for k, v in music_tools.items():
    print(k, v)

alien = []
for i in range(30):
    aliens_ship = {'color':'red',
                   'point': 5,
                   'speed': 'slow'
                   }
    alien.append(aliens_ship)

print(len(alien))
# print(alien[-1])
#
# aliens_flot = {'alien':[]}
#
# for i, v in aliens_flot.items():
#     print(i, v)

#dictionary into dictionary

mus_tool = {'favorite_drums': {
    'chad': 'dw',
    'dave': 'ludvig',
    'lars': 'tama',
    'evgenii':'yamaha',
    'david': 'premier'
},
    'guitars':{
      'fender': 'stratocaster',
     'gibson':'les paul',
    'squire':'telecaster'
}
}

# for i,v in mus_tool.items():
#     print(i, v)

list_1 = [mus_tool]

for i in list_1:
    print(i)