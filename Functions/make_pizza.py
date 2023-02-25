def make_pizza(size, *toppings):
    print(f'You ordered pizza {size} inch with:')
    for top in toppings:
        print(top)