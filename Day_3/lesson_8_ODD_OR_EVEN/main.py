# Which number do you want to check?
number = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if number % 2 == 0:
  type_of_number = "even"
else:
  type_of_number = "odd"

print(f"This is an {type_of_number} number.")