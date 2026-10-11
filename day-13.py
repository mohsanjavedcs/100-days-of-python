# Debugging 4 programs

# # number_guessing
# def number_guessing():
#     secret_number = 7
#     guess = int(input("Guess a number between 1 and 10: "))

#     if guess == secret_number:
#         print("Correct!")
#     elif guess < secret_number:
#         print("Too low!")
#     else:
#         print("Too high!")
# number_guessing()

# # calculate_average
# def calculate_average():
#     numbers = [10, 20, 30, 40, 50]
#     total = 0

#     for number in numbers:
#         total += number
#     average = total / len(numbers)
#     print(f"Average: {average}")

# calculate_average()

# # password_checker
# def password_checker():
#     password = input("Enter a password: ")
#     has_digit = False

#     for character in password:
#         if character.isdigit():
#             has_digit = True

#     if len(password) >= 8 and has_digit:
#         print("Password accepted!")
#     else:
#         print("Password must contain at least 8 characters and one digit.")

# password_checker()

# # calculate_cart_total
# def calculate_cart_total():
#     prices = [120, 250, 80, 150, 300]

#     total = 0

#     for price in prices:
#         total += price

#     if total >= 500:
#         discount = total * 0.1
#     else:
#         discount = 0

#     final_total = total - discount

#     print(f"Original total: {total}")
#     print(f"Discount: {discount}")
#     print(f"Final total: {final_total}")


# calculate_cart_total()

# # remove_duplicates
# def remove_duplicates(numbers):
#     new_numbers = []
#     for number in numbers:
#         if number not in new_numbers:
#             new_numbers.append(number)

#     return new_numbers


# data = [4, 2, 4, 7, 2, 9, 7, 7, 1, 2]

# result = remove_duplicates(data)

# print("Original list:", data)
# print("Unique list:", result)