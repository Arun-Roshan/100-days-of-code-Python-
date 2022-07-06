print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $ "))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

bill_tip = percentage / 100 * total_bill + total_bill
bill_per_person = bill_tip / people

bill = "{:.2f}".format(bill_per_person)

print(f"Each person should pay $ {bill}")
