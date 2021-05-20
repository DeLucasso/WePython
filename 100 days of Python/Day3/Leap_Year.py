year = int(input("Which year do you want to check? "))
# A Leap Year must be divisible by four. But Leap Years don't happen every four years … there is an exception. 
#If the year is also divisible by 100, it is not a Leap Year unless it is also divisible by 400.

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not a leap year.")
  else:
    print("Leap year.")
else:
  print("Not a leap year.")
