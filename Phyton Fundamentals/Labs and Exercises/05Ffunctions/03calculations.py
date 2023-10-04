def calculations(a, b, operation):
    if operation == "multiply":
        result = a * b
        return result
    elif operation == "divide":
        result = int(a / b)
        return result
    elif operation == "add":
        result = a + b
        return result
    elif operation == "subtract":
        result = a - b
        return result

operation = input()
first_num = int(input())
second_num = int(input())

result = 0

print(calculations(first_num, second_num, operation))