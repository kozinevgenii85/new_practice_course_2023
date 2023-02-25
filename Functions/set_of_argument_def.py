# def make_pizza(*toppings):
#     print(toppings)
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'sea food', 'cheese')

def make_pizza(size, *toppings):
    print(f'You ordered pizza {size} inch with:')
    for top in toppings:
        print(top)

make_pizza(16, 'mushrooms', 'sea food', 'cheese')