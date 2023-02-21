# drumer_from_rhcp = {'first_name': 'chad', 'last_name': 'smith', 'age': 60, 'city': 'LA'}
#
# for i, v in drumer_from_rhcp.items():
#     i = str(i)
#     v = str(v)
#     print(f" {i} {':'} {(v.upper())}")
#
# basser_from_rhcp = {'first_name': 'micale', 'last_name': 'bulzary', 'age': 57, 'city': 'LA'}
# guitarer_from_rhcp = {'first_name': 'john', 'last_name': 'fruschianto', 'age': 50, 'city': 'LA'}
#
# rhcp_band = []
# rhcp_band.append(drumer_from_rhcp)
# rhcp_band.append(basser_from_rhcp)
# rhcp_band.append(guitarer_from_rhcp)
# #print(rhcp_band)
#
# for i in rhcp_band:
#     for k, v in i.items():
#         k = str(k)
#         v = str(v)
#         print(f" {k} {':'} {(v.upper())}")

# pet_1 = {'kat': 'tina', 'owner': 'evgenii'}
# pet_2 = {'kat': 'tucha', 'owner': 'alona'}
# pet_3 = {'dog': 'dag', 'owner': 'maria'}
# pets = []
# pets.append(pet_1)
# pets.append(pet_2)
# pets.append(pet_3)
#
# for p in pets:
#     for k, v in p.items():
#         print(f"{k}{':'}{v.title()}")

# favorite_places = {'los angeles': {
#     'evgenii': ['golden gate','palm bitch','holliwood hills']
#     },
#     'toronto':{
#     'alona': ['sea side', 'down town', 'moll']
#     },
#     'paris': {
#         'maria': ['efel tower', 'provance', 'disney lend']
#     }
# }
#
# for  b in favorite_places.values():
#     for i, v in b.items():
#         print(f"{i.title()} {'favorite places are: '}")
#         for list in v:
#             print(f"\t{list}")

# cities = {'new york': {
#     'country':'usa', 'population': '10 millions', 'facts' :
#         'if every day visit to different cafe of new york, you need for this whole life'},
#     'moscow': {
#         'country': 'russia', 'population': '12 millions', 'facts': 'There sits putin'},
#     'tel aviv':{'country': 'israel', 'population': '2 millions', 'facts': 'There is expansive chip apartmens'}
#
# }
#
# for k, v in cities.items():
#     print(f" {'City'} {k.title()} {':'}")
#     for key, val in v.items():
#         print(f" {key} {':'} {val.title()} ")

dic = {'chad':['drumer', 'biker', 'good man'], 'flea': {'first_name': 'micael', 'last_name': 'bulzary'}}

for k, v in dic.items():
    print(f"{k.upper()} {'is a: '}")
    print(type(v))
    if type(v)==list:
        for i in v:
            print(i)
    if type(v) == dict:
        for key, val in v.items():
            print(f" {key} {':'} {val.title()} ")


    #else:
        #print(v)
    #for key, val in v.items():
            #print(f" {key} {':'} {val}")


















