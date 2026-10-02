print("Welcome to Treasure Island.")
print("Your goal is to find the treasure.")
direction = input('Youre at a cross road. Where do you want to go? Type "Left" or "Right"\n').lower()
if direction == "right":
    print("You fell into a hole. Game Over.")
else:
    action = input('You come to a lake. There is an island in the middle of the lake. Type "Wait" to wait for a boat. Type "Swim" to swim across.\n').lower()
    if action == "swim":
        print("You get attacked by an angry crocodile. Game Over.")
    else:
        choice = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n").lower()
        if choice == "red":
            print("It's a room full of fire. Game Over.")
        elif choice == "blue":
            print("You enter a room of beasts. Game Over.")
        elif choice == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")