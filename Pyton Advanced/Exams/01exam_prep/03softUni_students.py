def softuni_students(*args, **kwargs):
        invalid_students_names = []
        valid_students = {}
        for id, name in args:
            if id in kwargs.keys():
                valid_students[name] = kwargs[id]
            else:
                invalid_students_names.append(name)

        result = ""
        if valid_students:
            for name_student, name_courses in sorted(valid_students.items()):
                result += f"*** A student with the username {name_student} has successfully finished the course {name_courses}!\n"
        if invalid_students_names:
            result += f"!!! Invalid course students: {', '.join(sorted(invalid_students_names))}"

        return result
