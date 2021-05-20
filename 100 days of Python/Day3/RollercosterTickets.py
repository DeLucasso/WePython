print("Welcome to the rollercoaster!")
height = int(input("What's your height in cm? "))

if height >= 120:
  print("Awesome! You can ride with us!")
  age = int(input("What's your age? "))
  if age < 12:
    price = 5
    print(f"Child tickets are {price}")
  elif age <= 18:
    price = 7
    print(f"Youth Tickets are ${price}")
  else:
    price = 12
    print(f"Adult tickets are ${price}")
  photos = input("Do you want photos for extra $3? Y / N ? ")
  if photos == "Y" or photos == "y":
    price += 3
    print(f"Your ticket cost {price}")
else:
    print("You have to grow up, sorry, you can't ride yet!")
