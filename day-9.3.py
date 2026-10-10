import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Welcome to the secret auction program.")

bids = {}
max_bid = 0
winner = ""

should_continue = True
while (should_continue):
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: Rs."))
    bids[name] = bid
    cont = input("Are there any other bidders? type 'yes' or no'\n").lower()
    if cont == "no":
        should_continue = False
        for key, value in bids.items():
            if max_bid < value:
                max_bid = value
                winner = key

        print(f"The winner is {winner} with the bid of Rs.{max_bid}")
    elif cont == "yes":
        clear_terminal()