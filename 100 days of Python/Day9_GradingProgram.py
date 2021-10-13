student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}


student_grades = {}
student_grades_keys = {}


print(student_scores)
for student in student_scores:
  if ((student_scores[student] >= 71) and (student_scores[student] <= 80)):
    student_grades[student] = "Acceptable"
  elif ((student_scores[student] >= 81) and (student_scores[student] <= 90)):
    student_grades[student] = "Exceeds Expectations"
  elif student_scores[student] <= 70:
    student_grades[student] = "Fail"
  else:
    student_grades[student] = "Outstanding"

print("\n")
print(f"Database student_grades")
for results in student_grades:
  print(f"{results}: {student_grades[results]}")
