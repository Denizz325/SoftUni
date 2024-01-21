row, col = [int(num) for num in input().split()]

matrix = [input().split() for _ in range(row)]
equal_blocks = 0

for row_index in range(row - 1):
    for col_index in range(col - 1):
        current_el = matrix[row_index][col_index]
        next_el = matrix[row_index][col_index + 1]
        el_under = matrix[row_index + 1][col_index]
        el_under_next_el = matrix[row_index + 1][col_index + 1]

        if current_el == next_el == el_under == el_under_next_el:
            equal_blocks += 1

print(equal_blocks)