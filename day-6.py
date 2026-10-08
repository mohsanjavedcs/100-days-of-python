import random

def check_guess(guess, secret):
    if guess > secret:
        return "too high"
    elif guess < secret:
        return "too low"
    return "correct"

guess = None
secret = random.randint(1, 100)
attempts = 0
MAX_ATTEMPTS = 7

while guess != secret and attempts < MAX_ATTEMPTS:
    guess = int(input("Enter your guess: "))
    attempts += 1
    print(check_guess(guess, secret))

if guess == secret:
    print(f"You got it in {attempts} attempts!")
else:
    print(f"Game Over! The number was {secret}.")