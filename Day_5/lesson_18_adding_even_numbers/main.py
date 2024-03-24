target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
total_value = 0
if target % 2 == 0:
    for number in range(0,target + 1,2):
        total_value += number
else:
    for number in range(0,target,2):
        total_value += number

print(total_value)