print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

split_check = bill/people
tip_convert = tip/100
amount_due = split_check * tip_convert + split_check
final_amount = "{:.2f}".format(amount_due)

print(f"Each person should pay ${final_amount}")