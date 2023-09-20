num = int(input())

for i in range(num):
    num_2 = int(input())

    if num_2 == 88:
        print("Hello")
    elif num_2 == 86:
        print("How are you?")
    elif num_2 > 88:
        print("Bye.")
    elif num_2 < 88 and num_2 != 86:
        print("GREAT!")







#
# · If the number is 88 - "Hello"
#
# · If the number is 86 - "How are you?"
#
# · If the number is not 88 nor 86, and it is below 88 - "GREAT!"
#
# · If the number is over 88 - "Bye."