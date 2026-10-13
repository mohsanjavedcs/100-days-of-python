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

def process_coins():
    print("Please insert coins!")
    quarters = input("How many quarters? ")
    dimes = input("How many dimes? ")
    nickels = input("How many nickels? ")
    pennies = input("How many pennies? ")

    total_money = pennies + (nickels * 5) + (dimes  * 10) + (quarters * 25)

    return total_money

def check_resources(input):
    if input == "cappuccino" or input == "latte":
        if MENU[input]["ingredients"]["milk"] > resources["Milk"]:
            print("Sorry there is not enough milk.")
            return False
        elif MENU[input]["ingredients"]["milk"] <= resources["Milk"]:
            resources["Milk"] = resources["Milk"] - MENU[input]["ingredients"]["milk"]
    if MENU[input]["ingredients"]["water"] > resources["Water"]:
        print("Sorry there is not enough water.")
        return False
    elif MENU[input]["ingredients"]["water"] <= resources["Water"]:
        resources["Water"] = resources["Water"] - MENU[input]["ingredients"]["water"]
    if MENU[input]["ingredients"]["coffee"] > resources["Coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    elif MENU[input]["ingredients"]["coffee"] <= resources["Coffee"]:
        resources["Coffee"] = resources["Coffee"] - MENU[input]["ingredients"]["coffee"]
        return True

profit = 0

is_on = True

while is_on:
    input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if input == "off":
        print("Goodbye!")
        is_on = False
    elif input == "report":
        for key, value in resources.items():
            if key != "Coffee":
                print(f"{key}: {value}ml")
            else:
                print(f"{key}: {value}g")
        print(f"Money: ${profit}")
    elif input == "espresso":
        if check_resources(input):
            money = process_coins()
            if money < MENU["espresso"]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
                break
            elif money >= MENU["espresso"]["cost"]:
                profit += money

    elif input == "latte":
        pass
    elif input == "cappuccino":
        pass
    else:
        print("Invalid input, please try again!")