MENU = {
"espresso": {
"ingredients": {
"water": 50,
"coffee": 18,
},
"cost": 1.5,
},
"latte": {
"ingredients": {
"water": 200,
"milk": 150,
"coffee": 24,
},
"cost": 2.5,
},
"cappuccino": {
"ingredients": {
"water": 250,
"milk": 180,
"coffee": 24,
},
"cost": 3.0,
}
}

resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
}

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    'pennies': 0.01,
}

def process_coins():
    print("Please insert coins!")
    total_money = 0
    for coin, value in coins.items():
       money = int(input(f"How many {coin}? "))
       total_money += (money * value)

    return total_money

def check_resources(input):
    if input == "cappuccino" or input == "latte":
        if MENU[input]["ingredients"]["milk"] > resources["Milk"]:
            print("Sorry there is not enough milk.")
            return False
    if MENU[input]["ingredients"]["water"] > resources["Water"]:
        print("Sorry there is not enough water.")
        return False
    if MENU[input]["ingredients"]["coffee"] > resources["Coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    return True
    
def transaction_success(input):
    if input == "cappuccino" or input == "latte":
        resources["Milk"] = resources["Milk"] - MENU[input]["ingredients"]["milk"]
    resources["Water"] = resources["Water"] - MENU[input]["ingredients"]["water"]
    resources["Coffee"] = resources["Coffee"] - MENU[input]["ingredients"]["coffee"]

profit = 0

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        print("Goodbye!")
        is_on = False
    elif choice == "report":
        for key, value in resources.items():
            if key != "Coffee":
                print(f"{key}: {value}ml")
            else:
                print(f"{key}: {value}g")
        print(f"Money: ${profit:.2f}")
    elif choice in MENU:
        if check_resources(choice):
            money = process_coins()
            if money < MENU[choice]["cost"]:
                print(f"Sorry that's not enough money. ${money:.2f} refunded.")
            elif money >= MENU[choice]["cost"]:
                change = round(money - MENU[choice]["cost"], 2)
                profit += MENU[choice]["cost"]
                print(f"Here is your change: ${change}")
                transaction_success(choice)
                print(f"Here is your {choice}, Enjoy!")
    else:
        print("Invalid input, please try again!")