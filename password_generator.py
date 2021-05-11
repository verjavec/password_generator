#Password Generator Project
""" 
    Ask users how many letters, numbers and symbols they would like
    in their password. Then use those numbers to randomly generate a password.
"""

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_length = nr_letters + nr_symbols + nr_numbers

pw_letters = []
for l in range(1,nr_letters+1):
    pw_letters.append(random.choice(letters))
# print(pw_letters)

pw_symbols = []
for l in range(1,nr_symbols+1):
    pw_symbols.append(random.choice(symbols))
# print(pw_symbols)

pw_numbers = []
for l in range(1,nr_numbers+1):
    pw_numbers.append(random.choice(numbers))
# print(pw_numbers)

password = (pw_letters + pw_symbols + pw_numbers)

password_string = ""

# print(password)

random.shuffle(password)

for char in password:
    password_string += char
print(f"You're password is: {password_string}")