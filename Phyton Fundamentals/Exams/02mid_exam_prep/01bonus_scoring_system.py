number_of_student = int(input())
number_of_lectures = int(input())
bonus = int(input())
max_student_attendance = 0
max_total_bonus = 0
for student in range(1, number_of_student + 1):
    student_attendance = int(input())
    total_bonus = (student_attendance / number_of_lectures) * (5 + bonus)

    if student_attendance > max_student_attendance:
        max_student_attendance = student_attendance
    if total_bonus > max_total_bonus:
        max_total_bonus = total_bonus


print(f"Max Bonus: {round(max_total_bonus)}.")
print(f"The student has attended {max_student_attendance} lectures.")