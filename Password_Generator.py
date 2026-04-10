import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# your existing lists and inputs above here

password_list = []

for characters in range(nr_letters):
    random_letter = random.choice(letters)
    password_list.append(random_letter)

for icons in range(nr_symbols):
    random_symbols = random.choice(symbols)
    password_list.append(random_symbols)

for numerals in range(nr_numbers):
    random_numerals = random.choice(numbers)
    password_list.append(random_numerals)

# shuffle password_list
random.shuffle(password_list)
# turn password_list into a string
print(password_list)
final_password = ''.join(password_list)
# print the final password
print(final_password)