print("Menu:")
print("1. Draw a Triangle")
print("2. Draw a Rectangle")
print("3. Draw a Pyramid")
print("4. Quit")
print(' ')

type_of_figure = int(input("Enter your choice (1/2/3/4):"))

# if type_of_figure == 1:
#     number = 5
#     for y in range(1, number + 1):
#         for x in range(0, y):
#             print('*', end = '')
#         print()
#
# elif type_of_figure == 2:
#     rows = 4
#     colums = 6
#
#     for y in range(1, rows + 1):
#         for x in range(0, colums):
#             print('*', end='')
#         print()

if type_of_figure == 3:
    number = 4

    for y in range(1, number + 1):
        for x in range(number - y):
            print(' ', end=' ')
        for k in range(2 * y - 1):
            print('*', end=' ')
        print()

else:
    print("Goodbye!")

