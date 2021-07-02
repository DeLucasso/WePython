#Password Generator Project
# This is a different way, using WHILE and .CHOICE
# Check out the ver2, where I'm using RANGE and .SHUFFLE

import random
from random import randint
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

passw_letters = []
passw_symbols = []
passw_numbers = []

counter_letters = 0
counter_numbers = 0
counter_symbols = 0

while nr_numbers > counter_numbers:
  number = (random.choice(numbers))
  passw_numbers.append(number)
  counter_numbers += 1
print(passw_numbers)

# Add letters to a passw_letters list
while nr_letters > counter_letters:
  letter = (random.choice(letters))
  passw_letters.append(letter)
  counter_letters += 1
print(passw_letters)

# Add symbols to a passw_symbols list
while nr_symbols > counter_symbols:
  symbol = (random.choice(symbols))
  passw_symbols.append(symbol)
  counter_symbols += 1
print(passw_symbols)
print("\n")
final_password = [passw_letters, passw_numbers, passw_symbols]
print(("User Password is: ")+("".join(passw_letters))+("".join(passw_numbers))+("".join(passw_symbols)))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# listChar = ["a", "b", "c", "d"]
# someChar = ""
# for n in listChar:
#   someChar = someChar + n
# print(someChar)

hard_pwd = []
hardpass = passw_letters + passw_symbols + passw_numbers
hard_pwd2 = hardpass
print(hardpass)
for hard in hardpass:
  print(random.choice(hardpass),end='')
  hard_pwd += random.choice(hardpass)
print(f"\nHARD PWD IS: {hard_pwd}")
hard_pwd2 = random.shuffle(hardpass)
print(hard_pwd2)


