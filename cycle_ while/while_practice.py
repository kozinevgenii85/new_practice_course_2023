list_of_topping = ['mazarella', 'cheese', 'salami', 'mashrooms', 'srimps']
list_of_topping_order = []
order = ''

while order != 'Quit':
    order = input("What would you order:")
    if order in list_of_topping and len(list_of_topping_order) <= 4 and order != "Quit":
        list_of_topping_order.append(order)
        print(order)
        print(list_of_topping_order)
        continue
    else:
        print(list_of_topping_order)
        break


