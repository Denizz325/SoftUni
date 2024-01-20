n = int(input())
matrix = []

for _ in range(n):
    matrix.append(list(input()))

el_to_search = input()
is_found = False
for row_index in range(n):
    if is_found:
        break
    for col_index in range(len(matrix[row_index])):
        if matrix[row_index][col_index] == el_to_search:
            print(f"({row_index}, {col_index})")
            is_found = True
            break


if not is_found:
    print(f"{el_to_search} does not occur in the matrix")




