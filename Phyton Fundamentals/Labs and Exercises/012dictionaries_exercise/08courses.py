courses = {}
command = input()

while command != "end":
    course, name = command.split(" : ")

    if course not in courses:
        courses[course] = []
    courses[course].append(name)

    command = input()

for course_name, student_name in courses.items():
    names = " "
    print(f"{course_name}: {len(student_name)}")
    for i in student_name:
        names = i
        print(f"-- {names}")
