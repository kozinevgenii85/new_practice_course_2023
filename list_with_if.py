users = ['Anton', 'Evgenii', 'Alona', 'Maria', 'Admin']
i = input("Enter your nickname: ").title()
# for i in users:
#     if i == 'Admin':
#         print(f"{'Hello'} {i} {',would you like to see a status report?'}")
#     if i in users and i != 'Admin':
#         print(f"{'Hello'} {i} {'Thank you for login'}")
if i in users and i == 'Admin':
    print(f"{'Hello'} {i} {',would you like to see a status report?'}")
elif i in users and i != 'Admin':
    print(f"{'Hello'} {i} {'Thank you for login'}")
else:
    print("User did not find")



