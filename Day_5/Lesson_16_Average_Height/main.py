# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

total_height = sum(student_heights)
average_height = total_height / len(student_heights)

print(f"total height = {total_height}")
print(f"number of students = {len(student_heights)}")
print(f"average height = {round(average_height)}")

# Write your code below this row 👇