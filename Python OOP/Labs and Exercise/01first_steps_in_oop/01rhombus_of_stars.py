def prints(n, row):
    print(' ' * (n - row), end="")
    print(*["*"] * row)


def print_triangle(n):
    for row in range(1, n + 1):
        prints(n, row)


def print_reverse_triangle(n):
    for row in range(n - 1, 0, -1):
        prints(n, row)


def create_rhombus(n):
    print_triangle(n)
    print_reverse_triangle(n)


n = int(input())

create_rhombus(n)