import random

word_list = [
  "apple", "banana", "orange", "grape", "mango",
  "computer", "keyboard", "mouse", "monitor", "laptop",
  "program", "function", "variable", "array", "object",
  "javascript", "python", "java", "coding", "developer",
  "student", "teacher", "school", "college", "university",
  "book", "notebook", "pencil", "paper", "marker",
  "river", "mountain", "forest", "ocean", "desert",
  "sunshine", "rainbow", "thunder", "breeze", "cloud",
  "happy", "brave", "clever", "honest", "kind",
  "beautiful", "creative", "curious", "patient", "friendly",
  "house", "garden", "window", "door", "kitchen",
  "family", "friend", "brother", "sister", "parent",
  "football", "cricket", "tennis", "basketball", "hockey",
  "travel", "journey", "adventure", "explore", "discover",
  "science", "history", "geography", "mathematics", "physics",
  "music", "guitar", "piano", "violin", "drum",
  "morning", "evening", "midnight", "weekend", "holiday",
  "energy", "power", "strength", "wisdom", "knowledge",
  "dream", "future", "success", "freedom", "progress",
  "network", "internet", "website", "database", "security"
]

chosen_word = random.choice(word_list)

display = []
for _ in chosen_word:
    display.append("_")

print(display)

end_of_game = False
lives = 6

while not end_of_game:

    print(f"You have {lives} lives remaining!")
    guess = input("Guess a letter: ").lower()

    for pos in range(len(chosen_word)):
        letter = chosen_word[pos]
        if guess == letter:
            display[pos] = guess
    if guess not in chosen_word:
        lives -= 1

    print(display)

    if "_" not in display:
        print("You've Won!")
        end_of_game = True
    elif lives == 0:
        print("You've Lost.")
        end_of_game = True

print(f"The word is {chosen_word}")