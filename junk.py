import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

hold = []
for x in range(nr_letters):
    random.shuffle(letters)
    hold.append(letters[x])

for y in range(nr_symbols):
    random.shuffle(symbols)
    hold.append((symbols[y]))

for e in range(nr_numbers):
    random.shuffle(numbers)
    hold.append((numbers[e]))

random.shuffle(hold)

password = ''
for i in hold:
    password += str(i)

# print(hold)
print(f"\nCopy generated password here: {password.strip()} \n")

input("Type the close button to end the program")



