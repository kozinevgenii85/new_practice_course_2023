drums = ['tama', 'yamaha', 'dw', 'pearl', 'gretch', 'ludwig']
print(drums[0:3])
for i in drums[:3]:
    print(i)

print(f"{'My favorite drums brand is '} {drums[0].upper()}")
print(f"{'But i also like these brands such us'} \n{drums[1:4]}")
print(f"{'I would not say that this drum are bad'}\n{drums[-3:]}")

drums_top = drums.copy()
print(drums)
print(drums_top)
drums_top.append('sonor')
print(drums_top)

if drums == drums_top:
    print('My favorite drums are:')
    for i in drums:
        print(i)
else:
    print('my other favorite drums:')
    for i in drums_top:
        print(i)
