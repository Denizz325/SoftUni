def multiplication_sign(number1, number2, number3):
    sign = ""

    negative_count = 0

    if num1 < 0:
        negative_count += 1
    if num2 < 0:
        negative_count += 1
    if num3 < 0:
        negative_count += 1
    if negative_count % 2 == 0:
        sign = "positive"
    else:
        sign = "negative"

    if num1 == 0 or num2 == 0 or num3 == 0:
        sign = "zero"
    return sign

num1 = int(input())
num2 = int(input())
num3 = int(input())
print(multiplication_sign(num1,num2,num3))