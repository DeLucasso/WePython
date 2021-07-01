# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except
# and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

smallest = None
largest = -1
usr_inp = None
susr_ipn = None

while True:
    usr_inp = input("Enter a number: ")
    susr_inp = str(usr_inp)
    if susr_inp == "done":
        print(f"Maximum is {largest}")
        print(f"Minimum is {smallest}")
        break
    try:
        iusr_inp = int(usr_inp)
    except:
        print("Invalid input")
        continue
    if smallest == None:
        smallest = iusr_inp
    elif iusr_inp < smallest:
        smallest = iusr_inp
    elif iusr_inp > largest:
        largest = iusr_inp
