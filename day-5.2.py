import random
print("Welcome to the PyPassword Generator!")

no_letters = int(input("How many letters would you like in your password?\n"))
no_symbols = int(input("How many symbols would you like in your password?\n"))
no_numbers = int(input("How many numbers would you like in your password?\n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

password_list = []

for letter in range(1, no_letters + 1):
    password_list.append(random.choice(letters))

for symbol in range(1, no_symbols + 1):
    password_list.append(random.choice(symbols))

for number in range(1, no_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Here is your password: {password}")