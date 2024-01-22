def is_index_valid(matrix, row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
        return True
    return False


def add_func(matrix, coordinates, value_to_add):
    row, col = coordinates
    if is_index_valid(matrix, row, col):
        matrix[row][col] += value_to_add
    else:
        print("Invalid coordinates")


def subtract_func(matrix, coordinates, value_to_subtract):
    row, col = coordinates
    if is_index_valid(matrix, row, col):
        matrix[row][col] -= value_to_subtract
    else:
        print("Invalid coordinates")

rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

command = input()

while command != "END":
    command_type, *coordinates, value = command.split()
    coordinates = list(map(int, coordinates))
    value = int(value)

    if command_type == "Add":
        add_func(matrix, coordinates, value)
    elif command_type == "Subtract":
        subtract_func(matrix, coordinates, value)

    command = input()


for row in matrix:
    print(" ".join(map(str, row)))




    command = input()