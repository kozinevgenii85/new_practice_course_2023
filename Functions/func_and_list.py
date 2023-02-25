# list_of_guitars = ['prs', 'gibson', 'fender', 'ibanez']
#
# def guitars(brands):
#     for brand in brands:
#         msg = f"Do you use guitar {brand}?"
#         print(msg.upper())
#
# guitars(list_of_guitars)

### Changing list in function ###

# the_order = ['hello', 'How are you', 'What is up', 'Well done']
# made_order = []
#
# def make_shirt(texts):
#     for text in texts:
#         made_order.append(text)
#         # the_order.remove(text)
#     return made_order
#
# made_list = make_shirt(the_order)
# print(made_list)
# print(made_order)



# def order_in_work(the_order, made_order):
#     while the_order:
#         current_order = the_order.pop()
#         print(f'Passed to the work and removed from list the order {current_order}')
#         made_order.append(current_order)
#         print(f'Added to the list in the work {current_order}')
#
#
# def print_order(made_order):
#     print("Printed following text on the shirts")
#     for made in made_order:
#         print(f"Printed {made}")
#
#
#
#
#
#
#
# the_order = ['hello', 'How are you', 'What is up', 'Well done']
# made_order = []
# order_in_work(the_order,made_order)
# print_order(made_order)






# def guitars_in_the_work(check_guitars,checked_guitars):
#     while check_guitars:
#         checking_guitar = check_guitars.pop()
#         print(f'Passed to the work guitar {checking_guitar.title()}')
#         checked_guitars.append(checking_guitar)
#         print(f'Got to the work guitar {checking_guitar.title()}')
#
# def made_guitar(made):
#     print('We checked following guitars')
#     for make in made:
#         print(f' The {make.title()}')
#
#
#
# list_to_check_guitars = ['prs', 'gibson', 'fender', 'ibanez']
# list_checked_guitars = []
#
# guitars_in_the_work(list_to_check_guitars[:], list_checked_guitars)
# made_guitar(list_checked_guitars)
# print(list_to_check_guitars)

list_message = ['Hello my friend', 'How are you', 'I like your new look']
sent_message = []
# def show_message(messages):
#     for message in messages:
#         print(message)
#
# show_message(list_message)



def send_message(messages):
    while messages:
        sending_message = messages.pop()
        print(f'we are sending message "{sending_message.upper()}"')
        sent_message.append(sending_message)
        print(f'we sent message "{sending_message.upper()}"')

send_message(list_message[:])
print(sent_message)
print(list_message)
















