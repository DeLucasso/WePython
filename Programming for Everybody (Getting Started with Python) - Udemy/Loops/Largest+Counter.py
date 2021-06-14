largest = -1
count = 0
print("Before", count)
for num in [10,3,4,5,6,7,8,2,34,36,435,66]:
    count = count + 1
    print (count,":", num,"=",largest)
    if num > largest:
        largest = num
print("After", count)
