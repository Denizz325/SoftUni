row, col= [int(num) for num in input().split(", ")]

matrix = []

for _ in range(row):
    row_data = [int(el) for el in input().split()]
    matrix.append(row_data)

for col_index in range(col):
    col_total = 0
    for row_index in range(row):
        col_total += matrix[row_index][col_index]
    print(col_total)