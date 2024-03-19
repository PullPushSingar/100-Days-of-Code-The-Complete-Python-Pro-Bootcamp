print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
prize = 0
if size == "S":
    if add_pepperoni == "N":
        prize = 17
    else:
        prize = 15

elif size == "M":
    if add_pepperoni == "Y":
        prize = 23
    else:
        prize = 20
elif size == "L":
    if add_pepperoni == "Y":
        prize = 28
    else:
        prize = 25



if extra_cheese == "Y":
    prize = prize + 1

print(f"Your final bill is: ${prize}.")