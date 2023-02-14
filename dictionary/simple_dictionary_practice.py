famoust_person = {'first_name':'chad', 'last_name':'smith', 'age':'60','city':'LA'}
print(famoust_person)
for i,b in famoust_person.items():
    print(f"{'Key:'}{i}")
    print(f"{'Value:'}{b.title()}")

for i in famoust_person:
    print(i)

tama = {'sd':'14x5','bd':'20x22','tt':'10x12','ft':'16x16'}
pearl = {'sd':'14x5','bd':'20x22','tt':'10x12','ft':'16x16'}
dw = {'sd':'14x5','bd':'20x22','tt':'10x12','ft':'16x16'}
sonor = {'sd':'14x5','bd':'20x22','tt':'10x12','ft':'16x16'}

drums = [tama, pearl, dw, sonor]

for i in drums:
    print(i)

