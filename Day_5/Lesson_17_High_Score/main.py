# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
max_score = max(student_scores)

print(f"The highest score in the class is: {max_score}")

max_score = 0

for student_score in range(0, len(student_scores)):
  if max_score <= student_scores[student_score]:
    max_score = student_scores[student_score]

print(f"The highest score in the class is: {max_score}")