n = int(input())

matrix = [[int(el) for el in input().split(", ")]for _ in range(n)]


primary_diagonal = [matrix[r][r] for r in range(n)]
second_diagonal = [matrix[r][n - r - 1] for r in range(n)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")

print(f"Secondary diagonal: {', '.join(str(x) for x in second_diagonal)}. Sum: {sum(second_diagonal)}")