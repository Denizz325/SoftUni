row, col = [int(num) for num in input().split(", ")]

matrix = []
biggest_sum = float('-inf')
sub_matrix = []

for i in range(row):
    row_data = [int(el) for el in input().split(", ")]
    matrix.append(row_data)

for row_index in range(row - 1):
    for col_index in range(col - 1):
        current_el = matrix[row_index][col_index]
        next_el = matrix[row_index][col_index + 1]
        el_under = matrix[row_index + 1][col_index]
        el_under_next_el = matrix[row_index + 1][col_index + 1]
        # el_under_next_el = Това е елемента под next_el или елемента диагонал на current_el

        total_sum = current_el + next_el + el_under + el_under_next_el

        if biggest_sum < total_sum:
            biggest_sum = total_sum
            sub_matrix = [[current_el, next_el], [el_under, el_under_next_el]]


print(*sub_matrix[0])
print(*sub_matrix[1])
print(biggest_sum)