num_of_students = int(input())

students = {}

for _ in range(num_of_students):
    name, grade = input().split()
    grade = float(grade)
    if name not in students:
        students[name] = []
    students[name].append(grade)

for name, grades in students.items():
    average_grade = sum(grades) / len(grades)
    formatted_grades = f"{' '.join([f'{g:.2f}' for g in grades])}"

    print(f"{name} -> {formatted_grades} (avg: {average_grade:.2f})")

