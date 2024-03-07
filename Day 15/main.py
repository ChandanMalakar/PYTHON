print("Hello World")
# TODO 1: print report of all coffee machine resources
# TODO 2: check the resources are sufficient to make drink water
# TODO 3: process coins (check if the given coins are sufficient or not)
# TODO 4: check transaction successful
# TODO 5: make coffee and deduct the used resources from remaining

water = 300
milk = 200
coffee = 100
money = 0
price_latte = 1.50
price_espresso = 2.50
price_cappuccino = 3.00


def converter():
    print("Please insert coins.")
    quarter = float(input("How many quarters?:"))
    dimes = float(input("How many dimes?:"))
    nickles = float(input("How many nickles?:"))
    pennies = float(input("How many pennies?:"))
    total = (quarter * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    return total


def check_resources(x):
    if water == 0:
        print("water is deplpted")
    elif coffee == 0:
        print("coffee is depleted")
    elif milk == 0:
        print("milk is depleted")
    if x == 'latte':
        if water < 200:
            print("Sorry there is not enough water.")
        elif coffee < 24:
            print("Sorry there is not enough coffee.")
        elif milk < 150:
            print("Sorry there is not enough milk.")
        else:
            return 'ready'
    elif x == 'espresso':
        if water < 50:
            print("Sorry there is not enough water.")
        elif coffee < 18:
            print("Sorry there is not enough coffee.")
        else:
            return 'ready'
    elif x == 'cappuccino':
        if water < 250:
            print("Sorry there is not enough water.")
        elif coffee < 24:
            print("Sorry there is not enough coffee.")
        elif milk < 100:
            print("Sorry there is not enough milk.")
        else:
            return 'ready'


def coffee_machine():
    global money
    choice = input("What would you like? (espresso/latte/cappuccino) : ")
    if choice == "report":
        print("Water : ", water, "\nMilk : ", milk, "\nCoffee : ", coffee, "\nMoney : $", money)
        coffee_machine()
    elif choice == "off":
        exit()
    elif choice == "latte":
        ready_check = check_resources(x='latte')
        if ready_check == 'ready':
            total_amount = converter()
            if total_amount < 2.50:
                print("Insufficient Money")
                coffee_machine()
            money += 2.5
            remaining_amount = total_amount - price_latte
            print(f"Here is ${remaining_amount:.2f} in change.")
            print("Here is your latte Enjoy!")
            update(choice)
    elif choice == "espresso":
        ready_check = check_resources(x='espresso')
        if ready_check == 'ready':
            total_amount = converter()
            if total_amount < 1.50:
                print("Insufficient Money")
                coffee_machine()
            money += 1.5
            remaining_amount = total_amount - price_espresso
            print(f"Here is ${remaining_amount:.2f} in change.")
            print("Here is your Espresso Enjoy!")
            update(choice)
    elif choice == "cappuccino":
        ready_check = check_resources(x='cappuccino')
        if ready_check == 'ready':
            total_amount = converter()
            if total_amount < 3.00:
                print("Insufficient Money")
                coffee_machine()
            money += 3.0
            remaining_amount = total_amount - price_cappuccino
            print(f"Here is ${remaining_amount:.2f} in change.")
            print("Here is your Cappuccino Enjoy!")
            update(choice)
    else:
        print("Invalid Choice")


def update(choice):
    global water
    global milk
    global coffee
    if choice == 'espresso':
        water -= 50
        coffee -= 18
        coffee_machine()
    elif choice == 'latte':
        water -= 200
        coffee -= 24
        milk -= 150
        coffee_machine()
    elif choice == 'cappuccino':
        water -= 250
        coffee -= 24
        milk -= 100
        coffee_machine()


coffee_machine()
# print("Thank You ....")