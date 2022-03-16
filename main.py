import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

while nr_letters < nr_symbols + nr_numbers:
    print("Please make sure that you have enough letters to hold the number of symbols and numbers in your password.")
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

password = list(range(0, nr_letters))

for each in range(nr_numbers):
    num_index = random.randint(0, nr_letters - 1)
    while type(password[num_index]) == "int":
        num_index = random.randint(0, nr_letters - 1)
    password[num_index] = "n"

for each in range(nr_symbols):
    num_index = random.randint(0, nr_letters - 1)
    while type(password[num_index]) == "int":
        num_index = random.randint(0, nr_letters - 1)
    password[num_index] = "s"
final_pw = ""
for each in password:
    if each == "n":
        index = random.randint(0, len(numbers)-1)
        each = numbers[index]
    elif each == "s":
        index = random.randint(0, len(symbols)-1)
        each = symbols[index]
    else:
        index = random.randint(0, len(letters)-1)
        each = letters[index]
    final_pw += each

print(final_pw)