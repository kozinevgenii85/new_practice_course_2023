good_brands_guitar = ['fender', 'music man', 'gibson','gretch', 'epiphane','squire']
bed_brands_guitar = ['stagg', 'ural', 'cort', 'lp', 'squire']

for i in bed_brands_guitar:
    if i in good_brands_guitar:
        bed_brands_guitar.remove(i)
        print(f"{'I removed from list of bed guitar'} {i.upper()}")

print(bed_brands_guitar)

if bed_brands_guitar != 0:
    bed_brands_guitar.clear()
    print(f"{'I removed all elements from list bed_brands_guitar'} {bed_brands_guitar}")

bed_brands_guitar = good_brands_guitar.copy()
print(bed_brands_guitar)

list_nums = []
for i in range(1,10):
    list_nums.append(i)
print(list_nums)
for i in list_nums:
    if i == 1:
        print(f"{i}{'st'}")
    elif i == 2:
        print(f"{i}{'nd'}")
    elif i == 3:
        print(f"{i}{'rd'}")
    else:
        print(f"{i}{'th'}")



