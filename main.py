"""Definition of needed variables"""
five = 5
ten = 10
twenty = 20
fifty = 50
one_hundred = 100
two_hundred = 200
five_hundred = 500

menu = []
price = []

today_menu = dict([
    ("pizza", 9),
    ("pasta", 5),
    ("chivito", 5.90),
    ("bravas", 4),
    ("calamares", 4.50),
    ("albondigas", 6.20),
    ("tortilla", 5),
])

for k, v in today_menu.items():
    menu.append(k)
    price.append(v)
print("Today's menu is: ", menu, price, sep='\n')

"""Asking the client for what dishes he wants"""
client_order = list()
more_dishes = 1
while more_dishes == 1:
    order = input("Choose your dishes from the menu:").lower()
    if order not in menu:
        print("That dish is not in the menu")
        break
    client_order = [*client_order, order]
    more_dishes = int(input("Do you want to continue ordering?(Select 1 to continue, 0 to stop): "))
    if more_dishes == 0:
        print("Your order is:", client_order)
        break

"""Comparing menu and order client and show the price"""
total = 0
for menu in client_order:
    total = total + today_menu[menu]
print("Your total price is:", total, "€")

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
