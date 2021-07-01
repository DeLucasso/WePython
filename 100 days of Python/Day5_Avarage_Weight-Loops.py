student_heights = input("Input a list of student heights like : 200 230 203 196 etc. : ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# This is an example of loops usage.
# You can't use:
# print (sum(student_heights))
# print (len(student_heights))

len_counter = 0
sum_heights = 0
for height in student_heights:
  len_counter += 1
  sum_heights += int(height)
#   sum_heights = int(height) + sum_heights
  
print(f"Total sum of heights are : {sum_heights}")
print(f"Number of heights = {len_counter}")
print(f"Average height is : {sum_heights / len_counter}")
