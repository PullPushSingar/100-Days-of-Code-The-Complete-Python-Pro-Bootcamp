print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()

name = name1 + name2

love_index = 0

love_index += 10 * name.count("t") + 10 * name.count("r") + 10 * name.count("u") + 10 * name.count("e")
love_index += name.count("l") + name.count("o") + name.count("v") + name.count("e")

if love_index > 90 or love_index < 10:
    print(f"Your score is {love_index}, you go together like coke and mentos.")
elif 40 < love_index < 50:
    print(f"Your score is {love_index}, you are alright together.")
else:
    print(f"Your score is {love_index}.")