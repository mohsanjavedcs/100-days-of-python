print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip_amount = total_bill * (tip_percentage / 100)
final_amount = total_bill + tip_amount
person = int(input("How many people to split the bill? "))
amount_per_person = final_amount / person
print(f"Each person should pay: ${amount_per_person:.2f}")