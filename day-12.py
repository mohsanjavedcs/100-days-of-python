import random

number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose your difficulty. type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
else:
    print("Type a valid choice!")
is_game_over = False

while not is_game_over:
    if attempts > 0:
        print(f"You have {attempts} attempts to guess the number.")

        guess = int(input("Make a guess: "))

        if number == guess:
            print(f"You got it! The number was {number}")
            is_game_over = True
        elif number > guess:
            print("Too low.")
            attempts -= 1
        else:
            print("Too high.")
            attempts -= 1
    else:
        print("You've run out of guesses, You Lose.")
        is_game_over = True