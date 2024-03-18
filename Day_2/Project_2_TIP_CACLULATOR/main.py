print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percent = float(input("What percentage tip"))
people = int(input("How many people to split the bill? "))
total = (total_bill + (total_bill * tip_percent/100))/people
print(f"Each person should pay: {round(total,2)}$")