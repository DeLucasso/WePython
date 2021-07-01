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
  elif age > 18 and age < 45 or age >55:
    price = 12
    print(f"Adult tickets are ${price}")
  if age >= 45 and age <= 55:
    price = 0
    print(f"Mid-Life Crisis! You ride for free and price is ${price}")

  photos = input("Do you want photos for extra $3? Y / N ? ")
  if photos == "Y" or photos == "y":
    price += 3
    print(f"Your ticket cost {price}")
  else:
    print(f"Your total price is {price}")

else:
    print("You have to grow up, sorry, you can't ride yet!")
