# Pyhon basics (nested conditions) : if > if/else > else 
# Rollercoster ticketing system

#__author__ = "DeLucasso"
#__copyright__ = "Copyright (c) 2020 DeLucasso"
#__license__ = "Public Domain"
#__version__ = "1.0"

print("Welcome to the rollercoaster!")
height = int(input("What's your height in cm? "))

if height >= 120:
  print("Awesome! You can ride with us!")
  age = int(input("What's your age? "))
  if age < 12:
    print("Please pay $5")
  elif age < 18:
    print("Please pay $7")
  else:
    print("Please pay $12")
else:
    print("You have to grow up, sorry, you can't ride yet!")
