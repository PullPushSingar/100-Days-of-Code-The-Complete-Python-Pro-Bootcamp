import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = ""

while len(password) < nr_symbols + nr_numbers + nr_letters:
    choice = random.randint(0, 2)
    if choice == 0 and sum(password.count(sym) for sym in symbols) < nr_symbols:
        password += random.choice(symbols)
    elif choice == 1 and sum(password.count(num) for num in numbers) < nr_numbers:
        password += random.choice(numbers)
    elif choice == 2 and sum(password.count(let) for let in letters) < nr_letters:
        password += random.choice(letters)

print(password)
